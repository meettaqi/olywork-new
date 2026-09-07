def generate():
    html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Olywork — The OpenRouter for Agent Tools</title>
<meta name="description" content="Every tool your agent needs. 2,896 catalogued endpoints across 60+ providers. One token, pay per call in micro-USD."/>

<!-- {BASE} placeholder is substituted at runtime by the registry engine -->
<link rel="canonical" href="{BASE}/"/>
<link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
<link rel="apple-touch-icon" href="/media/brand/logo.png"/>

<meta property="og:type" content="website"/>
<meta property="og:site_name" content="Olywork"/>
<meta property="og:url" content="{BASE}/"/>
<meta property="og:title" content="Olywork — The OpenRouter for Agent Tools"/>
<meta property="og:description" content="Every tool your agent needs with one token. 2,896+ endpoints across 60+ providers."/>
<meta property="og:image" content="{BASE}/media/og.png"/>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">

<style>
:root {
  --bg: #F4F2EC;
  --surface: #FCFBFA;
  --surface-muted: #E8E5DA;
  --ink: #202020;
  --ink-secondary: #585750;
  --ink-muted: #7E7C74;
  --border: #E8E5DA;
  --accent: #9FF25F;
  --accent-hover: #8EE250;
  --primary-deep: #1A1A1A;
  --primary-soft: #D6E7EA;
  
  --font-heading: 'Plus Jakarta Sans', sans-serif;
  --font-body: 'Inter', sans-serif;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body { background-color: var(--bg); color: var(--ink); font-family: var(--font-body); overflow-x: hidden; -webkit-font-smoothing: antialiased; }
a { text-decoration: none; color: inherit; }
button { background: none; border: none; cursor: pointer; font-family: inherit; }

/* NAVBAR */
.navbar { position: fixed; top: 0; width: 100%; height: 80px; display: flex; align-items: center; justify-content: space-between; padding: 0 48px; background: rgba(244, 242, 236, 0.95); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(232, 229, 218, 0.6); z-index: 50; }
.brand { font-family: var(--font-heading); font-size: 24px; font-weight: 800; display: flex; align-items: center; gap: 8px; letter-spacing: -0.04em; }
.brand svg { height: 24px; width: auto; }
.nav-links { display: flex; gap: 32px; align-items: center; }
.nav-link { font-size: 15px; color: var(--ink-muted); font-weight: 500; transition: color 0.2s; }
.nav-link:hover { color: var(--ink); }

/* BUTTONS */
.btn-primary { background: var(--ink); color: #FFF; padding: 0 24px; height: 40px; border-radius: 99px; font-weight: 600; font-size: 14px; display: inline-flex; align-items: center; justify-content: center; transition: all 0.2s ease; }
.btn-primary:hover { transform: scale(1.03); background: #333; }
.btn-accent { background: var(--accent); color: var(--ink); padding: 0 40px; height: 56px; border-radius: 99px; font-weight: 700; font-size: 18px; font-family: var(--font-heading); display: inline-flex; align-items: center; gap: 12px; transition: all 0.2s ease; border: 1px solid rgba(0,0,0,0.05); }
.btn-accent:hover { transform: scale(1.03); background: var(--accent-hover); }

/* HERO */
.hero { position: relative; padding-top: 160px; min-height: 100vh; display: flex; flex-direction: column; align-items: center; z-index: 1; }
.hero-canvas { position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; opacity: 0.6; mask-image: linear-gradient(to bottom, #000 0%, #000 70%, transparent 100%); -webkit-mask-image: linear-gradient(to bottom, #000 0%, #000 70%, transparent 100%); }

.trusted { display: flex; align-items: center; gap: 16px; margin-bottom: 24px; font-size: 14px; font-weight: 500; color: var(--ink); }
.avatars { display: flex; }
.avatars img { width: 32px; height: 32px; border-radius: 50%; border: 2px solid var(--bg); margin-left: -12px; }
.avatars img:first-child { margin-left: 0; }

.headline { font-family: var(--font-heading); font-size: 72px; font-weight: 800; line-height: 1.05; text-align: center; letter-spacing: -0.04em; margin-bottom: 24px; max-width: 900px; }
.headline span { color: var(--ink-muted); }
.subhead { font-size: 20px; color: var(--ink-secondary); text-align: center; margin-bottom: 48px; max-width: 600px; line-height: 1.4; }

/* SEARCH BAR */
.search-wrapper { position: relative; width: 100%; max-width: 800px; margin-bottom: 64px; }
.search-wrapper::before { content: ''; position: absolute; inset: -4px; border-radius: 20px; background: transparent; border: 3px solid rgba(0,0,0,0.05); z-index: 0; }
.search-glass { position: relative; z-index: 1; background: rgba(255,255,255,0.4); backdrop-filter: blur(10px); border-radius: 16px; display: flex; flex-direction: column; padding: 8px; }
.search-input { width: 100%; background: transparent; border: none; font-family: var(--font-heading); font-size: 24px; padding: 24px 32px; outline: none; color: var(--ink); font-weight: 600; resize: none; overflow: hidden; min-height: 80px; }
.search-input::placeholder { color: var(--ink-muted); }
.search-btn-container { display: flex; justify-content: center; margin-top: -28px; z-index: 2; position: relative; }

/* FAN CARDS */
.fan-container { position: relative; width: 100%; max-width: 1200px; height: 500px; margin: 0 auto; perspective: 1000px; }
.fan-card { position: absolute; top: 0; width: 320px; height: 420px; border-radius: 24px; padding: 32px; display: flex; flex-direction: column; transition: transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1); transform-origin: bottom center; box-shadow: none; border: 1px solid rgba(0,0,0,0.04); }
.fan-card.c1 { background: var(--accent); left: 5%; transform: rotate(-8deg) translateY(40px); z-index: 1; }
.fan-card.c2 { background: var(--primary-deep); left: 30%; transform: rotate(-3deg) translateY(10px); z-index: 2; color: #FFF; }
.fan-card.c3 { background: var(--surface); left: 55%; transform: rotate(3deg) translateY(10px); z-index: 3; }
.fan-card.c4 { background: var(--primary-soft); left: 80%; transform: rotate(8deg) translateY(40px); z-index: 4; }

.fan-card h3 { font-family: var(--font-heading); font-size: 56px; font-weight: 800; line-height: 1; margin-bottom: 8px; letter-spacing: -0.04em; }
.fan-card p { font-size: 20px; font-weight: 600; }
.fan-card.c2 h3 { color: var(--accent); }
.fan-card.c2 p { color: #FFF; }

.fan-container:hover .fan-card.c1 { transform: rotate(-12deg) translateY(20px) translateX(-20px); }
.fan-container:hover .fan-card.c2 { transform: rotate(-5deg) translateY(-10px) translateX(-10px); }
.fan-container:hover .fan-card.c3 { transform: rotate(5deg) translateY(-10px) translateX(10px); }
.fan-container:hover .fan-card.c4 { transform: rotate(12deg) translateY(20px) translateX(20px); }


/* TICKER */
.ticker-section { padding: 40px 0; overflow: hidden; width: 100%; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); background: var(--surface); }
.ticker-row { display: flex; width: max-content; animation: ticker 40s linear infinite; gap: 32px; margin-bottom: 24px; }
.ticker-row.reverse { animation-direction: reverse; margin-bottom: 0; }
@keyframes ticker { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }

.ticker-item { display: flex; align-items: center; gap: 16px; background: var(--bg); padding: 12px 24px; border-radius: 99px; border: 1px solid var(--border); }
.ticker-tag { font-size: 13px; font-weight: 600; color: var(--ink-secondary); text-transform: uppercase; letter-spacing: 0.05em; }
.ticker-text { font-family: var(--font-heading); font-size: 18px; font-weight: 700; color: var(--ink); }

/* SPHERE SECTION */
.sphere-section { padding: 120px 0; display: flex; flex-direction: column; align-items: center; text-align: center; }
.sphere-wrapper { position: relative; width: 600px; height: 600px; display: flex; align-items: center; justify-content: center; }
.sphere-text { position: absolute; width: 100%; height: 100%; animation: spin 20s linear infinite; }
@keyframes spin { 100% { transform: rotate(360deg); } }
.sphere-center { width: 300px; height: 300px; border-radius: 50%; background: var(--surface); border: 1px solid var(--border); display: flex; align-items: center; justify-content: center; }

@media (max-width: 1024px) {
  .headline { font-size: 48px; }
  .fan-container { height: auto; display: grid; grid-template-columns: 1fr 1fr; gap: 24px; padding: 0 24px; }
  .fan-card { position: relative; left: 0 !important; top: 0 !important; transform: none !important; width: 100%; height: 300px; margin-bottom: 0; }
  .fan-container:hover .fan-card { transform: none !important; }
}
</style>
</head>
<body>

<nav class="navbar">
  <a href="/" class="brand">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
    Olywork
  </a>
  <div class="nav-links">
    <a href="/catalog" class="nav-link">Catalog</a>
    <a href="/docs" class="nav-link">Docs</a>
    <a href="/login" class="nav-link">Sign In</a>
    <a href="/post" class="btn-primary">Post a tool request</a>
  </div>
</nav>

<section class="hero">
  <canvas class="hero-canvas" id="heroCanvas"></canvas>
  
  <div class="trusted">
    <span>Trusted by 10,000+ early users</span>
    <div class="avatars">
      <img src="https://i.pravatar.cc/100?img=1" alt="User">
      <img src="https://i.pravatar.cc/100?img=2" alt="User">
      <img src="https://i.pravatar.cc/100?img=3" alt="User">
      <img src="https://i.pravatar.cc/100?img=4" alt="User">
      <img src="https://i.pravatar.cc/100?img=5" alt="User">
    </div>
  </div>

  <h1 class="headline">Get the tool you want connected.<br><span>Cheaper, faster, better.</span></h1>
  <p class="subhead">The open marketplace where AI agents seamlessly call 2,896+ tools with zero API keys and micro-USD pricing.</p>

  <div class="search-wrapper">
    <div class="search-glass">
      <textarea class="search-input" placeholder="Describe the tool integration you need..." rows="1"></textarea>
    </div>
  </div>
  <div class="search-btn-container">
    <button class="btn-accent">
      Connect a tool
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
    </button>
  </div>

  <div class="fan-container">
    <div class="fan-card c1">
      <div>
        <h3>2K+</h3>
        <p>Tools connected</p>
      </div>
    </div>
    <div class="fan-card c2">
      <div>
        <h3>100+</h3>
        <p>Active agents</p>
      </div>
    </div>
    <div class="fan-card c3">
      <div>
        <h3>$30K+</h3>
        <p>Verified API savings</p>
      </div>
    </div>
    <div class="fan-card c4">
      <div>
        <h3>99.9%</h3>
        <p>Uptime without errors</p>
      </div>
    </div>
  </div>
</section>

<section class="ticker-section">
  <div class="ticker-row">
    <!-- Duplicate for infinite scroll -->
    <div class="ticker-item"><span class="ticker-tag">Marketing</span><span class="ticker-text">Post to 5 social channels</span></div>
    <div class="ticker-item"><span class="ticker-tag">Scraping</span><span class="ticker-text">Extract top 20 competitors</span></div>
    <div class="ticker-item"><span class="ticker-tag">SEO</span><span class="ticker-text">Audit my landing page</span></div>
    <div class="ticker-item"><span class="ticker-tag">Video</span><span class="ticker-text">Generate a product demo</span></div>
    <div class="ticker-item"><span class="ticker-tag">Marketing</span><span class="ticker-text">Post to 5 social channels</span></div>
    <div class="ticker-item"><span class="ticker-tag">Scraping</span><span class="ticker-text">Extract top 20 competitors</span></div>
    <div class="ticker-item"><span class="ticker-tag">SEO</span><span class="ticker-text">Audit my landing page</span></div>
    <div class="ticker-item"><span class="ticker-tag">Video</span><span class="ticker-text">Generate a product demo</span></div>
  </div>
  <div class="ticker-row reverse">
    <div class="ticker-item"><span class="ticker-tag">Ads</span><span class="ticker-text">Create 10 ad creatives</span></div>
    <div class="ticker-item"><span class="ticker-tag">Email</span><span class="ticker-text">Find 100 qualified leads</span></div>
    <div class="ticker-item"><span class="ticker-tag">Code</span><span class="ticker-text">Review my latest PR</span></div>
    <div class="ticker-item"><span class="ticker-tag">Design</span><span class="ticker-text">Fix UI alignment issues</span></div>
    <div class="ticker-item"><span class="ticker-tag">Ads</span><span class="ticker-text">Create 10 ad creatives</span></div>
    <div class="ticker-item"><span class="ticker-tag">Email</span><span class="ticker-text">Find 100 qualified leads</span></div>
    <div class="ticker-item"><span class="ticker-tag">Code</span><span class="ticker-text">Review my latest PR</span></div>
    <div class="ticker-item"><span class="ticker-tag">Design</span><span class="ticker-text">Fix UI alignment issues</span></div>
  </div>
</section>

<section class="sphere-section">
  <div class="sphere-wrapper">
    <svg class="sphere-text" viewBox="0 0 500 500">
      <path id="curve" d="M 50, 250 a 200, 200 0 1, 1 400, 0 a 200, 200 0 1, 1 -400, 0" fill="transparent" />
      <text font-family="Plus Jakarta Sans" font-weight="700" font-size="28" letter-spacing="4" fill="var(--ink)">
        <textPath href="#curve">
          IF YOU CAN SAY WHAT DONE LOOKS LIKE, YOU CAN CONNECT IT.
        </textPath>
      </text>
    </svg>
    <div class="sphere-center">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" width="120" height="120" color="var(--ink)">
        <circle cx="12" cy="12" r="10"></circle>
        <line x1="2" y1="12" x2="22" y2="12"></line>
        <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
      </svg>
    </div>
  </div>
  <button class="btn-accent" style="margin-top: 48px;">
    Explore Catalog
  </button>
</section>

<script>
// Hero Canvas Animation (Rotating Grid/Particles)
const canvas = document.getElementById('heroCanvas');
const ctx = canvas.getContext('2d');
let width, height;

function resize() {
  width = window.innerWidth;
  height = window.innerHeight;
  canvas.width = width;
  canvas.height = height;
}
window.addEventListener('resize', resize);
resize();

const points = [];
const gridSize = 40;
for(let x = -10; x <= 10; x++) {
  for(let z = -10; z <= 10; z++) {
    points.push({x: x * gridSize, y: 0, z: z * gridSize});
  }
}

let angle = 0;
function draw() {
  ctx.clearRect(0, 0, width, height);
  ctx.fillStyle = '#F4F2EC';
  ctx.fillRect(0, 0, width, height);

  angle += 0.002;
  const cx = width / 2;
  const cy = height / 2 + 100;
  
  ctx.beginPath();
  ctx.strokeStyle = 'rgba(0, 0, 0, 0.08)';
  ctx.lineWidth = 1;

  points.forEach((p, i) => {
    // Rotate around Y
    const x = p.x * Math.cos(angle) - p.z * Math.sin(angle);
    const z = p.z * Math.cos(angle) + p.x * Math.sin(angle);
    
    // Simple projection
    const scale = 800 / (800 + z + 200);
    const px = cx + x * scale;
    const py = cy + (p.y + 150) * scale - 200;

    if (i % 21 !== 20) {
      const nextX = points[i+1].x * Math.cos(angle) - points[i+1].z * Math.sin(angle);
      const nextZ = points[i+1].z * Math.cos(angle) + points[i+1].x * Math.sin(angle);
      const nextScale = 800 / (800 + nextZ + 200);
      const npx = cx + nextX * nextScale;
      const npy = cy + (points[i+1].y + 150) * nextScale - 200;
      
      ctx.moveTo(px, py);
      ctx.lineTo(npx, npy);
    }
    
    if (i + 21 < points.length) {
      const nextX = points[i+21].x * Math.cos(angle) - points[i+21].z * Math.sin(angle);
      const nextZ = points[i+21].z * Math.cos(angle) + points[i+21].x * Math.sin(angle);
      const nextScale = 800 / (800 + nextZ + 200);
      const npx = cx + nextX * nextScale;
      const npy = cy + (points[i+21].y + 150) * nextScale - 200;
      
      ctx.moveTo(px, py);
      ctx.lineTo(npx, npy);
    }
  });
  ctx.stroke();
  requestAnimationFrame(draw);
}
draw();
</script>

</body>
</html>
"""
    with open("src/olywork/web/landing.html", "w") as f:
        f.write(html)
generate()
