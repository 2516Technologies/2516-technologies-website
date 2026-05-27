import re

with open('about.html', 'r') as f:
    c = f.read()

# Fix the broken desktop nav - replace the entire ul.nav-links block
old_nav_links = '''  <ul class="nav-links">
    <li><a href="index.html" class="active">Home</a></li>
    <li><a href="services.html">What You Gain</a></li>
    <li><a href="assessment.html">Data Health Check</a></li>
    <li><a href="pharma.html">Pre-Commercial Pharma</a></li>
    <li><a href="blog.html">Blog</a></li>
    <li><a href="blog.html">Blog</a>
    <a href="about.html">About</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ul>'''

new_nav_links = '''  <ul class="nav-links">
    <li><a href="index.html">Home</a></li>
    <li><a href="services.html">What You Gain</a></li>
    <li><a href="assessment.html">Data Health Check</a></li>
    <li><a href="pharma.html">Pre-Commercial Pharma</a></li>
    <li><a href="blog.html">Blog</a></li>
    <li><a href="about.html" class="active">About</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ul>'''

c = c.replace(old_nav_links, new_nav_links)

# Fix the mobile menu - it already has Blog, just make sure it's clean
old_mobile = '''<div class="mobile-menu">
<a href="index.html" class="active">Home</a>
    <a href="services.html">What You Gain</a>
    <a href="pharma.html">Pre-Commercial Pharma</a>
    <a href="blog.html">Blog</a>
    <a href="about.html">About</a>
    <a href="contact.html">Contact</a>
  <a href="contact.html" class="nav-cta">Book a Call</a>
  <a href="assessment.html" class="nav-cta">Data Health Check</a>
</div>'''

new_mobile = '''<div class="mobile-menu">
  <a href="index.html">Home</a>
  <a href="services.html">What You Gain</a>
  <a href="assessment.html">Data Health Check</a>
  <a href="pharma.html">Pre-Commercial Pharma</a>
  <a href="blog.html">Blog</a>
  <a href="about.html" class="active">About</a>
  <a href="contact.html">Contact</a>
  <a href="contact.html" class="nav-cta">Book a Call</a>
</div>'''

c = c.replace(old_mobile, new_mobile)

with open('about.html', 'w') as f:
    f.write(c)

print("about.html fixed")
print("\nRun: git add -A && git commit -m \"Fix about.html nav\" && git push")
