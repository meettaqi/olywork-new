import re

with open("src/olywork/web/index.html", "r") as f:
    content = f.read()

# Make the light theme use TryBounty variables
content = re.sub(r'\[data-theme="light"\]\s*\{[^}]*\}', """[data-theme="light"]{
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
  --ease: cubic-bezier(.2,.72,.25,1); --ease-out: cubic-bezier(.22,1,.36,1);
  --r: 16px; --rb: 12px;
  --sans: "Inter", sans-serif;
  --display: "Plus Jakarta Sans", sans-serif;
}""", content)

# Remove the body::before grain for dark theme as well just in case
content = re.sub(r'body::before[^}]*\}', '', content)

with open("src/olywork/web/index.html", "w") as f:
    f.write(content)

