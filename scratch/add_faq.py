import re

with open("src/olywork/web/landing.html", "r") as f:
    content = f.read()

faq_html = """
<style>
/* FAQ SECTION */
.faq-section { padding: 100px 24px; max-width: 800px; margin: 0 auto; }
.faq-title { font-family: var(--font-heading); font-size: 40px; font-weight: 800; text-align: center; margin-bottom: 48px; letter-spacing: -0.03em; }
.faq-item { border-bottom: 1px solid var(--border); padding: 24px 0; }
.faq-q { font-size: 18px; font-weight: 600; color: var(--ink); cursor: pointer; display: flex; justify-content: space-between; align-items: center; }
.faq-a { font-size: 15px; color: var(--ink-secondary); margin-top: 16px; line-height: 1.6; display: none; }
.faq-item.active .faq-a { display: block; }
.faq-icon { font-size: 24px; font-weight: 300; transition: transform 0.3s; }
.faq-item.active .faq-icon { transform: rotate(45deg); }
</style>

<section class="faq-section">
  <h2 class="faq-title">Frequently Asked Questions</h2>
  
  <div class="faq-item" onclick="this.classList.toggle('active')">
    <div class="faq-q">What is Olywork? <span class="faq-icon">+</span></div>
    <div class="faq-a">Olywork is an open marketplace and OpenRouter for AI agent tools. It provides a single API endpoint that gives your AI agents access to over 2,800 tools across 60+ providers like Google, Twitter, LinkedIn, and more, all with one unified token.</div>
  </div>
  
  <div class="faq-item" onclick="this.classList.toggle('active')">
    <div class="faq-q">How does pricing work? <span class="faq-icon">+</span></div>
    <div class="faq-a">We use a strict micro-USD pay-per-call model. There are no monthly subscriptions, no provider signups required, and no hidden markups. You simply pay fractions of a cent per successful API call based on the provider's base cost.</div>
  </div>
  
  <div class="faq-item" onclick="this.classList.toggle('active')">
    <div class="faq-q">Do I need my own API keys? <span class="faq-icon">+</span></div>
    <div class="faq-a">No. With Olywork, you don't need to manage API keys for dozens of services. Your single Olywork token instantly authenticates your agent across our entire catalog of 2,896+ endpoints.</div>
  </div>
  
  <div class="faq-item" onclick="this.classList.toggle('active')">
    <div class="faq-q">Can my agent act on behalf of my users? <span class="faq-icon">+</span></div>
    <div class="faq-a">Yes! Olywork handles all the OAuth connections natively. Your users simply click "Connect Twitter" (or any other service), and your agent is immediately authorized to act securely on their behalf.</div>
  </div>
</section>
"""

# Insert FAQ before footer
content = content.replace("<footer", faq_html + "\n<footer")

with open("src/olywork/web/landing.html", "w") as f:
    f.write(content)
