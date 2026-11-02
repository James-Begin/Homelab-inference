import {C,ease,lerp,g,text,rect,line,path,circle} from './drawing.mjs';

const qwen=Array.from({length:40},(_,i)=>(i+1)%4===0?'full':'linear');
const fullLayers=new Set([0,1,5,9,13,17,21,25,29,33,37,41,45,48]);
const flint=Array.from({length:49},(_,i)=>fullLayers.has(i)?'full':'sliding');
const color=kind=>kind==='full'?C.amber:kind==='linear'?C.blue:C.teal;

function strip(layers,x,y,step,w,h,selected=-1){
  return layers.map((kind,i)=>rect(x+i*step,y,w,h,color(kind),C.bg,1.5,2)
    +g(rect(x+i*step,y,w,h,color(kind),color(kind),0,2),i===selected?.8:.18)).join('');
}

function overview(t){
  const progress=ease(t,.8,4.3);
  const qi=Math.min(39,Math.floor(progress*40));
  const fi=Math.min(48,Math.floor(progress*49));
  let s=text('Attention layers · one block per layer',800,267,29,C.muted)
    +text('Qwen 3.6',105,355,30,C.white,{anchor:'start'})
    +strip(qwen,300,308,23,18,64,qi)
    +text('40 layers',105,401,26,C.muted,{anchor:'start'})
    +text('30 gated linear',520,446,29,C.blue)
    +text('10 full attention',1100,446,29,C.amber)
    +text('Recurrent state carries history',520,487,25,C.muted)
    +text('Available causal context',1100,487,25,C.muted)
    +text('Flint',105,595,30,C.white,{anchor:'start'})
    +strip(flint,300,548,23,18,64,fi)
    +text('49 layers',105,641,26,C.muted,{anchor:'start'})
    +text('35 sliding window',520,686,29,C.teal)
    +text('14 full attention',1100,686,29,C.amber)
    +text('513 positions · RoPE on',520,727,25,C.muted)
    +text('RoPE off',1100,727,25,C.muted)
    +text('Attention only; feed-forward blocks are omitted.',800,811,26,C.muted);
  return s;
}

function detail(t){
  const toFull=ease(t,12,13),toSliding=ease(t,18,19);
  const full=toFull*(1-toSliding);
  const il=t<12.5?2:t<18.5?5:6;
  const isFull=il===5;
  const position=1024+Math.floor(128*ease(t,19.4,22.4));
  const first=position-512;
  const x0=160,currentX=x0+position,localX=x0+first;
  const left=lerp(localX,x0,full);
  const hue=isFull?C.amber:C.teal;

  let s=text('Flint attention layers · zero-based indices',800,260,27,C.muted)
    +strip(flint,190,288,25,19,35)
    +rect(187+il*25,284,25,43,hue,'none',2.5,3)
    +text('0',200,358,23,C.muted,{mono:true})
    +text('2',250,358,23,C.teal,{mono:true})
    +text('5',325,358,23,C.amber,{mono:true})
    +text('48',1400,358,23,C.muted,{mono:true})
    +text('il = '+il+' · '+(isFull?'full attention':'sliding attention'),160,418,31,hue,{anchor:'start'})
    +text(isFull?'RoPE off':'RoPE on',1440,418,28,hue,{anchor:'end'});

  s+=text(isFull?'All available causal context':'Older positions masked at this layer',160,453,23,C.muted,{anchor:'start'})
    +rect(x0,468,1280,56,C.faint,C.bg,1,2)
    +rect(x0,468,position+1,56,C.line,C.bg,1,2)
    +g(rect(localX-.5,468,513,56,C.teal,C.teal,0,1),.22*(1-full))
    +g(rect(x0-.5,468,position+1,56,C.amber,C.amber,0,1),.22*full)
    +line(left,468,currentX,468,hue,2.5)
    +line(left,524,currentX,524,hue,2.5);
  for(let i=0;i<=1280;i+=16){
    const attended=i<=position&&(isFull||i>=first);
    s+=line(x0+i,480,x0+i,512,attended?hue:C.faint,i%256===0?2:1);
  }
  s+=line(currentX,454,currentX,541,hue,3)
    +circle(currentX,468,5,hue)
    +text('current t = '+position,currentX,577,25,hue,{mono:true})
    +text('0',160,561,23,C.muted,{mono:true})
    +text('future',1440,453,23,C.muted,{anchor:'end'})
    +g(text('t − 512 = '+first,localX,561,24,C.teal,{mono:true}),1-full)
    +path(`M ${left} 605 L ${left} 617 L ${currentX} 617 L ${currentX} 605`,hue,2)
    +g(text('512 previous + current = 513 positions',(localX+currentX)/2,656,26,C.teal),1-full)
    +g(text((position+1).toLocaleString('en-US')+' available positions · no future tokens',(x0+currentX)/2,656,26,C.amber),full);

  s+=line(160,684,1440,684,C.faint,1.5)
    +text('const bool is_swa = hparams.swa_layers[il];',190,726,26,C.white,{mono:true,anchor:'start'})
    +text('const bool do_rope = hparams.has_rope(il);',190,767,26,C.white,{mono:true,anchor:'start'})
    +text('auto KQ_mask_l = is_swa ? KQ_mask_swa : KQ_mask;',190,808,26,C.white,{mono:true,anchor:'start'})
    +text(isFull?'false':'true',1390,726,26,hue,{mono:true,anchor:'end'})
    +text(isFull?'false':'true',1390,767,26,hue,{mono:true,anchor:'end'});
  const prefix=isFull?'auto KQ_mask_l = is_swa ? KQ_mask_swa : ':'auto KQ_mask_l = is_swa ? ';
  const selectedMask=isFull?'KQ_mask':'KQ_mask_swa';
  const maskX=190+prefix.length*26*.60205;
  s+=line(maskX,818,maskX+selectedMask.length*26*.60205,818,hue,2.5);
  return s;
}

