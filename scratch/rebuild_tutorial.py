import os

logos = [f.replace(".svg","") for f in os.listdir("src/olywork/web/logos/platforms") if f.endswith(".svg") and f not in ["companies.svg","README.md"]]
logos_html = ""
for l in logos[:30]:
    logos_html += f'<div class="ow-ticker-logo"><img src="/logos/platforms/{l}.svg" alt="{l}" loading="lazy"></div>\n'

html = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Olywork Tutorial — Get started in 5 minutes</title>
<meta name="description" content="Learn Olywork in five minutes: connect an agent, call 2,800+ tools through one key, bring your own API keys and start building."/>
<link rel="canonical" href="{BASE}/tutorial"/>
<link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/olywork.css"/>
<style>
:root{
  --bg:#F4F2EC; --surface:#FCFBFA; --panel:#FFFFFF; --panel2:#EDEAE0;
  --ink:#202020; --muted:#7E7C74; --muted2:#A09E96;
  --line:#E8E5DA; --line2:#D5D1C3;
  --accent:#9FF25F; --accent-hover:#8EE250;
  --inverse:#1A1A1A; --inverse-surf:#282828; --inverse-ink:#FCFBFA;
  --green:#22C55E; --amber:#F59E0B; --red:#EF4444;
  --shadow-sm:none; --shadow-md:none; --shadow-lg:none;
  --ease:cubic-bezier(.2,.72,.25,1); --ease-out:cubic-bezier(.22,1,.36,1);
  --r:20px; --rb:12px;
  --display:"Plus Jakarta Sans", sans-serif;
  --sans:"Inter", sans-serif;
  --mono:ui-monospace, "SF Mono", Menlo, Consolas, monospace;
}
body { background:var(--bg); color:var(--ink); font-family:var(--sans); }

/* Sidebar */
.tut-layout { display:grid; grid-template-columns:240px 1fr; min-height:calc(100vh - 80px); }
.tut-sidebar {
  border-right:1px solid var(--line);
  padding:32px 20px;
  position:sticky; top:80px; height:calc(100vh - 80px);
  overflow-y:auto;
  background:var(--surface);
}
.tut-sidebar-sec { margin-bottom:28px; }
.tut-sidebar-label { font-size:10.5px; font-weight:700; text-transform:uppercase; letter-spacing:0.1em; color:var(--muted2); margin-bottom:8px; padding:0 8px; }
.tut-sidebar a { display:block; padding:7px 10px; border-radius:8px; font-size:13px; color:var(--muted); font-weight:500; text-decoration:none; transition:background 0.15s,color 0.15s; }
.tut-sidebar a:hover { background:var(--panel2); color:var(--ink); }
.tut-sidebar a.active { background:var(--accent); color:var(--ink); font-weight:700; }

/* Content */
.tut-content { padding:56px 64px 120px; max-width:820px; }
.tut-content h1 { font-family:var(--display); font-weight:800; font-size:40px; letter-spacing:-0.04em; margin:0 0 12px; }
.tut-content .lead { font-size:17px; color:var(--muted); margin:0 0 48px; line-height:1.5; }

/* Step headings */
.tut-step {
  margin-bottom:64px;
  padding-top:64px;
  border-top:1px solid var(--line);
  scroll-margin-top:96px;
}
.tut-step:first-of-type { border-top:none; padding-top:0; }
.tut-step-badge {
  display:inline-flex; align-items:center; justify-content:center;
  width:32px; height:32px; border-radius:50%;
  background:var(--ink); color:var(--bg);
  font-weight:800; font-size:13px; font-family:var(--display);
  margin-bottom:16px;
}
.tut-step h2 { font-family:var(--display); font-weight:800; font-size:26px; letter-spacing:-0.03em; margin:0 0 10px; }
.tut-step p, .tut-step li { font-size:14.5px; color:var(--muted); line-height:1.75; }
.tut-step ul, .tut-step ol { padding-left:20px; margin:12px 0; }
.tut-step li { margin:6px 0; }
.tut-step code { font-family:var(--mono); font-size:12.5px; background:var(--panel2); border:1px solid var(--line); border-radius:5px; padding:1px 6px; color:var(--ink); }
.tut-step a { color:var(--ink); font-weight:600; text-decoration:underline; text-underline-offset:3px; }

