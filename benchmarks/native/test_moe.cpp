#include "ggml.h"
#include "ggml-quants.h"
#include "iqk_mul_mat.h"

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <limits>
#include <thread>
#include <vector>

struct RowMapping {
    int32_t i1;
    int32_t i2;
};

static int weight(int x, int k, bool gate) {
    return (x*(gate ? 7 : 11) + k*(gate ? 5 : 3) + (k/32)*7)%15 - 7;
}

static int activation(int row, int k) {
    return (row*5 + k*7 + (k/32)*3)%13 - 6;
}

static float weight_scale(int x, int block, bool gate) {
    return (gate ? 0.125f : 0.25f)*(1 + ((x + block)&1));
}

static float activation_scale(int block) {
    return 0.125f*(1 + (block&1));
}

static std::vector<block_q8_0> make_weights(int nx, int k, bool gate) {
    std::vector<block_q8_0> result(nx*(k/32));
    for (int x = 0; x < nx; ++x) {
        for (int ib = 0; ib < k/32; ++ib) {
            auto& b = result[x*(k/32) + ib];
            b.d = ggml_fp32_to_fp16(weight_scale(x, ib, gate));
            for (int j = 0; j < 32; ++j) b.qs[j] = weight(x, ib*32 + j, gate);
        }
    }
    return result;
}

static std::vector<block_q8_2_x4> make_activations(int rows, int k) {
    std::vector<block_q8_2_x4> result(rows*(k/128));
    for (int row = 0; row < rows; ++row) {
        for (int ib = 0; ib < k/32; ++ib) {
            auto& b = result[row*(k/128) + ib/4];
            int lane = ib%4;
            b.d[lane] = (ib&1) ? 0x3e80 : 0x3e00; // BF16: 0.25 or 0.125.
            int sum = 0;
            for (int j = 0; j < 32; ++j) {
                int q = activation(row, ib*32 + j);
                b.qs[lane*32 + j] = q;
                sum += q;
            }
            b.d[lane + 4] = uint16_t(int16_t(sum));
        }
    }
    return result;
}

static float reference_dot(int x, int row, int k, bool gate) {
    double sum = 0;
    for (int i = 0; i < k; ++i) {
        sum += weight(x, i, gate)*activation(row, i)*
            weight_scale(x, i/32, gate)*activation_scale(i/32);
    }
    return float(sum);
}

static void check_output(const std::vector<float>& actual, const std::vector<float>& expected,
                         int nx, int ny, int k, int nth, bool fused, bool parallel) {
    for (size_t i = 0; i < expected.size(); ++i) {
        bool ok = std::isnan(expected[i]) ? std::isnan(actual[i]) :
            std::isfinite(actual[i]) && std::abs(actual[i] - expected[i]) <= 1e-4f;
        if (!ok) {
            std::fprintf(stderr, "Nx=%d Ny=%d K=%d nth=%d fused=%d parallel=%d offset=%zu actual=%g expected=%g\n",
                         nx, ny, k, nth, fused, parallel, i, actual[i], expected[i]);
            std::exit(1);
        }
    }
}

