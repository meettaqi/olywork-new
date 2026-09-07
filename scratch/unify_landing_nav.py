import re

nav_html = """<div class="navwrap"><nav class="nav" style="position:fixed;top:0;width:100%;height:80px;display:flex;align-items:center;justify-content:space-between;padding:0 48px;background:rgba(244,242,236,0.95);backdrop-filter:blur(12px);border-bottom:1px solid rgba(232,229,218,0.6);z-index:50;left:0;">
  <a class="brand" href="/" style="display:flex;align-items:center;gap:8px;font-family:var(--display);font-weight:800;font-size:24px;letter-spacing:-0.04em;">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:24px;height:24px;"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
    Olywork
  </a>
  <div class="links" style="display:flex;gap:32px;align-items:center;">
    <a href="/catalog" style="font-weight:500;">Catalog</a>
    <a href="/docs" style="font-weight:500;">API</a>
    <a href="/tutorial" style="font-weight:500;">Tutorial</a>
    <a href="/app" style="background:var(--ink);color:var(--bg);padding:10px 24px;border-radius:99px;font-weight:600;">Start free</a>
  </div>
</nav></div>"""

with open("src/olywork/web/landing.html", "r") as f:
    landing = f.read()

landing = re.sub(r'<nav class="navbar">.*?</nav>', nav_html, landing, flags=re.DOTALL)

with open("src/olywork/web/landing.html", "w") as f:
    f.write(landing)