/* Code block */
.code-block {
  background:var(--inverse);
  border-radius:16px;
  overflow:hidden;
  margin:20px 0;
}
.code-block-head {
  display:flex; align-items:center; justify-content:space-between;
  padding:12px 20px;
  border-bottom:1px solid rgba(255,255,255,0.06);
  font-family:var(--mono);
  font-size:12px;
  color:rgba(255,255,255,0.4);
}
.code-block pre {
  margin:0; padding:24px;
  font-family:var(--mono); font-size:13px; line-height:1.75;
  color:#d4d0c8; overflow-x:auto;
}
.code-block .c-key { color:#9FF25F; }
.code-block .c-str { color:#7ec8e3; }
.code-block .c-cmt { color:#5e5e5a; font-style:italic; }
.code-block .c-num { color:#f5a623; }
.code-block .c-fn  { color:#e8c468; }

/* Callout */
.callout {
  border-radius:12px;
  padding:16px 20px;
  margin:20px 0;
  font-size:13.5px;
  line-height:1.6;
}
.callout.info { background:rgba(159,242,95,0.12); border:1px solid rgba(159,242,95,0.3); color:var(--ink); }
.callout.tip  { background:rgba(252,251,250,1); border:1px solid var(--line); color:var(--muted); }
.callout.warn { background:rgba(245,158,11,0.08); border:1px solid rgba(245,158,11,0.25); color:var(--ink); }
.callout b { color:var(--ink); font-weight:700; }

/* CTA box */
.tut-cta {
  background:var(--inverse);
  border-radius:var(--r);
  padding:48px;
  text-align:center;
  margin-top:80px;
}
.tut-cta h2 { font-family:var(--display); font-weight:800; font-size:32px; letter-spacing:-0.04em; color:var(--inverse-ink); margin:0 0 12px; }
.tut-cta p { color:rgba(252,251,250,0.6); font-size:15px; margin:0 0 28px; }
.tut-cta .btns { display:flex; gap:12px; justify-content:center; flex-wrap:wrap; }

@media (max-width:900px) {
  .tut-layout { grid-template-columns:1fr; }
  .tut-sidebar { display:none; }
  .tut-content { padding:32px 24px 80px; }
}
</style>
</head>
<body>
<nav class="ow-nav" aria-label="Main navigation">
  <a class="ow-nav-brand" href="/">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
    Olywork
  </a>
  <div class="ow-nav-links">
    <a href="/catalog">Catalog</a>
    <a href="/docs">API Docs</a>
    <a href="/tutorial" aria-current="page">Tutorial</a>
    <a href="/pricing">Pricing</a>
    <a href="/app" class="ow-btn-nav">Start free &rarr;</a>
  </div>
</nav>

<div class="tut-layout">
  <!-- SIDEBAR -->
  <aside class="tut-sidebar">
    <div class="tut-sidebar-sec">
      <div class="tut-sidebar-label">Getting started</div>
      <a href="#overview" class="active">What is Olywork?</a>
      <a href="#install">Install in 60 seconds</a>
      <a href="#first-call">Make your first call</a>
    </div>
    <div class="tut-sidebar-sec">
      <div class="tut-sidebar-label">Core concepts</div>
      <a href="#catalog">Browse the catalog</a>
      <a href="#pricing">Pricing &amp; billing</a>
      <a href="#own-keys">Bring your own keys</a>
      <a href="#oauth">OAuth connections</a>
    </div>
    <div class="tut-sidebar-sec">
      <div class="tut-sidebar-label">Integration</div>
      <a href="#mcp">MCP (Claude/Cursor)</a>
      <a href="#http">Direct HTTP</a>
      <a href="#cli">CLI reference</a>
    </div>
    <div class="tut-sidebar-sec">
      <div class="tut-sidebar-label">Resources</div>
      <a href="/docs">API Reference</a>
      <a href="/catalog">Browse catalog</a>
      <a href="/support">Get support</a>
    </div>
  </aside>

  <!-- MAIN CONTENT -->
  <main class="tut-content">
    <h1>Get started with Olywork</h1>
    <p class="lead">Give your AI agent access to 2,800+ tools — Google, Twitter, LinkedIn, GitHub, and more — through a single endpoint. No API keys to manage. Pay per call, in micro-USD, with no markup.</p>

    <!-- STEP 0: What is Olywork -->
    <section class="tut-step" id="overview">
      <div class="tut-step-badge">★</div>
      <h2>What is Olywork?</h2>
      <p>Olywork is the <strong>OpenRouter for AI Agent Tools</strong>. Just like OpenRouter gives your LLM a single endpoint to call any model, Olywork gives your agent a single endpoint to call any tool.</p>
      <p>Instead of signing up for 60 different APIs, holding 60 different keys, and managing 60 different billing portals — your agent calls one URL. Olywork handles credentials, routing, rate limits, and billing automatically.</p>

      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:28px 0;">
        <div style="background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:24px;text-align:center;">
          <div style="font-family:var(--display);font-weight:800;font-size:36px;letter-spacing:-0.04em;">2,896</div>
          <div style="font-size:13px;color:var(--muted);margin-top:4px;">Endpoints</div>
        </div>
        <div style="background:var(--accent);border-radius:16px;padding:24px;text-align:center;">
          <div style="font-family:var(--display);font-weight:800;font-size:36px;letter-spacing:-0.04em;">60+</div>
          <div style="font-size:13px;margin-top:4px;font-weight:600;">Providers</div>
        </div>
        <div style="background:var(--inverse);border-radius:16px;padding:24px;text-align:center;">
          <div style="font-family:var(--display);font-weight:800;font-size:36px;letter-spacing:-0.04em;color:var(--accent);">$0</div>
          <div style="font-size:13px;color:rgba(255,255,255,0.6);margin-top:4px;">Markup</div>
        </div>
      </div>
    </section>

    <!-- STEP 1: Install -->
    <section class="tut-step" id="install">
      <div class="tut-step-badge">1</div>
      <h2>Install in 60 seconds</h2>
      <p>Add Olywork to your agent with one command. It registers the MCP server into Claude Code, Cursor, and <code>opencode</code> automatically.</p>

      <div class="code-block">
        <div class="code-block-head"><span>Shell</span></div>
        <pre><span class="c-cmt"># Install the Olywork CLI</span>
<span class="c-fn">pip</span> install olywork

<span class="c-cmt"># Register into your agent (Claude Code, Cursor, opencode)</span>
<span class="c-fn">olywork</span> install</pre>
      </div>

      <div class="callout info">
        <b>First $1.00 free.</b> No credit card required to get started. The first dollar of calls is on us.
      </div>

      <p>Or add the MCP server manually to any client that supports the MCP authorization spec:</p>
      <div class="code-block">
        <div class="code-block-head"><span>~/.cursor/mcp.json</span></div>
        <pre>{
  <span class="c-key">"mcpServers"</span>: {
    <span class="c-key">"olywork"</span>: {
      <span class="c-key">"url"</span>: <span class="c-str">"{BASE}/mcp"</span>,
      <span class="c-key">"headers"</span>: {
        <span class="c-key">"Authorization"</span>: <span class="c-str">"Bearer YOUR_TOKEN"</span>
      }
    }
  }
}</pre>
      </div>
    </section>

    <!-- STEP 2: First call -->
    <section class="tut-step" id="first-call">
      <div class="tut-step-badge">2</div>
      <h2>Make your first call</h2>
      <p>Every tool is callable through a single REST endpoint. Find a tool ID in the catalog, then call it:</p>

      <div class="code-block">
        <div class="code-block-head"><span>HTTP / curl</span></div>
        <pre><span class="c-fn">curl</span> -X POST {BASE}/call/ \\
  -H <span class="c-str">"Authorization: Bearer $OLYWORK_TOKEN"</span> \\
  -H <span class="c-str">"Content-Type: application/json"</span> \\
  -d <span class="c-str">&#39;{
    "id": "google.search",
    "q": "latest AI agent frameworks 2025"
  }&#39;</span></pre>
      </div>

      <div class="code-block">
        <div class="code-block-head"><span>Python</span></div>
        <pre><span class="c-key">import</span> olywork

client = olywork.Client(token=<span class="c-str">"YOUR_TOKEN"</span>)

result = client.call(
    <span class="c-str">"google.search"</span>,
    q=<span class="c-str">"latest AI agent frameworks 2025"</span>
)
<span class="c-fn">print</span>(result)</pre>
      </div>

      <div class="callout tip">
        <b>Tip:</b> Use <code>olywork catalog search &lt;keyword&gt;</code> in the CLI to find the right tool ID for any task.
      </div>
    </section>

    <!-- STEP 3: Catalog -->
    <section class="tut-step" id="catalog">
      <div class="tut-step-badge">3</div>
      <h2>Browse the catalog</h2>
      <p>The <a href="/catalog">public catalog</a> shows every tool your agent can call. Browse by category or search by what you want to do — not by API name.</p>
      <ul>
        <li><strong>Platform pages</strong> — e.g. <a href="/catalog/google">/catalog/google</a> — list every endpoint for one provider with live pricing.</li>
        <li><strong>Use-case pages</strong> — group providers that do the same job so you can compare them side by side.</li>
        <li><strong>Workflow pages</strong> — show multi-step agents with the cost of each hop.</li>
      </ul>
      <p>Every endpoint shows its cost before you call it. No surprise bills.</p>
    </section>

    <!-- STEP 4: Pricing -->
    <section class="tut-step" id="pricing">
      <div class="tut-step-badge">4</div>
      <h2>Pricing &amp; billing</h2>
      <p>Olywork charges in <strong>integer micro-USD</strong> — fractions of a cent per call. There are no monthly seats, no tiers, no API rate limits beyond the upstream provider.</p>
      <ul>
        <li>A Google Search call costs ~$0.004.</li>
        <li>A Twitter post costs ~$0.002.</li>
        <li>Some providers (GitHub public API) are effectively free.</li>
      </ul>
      <p>You can top up your balance any time. Failed calls are never billed. If a call succeeds upstream but the response is lost, an <code>Idempotency-Key</code> returns the stored result without paying twice.</p>

      <div class="code-block">
        <div class="code-block-head"><span>Check balance</span></div>
        <pre><span class="c-fn">olywork</span> balance</pre>
      </div>
    </section>

    <!-- STEP 5: Own keys -->
    <section class="tut-step" id="own-keys">
      <div class="tut-step-badge">5</div>
      <h2>Bring your own API keys</h2>
      <p>If you already have an API key for a provider, register it once. Your key takes precedence over Olywork's — those calls are never metered against your balance.</p>

      <div class="code-block">
        <div class="code-block-head"><span>Register your own key</span></div>
        <pre><span class="c-fn">olywork</span> keys set openai sk-proj-abc123...</pre>
      </div>

      <div class="callout info">
        <b>Your key always wins.</b> It is never routed through Olywork's proxy. If you have a key, it&#39;s used directly with zero metering.
      </div>
    </section>

    <!-- STEP 6: OAuth -->
    <section class="tut-step" id="oauth">
      <div class="tut-step-badge">6</div>
      <h2>OAuth — act on behalf of your users</h2>
      <p>For tools that require OAuth (Twitter DMs, LinkedIn posts, Google Drive access), Olywork handles the entire consent flow. Your users click "Connect Twitter" and your agent is immediately authorized to act on their behalf.</p>
      <p>Connections are scoped per-user and per-org. You never see the raw token — Olywork injects it server-side and relays the upstream response verbatim.</p>
      <p><a href="/catalog">Browse OAuth-enabled tools &rarr;</a></p>
    </section>

    <!-- STEP 7: MCP -->
    <section class="tut-step" id="mcp">
      <div class="tut-step-badge">7</div>
      <h2>MCP integration (Claude, Cursor, opencode)</h2>
      <p>Olywork ships two MCP endpoints: <code>/mcp</code> (MCP v1) and <code>/mcp/v2</code>. Claude Code, Cursor, and opencode all connect to the v2 endpoint automatically when you run <code>olywork install</code>.</p>

      <div class="code-block">
        <div class="code-block-head"><span>Manual MCP v2 config</span></div>
        <pre>{
  <span class="c-key">"mcpServers"</span>: {
    <span class="c-key">"olywork"</span>: {
      <span class="c-key">"url"</span>: <span class="c-str">"{BASE}/mcp/v2"</span>,
      <span class="c-key">"headers"</span>: {
        <span class="c-key">"Authorization"</span>: <span class="c-str">"Bearer $OLYWORK_TOKEN"</span>
      }
    }
  }
}</pre>
      </div>
    </section>

    <!-- CTA -->
    <div class="tut-cta">
      <h2>Ready to connect your agent?</h2>
      <p>Start with $1 of free credit. No credit card required.</p>
      <div class="btns">
        <a href="/app" class="btn-accent" style="text-decoration:none;">Create free account &rarr;</a>
        <a href="/catalog" class="btn-ghost" style="text-decoration:none;color:rgba(252,251,250,0.7);border-color:rgba(255,255,255,0.15);">Browse catalog</a>
      </div>
    </div>
  </main>
</div>

<footer class="ow-footer">
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
</footer>
<script>
// Active sidebar link on scroll
const sections = document.querySelectorAll('.tut-step[id]');
const navLinks = document.querySelectorAll('.tut-sidebar a');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      navLinks.forEach(l => l.classList.toggle('active', l.getAttribute('href') === '#'+e.target.id));
    }
  });
}, { rootMargin: '-80px 0px -60% 0px' });
sections.forEach(s => observer.observe(s));
</script>
</body>
</html>'''

with open("src/olywork/web/tutorial.html", "w") as f:
    f.write(html)
print("tutorial.html written")