static void run_case(int nx, int ny, int k) {
    const int ne11 = (ny + 1)/2;
    const int source_rows = 2*ne11;
    const int dst_stride = nx + 7;
    const int dst_plane = ne11*dst_stride + 11;
    const int guard = 16;
    const float nan = std::numeric_limits<float>::quiet_NaN();
    auto up = make_weights(nx, k, false);
    auto gate = make_weights(nx, k, true);
    auto b = make_activations(source_rows, k);
    std::vector<RowMapping> mapping(ny);
    std::vector<float> up_bias(nx), gate_bias(nx);
    for (int x = 0; x < nx; ++x) {
        up_bias[x] = 0.125f*((x%5) - 2);
        gate_bias[x] = 0.125f*((x%3) - 1);
    }
    std::vector<float> expected(2*guard + 2*dst_plane, nan);
    auto expected_fused = expected;
    for (int y = 0; y < ny; ++y) {
        int source = (y*17 + 3)%ny;
        mapping[y] = {source%ne11, source/ne11};
        size_t offset = guard + mapping[y].i1*dst_stride + mapping[y].i2*dst_plane;
        for (int x = 0; x < nx; ++x) {
            float u = reference_dot(x, source, k, false);
            float g = reference_dot(x, source, k, true);
            expected[offset + x] = u;
            expected_fused[offset + x] = (u + up_bias[x])*std::max(0.f, g + gate_bias[x]);
        }
    }
    if ((ny >= 32) != (iqk_dequant_type(GGML_TYPE_Q8_0, ny) == GGML_TYPE_Q8_0_R8)) {
        std::fprintf(stderr, "Unexpected Q8_0 conversion threshold; this test targets the AVX2 path.\n");
        std::exit(1);
    }
    for (int nth : {1, 7, 14, 28}) {
        for (bool fused : {false, true}) {
            for (bool parallel : {false, true}) {
                std::vector<float> actual(expected.size(), nan);
                std::vector<uint8_t> supported(nth);
                auto call = [&](int ith) {
                    if (fused) {
                        supported[ith] = iqk_moe_fused_up_gate(nx, ny, k, ne11, GGML_UNARY_OP_RELU,
                            GGML_TYPE_Q8_0, up.data(), gate.data(), (k/32)*sizeof(block_q8_0),
                            GGML_TYPE_Q8_2_X4, b.data(), (k/128)*sizeof(block_q8_2_x4),
                            (const char *)up_bias.data(), (const char *)gate_bias.data(),
                            actual.data() + guard, dst_stride*sizeof(float), dst_plane*sizeof(float),
                            mapping.data(), 0.f, ith, nth);
                    } else {
                        supported[ith] = iqk_mul_mat_moe(nx, ny, k, ne11,
                            GGML_TYPE_Q8_0, up.data(), (k/32)*sizeof(block_q8_0),
                            GGML_TYPE_Q8_2_X4, b.data(), (k/128)*sizeof(block_q8_2_x4),
                            actual.data() + guard, dst_stride*sizeof(float), dst_plane*sizeof(float),
                            mapping.data(), ith, nth);
                    }
                };
                if (parallel) {
                    std::vector<std::thread> threads;
                    for (int ith = 0; ith < nth; ++ith) threads.emplace_back(call, ith);
                    for (auto& thread : threads) thread.join();
                } else {
                    for (int ith = 0; ith < nth; ++ith) call(ith);
                }
                if (std::find(supported.begin(), supported.end(), 0) != supported.end()) {
                    std::fprintf(stderr, "Kernel rejected the test format.\n");
                    std::exit(1);
                }
                check_output(actual, fused ? expected_fused : expected, nx, ny, k, nth, fused, parallel);
            }
        }
    }
    std::printf("PASS Nx=%d Ny=%d K=%d: scalar reference, mapped rows, output guards, 1/7/14/28 workers\n", nx, ny, k);
}

static void test_threshold_sort() {
    for (int minimum : {4, 20}) {
        ggml_init_params params = {1 << 20, nullptr, false};
        ggml_context * context = ggml_init(params);
        auto * input = ggml_new_tensor_1d(context, GGML_TYPE_F32, 64);
        auto * values = (float *)input->data;
        for (int i = 0; i < 64; ++i) values[i] = float((i*17 + 3)%64 + 1);
        auto * output = ggml_top_k_thresh(context, input, 64, minimum, 0.75f);
        auto * graph = ggml_new_graph_custom(context, 32, false);
        ggml_build_forward_expand(graph, output);
        if (ggml_graph_compute_with_ctx(context, graph, 4) != GGML_STATUS_SUCCESS) std::exit(1);
        auto * indices = (int32_t *)output->data;
        for (int rank = 0; rank < 64; ++rank) {
            int wanted_value = 64 - rank;
            int expected = -1;
            if (rank < minimum || wanted_value >= 48) {
                for (int i = 0; i < 64; ++i) if (values[i] == wanted_value) expected = i;
            }
            if (indices[rank] != expected) {
                std::fprintf(stderr, "Threshold sort minimum=%d rank=%d actual=%d expected=%d\n",
                             minimum, rank, indices[rank], expected);
                std::exit(1);
            }
        }
        ggml_free(context);
    }
    std::puts("PASS threshold sort: ranks beyond 16, minimum 4/20, threshold mask");
}

int main() {
    test_threshold_sort();
    ggml_init_params params = {1 << 20, nullptr, true};
    ggml_context * context = ggml_init(params);
    if (!context) return 1;
    for (int k : {256, 512, 1024}) {
        for (int ny : {31, 32, 64, 65}) run_case(8, ny, k);
    }
    run_case(24, 33, 256);
    run_case(40, 65, 512);
    run_case(512, 64, 256);
    run_case(2048, 33, 256);
    ggml_free(context);
    return 0;
}
