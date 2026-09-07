---
title: Shell mode (olywork shell) — transparent CLI interception
status: shipped
sources:
  - src/olywork/shell.py
  - src/olywork/cli.py
related:
  - architecture/local-run.md
  - architecture/local-proxy.md
  - interface/cli.md
---

# Shell mode (`olywork shell`)

Run a team's registered CLIs (`stripe`, `gh`, `neonctl`, …) as if they were installed with the team
credential — no key typed, no `olywork run`. `olywork shell start` opens a subshell; inside it, `stripe balance`
just works; `exit` (or closing the terminal) reverts everything.

## The mechanic — shadow CLIs on `PATH`, not a shell hook
`start_session` creates a private `0700` session dir under `$XDG_RUNTIME_DIR`/`$TMPDIR`, writes one **shim**
per registered CLI into its `bin/`, and launches `$SHELL` with that dir **first on `PATH`**. The shell's own
name resolution does the "is this a registered CLI?" test for free: `stripe` finds our shim first and is
routed through olywork; `ls`/`git` have no shim and resolve normally. No `preexec`/`DEBUG` traps.

`plan_shims(tools, server_for)` picks which CLIs to shadow — every tool with a `cli.bin` that is
`cli.enabled` (owner opt-in; a non-enabled tool's `olywork run` would 403) — and assigns each a route
(`local`/`server`), returning `(entries, warnings)`. A bin that isn't a plain filename is skipped (a shim is
a file we write).

## The shim (`shim_script` / `write_shims`)
Each shim is `exec env PATH="$OLYWORK_SHELL_REALPATH" olywork run [--server] <tool> -- "$@"`. Two things the clean
`$OLYWORK_SHELL_REALPATH` (the original PATH, captured before the shim dir was prepended) buys: `olywork run`'s own
`shutil.which(<bin>)` finds the REAL binary, so the shim can't recurse into itself, AND the real CLI runs.
The literal `--` fences olywork's parsing from the user's args (which `_run_local` then strips), so the CLI
receives exactly what was typed. A **cobra `__complete*` bypass** execs the real bin directly for shell
tab-completion — completion is local shell metadata that needs no credential, and routing it through olywork
would flood the audit and burn the daily cap one keystroke at a time.

## Session lifecycle
`start_session` publishes `OLYWORK_SHELL` (marks/blocks a nested session), `OLYWORK_SHELL_DIR`,
`OLYWORK_SHELL_REALPATH`, and `OLYWORK_SHELL_PID`, then runs the subshell via `_run_subshell` and tears the session
dir down on exit. `_run_subshell` IGNORES `SIGINT`/`SIGQUIT` (they belong to the interactive foreground child)
and handles `SIGTERM`/`SIGHUP` by stopping the child — so `stop_session` (which signals `OLYWORK_SHELL_PID`) and
a closed terminal both return control for teardown, no orphan. An optional `--ttl` arms a daemon timer that
closes the session after N minutes. `cmd_shell_start` / `cmd_shell_stop` (in `cli.py`) wire the command.

## Routing (`--server-for`) + tiers
By default every shimmed CLI runs **local** (`olywork run <tool>`). `--server-for stripe,render` routes those to
`olywork run --server` — the key never touches the machine, output is streamed back — but only for a tool that is
`server_runnable`; a requested tool that isn't falls back to local with a warning. `--ttl` sets a hard cap.

## `--proxy`: the other half of interception
**Note the sibling.** `olywork <command>` (`cmd_with`, see [local-proxy](../architecture/local-proxy.md))
does the same capture for ONE command without a subshell, and is the door most people should use.
`--proxy` is for a session where the team's CLIs (via shims) and raw HTTPS calls (via the proxy) should
both work at once.

A shim catches a registered CLI the **member types** (`stripe balance`). `olywork shell start --proxy` also
catches an HTTPS call the **agent makes on its own**, from a script that never heard of olywork — see
[local-proxy](../architecture/local-proxy.md). It is **opt-in** while the feature is new: interception is
the first thing here that can break an agent's own calls (a certificate-pinned client), and a surprise is
worse than a flag.

`cmd_shell_start` → `_start_local_proxy` (in `cli.py`) generates/loads the CA, seeds the allow-list from
the tool listing **already fetched for the shims** (every registered host, including tools with no CLI, so
no second request), starts the proxy and hands `start_session` two things: `extra_env` (the proxy URL +
trust bundle) and `on_close` (stop the proxy). `extra_env` is applied AFTER our own variables and skips
`PATH`/`OLYWORK_SHELL*`, so an add-on cannot break name resolution or fake a nested session. The banner lists
the captured hosts and says everything else goes out untouched — a member must never discover
interception by accident. `--proxy-port` moves it off 18791; `--renew-ca` regenerates the authority.

## Phasing (why no in-memory agent)
This is Phase 1 — the shims call `olywork run`, reusing the whole local-run path (grant, deny, runner-proof,
OAuth leaf, audit → metering/caps) for free. The planned Phase-2 in-memory session agent was **deliberately
dropped**: `olywork run`'s per-command dedicated-user isolation ([local-run](../architecture/local-run.md)) leaves
nothing in the member's process after each call, which is a *stronger* posture than a long-lived agent holding
credentials in RAM. So shell mode stays a thin convenience over `olywork run`; the real guarantees live in the
[local-run sandbox](../architecture/local-run.md) (isolation + egress + redaction + deny).
