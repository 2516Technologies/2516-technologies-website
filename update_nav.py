import os, re

# ── 1. Add Blog link to all existing pages ──────────────────────────────────
pages = ['index.html', 'about.html', 'contact.html', 'pharma.html', 'data-health-check.html']

for page in pages:
    if not os.path.exists(page):
        print(f"SKIP (not found): {page}")
        continue

    with open(page, 'r') as f:
        c = f.read()

    original = c

    # Desktop nav: insert Blog before About
    c = c.replace(
        '<li><a href="about.html">About</a></li>',
        '<li><a href="blog.html">Blog</a></li>\n    <li><a href="about.html">About</a></li>'
    )

    # Mobile menu: insert Blog before About
    c = c.replace(
        '<a href="about.html">About</a>',
        '<a href="blog.html">Blog</a>\n    <a href="about.html">About</a>'
    )

    if c != original:
        with open(page, 'w') as f:
            f.write(c)
        print(f"Updated: {page}")
    else:
        print(f"NO MATCH (check nav structure): {page}")


# ── 2. Replace blog.html nav with index.html nav style ──────────────────────
if not os.path.exists('blog.html'):
    print("SKIP: blog.html not found")
else:
    with open('blog.html', 'r') as f:
        blog = f.read()

    # The new nav block — matches index.html exactly, with Blog marked active
    new_nav = '''<nav class="nav">
  <a href="index.html" class="nav-brand">
    <div class="jazz-bars">
      <div class="bar bar1"></div>
      <div class="bar bar2"></div>
      <div class="bar bar3"></div>
      <div class="bar bar4"></div>
    </div>
    <span class="nav-wordmark">2516 Technologies</span>
  </a>
  <ul class="nav-links">
    <li><a href="index.html#gain">What You Gain</a></li>
    <li><a href="data-health-check.html">Data Health Check</a></li>
    <li><a href="pharma.html">Pre-Commercial Pharma</a></li>
    <li><a href="about.html">About</a></li>
    <li><a href="blog.html" class="active">Blog</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ul>
  <button class="hamburger" id="hamburger" aria-label="Toggle menu">
    <span class="hamburger-line"></span>
    <span class="hamburger-line"></span>
    <span class="hamburger-line"></span>
  </button>
</nav>
<div class="mobile-menu" id="mobile-menu">
  <a href="index.html#gain">What You Gain</a>
  <a href="data-health-check.html">Data Health Check</a>
  <a href="pharma.html">Pre-Commercial Pharma</a>
  <a href="about.html">About</a>
  <a href="blog.html" class="active">Blog</a>
  <a href="contact.html">Contact</a>
  <a href="contact.html" class="nav-cta">Book a Call</a>
</div>'''

    # Replace blog.html's existing nav + mobile-menu block
    # Find from <nav> to end of </div> (mobile-menu closing)
    nav_start = blog.find('  <!-- NAV -->\n  <nav')
    if nav_start == -1:
        nav_start = blog.find('<nav')

    mobile_end = blog.find('</div>', blog.find('id="mobile-menu"'))
    if mobile_end == -1:
        print("Could not find mobile-menu end in blog.html")
    else:
        mobile_end += len('</div>')
        blog = blog[:nav_start] + new_nav + blog[mobile_end:]
        print("Replaced blog.html nav")

    # Add index.html nav CSS variables and nav styles to blog.html <style>
    # Replace blog's existing nav CSS block with index.html's nav styles
    index_nav_css = """\n    /* NAV — matches index.html */
    .nav{position:fixed;top:0;left:0;right:0;z-index:200;display:grid;grid-template-columns:auto 1fr auto;align-items:center;padding:1.1rem 3.5rem;background:rgba(10,22,40,0.92);backdrop-filter:blur(16px);border-bottom:1px solid var(--border)}
    .nav-brand{display:flex;align-items:center;gap:.9rem;text-decoration:none}
    .nav-wordmark{font-family:'Cormorant Garamond',serif;font-size:1.05rem;font-weight:400;letter-spacing:.18em;text-transform:uppercase;color:var(--text)}
    .nav-links{display:flex;gap:0;list-style:none;justify-content:center}
    .nav-links a{display:block;padding:.45rem 1rem;font-size:.76rem;font-weight:400;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted);text-decoration:none;transition:color .2s}
    .nav-links a:hover{color:var(--text)} .nav-links a.active{color:var(--accent-gold)}
    .nav-cta{background:var(--accent-gold);color:#0A1628;padding:.58rem 1.35rem;border-radius:3px;font-size:.74rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;text-decoration:none;transition:opacity .2s,transform .15s;white-space:nowrap}
    .nav-cta:hover{opacity:.84;transform:translateY(-1px)}
    .hamburger{display:none;flex-direction:column;gap:5px;background:none;border:none;cursor:pointer;padding:8px}
    .hamburger-line{width:22px;height:2px;background:var(--text);border-radius:2px;transition:all 0.3s}
    .hamburger.active .hamburger-line:nth-child(1){transform:rotate(45deg) translate(7px,7px)}
    .hamburger.active .hamburger-line:nth-child(2){opacity:0}
    .hamburger.active .hamburger-line:nth-child(3){transform:rotate(-45deg) translate(7px,-7px)}
    .mobile-menu{display:none;position:fixed;top:60px;left:0;right:0;background:rgba(10,22,40,0.98);border-bottom:1px solid var(--border);padding:1.5rem;flex-direction:column;gap:0;z-index:199}
    .mobile-menu.open{display:flex}
    .mobile-menu a{display:block;padding:0.9rem 0;font-size:0.82rem;font-weight:400;letter-spacing:0.08em;text-transform:uppercase;color:var(--text-muted);text-decoration:none;border-bottom:1px solid var(--border);transition:color .2s}
    .mobile-menu a:last-child{border-bottom:none}
    .mobile-menu a:hover{color:var(--text)}
    .mobile-menu a.active{color:var(--accent-gold)}
    .mobile-menu .nav-cta{background:var(--accent-gold);color:#0A1628;padding:0.7rem 1.2rem;border-radius:3px;text-align:center;margin-top:0.8rem;font-weight:600;border-bottom:none}
    @media(max-width:768px){.hamburger{display:flex}.nav-links{display:none}.nav{display:flex;justify-content:space-between;padding:1rem 1.5rem}}
    /* Jazz bars (small nav version) */
    .jazz-bars{display:flex;align-items:flex-end;gap:3px;height:28px}
    .bar{width:5px;border-radius:2px 2px 0 0;transform-origin:bottom}
    .bar1{height:16px;background:#1e3a8a;animation:b1 1.8s ease-in-out infinite}
    .bar2{height:28px;background:#3b82f6;animation:b2 1.8s ease-in-out infinite .2s}
    .bar3{height:20px;background:#1e3a8a;animation:b3 1.8s ease-in-out infinite .4s}
    .bar4{height:24px;background:#3b82f6;animation:b4 1.8s ease-in-out infinite .1s}
    @keyframes b1{0%,100%{height:16px}50%{height:9px}}
    @keyframes b2{0%,100%{height:28px}50%{height:14px}}
    @keyframes b3{0%,100%{height:20px}50%{height:28px}}
    @keyframes b4{0%,100%{height:24px}50%{height:11px}}\n"""

    # Add index.html CSS vars that blog.html is missing
    index_vars = "--bg:#0A1628;--bg-card:#0F2144;--bg-card2:#0D1C3A;--accent:#4A7FFF;--accent-gold:#C9A84C;--text:#E8EEF8;--text-muted:#8A9BBC;--text-dim:#4A5A78;--border:rgba(74,127,255,0.12);--border-mid:rgba(74,127,255,0.26);--white:#FFFFFF"

    # Replace existing :root vars in blog.html
    blog = re.sub(r':root\s*\{[^}]+\}', ':root{' + index_vars + '}', blog)

    # Remove old nav CSS block and replace with new one
    old_nav_css_start = blog.find('    /* ── NAV ── */')
    if old_nav_css_start == -1:
        old_nav_css_start = blog.find('    /* NAV */')
    old_nav_css_end = blog.find('    /* ── HERO ── */')
    if old_nav_css_end == -1:
        old_nav_css_end = blog.find('    /* HERO */')

    if old_nav_css_start != -1 and old_nav_css_end != -1:
        blog = blog[:old_nav_css_start] + index_nav_css + '    ' + blog[old_nav_css_end:]
        print("Replaced blog.html nav CSS")

    # Fix hamburger JS to use index.html pattern (classList active instead of open)
    old_hamburger_js = """    // Hamburger
    const hamburger = document.getElementById('hamburger');
    const mobileMenu = document.getElementById('mobile-menu');
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('open');
      mobileMenu.classList.toggle('open');
    });"""

    new_hamburger_js = """    // Hamburger
    const hamburger = document.getElementById('hamburger');
    const mobileMenu = document.getElementById('mobile-menu');
    if (hamburger && mobileMenu) {
      hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        mobileMenu.classList.toggle('open');
      });
    }"""

    blog = blog.replace(old_hamburger_js, new_hamburger_js)

    with open('blog.html', 'w') as f:
        f.write(blog)
    print("blog.html updated")

print("\nAll done. Run: git add -A && git commit -m \"Add Blog to nav, sync blog.html nav\" && git push")
