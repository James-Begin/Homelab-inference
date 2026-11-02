import {C,ease,lerp,g,text,rect,line,path,routePath,traveling} from './drawing.mjs';

const rowY=[302,400,498];
const rowNames=['rows 0–7','rows 8–15','rows 16–23'];

function frame(t){
  const firstAdvance=ease(t,4.7,5.5);
  const lastAdvance=ease(t,9.1,9.9);
  const current=firstAdvance<.5?0:lastAdvance<.5?1:2;
  const next=current+1;
  const currentIx=current*8;
  const isLast=current===2;
  const hint1=ease(t,1.4,3.4);
  const hint2=ease(t,6,8.1);
  const request=current===0?hint1:current===1?hint2:1;
  const transferAlpha=current===0?ease(t,1.1,1.4)*(1-ease(t,4.3,4.7)):
    current===1?ease(t,5.7,6)*(1-ease(t,8.7,9.1)):0;
  const cacheAlpha=current===0?ease(t,3.25,3.6)*(1-ease(t,4.3,4.7)):
    current===1?ease(t,7.95,8.3)*(1-ease(t,8.7,9.1)):0;
  const conditionAlpha=ease(t,10.1,10.7);
  const selectorY=lerp(rowY[0],rowY[1],firstAdvance)+98*lastAdvance;

  let s=text('Prefetch the next eight rows',800,108,43,C.white,{serif:true})
    +text('My added cache hint runs ahead of the existing AVX2 computation.',800,174,27,C.muted)
    +text('Weight groups in memory',330,251,29,C.white)
    +text('L1 cache line · 64 B',880,251,29,C.white)
    +text('AVX2 computation',1285,251,29,C.white);

  for(let i=0;i<3;i++){
    const active=i===current;
    s+=rect(100,rowY[i],460,72,active?C.teal:C.faint,C.bg,active?2.5:1.5,3)
      +text(rowNames[i],330,rowY[i]+46,29,active?C.teal:C.muted,{mono:true});
    if(i===next&&!isLast){
      s+=g(rect(100,rowY[i],24,72,C.amber,C.amber,1,0),transferAlpha)
        +g(text('start',148,rowY[i]+46,25,C.amber,{anchor:'start'}),transferAlpha);
    }
  }
  s+=path(`M 580 ${selectorY+20} L 595 ${selectorY+36} L 580 ${selectorY+52}`,C.teal,3)
    +text('ix = '+currentIx,330,605,28,C.white,{mono:true});

  s+=rect(750,352,260,72,C.line,C.bg,2,3)
    +g(rect(750,352,260,72,C.amber,C.bg,2.5,3)
      +text(rowNames[next]+' start',880,397,26,C.amber),cacheAlpha)
    +g(text(isLast?'no next group':'awaiting hint',880,397,26,C.muted),1-cacheAlpha)
    +text('_MM_HINT_T0',880,477,26,C.amber,{mono:true})
    +text('hint, not a guarantee',880,520,26,C.muted);

  if(!isLast){
    const points=[[560,rowY[next]+36],[660,rowY[next]+36],[660,388],[750,388]];
    s+=g(routePath(points,C.amber,2)+traveling(points,request,C.amber,18),transferAlpha);
  }

  s+=rect(1130,302,350,268,C.line,C.bg,2,3)
    +text(rowNames[current],1305,347,29,C.teal,{mono:true})
    +text('current group',1305,393,26,C.muted);
  const computeStart=current===0?0:current===1?5.5:9.9;
  for(let i=0;i<8;i++){
    const baseX=1175+i*35;
    const progress=(t-computeStart)*.5+i*.12;
    const pulse=(Math.sin(progress*Math.PI*2)+1)/2;
    s+=line(baseX,442,baseX,520,C.faint,8)
      +line(baseX,520,baseX,lerp(495,444,pulse),C.teal,8);
  }
  s+=text('8 rows per iteration',1305,605,27,C.muted);

  s+=line(100,634,1500,634,C.faint,1.5)
    +text('if (ix + 8 < nrc_x) {',150,683,27,isLast?C.amber:C.white,{mono:true,anchor:'start'})
    +text('_mm_prefetch((const char *)vx + (ix + 8)*bx, _MM_HINT_T0);',210,726,26,isLast?C.muted:C.teal,{mono:true,anchor:'start'})
    +text('}',150,769,27,C.white,{mono:true,anchor:'start'});

  if(isLast){
    s+=g(text('16 + 8 < 24 is false → skip the hint',800,819,28,C.amber,{mono:true}),conditionAlpha);
  }else{
    s+=text('Compute this group while requesting the next group’s starting line.',800,819,27,C.muted);
  }
  s+=text('Illustrative 24-row loop · timing and cache arrival are schematic',800,873,24,C.muted);
  return s;
}

export default {
  id:'avx2-prefetch',
  title:'Prefetch the next eight rows',
  duration:16,
  poster:3.7,
  checks:[0,1.7,3.7,5.5,7.4,8.4,10.7,12.5,15.95],
  facts:[
    'Patch 0002 adds the displayed guarded _mm_prefetch in mul_mat_q4_0_r8_q8_2_avx2.',
    'The loop advances ix by eight rows; bx is the row stride.',
    'The request targets the cache line containing the next group’s starting address.',
    'Talos uses 64-byte cache lines. The hint does not fetch an entire eight-row group.',
    'The 24-row loop, cache arrival, and computation timing are illustrative.',
    'The final illustrative group has ix = 16, so ix + 8 < nrc_x is false.',
    'Vector arithmetic and the repacked format are upstream; the shown prefetch lines are the local change.',
    'No isolated speedup, guaranteed cache residency, or exact hardware schedule is asserted.'
  ],
  frame(t){
    if(t<15.4)return frame(Math.min(t,12.5));
    const u=ease(t,15.4,16);
    return g(frame(12.5),1-u)+g(frame(0),u);
  }
};