function frame(t){
  const zoom=ease(t,6,7);
  return text('From Qwen to Flint',800,108,43,C.white,{serif:true})
    +text('The new model needed its own attention graph.',800,174,27,C.muted)
    +g(overview(t),1-zoom,`translate(0 ${-20*zoom})`)
    +g(detail(t),zoom,`translate(0 ${20*(1-zoom)})`)
    +text(t<6.5?'Exact layer patterns · movement does not represent runtime':'Patch 0003 · exact mask and RoPE choices; context and motion are illustrative',800,872,24,C.muted);
}

export default {
  id:'flint-vs-qwen',
  title:'From Qwen to Flint',
  duration:22,
  gifColors:64,
  gifDither:'none',
  poster:10*22/26,
  checks:[0,4.8,6.5,8,10,12.5,14.5,18.5,21,24,25.98].map(t=>t*22/26),
  sources:[
    'https://huggingface.co/Qwen/Qwen3.6-35B-A3B/blob/7da1103/config.json',
    'https://huggingface.co/RecursiveSI/flint/blob/2a247be0c0aec895ccb0ac7ca92229ec6df37288/config.json',
    'https://huggingface.co/docs/transformers/main/model_doc/flint',
    'https://github.com/James-Begin/Homelab-inference/blob/e72afab125d7bb5bf844e1c2d23ff3a204ba1727/patches/0003-flint-40b-moe-architecture-port.patch'
  ],
  facts:[
    'Qwen has 40 text-trunk layers: 30 gated linear and 10 full attention. Its auxiliary MTP layer is omitted.',
    'Flint has 49 layers: 35 sliding and 14 full attention. Full layers are 0,1,5,9,13,17,21,25,29,33,37,41,45,48.',
    'Flint sliding attention includes the current position and 512 prior positions, with RoPE; full attention skips RoPE.',
    'The zoom visits actual Flint layers 2,5,6. The timeline uses illustrative positions 1024 through 1152.',
    'Masked older positions are unavailable to the current sliding layer, rather than erased from the model.',
    'Code is copied from patch 0003. The selected expression is underlined; booleans show that layer’s settings.',
    'The diagram omits feed-forward blocks, attention sinks, head geometry, and runtime costs.',
    'The animation explains architecture support and does not attribute the coding-test difference to an isolated architecture choice.'
  ],
  frame(t){
    const time=t*26/22;
    if(time<25)return frame(time);
    const u=ease(time,25,26);
    return g(frame(24),1-u)+g(frame(0),u);
  }
};
