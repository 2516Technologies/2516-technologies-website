with open('blog.html', 'r') as f:
    c = f.read()

# Fix desktop nav - replace minimal links with full set, Blog marked active
c = c.replace(
    '''    <ul class="nav-links">
      <li><a href="index.html#gain">What You Gain</a></li>
      <li><a href="data-health-check.html">Data Health Check</a></li>
      <li><a href="pharma.html">Pre-Commercial Pharma</a></li>
      <li><a href="about.html">About</a></li>
      <li><a href="blog.html" class="active">Writing</a></li>
      <li><a href="contact.html">Contact</a></li>
    </ul>''',
    '''    <ul class="nav-links">
      <li><a href="index.html">Home</a></li>
      <li><a href="services.html">What You Gain</a></li>
      <li><a href="assessment.html">Data Health Check</a></li>
      <li><a href="pharma.html">Pre-Commercial Pharma</a></li>
      <li><a href="blog.html" class="active">Blog</a></li>
      <li><a href="about.html">About</a></li>
      <li><a href="contact.html">Contact</a></li>
    </ul>'''
)

# Fix mobile menu
c = c.replace(
    '''  <div class="mobile-menu" id="mobile-menu">
    <a href="index.html#gain">What You Gain</a>
    <a href="data-health-check.html">Data Health Check</a>
    <a href="pharma.html">Pre-Commercial Pharma</a>
    <a href="about.html">About</a>
    <a href="blog.html" class="active">Writing</a>
    <a href="contact.html">Contact</a>
  </div>''',
    '''  <div class="mobile-menu" id="mobile-menu">
    <a href="index.html">Home</a>
    <a href="services.html">What You Gain</a>
    <a href="assessment.html">Data Health Check</a>
    <a href="pharma.html">Pre-Commercial Pharma</a>
    <a href="blog.html" class="active">Blog</a>
    <a href="about.html">About</a>
    <a href="contact.html">Contact</a>
    <a href="contact.html" class="nav-cta">Book a Call</a>
  </div>'''
)

with open('blog.html', 'w') as f:
    f.write(c)

print("Done — nav links updated")
print("Run: git add blog.html && git commit -m 'Update blog.html nav links' && git push")
