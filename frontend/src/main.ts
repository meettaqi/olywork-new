import { createApp } from 'vue'
import App from './App.vue'
import './styles/base.css'
import '../../src/olywork/web/media/redesign/dashboard.css'

const app = createApp(App)
const win = window as unknown as { OlyworkAgentSetup?: Record<string, object>; TregAgentSetup?: Record<string, object> }
const setup = (win.OlyworkAgentSetup || win.TregAgentSetup || {}) as Record<string, object>
if (setup.TryItOut) app.component('TregTryItOut', setup.TryItOut)
if (setup.AgentPicker) app.component('TregAgentPicker', setup.AgentPicker)
if (setup.SetupInstructions) app.component('TregSetupInstructions', setup.SetupInstructions)
app.mount('#app')
