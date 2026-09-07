import re

with open("src/olywork/web/connect-demo.html", "r") as f:
    content = f.read()

# Replace hardcoded dark colors
content = content.replace("border:1px solid #2a2a2a", "border:1px solid var(--line)")
content = content.replace("border:1px solid #333", "border:1px solid var(--line)")
content = content.replace("border-color:#1c5c3a", "border-color:var(--green)")
content = content.replace("background:#123a25", "background:rgba(34, 197, 94, 0.1)")
content = content.replace("color:#7fdcae", "color:var(--green)")
content = content.replace("background:#1a1a1a", "background:var(--surface)")
content = content.replace("background:#e0703f", "background:var(--accent)")
content = content.replace("border-color:#e0703f", "border-color:var(--accent)")
content = content.replace("color:#161310", "color:var(--ink)")
content = content.replace("background:#141414", "background:var(--bg)")
content = content.replace("border:1px solid #262626", "border:1px solid var(--line)")

with open("src/olywork/web/connect-demo.html", "w") as f:
    f.write(content)

