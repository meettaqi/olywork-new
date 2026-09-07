import glob
import re

html_files = glob.glob("src/olywork/web/*.html")

font_tags = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">"""

for f in html_files:
    if "tutorial" in f or "index.html" in f:
        # Avoid breaking the tutorial or Vue app
        pass
    
    with open(f, "r") as file:
        content = file.read()
        
    if "Plus+Jakarta+Sans" not in content and "<head>" in content:
        content = content.replace("</head>", font_tags + "\n</head>")
        with open(f, "w") as file:
            file.write(content)
