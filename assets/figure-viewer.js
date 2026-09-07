(()=>{'use strict';document.querySelectorAll('.report-figure').forEach(figure=>{
const viewport=figure.querySelector('.figure-viewport'),img=viewport.querySelector('img'),label=figure.querySelector('.figure-scale');let zoom=1,drag;
function scale(value){zoom=Math.max(.5,Math.min(12,value));img.style.width=(zoom*100)+'%';label.textContent=Math.round(zoom*100)+'%'}
figure.querySelector('[data-zoom-in]').addEventListener('click',()=>scale(zoom*1.25));
figure.querySelector('[data-zoom-out]').addEventListener('click',()=>scale(zoom/1.25));
figure.querySelector('[data-zoom-fit]').addEventListener('click',()=>{scale(1);viewport.scrollTo(0,0)});
viewport.addEventListener('pointerdown',e=>{if(e.pointerType!=='mouse'||e.button!==0)return;drag={x:e.clientX,y:e.clientY,left:viewport.scrollLeft,top:viewport.scrollTop};viewport.setPointerCapture(e.pointerId);viewport.classList.add('dragging');e.preventDefault()});
viewport.addEventListener('pointermove',e=>{if(!drag)return;viewport.scrollLeft=drag.left+drag.x-e.clientX;viewport.scrollTop=drag.top+drag.y-e.clientY});
function stop(){drag=null;viewport.classList.remove('dragging')}viewport.addEventListener('pointerup',stop);viewport.addEventListener('pointercancel',stop);viewport.addEventListener('lostpointercapture',stop);
scale(1);
});})();
