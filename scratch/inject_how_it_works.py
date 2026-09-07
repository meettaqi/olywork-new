import re

how_html = '''
<!-- HOW IT WORKS -->
<style>
/* Override/extend any existing styles for the "how it works" section */
.ow-hiw-section { padding:120px 32px; max-width:1200px; margin:0 auto; }
.ow-hiw-header { text-align:center; margin-bottom:80px; }
.ow-hiw-header .ow-eyebrow { display:inline-block; font-family:var(--mono,monospace); font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:0.14em; color:var(--ink-muted,#7E7C74); margin-bottom:16px; }
.ow-hiw-header h2 { font-family:var(--font-heading,"Plus Jakarta Sans",sans-serif); font-size:clamp(36px,4.5vw,56px); font-weight:800; letter-spacing:-0.04em; line-height:1.06; margin:0 0 16px; }
.ow-hiw-header p { font-size:18px; color:var(--ink-secondary,#7E7C74); max-width:52ch; margin:0 auto; line-height:1.5; }

.ow-hiw-steps { display:grid; grid-template-columns:repeat(3,1fr); gap:20px; }
.ow-hiw-step {
  background:var(--surface,#FCFBFA);
  border:1px solid var(--border,#E8E5DA);
  border-radius:24px;
  padding:44px 36px;
  position:relative;
  overflow:hidden;
  transition:transform 0.35s cubic-bezier(.2,.72,.25,1), border-color 0.35s;
  cursor:default;
}
.ow-hiw-step::before {
  content:attr(data-num);
  position:absolute; top:20px; right:28px;
  font-family:var(--font-heading,"Plus Jakarta Sans",sans-serif);
  font-size:96px; font-weight:800; line-height:1;
  color:rgba(32,32,32,0.05);
  letter-spacing:-0.06em;
  pointer-events:none;
  transition:transform 0.35s;
}
.ow-hiw-step:hover { transform:translateY(-6px); border-color:var(--border-strong,#D5D1C3); }
.ow-hiw-step:hover::before { transform:scale(1.05) translateY(-4px); }
.ow-hiw-step-icon {
  width:56px; height:56px; border-radius:16px;
  border:1px solid var(--border,#E8E5DA);
  display:grid; place-items:center;
  font-size:26px; margin-bottom:28px;
  background:var(--bg,#F4F2EC);
  transition:transform 0.3s;
}
.ow-hiw-step:hover .ow-hiw-step-icon { transform:scale(1.08); }
.ow-hiw-step h3 {
  font-family:var(--font-heading,"Plus Jakarta Sans",sans-serif);
  font-size:22px; font-weight:800; letter-spacing:-0.03em;
  margin:0 0 12px;
}
.ow-hiw-step p { font-size:14.5px; color:var(--ink-secondary,#7E7C74); line-height:1.65; margin:0; }

/* Accent card: lime green */
.ow-hiw-step.s-accent { background:var(--accent,#9FF25F); border-color:transparent; }
.ow-hiw-step.s-accent::before { color:rgba(32,32,32,0.07); }
.ow-hiw-step.s-accent .ow-hiw-step-icon { background:rgba(32,32,32,0.08); border-color:rgba(32,32,32,0.1); }
.ow-hiw-step.s-accent h3, .ow-hiw-step.s-accent p { color:#202020; }

/* Dark card */
.ow-hiw-step.s-dark { background:#1A1A1A; border-color:transparent; }
.ow-hiw-step.s-dark::before { color:rgba(255,255,255,0.05); }
.ow-hiw-step.s-dark .ow-hiw-step-icon { background:rgba(255,255,255,0.07); border-color:rgba(255,255,255,0.1); filter:invert(1); }
.ow-hiw-step.s-dark h3 { color:#9FF25F; }
.ow-hiw-step.s-dark p { color:rgba(252,251,250,0.58); }

/* Flow connector */
.ow-hiw-flow {
  display:flex; align-items:center; justify-content:center;
  gap:0; margin:40px 0;
}
.ow-hiw-flow-item { flex:1; text-align:center; padding:0 16px; }
.ow-hiw-flow-arrow { color:var(--border-strong,#D5D1C3); font-size:28px; flex-shrink:0; }

/* FAQ styles */
.ow-faq-section { padding:100px 32px; max-width:800px; margin:0 auto; }
.ow-faq-section .ow-eyebrow { display:block; text-align:center; margin-bottom:12px; font-family:var(--mono,monospace); font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:0.14em; color:var(--ink-muted,#7E7C74); }
.ow-faq-section h2 { font-family:var(--font-heading,"Plus Jakarta Sans",sans-serif); font-size:clamp(32px,4vw,48px); font-weight:800; letter-spacing:-0.04em; text-align:center; margin:0 0 56px; }

.faq-item { border-bottom:1px solid var(--border,#E8E5DA); overflow:hidden; }
.faq-item:first-of-type { border-top:1px solid var(--border,#E8E5DA); }
.faq-q {
  display:flex; align-items:center; justify-content:space-between;
  gap:16px; padding:22px 4px;
  font-weight:600; font-size:16px;
  cursor:pointer; user-select:none;
  background:none; border:none; width:100%; text-align:left;
  color:var(--ink,#202020);
  font-family:var(--font-body,"Inter",sans-serif);
}
.faq-icon {
  flex-shrink:0; width:30px; height:30px; border-radius:50%;
  border:1.5px solid var(--border,#E8E5DA);
  display:grid; place-items:center;
  font-size:18px; color:var(--ink-muted,#7E7C74);
  transition:transform 0.3s cubic-bezier(.2,.72,.25,1), border-color 0.3s, background 0.3s;
}
.faq-item.open .faq-icon { transform:rotate(45deg); border-color:var(--ink,#202020); background:var(--ink,#202020); color:#fff; }
.faq-a { max-height:0; overflow:hidden; transition:max-height 0.4s cubic-bezier(.2,.72,.25,1); }
.faq-item.open .faq-a { max-height:500px; }
.faq-a p { padding:0 4px 24px; font-size:14.5px; color:var(--ink-secondary,#7E7C74); line-height:1.75; margin:0; }
.faq-a code { font-family:var(--mono,monospace); font-size:12.5px; background:var(--panel2,#EDEAE0); border:1px solid var(--border,#E8E5DA); border-radius:5px; padding:1px 6px; color:var(--ink,#202020); }

@media(max-width:900px) {
  .ow-hiw-steps { grid-template-columns:1fr; gap:12px; }
  .ow-hiw-section { padding:72px 20px; }
  .ow-faq-section { padding:64px 20px; }
}
</style>

<section class="ow-hiw-section">
  <div class="ow-hiw-header">
    <span class="ow-eyebrow">How it works</span>
    <h2>One call.<br><span style="opacity:0.35">Unlimited tools.</span></h2>
    <p>Your agent makes a single REST or MCP call to Olywork. We handle credentials, routing, and billing. The result comes back directly — no buffering, no transformation.</p>
  </div>

  <div class="ow-hiw-steps">
    <div class="ow-hiw-step" data-num="1">
      <div class="ow-hiw-step-icon">🤖</div>
      <h3>Your Agent Calls Us</h3>
      <p>Your AI agent makes one standard REST or MCP call to <code>olywork.com/call/</code> using a single API token. No per-provider setup needed.</p>
    </div>
    <div class="ow-hiw-step s-dark" data-num="2">
      <div class="ow-hiw-step-icon" style="font-size:20px;">▚</div>
      <h3>We Route &amp; Inject</h3>
      <p>Olywork identifies the right provider, injects their credential server-side, meters the micro-USD cost, and relays your request faithfully — no body rewriting.</p>
    </div>
    <div class="ow-hiw-step s-accent" data-num="3">
      <div class="ow-hiw-step-icon">🌐</div>
      <h3>Tool Executes &amp; Returns</h3>
      <p>The upstream provider executes the task. The response comes back verbatim to your agent. You get billed only on success — failed calls cost nothing.</p>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="ow-faq-section">
  <span class="ow-eyebrow">FAQ</span>
  <h2>Common questions</h2>

  <div class="faq-item">
    <button class="faq-q" onclick="this.parentElement.classList.toggle(\'open\')">
      What exactly is Olywork?
      <span class="faq-icon">+</span>
    </button>
    <div class="faq-a"><p>Olywork is the OpenRouter for AI agent tools. One API endpoint, one token, and your agent can call 2,896+ tools across 60+ providers — Google, Twitter, LinkedIn, GitHub, and many more. We never model the upstream APIs; we faithfully relay your request with injected credentials.</p></div>
  </div>

  <div class="faq-item">
    <button class="faq-q" onclick="this.parentElement.classList.toggle(\'open\')">
      How does pricing work?
      <span class="faq-icon">+</span>
    </button>
    <div class="faq-a"><p>You pay in micro-USD per call, at cost with no markup. A Google Search is ~$0.004. A Twitter post is ~$0.002. Failed calls are never billed. New accounts start with $1.00 free credit — no credit card required. Top up any time.</p></div>
  </div>

  <div class="faq-item">
    <button class="faq-q" onclick="this.parentElement.classList.toggle(\'open\')">
      Do I need my own API keys?
      <span class="faq-icon">+</span>
    </button>
    <div class="faq-a"><p>No. Your single Olywork token authenticates your agent across every provider in the catalog. If you <em>do</em> have a key for a specific provider, register it once with <code>olywork keys set &lt;provider&gt; &lt;key&gt;</code> — your key always takes precedence and those calls are never metered.</p></div>
  </div>

  <div class="faq-item">
    <button class="faq-q" onclick="this.parentElement.classList.toggle(\'open\')">
      Can my agent act on behalf of my users?
      <span class="faq-icon">+</span>
    </button>
    <div class="faq-a"><p>Yes. Olywork handles OAuth flows natively. Your users click "Connect Twitter" (or any supported provider), and your agent is immediately authorized to act on their behalf. The raw token is never exposed — Olywork injects it server-side and relays responses verbatim.</p></div>
  </div>

  <div class="faq-item">
    <button class="faq-q" onclick="this.parentElement.classList.toggle(\'open\')">
      What agents and frameworks does it support?
      <span class="faq-icon">+</span>
    </button>
    <div class="faq-a"><p><code>olywork install</code> registers the MCP server into Claude Code, Cursor, and opencode automatically. Any MCP client that supports the authorization spec can connect with OAuth. Any system that can make an HTTP request — including LangChain, AutoGen, CrewAI, and raw <code>curl</code> — can use the REST endpoint directly.</p></div>
  </div>

  <div class="faq-item">
    <button class="faq-q" onclick="this.parentElement.classList.toggle(\'open\')">
      Is there a rate limit?
      <span class="faq-icon">+</span>
    </button>
    <div class="faq-a"><p>Olywork itself does not add rate limits beyond the upstream provider's own limits. If the provider throttles, the call returns the provider's error — Olywork relays it verbatim and does not bill the call. You can set daily spend caps per tag or per team to prevent runaway costs.</p></div>
  </div>
</section>
'''

with open("src/olywork/web/landing.html", "r") as f:
    content = f.read()

# Replace old how-it-works and faq sections
content = re.sub(r'<section class="how-section">.*?</section>\s*<section class="faq-section">.*?</section>', '', content, flags=re.DOTALL)

# Insert before footer
footer_idx = content.rfind('<footer')
if footer_idx != -1:
    content = content[:footer_idx] + how_html + '\n' + content[footer_idx:]

with open("src/olywork/web/landing.html", "w") as f:
    f.write(content)

print("Done — how-it-works + FAQ injected")
