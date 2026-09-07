def generate():
    with open("src/olywork/web/landing.html", "r") as f:
        html = f.read()
    
    # insert before </body>
    insertion = """
<style>
/* BENTO GRID */
.bento-section { padding: 100px 24px; max-width: 1200px; margin: 0 auto; }
.bento-header { text-align: center; margin-bottom: 64px; }
.bento-tag { font-size: 12px; font-weight: 700; color: var(--ink-muted); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 16px; display: block; }
.bento-title { font-family: var(--font-heading); font-size: 48px; font-weight: 800; color: var(--ink); letter-spacing: -0.03em; margin-bottom: 24px; line-height: 1.1; }
.bento-grid { display: grid; grid-template-columns: repeat(12, 1fr); gap: 24px; }
.bento-card { background: var(--surface); border-radius: 24px; padding: 40px; border: 1px solid rgba(0,0,0,0.05); display: flex; flex-direction: column; }
.bento-card h3 { font-family: var(--font-heading); font-size: 28px; font-weight: 700; margin-bottom: 12px; letter-spacing: -0.02em; }
.bento-card p { font-size: 16px; color: var(--ink-secondary); line-height: 1.5; }
.bento-card.col-7 { grid-column: span 7; }
.bento-card.col-5 { grid-column: span 5; }
.bento-card.col-12 { grid-column: span 12; display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center; }

/* TERMINAL MOCKUP */
.terminal { background: #1A1A1A; border-radius: 16px; padding: 24px; color: #E8E5DA; font-family: monospace; font-size: 14px; margin-top: 32px; overflow-x: auto; border: 1px solid #333; }
.terminal-header { display: flex; gap: 8px; margin-bottom: 16px; }
.dot { width: 12px; height: 12px; border-radius: 50%; background: #444; }

/* FOOTER */
.footer { padding: 64px 48px; background: var(--surface); border-top: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; font-size: 14px; color: var(--ink-muted); font-weight: 500; }
.footer-links { display: flex; gap: 24px; }
.footer-link { transition: color 0.2s; }
.footer-link:hover { color: var(--ink); }
</style>

<section class="bento-section">
  <div class="bento-header">
    <span class="bento-tag">Designed for Agents</span>
    <h2 class="bento-title">Every tool your agent needs.<br>Zero headaches.</h2>
  </div>
  
  <div class="bento-grid">
    <div class="bento-card col-7">
      <h3>One Token, 2,896 Tools</h3>
      <p>Forget managing API keys across 60+ providers. Give your agent a single Olywork token, and let it access everything from web scraping to video generation instantly.</p>
      
      <div class="terminal">
        <div class="terminal-header">
          <div class="dot" style="background:#FF5F56;"></div>
          <div class="dot" style="background:#FFBD2E;"></div>
          <div class="dot" style="background:#27C93F;"></div>
        </div>
        <div>$ curl -X POST https://olywork.com/api/v1/tools/search_web \</div>
        <div style="color: #9FF25F;">  -H "Authorization: Bearer oly_..." \</div>
        <div>  -d '{"query": "Latest AI agents"}'</div>
      </div>
    </div>
    
    <div class="bento-card col-5" style="background: var(--primary-deep); color: white;">
      <h3 style="color: var(--accent);">Micro-USD Pricing</h3>
      <p style="color: #A09E96; margin-bottom: 24px;">No subscriptions. No massive prepays. You pay per successful API call in fractions of a cent.</p>
      
      <div style="background: rgba(255,255,255,0.05); border-radius: 12px; padding: 24px; border: 1px solid rgba(255,255,255,0.1);">
        <div style="display: flex; justify-content: space-between; margin-bottom: 12px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px;">
          <span style="font-weight: 600;">Google Search</span>
          <span style="font-family: monospace; color: var(--accent);">$0.001 / call</span>
        </div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 12px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px;">
          <span style="font-weight: 600;">Browser Automate</span>
          <span style="font-family: monospace; color: var(--accent);">$0.005 / min</span>
        </div>
        <div style="display: flex; justify-content: space-between;">
          <span style="font-weight: 600;">Twitter Post</span>
          <span style="font-family: monospace; color: var(--accent);">$0.002 / call</span>
        </div>
      </div>
    </div>
    
    <div class="bento-card col-12">
      <div>
        <h3>BYO OAuth & Connections</h3>
        <p>If your agent needs to act on your behalf, we handle the OAuth flows. Your users just click "Connect Twitter" and the agent can immediately post, read, and reply securely.</p>
        <button class="btn-primary" style="margin-top: 24px;">View Documentation</button>
      </div>
      <div style="background: var(--bg); border-radius: 16px; padding: 32px; display: flex; flex-direction: column; gap: 16px; border: 1px solid rgba(0,0,0,0.05);">
        <div style="display: flex; align-items: center; justify-content: space-between; background: var(--surface); padding: 16px 24px; border-radius: 12px; border: 1px solid rgba(0,0,0,0.05);">
          <div style="display: flex; align-items: center; gap: 12px; font-weight: 600; color: var(--ink);">
            <div style="width: 32px; height: 32px; background: #000; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">X</div>
            X (Twitter)
          </div>
          <span style="background: #E8E5DA; color: var(--ink-secondary); padding: 4px 12px; border-radius: 99px; font-size: 12px; font-weight: 600;">Connected</span>
        </div>
        <div style="display: flex; align-items: center; justify-content: space-between; background: var(--surface); padding: 16px 24px; border-radius: 12px; border: 1px solid rgba(0,0,0,0.05);">
          <div style="display: flex; align-items: center; gap: 12px; font-weight: 600; color: var(--ink);">
            <div style="width: 32px; height: 32px; background: #0A66C2; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">in</div>
            LinkedIn
          </div>
          <span style="background: var(--ink); color: #FFF; padding: 4px 12px; border-radius: 99px; font-size: 12px; font-weight: 600;">Connect</span>
        </div>
      </div>
    </div>
  </div>
</section>

<footer class="footer">
  <div class="brand">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
    Olywork
  </div>
  <div class="footer-links">
    <a href="/catalog" class="footer-link">Catalog</a>
    <a href="/docs" class="footer-link">Documentation</a>
    <a href="/terms" class="footer-link">Terms</a>
    <a href="/privacy" class="footer-link">Privacy</a>
  </div>
</footer>
"""
    
    html = html.replace("</body>", insertion + "\n</body>")
    with open("src/olywork/web/landing.html", "w") as f:
        f.write(html)
generate()
