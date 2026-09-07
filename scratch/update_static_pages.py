import os, re

# The canonical nav block to inject into every static page
NAV_BLOCK = '''<nav class="ow-nav" aria-label="Main navigation">
  <a class="ow-nav-brand" href="/">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
    Olywork
  </a>
  <div class="ow-nav-links">
    <a href="/catalog">Catalog</a>
    <a href="/docs">API Docs</a>
    <a href="/tutorial">Tutorial</a>
    <a href="/pricing">Pricing</a>
    <a href="/app" class="ow-btn-nav">Start free &rarr;</a>
  </div>
</nav>'''

FOOTER_BLOCK = '''<footer class="ow-footer">
  <div class="ow-footer-inner">
    <div>
      <div class="ow-footer-brand-name">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:22px;height:22px;"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        Olywork
      </div>
      <div class="ow-footer-tagline">The OpenRouter for AI Agent Tools.<br>One token. 2,800+ endpoints. Zero key management.</div>
    </div>
    <nav class="ow-footer-cols">
      <div class="ow-footer-col">
        <div class="ow-footer-col-label">Explore</div>
        <a href="/catalog">Catalog</a>
        <a href="/pricing">Pricing</a>
      </div>
      <div class="ow-footer-col">
        <div class="ow-footer-col-label">Build</div>
        <a href="/tutorial">Tutorial</a>
        <a href="/docs">API Reference</a>
      </div>
      <div class="ow-footer-col">
        <div class="ow-footer-col-label">Company</div>
        <a href="/support">Support</a>
        <a href="/terms">Terms</a>
        <a href="/privacy">Privacy</a>
      </div>
    </nav>
  </div>
  <div class="ow-footer-bottom">
    <span>&copy; 2025 Olywork. All rights reserved.</span>
    <span>Open source &middot; Pay-per-call &middot; No markup</span>
  </div>
</footer>'''

FONTS_LINK = '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'
OLY_CSS_LINK = '<link rel="stylesheet" href="/olywork.css"/>'

pages = ["privacy.html", "terms.html", "support.html"]
web_dir = "src/olywork/web"

for page in pages:
    path = os.path.join(web_dir, page)
    if not os.path.exists(path):
        print(f"Skipping {page} (not found)")
        continue
    with open(path) as f:
        content = f.read()

    # Ensure Plus Jakarta Sans is loaded
    if "Plus Jakarta Sans" not in content:
        content = content.replace("</head>", f"{FONTS_LINK}\n</head>")
    if "/olywork.css" not in content:
        content = content.replace("</head>", f"{OLY_CSS_LINK}\n</head>")

    # Remove old topbar/nav variations and inject clean nav
    # Pattern: any existing nav-like structure
    content = re.sub(r'<div class="topbar">.*?</div>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<nav class="ow-nav".*?</nav>', '', content, flags=re.DOTALL)
    # Inject after <body>
    content = content.replace('<body>', f'<body>\n{NAV_BLOCK}\n', 1)

    # Update/replace footer
    old_footer = re.search(r'<footer.*?</footer>', content, re.DOTALL)
    if old_footer:
        content = content[:old_footer.start()] + FOOTER_BLOCK + content[old_footer.end():]
    else:
        content = content.replace('</body>', f'\n{FOOTER_BLOCK}\n</body>')

    with open(path, "w") as f:
        f.write(content)
    print(f"Updated: {page}")

print("Done")
