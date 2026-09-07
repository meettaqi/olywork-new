# tools-registry — onboarding

The bootstrap an agent (or human) follows to start calling shared tools and to share its own.
The CLI is a thin client over the API at `https://olywork.com`; the API is the only brain.

## 1. Install the CLI

```bash
curl -fsSL https://olywork.com/install.sh | sh   # installs `olywork`, points it at the registry
```

(Working from a clone instead? `uv sync && uv run olywork --help`.)

## 2. Sign in

Three doors, one identity (your email):

```bash
olywork login                                  # GitHub OAuth (opens the browser)
olywork login --email you@example.com          # email one-time code
olywork login --token <TOKEN>                  # agents/CI: a per-org token from a team owner
```

Your token identifies you on every call (`X-Olywork-Token`). New here? `olywork onboard` walks you
through everything with a disposable demo team.

## 3a. Use a tool someone already shared (consumer)

```bash
olywork tool ls                                 # what's available
olywork call posthog query/events --query limit=5
olywork run gh -- pr list                       # vendor CLIs work too
```

You hold **no upstream key** — the registry injects it server-side.

## 3b. Share your own (creator)

Point olywork at a project — it finds the provider keys in the `.env`, the skill folders, and the
installed catalog CLIs, and registers what you pick:

```bash
olywork scan          # read-only preview; nothing leaves the machine
olywork upload        # register (encrypted server-side); idempotent, --replace to update
```

For one skill or a tricky tool (multi-credential, OAuth), see the manual flow in
[`USAGE.md`](../USAGE.md) — `olywork skill init` / `skill add`, `olywork tool add --bind`,
`olywork oauth connect`.

## 4. Verify + observe

```bash
olywork call <tool> <upstream-path>     # smoke-test
olywork calls                           # audit: who called which tool, when, status
olywork health                          # credential health across the org
```

## Notes

- Secrets are write-only; the API never returns a stored value.
- A tool can reference a secret another member uploaded (use-without-hold).
- Everything is org-scoped: `olywork org ls` / `olywork org use <slug>` picks the active team.
