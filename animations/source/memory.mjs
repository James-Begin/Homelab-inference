import {C,ease,g,text,rect,line,traveling,routePath} from './drawing.mjs';

function diagram(t){
  const cachePath=[[230,430],[230,398],[312,398],[312,363]];
  const localPath=[[190,590],[190,398],[312,398],[312,363]];
  const requestPath=[[312,363],[312,350],[1130,350],[1130,590]];
  const responsePath=[[1130,590],[1130,378],[312,378],[312,363]];
  let s=text('Cache, local RAM, or a trip across QPI',800,108,43,C.white,{serif:true});
  s+=text('Talos · current memory inventory · 31 October 2026',800,174,27,C.muted);
  [90,1030].forEach((x,k)=>{
    s+=rect(x,230,480,292,C.line,C.bg,2);
    s+=text('Socket '+k+' · 14 cores',x+240,275,29,C.white);
    for(let i=0;i<14;i++){
      const cx=x+60+(i%7)*54,cy=315+Math.floor(i/7)*48;
      s+=rect(cx-19,cy-16,38,32,k===0&&i===10?C.teal:C.line,C.bg,1.5);
    }
    s+=rect(x+38,430,404,64,C.violet,C.bg,1.5);
    s+=text('35 MiB L3',x+240,472,28,C.violet,{mono:true});
    for(const offset of [100,240,380])s+=line(x+offset,522,x+offset,590,C.blue,1.5);
    s+=rect(x,590,480,140,C.blue,C.bg,2);
    s+=text('128 GB local DDR4',x+240,630,29,C.blue);
    s+=text('3 channels · 1866 MT/s',x+240,672,27,C.white);
    s+=text('≈44.8 GB/s bus ceiling',x+240,713,27,C.blue,{mono:true});
  });
  s+=text('2 bidirectional QPI links',800,270,30,C.amber);
  s+=text('up to 9.6 GT/s per link',800,315,27,C.amber);
  s+=line(570,350,1030,350,C.amber,1.5)+line(570,378,1030,378,C.amber,1.5);
  s+=text('≈34.1 GB/s',800,441,31,C.amber,{mono:true});
  s+=text('64 B response ceiling',800,481,25,C.muted);
  s+=text('one direction · both links',800,520,25,C.muted);
  s+=text('L1 read peak',800,591,26,C.teal);
  s+=text('64 B/cycle per core',800,632,27,C.teal,{mono:true});
  s+=text('2 × 32 B loads',800,673,25,C.muted);
  const phase=t<4?'L3 cache hit':t<8?'Local DRAM read':t<10.7?'Remote read: request crosses QPI':'Remote read: data returns over QPI';
  const color=t<4?C.violet:t<8?C.teal:C.amber;
  s+=text(phase,800,776,31,color);
  function packet(points,start,end,fadeEnd,color,size=23){
    const a=ease(t,start,start+.25)*(1-ease(t,end,fadeEnd));
    return g(routePath(points,color,2.5,ease(t,start,start+.45))+traveling(points,ease(t,start+.2,end),color,size),a);
  }
  if(t<4)s+=packet(cachePath,.7,2.7,3.6,C.violet);
  else if(t<8)s+=packet(localPath,4.1,6.7,7.7,C.teal);
  else{
    s+=packet(requestPath,8.1,10.5,10.9,C.amber,17);
    s+=packet(responsePath,10.8,13.6,14.6,C.amber,25);
    if(t>=13.6)s+=g(routePath(responsePath,C.amber,2)+rect(293,347,38,32,C.amber,C.bg,2),ease(t,13.6,14.2));
  }
  s+=text('Intel reference hit latency: L1D 4–6 · L2 12 · L3 50–60 core cycles',800,823,25,C.muted);
  s+=text('RAM/QPI figures are theoretical ceilings. Packet timing is illustrative.',800,868,24,C.muted);
  return s;
}

export const memoryScenes=[{
  id:'numa-traffic',title:'Cache, local RAM, and remote memory',duration:18,poster:14.8,
  checks:[0,1.8,5.5,9.5,12.4,14.8,17.95],
  frame(t){
    if(t<17.4)return diagram(Math.min(t,14.8));
    const u=ease(t,17.4,18);
    return g(diagram(14.8),1-u)+g(diagram(0),u);
  }
}];
