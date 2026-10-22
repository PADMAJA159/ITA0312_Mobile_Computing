const modal = document.getElementById('loginModal');
const toast = document.getElementById('toast');
let toastTimer;
function notify(message){
  toast.textContent = message;
  toast.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(()=>toast.classList.remove('show'), 2800);
}
document.getElementById('loginOpen').addEventListener('click',()=>{modal.classList.add('open');modal.setAttribute('aria-hidden','false');});
document.getElementById('loginClose').addEventListener('click',()=>{modal.classList.remove('open');modal.setAttribute('aria-hidden','true');});
modal.addEventListener('click',e=>{if(e.target===modal){modal.classList.remove('open');modal.setAttribute('aria-hidden','true');}});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){modal.classList.remove('open');modal.setAttribute('aria-hidden','true');}});
document.getElementById('getStarted').addEventListener('click',()=>document.querySelector('.signup-panel').scrollIntoView({behavior:'smooth',block:'center'}));
document.getElementById('learnMore').addEventListener('click',()=>document.getElementById('features').scrollIntoView({behavior:'smooth'}));
document.getElementById('registerForm').addEventListener('submit',e=>{
  e.preventDefault();
  const name = new FormData(e.currentTarget).get('name').trim();
  document.getElementById('registerMessage').textContent = `Thanks, ${name}! Your demo registration is complete.`;
  e.currentTarget.reset();
  notify('Demo account created — connect a backend for real accounts.');
});
document.getElementById('loginForm').addEventListener('submit',e=>{
  e.preventDefault();
  document.getElementById('loginMessage').textContent='Demo login submitted. Authentication is not connected yet.';
  notify('Demo login submitted.');
});
document.querySelectorAll('[data-action]').forEach(button=>{
  button.addEventListener('click',()=>notify(button.dataset.action));
});
