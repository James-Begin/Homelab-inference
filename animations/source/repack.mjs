import {C, ease, lerp, g, text, rect, line, curvePoint} from './drawing.mjs';
import {facts} from './facts.mjs';

const colors = [C.teal, C.blue, C.violet, C.amber, C.red, '#A9D68B', '#79C9D0', '#D6ACCB'];
const sx = 160, sy = 270, rowGap = 56, sh = 34;
const dx = 930, scaleY = 270, quantY = [380, 476, 572, 668], dh = 48;
const qx = sx + 48, scaleW = 32, quantW = 64;

function moved(k, group, t) {
  const isScale = group === -1;
  const start = isScale ? [sx, sy + rowGap * k] : [qx + quantW * group, sy + rowGap * k];
  const end = isScale ? [dx + scaleW * k, scaleY] : [dx + quantW * k, quantY[group]];
  const begin = isScale ? 1.6 + .065 * k : 4 + 1.8 * group + .045 * k;
  const u = ease(t, begin, begin + 1.35);
  const [x,y] = curvePoint(start, end, u, (k - 3.5) * 7);
  const h = lerp(sh, dh, u);
  const labelOpacity = isScale ? 0 : ease(u, .55, .95);
  const w = isScale ? scaleW : quantW;
  return rect(x,y,w,h,colors[k],C.bg,2)
    + g(text(k,x + w / 2,y + h / 2 + 8,24,colors[k],{mono:true}), labelOpacity);
}

function scene(t) {
  let s = text('Repacking eight Q4_0 rows',800,108,43,C.white,{serif:true})
    + text('Same 144 bytes. A different order for the AVX2 kernel.',800,174,27,C.muted)
    + text('8 source rows · Q4_0',110,214,28,C.white,{anchor:'start'})
    + text('2 B',sx + scaleW / 2,248,24,C.muted,{mono:true})
    + text('4 × 4 B',qx + 2 * quantW,248,24,C.muted,{mono:true})
    + text('Q4_0_R8 · 144 B',dx,214,28,C.white,{anchor:'start'})
    + text('offset',880,249,24,C.muted,{mono:true,anchor:'end'})
    + text('0',880,scaleY + 32,24,C.muted,{mono:true,anchor:'end'})
    + rect(dx,scaleY,8 * scaleW,dh,C.line,C.bg,1.5)
    + text('16 B scales',dx + 8 * scaleW + 24,scaleY + 32,26,C.muted,{anchor:'start'});

  for(let k=0;k<8;k++) {
    const y=sy + rowGap*k;
    s += text(k,128,y + 26,24,colors[k],{mono:true,anchor:'end'})
      + rect(sx,y,scaleW,sh,C.faint,C.bg,1.5);
    for(let group=0;group<4;group++) s += rect(qx + quantW*group,y,quantW,sh,C.faint,C.bg,1.5);
  }

  for(let group=0;group<4;group++) {
    const y=quantY[group], offset=facts.repackScaleBytes + group*32;
    s += text(offset,880,y + 32,24,C.muted,{mono:true,anchor:'end'})
      + rect(dx,y,8*quantW,dh,C.line,C.bg,1.5)
      + text('32 B',dx + 4*quantW,y + dh + 33,24,C.muted,{mono:true});
  }

  for(let k=0;k<8;k++) s += moved(k,-1,t);
  for(let group=0;group<4;group++) for(let k=0;k<8;k++) s += moved(k,group,t);

  const a=ease(t,1.6,3.6), b=ease(t,4,11.1);
  s += line(70,769,1530,769,C.faint,1.5)
    + text('ik_llama.cpp · Q4_0_R8 layout',70,813,24,C.muted,{anchor:'start'})
    + text('8 × 32 = 256 quantized weights',1530,813,26,C.white,{mono:true,anchor:'end'})
    + g(line(dx,scaleY + dh + 4,dx + 8*scaleW,scaleY + dh + 4,C.white,2),a*(1-b));
  return s;
}

export default {
  id:'repack-eight-rows',
  title:'Repacking eight Q4_0 rows',
  duration:14,
  poster:11.5,
  checks:[0,2.8,5.2,8.7,11.5,13.9],
  facts:[
    'Eight Q4_0 rows each contain a 2-byte scale and 16 bytes of packed weights.',
    'Eight scales form the first 16 bytes of Q4_0_R8.',
    'Four 32-byte groups each contain one 4-byte chunk from all eight source rows.',
    'The full-tile quant group offsets are 16, 48, 80, and 112 bytes.',
    'The repacked tile is 144 bytes and represents 256 quantized weights.',
    'Q4_0_R8 is credited to upstream ik_llama.cpp; no isolated performance claim is made.'
  ],
  frame(t) {
    if(t<13.4) return scene(t);
    const u=ease(t,13.4,14);
    return g(scene(t),1-u)+g(scene(0),u);
  }
};
