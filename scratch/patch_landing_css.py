import re

with open("src/olywork/web/landing.html") as f:
    content = f.read()

if "/olywork.css" not in content:
    content = content.replace("</head>", '<link rel="stylesheet" href="/olywork.css"/>\n</head>', 1)
    print("Added olywork.css link")
else:
    print("olywork.css already linked")

# Make sure Plus Jakarta Sans is loaded
if "Plus+Jakarta+Sans" not in content:
    content = content.replace("</head>", '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">\n</head>', 1)
    print("Added Plus Jakarta Sans")

# Fix the old Geist font - replace it
content = re.sub(
    r'<link href="https://fonts.googleapis.com/css2\?family=Geist[^"]*" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">',
    content
)

# Patch the root CSS variables in landing page inline styles
content = content.replace(
    '--font-heading: \'Plus Jakarta Sans\', sans-serif;',
    '--font-heading: "Plus Jakarta Sans", sans-serif;'
).replace(
    '--font-heading: \'Geist Pixel\'',
    '--font-heading: "Plus Jakarta Sans"'
).replace(
    'font-family: \'Geist Pixel\'',
    'font-family: "Plus Jakarta Sans"'
)

with open("src/olywork/web/landing.html", "w") as f:
    f.write(content)
print("Patched landing.html")
