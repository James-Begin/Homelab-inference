import {C,ease,lerp,g,text,rect,line,path,check,cross} from './drawing.mjs';

const xs=[500,700,900,1100];
const token=(label,x,y,color=C.violet,alpha=1)=>g(
  rect(x-58,y-37,116,74,color,C.bg,2.5,4)+
  text(label,x,y+10,32,color,{mono:true}),alpha);

function historyUpdate(t){
  const bridge=ease(t,5.15,6);
  const detail=1-ease(t,5.05,5.65);
  const i=Math.min(3,Math.floor(Math.max(0,t-2.45)/.61));
  const active=ease(t,2.05,2.45)*(1-ease(t,4.85,5.15));
  const first=380,step=120;
  let s='';
  let code=text('Example indices: n = 4, i_last = 0, cur_len = 8',800,239,27,C.muted,{mono:true});
  code+=text('before',245,321,27,C.muted);
  code+=text('if (i_last + 32 < cur_len)',800,321,29,C.white,{mono:true});
  code+=g(text('32 < 8',1246,321,27,C.red,{mono:true})+cross(1370,312,C.red),ease(t,.65,1.15));
  code+=text('patch',245,408,27,C.teal);
  code+=text('if (i_last < cur_len - n)',800,408,29,C.teal,{mono:true});
  code+=g(text('0 < 4',1246,408,27,C.teal,{mono:true})+check(1370,398,C.teal),ease(t,1.15,1.7));
  code+=line(160,453,1440,453,C.faint,1.5);
  s+=g(code,detail);

  for(let k=0;k<8;k++){
    const inWindow=k>=i&&k<i+4;
    const following=k===i+4;
    const color=active>.1?(inWindow?C.teal:following?C.violet:C.line):C.white;
    const x=k>=4?lerp(first+k*step,xs[k-4],bridge):first+k*step;
    const y=k>=4?lerp(566,290,bridge):566;
    s+=token('h'+k,x,y,color,k>=4?1:1-bridge);
  }
  let window='';
  window+=rect(first+i*step-67,516,494,101,C.teal,'none',2,6);
  window+=text('i = '+i,first+i*step+180,660,27,C.teal,{mono:true});
  window+=text('context',first+i*step+180,494,27,C.teal);
  window+=text('next token',first+(i+4)*step,660,27,C.violet);
  window+=text('mod.add(prompt_tgt.data() + i);',800,738,29,C.white,{mono:true});
  s+=g(window,active*detail);
  s+=g(text('Add each available context and its next token.',800,737,29,C.muted),
    (1-ease(t,2.05,2.45))*detail);
  return s;
}

function diagram(t){
  let s='';
  const fold=ease(t,3.9,4.7);
  const contextIn=ease(t,.9,2.1);
  let lookup=text('4-token context',800,222,29,C.white);
  for(let i=0;i<4;i++){
    lookup+=token('h'+(i+4),xs[i],lerp(290,465,contextIn),C.white,1-ease(t,1.95,2.3));
  }
  lookup+=path('M 800 338 V 377',C.line,2,1-ease(t,.95,1.3));
  lookup+=rect(390,385,820,160,C.line,C.bg,2,4);
  lookup+=text('Token-history lookup',800,428,30,C.white);
  for(let i=0;i<3;i++){
    const active=ease(t,1.8+i*.12,2.05+i*.12)*(1-ease(t,3.45,3.8));
    lookup+=rect(430,451+i*24,740,16,i===1&&active>.15?C.teal:C.faint,C.bg,1.5,1);
  }
  lookup+=g(path('M 1210 426 H 1270 V 510 H 1210',C.teal,2)+
    path('M 1221 503 L 1210 510 L 1221 517',C.teal,2)+
    text('repeat',1342,477,25,C.teal),ease(t,2.1,2.4));
  lookup+=text('Proposed continuation',800,738,28,C.muted);
  s+=g(lookup,1-fold);

  const judged=ease(t,6.15,6.75);
  const transfer=ease(t,7.25,8.55);
  const modelOpacity=ease(t,4.35,4.95)*(1-ease(t,7.55,8.4));
  let model=rect(390,475,820,95,C.blue,C.bg,2,4);
  model+=text('Flint · one verification batch',800,533,30,C.blue);
  s+=g(model,modelOpacity);
  for(let i=0;i<4;i++){
    const arrival=ease(t,2.35+i*.24,2.98+i*.24);
    const sourceY=lerp(485,645,arrival);
    let y=lerp(sourceY,385,fold);
    let alpha=arrival;
    let color=C.violet;
    if(i<2){
      y=lerp(y,660,transfer);
      if(judged>.45)color=C.teal;
    }else if(i===2){
      alpha*=1-ease(t,7.25,7.95);
      if(judged>.45)color=C.red;
    }else{
      y-=70*ease(t,7.25,8.05);
      alpha*=1-ease(t,7.25,8.05);
      if(judged>.45)color=C.muted;
    }
    s+=g(path(`M ${xs[i]} 425 V 467`,C.line,2,ease(t,4.75,5.45))+
      path(`M ${xs[i]-7} 456 L ${xs[i]} 467 L ${xs[i]+7} 456`,C.line,2,ease(t,4.75,5.45)),
      1-ease(t,7.15,7.65));
    s+=token('d'+i,xs[i],y,color,alpha);
    if(i<2){
      s+=g(check(xs[i],321,C.teal,judged),1-ease(t,7.25,7.9));
    }else if(i===2){
      s+=g(cross(xs[i],321,C.red,judged),1-ease(t,7.25,7.9));
    }else{
      s+=g(text('after mismatch',xs[i],324,24,C.muted),judged*(1-ease(t,7.25,7.9)));
    }
  }

  const correction=ease(t,7.55,8.55);
  s+=token('c2',900,lerp(530,660,correction),C.amber,correction);
  s+=g(text('discarded',1100,388,27,C.muted),ease(t,7.85,8.3)*(1-ease(t,8.7,9.15)));
  s+=g(text('Returned continuation',800,600,28,C.white),ease(t,7.7,8.35));
  s+=g(text('2 accepted draft tokens + 1 correction',800,754,29,C.teal),ease(t,8.45,9.05));
  return s;
}

export default {
  id:'draft-and-verify',
  title:'Update the history. Reuse the continuation.',
  duration:16,
  poster:4.4,
  checks:[0,1.6,2.7,3.4,4.4,5.6,6.3,8.8,10.7,11.7,13.2,14.7,15.8],
  frame(t){
    const mechanism=u=>diagram(Math.max(0,(u-6)/.85));
    const body=u=>u<5.65?historyUpdate(u):u<6?
      g(historyUpdate(u),1-ease(u,5.65,6))+g(diagram(0),ease(u,5.65,6)):mechanism(u);
    const reset=ease(t,15.4,16);
    const content=t<15.4?body(t):g(body(15.4),1-reset)+g(body(0),reset);
    return text('Update the history. Reuse the continuation.',800,108,43,C.white,{serif:true})+
      text('ngram-mod · 4-token context · up to 4 draft tokens',800,174,27,C.muted)+
      content+
      text('Actual patch and settings; token positions and acceptance are examples.',800,824,25,C.muted);
  }
};
