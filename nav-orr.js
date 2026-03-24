const NAV_CONFIG = {
  brandName:  '2516 Technologies',
  clientName: 'CJ Orr | Orr Group',
  ctaText:    'Schedule a Call',
  ctaEmail:   'mark@2516technologies.com',
  pages: [
    { label: 'Home',         file: 'orr-index.html' },
    { label: 'Opportunity',  file: 'orr-opportunity.html' },
    { label: 'Market Sizing', file: 'orr-market-sizing.html' },
    { label: 'Assessment',   file: 'orr-assessment.html' },
    { label: 'Architecture', file: 'orr-architecture.html' },
    { label: 'Roadmap',      file: 'orr-roadmap.html' },
    { label: 'Delivery',     file: 'orr-delivery.html' },
    { label: 'Investment',   file: 'orr-investment.html' },
    { label: 'Why 2516',     file: 'orr-why-2516.html' },
    { label: 'Next Steps',   file: 'orr-next-steps.html' },
  ]
};

// (rest of nav.js logic below — copy from assets/nav.js)
 * ─────────────────────────────────────────────────────────────────
 */

const NAV_CONFIG = {
  brandName:  '2516 Technologies',
  clientName: '[CLIENT NAME]',        // ← REPLACE per proposal
  ctaText:    'Schedule a Call',
  ctaEmail:   'mark@2516technologies.com',
  pages: [
    { label: 'Home',         file: 'orr-index.html' },
    { label: 'Opportunity',  file: 'orr-opportunity.html' },
    { label: 'Market Sizing', file: 'orr-market-sizing.html' },
    { label: 'Assessment',   file: 'orr-assessment.html' },
    { label: 'Architecture', file: 'orr-architecture.html' },
    { label: 'Roadmap',      file: 'orr-roadmap.html' },
    { label: 'Delivery',     file: 'orr-delivery.html' },
    { label: 'Investment',   file: 'orr-investment.html' },
    { label: 'Why 2516',     file: 'orr-why-2516.html' },
    { label: 'Next Steps',   file: 'orr-next-steps.html' },
  ]
};

/* ── Build & inject nav ─────────────────────────────────────────── */
function buildNav() {
  const currentFile = window.location.pathname.split('/').pop() || 'orr-index.html';

  const linkHTML = NAV_CONFIG.pages.map(p => {
    const isActive = currentFile === p.file ? ' class="active"' : '';
    return `<a href="${p.file}"${isActive}>${p.label}</a>`;
  }).join('');

  const drawerHTML = NAV_CONFIG.pages.map(p => {
    const isActive = currentFile === p.file ? ' class="active"' : '';
    return `<a href="${p.file}"${isActive}>${p.label}</a>`;
  }).join('');

  const navHTML = `
    <nav class="site-nav" role="navigation" aria-label="Main navigation">
      <div class="nav-inner">
        <div class="nav-brand" style="display:flex;align-items:center;gap:10px;">
          <img src="https://www.2516technologies.com/2516_logo_horizontal_dark_web.png"
               alt="2516 Technologies"
               style="height:22px;width:auto;object-fit:contain;opacity:0.92;"
               onerror="this.style.display='none';this.nextElementSibling.style.display='inline';">
          <span style="display:none;">${NAV_CONFIG.brandName}</span>
          <span style="color:var(--text-muted);font-size:10px;letter-spacing:0.1em;text-transform:uppercase;padding-left:8px;border-left:1px solid var(--border-default);">/ ${NAV_CONFIG.clientName}</span>
        </div>
        <div class="nav-links" role="menubar">
          ${linkHTML}
        </div>
        <div class="nav-right">
          <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme" title="Toggle dark/light mode">
            ☀️
          </button>
          <a href="mailto:${NAV_CONFIG.ctaEmail}" class="nav-cta">
            ${NAV_CONFIG.ctaText}
          </a>
          <button class="nav-hamburger" id="navHamburger" aria-label="Open menu">
            <span></span><span></span><span></span>
          </button>
        </div>
      </div>
    </nav>
    <div class="nav-drawer" id="navDrawer" role="menu">
      ${drawerHTML}
      <a href="mailto:${NAV_CONFIG.ctaEmail}" class="nav-cta" style="margin-top:8px;display:inline-flex;width:fit-content;">
        ${NAV_CONFIG.ctaText}
      </a>
    </div>
  `;

  document.body.insertAdjacentHTML('afterbegin', navHTML);
}

/* ── Theme management ───────────────────────────────────────────── */
function getStoredTheme() {
  return localStorage.getItem('2516-theme') || 'dark';
}

function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('2516-theme', theme);
  const btn = document.getElementById('themeToggle');
  if (btn) btn.textContent = theme === 'dark' ? '☀️' : '🌙';
}

function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme') || 'dark';
  applyTheme(current === 'dark' ? 'light' : 'dark');
}

/* ── Mobile hamburger ───────────────────────────────────────────── */
function initHamburger() {
  const btn    = document.getElementById('navHamburger');
  const drawer = document.getElementById('navDrawer');
  if (!btn || !drawer) return;

  btn.addEventListener('click', () => {
    drawer.classList.toggle('open');
    btn.setAttribute('aria-expanded', drawer.classList.contains('open'));
  });

  // Close drawer when a link is clicked
  drawer.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => drawer.classList.remove('open'));
  });

  // Close on outside click
  document.addEventListener('click', e => {
    if (!btn.contains(e.target) && !drawer.contains(e.target)) {
      drawer.classList.remove('open');
    }
  });
}

/* ── Scroll progress bar (optional, appended to nav) ───────────── */
function initScrollProgress() {
  const bar = document.createElement('div');
  bar.style.cssText = `
    position:fixed; top:60px; left:0; right:0; height:2px; z-index:101;
    background:linear-gradient(90deg, var(--accent-primary), var(--accent-secondary));
    transform-origin:left; transform:scaleX(0);
    transition:transform 0.1s linear;
  `;
  document.body.appendChild(bar);

  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress  = docHeight > 0 ? scrollTop / docHeight : 0;
    bar.style.transform = `scaleX(${progress})`;
  }, { passive: true });
}

/* ── Boot ───────────────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  buildNav();
  applyTheme(getStoredTheme());

  document.getElementById('themeToggle')?.addEventListener('click', toggleTheme);
  initHamburger();
  initScrollProgress();
});
