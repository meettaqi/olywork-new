import re

nav_html = """<div class="navwrap"><nav class="nav" style="position:fixed;top:0;width:100%;height:80px;display:flex;align-items:center;justify-content:space-between;padding:0 48px;background:rgba(244,242,236,0.95);backdrop-filter:blur(12px);border-bottom:1px solid rgba(232,229,218,0.6);z-index:50;">
  <a class="brand" href="/" style="display:flex;align-items:center;gap:8px;font-family:var(--display);font-weight:800;font-size:24px;letter-spacing:-0.04em;">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:24px;height:24px;"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
    Olywork
  </a>
  <div class="links" style="display:flex;gap:32px;align-items:center;">
    <a href="/catalog" style="font-weight:500;">Catalog</a>
    <a href="/docs" style="font-weight:500;">API</a>
    <a href="/tutorial" style="font-weight:500;">Tutorial</a>
    <a href="/app" style="background:var(--ink);color:#fff;padding:10px 24px;border-radius:99px;font-weight:600;">Start free</a>
  </div>
</nav></div>"""

footer_html = """<footer style="padding:80px 48px;background:var(--surface);border-top:1px solid var(--border);display:flex;justify-content:space-between;max-width:1200px;margin:100px auto 0;width:100%;">
  <div class="foot-brand" style="max-width:300px;">
    <div class="brand" style="display:flex;align-items:center;gap:8px;font-family:var(--display);font-weight:800;font-size:24px;letter-spacing:-0.04em;margin-bottom:16px;">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:24px;height:24px;"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
      Olywork
    </div>
    <div style="color:var(--muted);font-size:14px;line-height:1.5;">The OpenRouter for AI Agent Tools. One unified token for 2,800+ endpoints.</div>
  </div>
  <nav class="foot-cols" style="display:flex;gap:64px;">
    <div class="foot-col" style="display:flex;flex-direction:column;gap:12px;">
      <div style="font-weight:700;color:var(--ink);margin-bottom:8px;">Explore</div>
      <a href="/catalog" style="color:var(--muted);">Catalog</a>
    </div>
    <div class="foot-col" style="display:flex;flex-direction:column;gap:12px;">
      <div style="font-weight:700;color:var(--ink);margin-bottom:8px;">Build</div>
      <a href="/docs" style="color:var(--muted);">API Docs</a>
      <a href="/tutorial" style="color:var(--muted);">Tutorial</a>
    </div>
    <div class="foot-col" style="display:flex;flex-direction:column;gap:12px;">
      <div style="font-weight:700;color:var(--ink);margin-bottom:8px;">Company</div>
      <a href="/support" style="color:var(--muted);">Support</a>
      <a href="/terms" style="color:var(--muted);">Terms</a>
      <a href="/privacy" style="color:var(--muted);">Privacy</a>
    </div>
  </nav>
</footer>"""

for file_name in ["src/olywork/web/privacy.html", "src/olywork/web/terms.html", "src/olywork/web/support.html", "src/olywork/web/tutorial.html"]:
    with open(file_name, "r") as f:
        content = f.read()

    # Replace topbar
    content = re.sub(r'<div class="topbar">.*?</div></div>', nav_html, content, flags=re.DOTALL)
    # If tutorial has nav, replace that
    content = re.sub(r'<nav class="tut-nav">.*?</nav>', nav_html, content, flags=re.DOTALL)

    # Insert footer before </body> if it's not already there
    if "<footer" not in content:
        content = content.replace("</body>", footer_html + "\n</body>")
    else:
        content = re.sub(r'<footer.*?</footer>', footer_html, content, flags=re.DOTALL)
    
    with open(file_name, "w") as f:
        f.write(content)

