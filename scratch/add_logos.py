import glob
import os

logos = glob.glob("src/olywork/web/logos/platforms/*.svg")
logos = [os.path.basename(l) for l in logos if os.path.basename(l) != "companies.svg"]

# Create a marquee of provider logos
marquee_html = f"""
<style>
.logo-ticker {{ padding: 60px 0; overflow: hidden; width: 100%; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); background: var(--bg); }}
.logo-row {{ display: flex; width: max-content; animation: ticker 60s linear infinite; gap: 40px; align-items: center; }}
.logo-item {{ display: flex; align-items: center; justify-content: center; width: 64px; height: 64px; background: var(--surface); border-radius: 16px; border: 1px solid var(--border); padding: 12px; }}
.logo-item img {{ width: 100%; height: 100%; object-fit: contain; }}
</style>
<section class="logo-ticker">
  <div class="logo-row">
"""
# Generate two sets to ensure seamless infinite scroll
items = ""
for logo in logos:
    items += f'    <div class="logo-item" title="{logo.replace(".svg", "")}"><img src="/logos/platforms/{logo}" alt="{logo.replace(".svg", "")}"></div>\n'

marquee_html += items * 2
marquee_html += """  </div>
</section>
"""

with open("src/olywork/web/landing.html", "r") as f:
    content = f.read()

# Insert the logo marquee just after the hero section
content = content.replace("</section>\n\n<section class=\"ticker-section\">", "</section>\n" + marquee_html + "\n<section class=\"ticker-section\">")

with open("src/olywork/web/landing.html", "w") as f:
    f.write(content)

