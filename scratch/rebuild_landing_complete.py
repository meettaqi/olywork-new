import os, re

logos = [f for f in os.listdir("src/olywork/web/logos/platforms") if f.endswith(".svg") and f not in ["companies.svg"]]
# Build two rows for seamless marquee
row1 = logos[:len(logos)//2]
row2 = logos[len(logos)//2:]

def logo_items(items, count=2):
    html = ""
    for _ in range(count):  # duplicate for seamless loop
        for l in items:
            name = l.replace(".svg","").replace("-"," ").title()
            html += f'<div class="ow-ticker-logo" title="{name}"><img src="/logos/platforms/{l}" alt="{name}" loading="lazy"></div>\n'
    return html

with open("src/olywork/web/landing.html", "r") as f:
    content = f.read()

# Replace logo ticker section with new design
old_ticker = re.search(r'<section class="logo-ticker">.*?</section>', content, re.DOTALL)
if old_ticker:
    new_ticker = f'''<div class="ow-ticker" style="padding:32px 0;margin:0;">
  <div class="ow-ticker-row">
{logo_items(row1)}
  </div>
  <div class="ow-ticker-row rev">
{logo_items(row2)}
  </div>
</div>'''
    content = content[:old_ticker.start()] + new_ticker + content[old_ticker.end():]

with open("src/olywork/web/landing.html", "w") as f:
    f.write(content)

print("Landing logo ticker rebuilt")
