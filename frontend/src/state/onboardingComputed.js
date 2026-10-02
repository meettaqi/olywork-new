export default {
// first-run welcome: the agent picker (step 1) and the per-agent setup line (step 2)
    welcomeAgents(){ const s = window.OlyworkAgentSetup || window.TregAgentSetup || {}; return s.agents || []; },
welcomeMoreAgents(){ const s = window.OlyworkAgentSetup || window.TregAgentSetup || {}; return s.moreAgents || []; },
welcomeAgent(){ return this.welcomeAgents.concat(this.welcomeMoreAgents).find(a=>a.id===this.welcome.agent) || this.welcomeAgents[0]; },
welcomeIsMore(){ return this.welcomeMoreAgents.some(a=>a.id===this.welcome.agent); },
welcomeSetupCmd(){ return this.buildAgentPrompt('agent', true); },
// onboarding modal: the setup line + team/token as ONE copyable block (token masked until shown)
    welcomeSetupFull(){ return this.welcomeSetupCmd+'\n\nwith team '+(this.activeSlugNow||'<team-slug>')+' token: '+(this.myToken||'<YOUR_TOKEN>'); },
welcomeSetupMasked(){ const t=this.myToken?(this.startTokenShow?this.myToken:(this.myToken.slice(0,14)+'••••••••••••••••')):'<YOUR_TOKEN>';
      return this.welcomeSetupCmd+'\n\nwith team '+(this.activeSlugNow||'<team-slug>')+' token: '+t; },
tryExamples(){ const s = window.OlyworkAgentSetup || window.TregAgentSetup || {}; return s.examples || []; },
tryOauth(){ const s = window.OlyworkAgentSetup || window.TregAgentSetup || {}; return s.oauthGroups || []; }
}
