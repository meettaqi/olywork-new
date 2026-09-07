#!/usr/bin/env bash
# fresh-test-reset.sh — wipe every trace of olywork from this machine so the next
# onboarding run is a true first-time experience. No backups: this is a dev tool
# for testing signup/install flows, and everything it removes is re-creatable
# (`olywork login`, `olywork mcp install`, install.sh).
#
# Removes, when present:
#   ~/.olywork/                      CLI login token, active org, local-proxy CA state
#   ~/.claude/skills/olywork/        the agent skill install.sh drops into Claude Code
#   Claude Code MCP registration  `claude mcp remove olywork` (user scope)
#   Codex MCP registration        `codex mcp remove olywork`, if a codex CLI exists
#   the olywork binary itself        uv tool / pipx / brew / pip, whichever answers
#
# Deliberately NOT touched: a repo checkout's .env (server-side platform keys,
# not user state) and ~/.local/bin on PATH generally.

set -uo pipefail

say()  { printf '  %-34s %s\n' "$1" "$2"; }

echo "olywork fresh-test reset"

# ---- CLI state --------------------------------------------------------------
if [ -d "$HOME/.olywork" ]; then
  rm -rf "$HOME/.olywork" && say "~/.olywork" "removed (login + proxy state)"
else
  say "~/.olywork" "not present"
fi

# ---- agent skill ------------------------------------------------------------
if [ -d "$HOME/.claude/skills/olywork" ]; then
  rm -rf "$HOME/.claude/skills/olywork" && say "~/.claude/skills/olywork" "removed"
else
  say "~/.claude/skills/olywork" "not present"
fi

# ---- MCP registrations ------------------------------------------------------
if command -v claude >/dev/null 2>&1; then
  if claude mcp get olywork >/dev/null 2>&1; then
    claude mcp remove olywork >/dev/null 2>&1 && say "claude mcp (olywork)" "removed"
  else
    say "claude mcp (olywork)" "not registered"
  fi
else
  say "claude mcp (olywork)" "claude CLI not found — skipped"
fi

if command -v codex >/dev/null 2>&1; then
  if codex mcp get olywork >/dev/null 2>&1; then
    codex mcp remove olywork >/dev/null 2>&1 && say "codex mcp (olywork)" "removed"
  else
    say "codex mcp (olywork)" "not registered"
  fi
fi

# ---- the binary -------------------------------------------------------------
# Try each installer that could own it; the package is named tools-registry on
# PyPI but olywork in Homebrew. Loop because more than one can be present at once.
removed_binary=""
if command -v uv >/dev/null 2>&1 && uv tool list 2>/dev/null | grep -q '^tools-registry '; then
  uv tool uninstall tools-registry >/dev/null 2>&1 && removed_binary="$removed_binary uv-tool"
fi
if command -v pipx >/dev/null 2>&1 && pipx list 2>/dev/null | grep -q 'tools-registry'; then
  pipx uninstall tools-registry >/dev/null 2>&1 && removed_binary="$removed_binary pipx"
fi
if command -v brew >/dev/null 2>&1 && brew list olywork >/dev/null 2>&1; then
  brew uninstall olywork >/dev/null 2>&1 && removed_binary="$removed_binary brew"
fi
if command -v olywork >/dev/null 2>&1; then
  # Still resolvable → a plain `pip install` (or stray copy). Ask pip, then fall
  # back to deleting the executable pointed at, which is at worst a dangling shim.
  pip uninstall -y tools-registry >/dev/null 2>&1 || pip3 uninstall -y tools-registry >/dev/null 2>&1
  command -v olywork >/dev/null 2>&1 && rm -f "$(command -v olywork)"
  command -v olywork >/dev/null 2>&1 || removed_binary="$removed_binary pip/stray"
fi
if [ -n "$removed_binary" ]; then
  say "olywork binary" "removed (${removed_binary# })"
elif command -v olywork >/dev/null 2>&1; then
  say "olywork binary" "STILL PRESENT at $(command -v olywork) — remove by hand"
else
  say "olywork binary" "not installed"
fi

# ---- verdict ----------------------------------------------------------------
echo
leftover=0
[ -d "$HOME/.olywork" ] && leftover=1
[ -d "$HOME/.claude/skills/olywork" ] && leftover=1
command -v olywork >/dev/null 2>&1 && leftover=1
if [ "$leftover" -eq 0 ]; then
  echo "clean — this machine now looks like a first-time user's."
else
  echo "⚠ some state survived (see above)."
  exit 1
fi
