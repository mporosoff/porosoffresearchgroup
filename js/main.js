/* ============================================================
   POROSOFF RESEARCH GROUP — Shared JS
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  /* ── Mobile hamburger ── */
  const toggle = document.querySelector('.nav-toggle');
  const drawer = document.querySelector('.nav-drawer');
  if (toggle && drawer) {
    toggle.addEventListener('click', () => {
      toggle.classList.toggle('open');
      drawer.classList.toggle('open');
    });
    // Close drawer on link click
    drawer.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        toggle.classList.remove('open');
        drawer.classList.remove('open');
      });
    });
  }

  /* ── Active nav link ── */
  const page = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a, .nav-drawer a').forEach(a => {
    const href = a.getAttribute('href');
    if (href === page || (page === '' && href === 'index.html')) {
      a.classList.add('active');
    }
  });

  /* ── News archive accordion ── */
  document.querySelectorAll('.archive-toggle').forEach(btn => {
    btn.addEventListener('click', () => {
      const body = btn.nextElementSibling;
      btn.classList.toggle('open');
      if (body) body.classList.toggle('open');
    });
  });

});
