document.getElementById('year') && (document.getElementById('year').textContent = new Date().getFullYear());
document.querySelectorAll('.nav-toggle').forEach(btn => btn.addEventListener('click', () => btn.closest('.nav').classList.toggle('open')));
