import re

with open("src/olywork/web/tutorial.html", "r") as f:
    content = f.read()

# Replace variables in tutorial.html
content = re.sub(r':root\{[^}]*\}', """:root{
  --bg: #F4F2EC; --surface: #FCFBFA; --panel: #FFFFFF; --panel2: #F0EEE6;
  --ink: #202020; --muted: #7E7C74; --muted2: #A09E96;
  --line: #E8E5DA; --line2: #D5D1C3; --hover: rgba(0,0,0,0.05);
  --green: #22C55E; --amber: #F59E0B; --red: #EF4444; --teal: #202020;
  --accent: #9FF25F;
  --shadow-sm: none; --shadow-md: none;
  --ease: cubic-bezier(.2,.72,.25,1); --r: 16px; --rb: 12px;
  --mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  --sans: "Inter", sans-serif;
  --display: "Plus Jakarta Sans", sans-serif;
}""", content)

# Remove any data-theme="dark" variations if they exist, or fix them
content = re.sub(r'\[data-theme=dark\]\{[^}]*\}', '', content)

# Make body use Inter
content = content.replace("font-family:var(--sans)", "font-family:var(--sans)")

with open("src/olywork/web/tutorial.html", "w") as f:
    f.write(content)
