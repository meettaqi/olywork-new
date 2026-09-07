import re

nav_html = """<div class="navwrap"><nav class="nav" style="position:fixed;top:0;width:100%;height:80px;display:flex;align-items:center;justify-content:space-between;padding:0 48px;background:rgba(244,242,236,0.95);backdrop-filter:blur(12px);border-bottom:1px solid rgba(232,229,218,0.6);z-index:50;left:0;box-sizing:border-box;">
  <a class="brand" href="/" style="display:flex;align-items:center;gap:8px;font-family:var(--display);font-weight:800;font-size:24px;letter-spacing:-0.04em;">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:24px;height:24px;"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
    Olywork
  </a>
  <div class="links" style="display:flex;gap:32px;align-items:center;">
    {navlink("/catalog", "Catalog", 'style="font-weight:500;"')}
    {navlink("/docs", "API", 'style="font-weight:500;"')}
    {navlink("/tutorial", "Tutorial", 'style="font-weight:500;"')}
    <a href="/app?ref={ref}" style="background:var(--ink);color:var(--bg);padding:10px 24px;border-radius:99px;font-weight:600;">Start free</a>
  </div>
</nav></div>"""

footer_html = """<footer style="padding:80px 48px;background:var(--surface);border-top:1px solid var(--border);display:flex;justify-content:space-between;max-width:1200px;margin:100px auto 0;width:100%;box-sizing:border-box;">
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
      {hub_links}
    </div>
    <div class="foot-col" style="display:flex;flex-direction:column;gap:12px;">
      <div style="font-weight:700;color:var(--ink);margin-bottom:8px;">Build</div>
      <a href="/docs" style="color:var(--muted);">API Docs</a>
      <a href="/tutorial" style="color:var(--muted);">Tutorial</a>
      <a href="{_GH}" style="color:var(--muted);">GitHub</a>
    </div>
    <div class="foot-col" style="display:flex;flex-direction:column;gap:12px;">
      <div style="font-weight:700;color:var(--ink);margin-bottom:8px;">Company</div>
      <a href="/support" style="color:var(--muted);">Support</a>
      <a href="/terms" style="color:var(--muted);">Terms</a>
      <a href="/privacy" style="color:var(--muted);">Privacy</a>
    </div>
  </nav>
</footer>"""

with open("src/olywork/routers/web.py", "r") as f:
    web_py = f.read()

web_py = re.sub(r'<div class="navwrap"><nav class="nav">.*?</nav></div>', nav_html, web_py, flags=re.DOTALL)
web_py = re.sub(r'<footer.*?</footer>', footer_html, web_py, flags=re.DOTALL)

with open("src/olywork/routers/web.py", "w") as f:
    f.write(web_py)

