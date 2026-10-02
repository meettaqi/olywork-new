<script>
import { useDashboard } from '../state/context'
import BrandMark from './BrandMark.vue'
export default { components: { BrandMark }, setup: useDashboard }
</script>

<template>
  <div class="lp">
    <header class="lp-nav">
      <a href="/" class="brand"><BrandMark/>olywork</a>
      <nav class="lp-links">
        <a href="/tutorial">Docs</a>
        <button class="iconbtn" @click="toggleTheme" :aria-label="theme==='dark'?'Light theme':'Dark theme'">{{theme==='dark'?'◐':'◑'}}</button>
      </nav>
    </header>
    <main class="lp-hero" style="min-height:55vh">
      <template v-if="shareGate">
        <div class="lp-eyebrow">shared with you</div>
        <h1 class="lp-h1">{{shareGate.name}} <span style="color:var(--accent)">· {{shareGate.kind}}</span></h1>
        <p class="lp-lead">A teammate shared this {{shareGate.kind}} with you. Sign in to view it.</p>
      </template>
      <template v-else>
        <h1 class="lp-h1">Sign in to olywork</h1>
        <p class="lp-lead">Connect your agent and manage your team.</p>
      </template>
      <div class="lp-cta"><button class="btn primary lg" @click="demo.signin=true">{{shareGate?'Sign in to view':'Sign in'}}</button></div>
    </main>
    <footer class="ow-footer">
      <div class="ow-footer-inner">
        <div class="ow-footer-brand-wrap">
          <a class="ow-footer-brand" href="/" aria-label="olywork">
            <img src="/media/brand/olywork_Official.svg" alt="olywork" style="height:28px;width:auto;display:block;">
          </a>
          <p class="ow-footer-tagline">The OpenRouter for AI Agent Tools.<br>One token for 2,800+ endpoints. Zero key management.</p>
        </div>
        <nav class="ow-footer-nav" aria-label="Site navigation">
          <div class="ow-footer-col">
            <div class="ow-footer-head">Explore</div>
            <a href="/catalog">Catalog</a>
            <a href="/pricing">Pricing</a>
            <a href="/use-cases">Use cases</a>
            <a href="/workflows">Workflows</a>
            <a href="/agents">Agents</a>
          </div>
          <div class="ow-footer-col">
            <div class="ow-footer-head">Build</div>
            <a href="/docs">API Reference</a>
            <a href="/tutorial">Tutorial</a>
            <a href="/llms.txt">llms.txt</a>
          </div>
          <div class="ow-footer-col">
            <div class="ow-footer-head">Resources</div>
            <a href="/resources">Workflows</a>
            <a href="/use-cases/seo-data-for-ai-agents">Use Cases</a>
            <a href="/agents/claude-code">Agents</a>
          </div>
          <div class="ow-footer-col">
            <div class="ow-footer-head">Company</div>
            <a href="/blog">Blog</a>
            <a href="/support">Support</a>
            <a href="/terms">Terms</a>
            <a href="/privacy">Privacy</a>
            <a href="https://github.com/meettaqi/olywork-new" target="_blank" rel="noopener">GitHub ↗</a>
          </div>
        </nav>
      </div>
      <div class="ow-footer-bottom">
        <span class="ow-footer-copy">&copy; 2026 Olywork. All rights reserved.</span>
        <span class="ow-footer-note">Open source · Pay-per-call · No markup</span>
      </div>
    </footer>
  </div>
</template>
