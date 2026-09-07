import re
import glob

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

files = glob.glob("src/olywork/web/*.html")

for file_name in files:
    if "index.html" in file_name or "claude-connector.html" in file_name or "archive-panel.html" in file_name or "connect-demo-callback.html" in file_name or "fable-gtm.html" in file_name or "landing.html" in file_name or "people-search.html" in file_name:
        continue
        
    with open(file_name, "r") as f:
        content = f.read()

    # Nav replacements
    # Check what topbar structure exists
    if '<div class="topbar">' in content:
        content = re.sub(r'<div class="topbar">.*?</div>\s*</div>', nav_html, content, flags=re.DOTALL)
        content = re.sub(r'<div class="topbar">.*?</div>', nav_html, content, flags=re.DOTALL)
    elif '<nav class="tut-nav">' in content:
        content = re.sub(r'<nav class="tut-nav">.*?</nav>', nav_html, content, flags=re.DOTALL)
    elif '<nav class="uc-nav">' in content:
        content = re.sub(r'<nav class="uc-nav">.*?</nav>', nav_html, content, flags=re.DOTALL)
    else:
        # Just inject it after <body>
        content = content.replace("<body>", "<body>\n" + nav_html)

    # Footer replacements
    if '<footer' in content:
        content = re.sub(r'<footer.*?</footer>', footer_html, content, flags=re.DOTALL)
    elif '<div class="uc-foot">' in content:
        content = re.sub(r'<div class="uc-foot">.*?</div>', footer_html, content, flags=re.DOTALL)
    else:
        content = content.replace("</body>", footer_html + "\n</body>")
        
    # Also adjust any body padding if nav is fixed
    if "<style>" in content and "padding-top: 80px;" not in content:
        content = content.replace("<style>", "<style>\nbody { padding-top: 80px; }\n")
        
    with open(file_name, "w") as f:
        f.write(content)

