// header scroll
const header=document.getElementById('header');
if(header) window.addEventListener('scroll',()=>header.classList.toggle('scrolled',window.scrollY>40));

// mobile menu
const burger=document.getElementById('burger'), menu=document.getElementById('menu');
if(burger&&menu){
  burger.addEventListener('click',()=>menu.classList.toggle('open'));
  menu.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>menu.classList.remove('open')));
}

// reveal on scroll
const io=new IntersectionObserver((es)=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));

// persian digits
const fa=n=>n.toString().replace(/\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d]);

// count up
const co=new IntersectionObserver((es)=>es.forEach(e=>{
  if(!e.isIntersecting)return;
  const el=e.target, target=+el.dataset.count, suf=el.dataset.suffix||'';
  let cur=0; const step=Math.max(1,Math.ceil(target/55));
  const t=setInterval(()=>{cur+=step;if(cur>=target){cur=target;clearInterval(t)}el.textContent=fa(cur)+suf},25);
  co.unobserve(el);
}),{threshold:.5});
document.querySelectorAll('[data-count]').forEach(c=>co.observe(c));

// lightbox for galleries
const lb=document.getElementById('lightbox');
if(lb){
  const lbImg=lb.querySelector('img');
  document.querySelectorAll('.gallery img').forEach(img=>{
    img.addEventListener('click',()=>{lbImg.src=img.src;lb.classList.add('open')});
  });
  lb.addEventListener('click',()=>lb.classList.remove('open'));
  document.addEventListener('keydown',e=>{if(e.key==='Escape')lb.classList.remove('open')});
}

// contact form
function submitForm(e){
  e.preventDefault();
  const note=document.getElementById('formNote');
  if(note){note.textContent='✓ پیام شما با موفقیت ثبت شد. به‌زودی با شما تماس می‌گیریم!';
    note.style.color='#16a34a';note.style.fontWeight='700';}
  e.target.reset();
  return false;
}
