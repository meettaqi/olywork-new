import re

how_it_works_html = """
<style>
.how-section { padding: 120px 24px; max-width: 1000px; margin: 0 auto; text-align: center; }
.how-title { font-family: var(--font-heading); font-size: 48px; font-weight: 800; margin-bottom: 24px; letter-spacing: -0.03em; }
.how-sub { font-size: 18px; color: var(--ink-secondary); margin-bottom: 80px; max-width: 600px; margin-left: auto; margin-right: auto; line-height: 1.5; }
.how-diagram { display: flex; align-items: center; justify-content: center; gap: 24px; }
.how-box { background: var(--surface); border: 1px solid var(--border); border-radius: 24px; padding: 40px; flex: 1; position: relative; }
.how-box-icon { width: 48px; height: 48px; background: var(--bg); border: 1px solid var(--border); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px; font-weight: bold; }
.how-box h4 { font-family: var(--font-heading); font-size: 24px; margin-bottom: 12px; font-weight: 700; }
.how-box p { font-size: 15px; color: var(--ink-secondary); line-height: 1.5; }
.how-arrow { color: var(--ink-muted); font-size: 24px; }
@media (max-width: 768px) {
  .how-diagram { flex-direction: column; }
  .how-arrow { transform: rotate(90deg); }
}
</style>

<section class="how-section">
  <h2 class="how-title">How Olywork works</h2>
  <p class="how-sub">Give your AI agents the power to interact with the world, without managing 60 different API keys and billing portals.</p>
  
  <div class="how-diagram">
    <div class="how-box">
      <div class="how-box-icon">🤖</div>
      <h4>1. Your Agent</h4>
      <p>Your AI agent makes a single standard REST or MCP call to the Olywork endpoint, using one unified token.</p>
    </div>
    
    <div class="how-arrow">→</div>
    
    <div class="how-box" style="background: var(--primary-deep); color: white;">
      <div class="how-box-icon" style="background: var(--ink); border: none;">▚</div>
      <h4 style="color: var(--accent);">2. Olywork</h4>
      <p style="color: #A09E96;">We instantly route the request, inject the appropriate provider credentials, and meter the micro-USD cost.</p>
    </div>
    
    <div class="how-arrow">→</div>
    
    <div class="how-box">
      <div class="how-box-icon">🌍</div>
      <h4>3. 2,800+ Tools</h4>
      <p>The upstream provider (Google, Twitter, TikTok, etc.) executes the task and the result is returned directly to your agent.</p>
    </div>
  </div>
</section>
"""

with open("src/olywork/web/landing.html", "r") as f:
    content = f.read()

# Insert before FAQ section
content = content.replace("<section class=\"faq-section\">", how_it_works_html + "\n<section class=\"faq-section\">")

with open("src/olywork/web/landing.html", "w") as f:
    f.write(content)
