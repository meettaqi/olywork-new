import re

footer_html = """<footer style="padding:80px 48px;background:var(--surface);border-top:1px solid var(--border);display:flex;justify-content:space-between;max-width:1200px;margin:0 auto;width:100%;">
  <div class="foot-brand" style="max-width:300px;">
    <div class="brand" style="display:flex;align-items:center;gap:8px;font-family:var(--font-heading);font-weight:800;font-size:24px;letter-spacing:-0.04em;margin-bottom:16px;">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:24px;height:24px;"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
      Olywork
    </div>
    <div style="color:var(--ink-secondary);font-size:14px;line-height:1.5;">The OpenRouter for AI Agent Tools. One unified token for 2,800+ endpoints.</div>
  </div>
  <nav class="foot-cols" style="display:flex;gap:64px;">
    <div class="foot-col" style="display:flex;flex-direction:column;gap:12px;">
      <div style="font-weight:700;color:var(--ink);margin-bottom:8px;">Explore</div>
      <a href="/catalog" style="color:var(--ink-secondary);transition:color 0.2s;">Catalog</a>
    </div>
    <div class="foot-col" style="display:flex;flex-direction:column;gap:12px;">
      <div style="font-weight:700;color:var(--ink);margin-bottom:8px;">Build</div>
      <a href="/docs" style="color:var(--ink-secondary);transition:color 0.2s;">API Docs</a>
      <a href="/tutorial" style="color:var(--ink-secondary);transition:color 0.2s;">Tutorial</a>
    </div>
    <div class="foot-col" style="display:flex;flex-direction:column;gap:12px;">
      <div style="font-weight:700;color:var(--ink);margin-bottom:8px;">Company</div>
      <a href="/support" style="color:var(--ink-secondary);transition:color 0.2s;">Support</a>
      <a href="/terms" style="color:var(--ink-secondary);transition:color 0.2s;">Terms</a>
      <a href="/privacy" style="color:var(--ink-secondary);transition:color 0.2s;">Privacy</a>
    </div>
  </nav>
</footer>"""

with open("src/olywork/web/landing.html", "r") as f:
    landing = f.read()

landing = re.sub(r'<footer class="footer">.*?</footer>', footer_html, landing, flags=re.DOTALL)

with open("src/olywork/web/landing.html", "w") as f:
    f.write(landing)

