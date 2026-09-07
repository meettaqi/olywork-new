import glob

def process_css(filename):
    with open(filename, "r") as f:
        content = f.read()
    
    # Overwrite the :root to standard TryBounty colors
    if ":root" in content:
        import re
        content = re.sub(r':root\s*\{[^}]*\}', """:root{
  --bg: #F4F2EC; --surface: #FCFBFA; --panel: #FFFFFF; --panel2: #F0EEE6;
  --ink: #202020; --muted: #7E7C74; --muted2: #A09E96;
  --line: #E8E5DA; --line2: #D5D1C3;
  --teal: #202020;
  --green: #22C55E; --amber: #F59E0B; --red: #EF4444;
  --accent: #9FF25F;
  --inverse: #1A1A1A; --inverse-ink: #FCFBFA;
  --shadow-sm: none;
  --shadow-md: none;
  --shadow-lg: none;
  --ease: cubic-bezier(.2,.72,.25,1);
  --r: 16px; --rb: 12px;
  --display: "Plus Jakarta Sans", sans-serif;
  --sans: "Inter", sans-serif;
  --mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
}""", content)
    
    # Also adjust any dark mode hardcoded values like background: #151412
    content = content.replace("background:#151412", "background:var(--bg)")
    content = content.replace("background:rgba(21,20,18,.86)", "background:rgba(244,242,236,.86)")
    content = content.replace("color:var(--ink70)", "color:var(--muted)")
    content = content.replace("color:var(--ink55)", "color:var(--muted2)")
    content = content.replace("background:linear-gradient(var(--bg) 60%,transparent)", "background:rgba(244,242,236,.95); backdrop-filter:blur(12px);")
    content = content.replace("box-shadow:var(--shadow-md)", "box-shadow:none; border:1px solid var(--line)")
    content = content.replace("box-shadow:var(--shadow-lg)", "box-shadow:none; border:1px solid var(--line)")
    
    # Remove film grain
    content = re.sub(r'body::before[^}]*\}', '', content)

    # Make buttons TryBounty style
    content = content.replace("border-radius:var(--rb)", "border-radius:999px")
    
    with open(filename, "w") as f:
        f.write(content)

for f in ["src/olywork/web/catalog.css", "src/olywork/web/legal.css", "src/olywork/web/usecase.css"]:
    process_css(f)

