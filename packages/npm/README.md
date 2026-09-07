# @olywork/cli

npm launcher for **olywork** — call your team's APIs through one credential-injecting
proxy, with no keys on your machine.

```bash
npx @olywork/cli login
npx @olywork/cli tool ls
```

Or install globally:

```bash
npm install -g @olywork/cli
olywork login
```

olywork itself is a Python CLI; this package finds it on your machine and runs it,
installing it first (via `uv`, `pipx`, or `pip3`) if it's missing.

- Docs & interactive tutorial: https://olywork.com/tutorial
- Source: https://github.com/meettaqi/olywork-new
