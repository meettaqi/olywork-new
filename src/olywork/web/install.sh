#!/bin/sh
# olywork CLI installer  -  curl -fsSL https://olywork.com/install.sh | sh
# Installs the `olywork` command and points it at this server ({BASE}).
set -e

BASE="{BASE}"

# Optional token for a one-shot, fully-authed setup:
#   curl -fsSL {BASE}/install.sh | sh -s -- --token <key>      (or: OLYWORK_TOKEN=<key> … | sh)
# With it, this installs the CLI + skill AND signs in + registers the MCP server into every supported
# agent, header-authed — no browser. The key bakes in the team, so nothing else is needed. Without a
# token, it installs the CLI + skill and prints the sign-in step (the original behavior, unchanged).
TOKEN="${OLYWORK_TOKEN:-${OLYWORK_TOKEN:-}}"
while [ $# -gt 0 ]; do
  case "$1" in
    --token) TOKEN="$2"; shift 2 ;;
    --token=*) TOKEN="${1#--token=}"; shift ;;
    *) shift ;;
  esac
done
# Install from PyPI (fast, public, no git clone). The base package is the light CLI; the FastAPI/DB
# server stack is the `tools-registry[server]` extra, which people who self-host install separately.
#
# `[proxy]` is included here on purpose. It adds only `cryptography`, which is what `olywork <command>`
# needs to generate this machine's certificate authority — and it ships as a prebuilt wheel, so there
# is no compiler and no meaningful wait.
SRC="tools-registry[proxy]"

# The supported interpreter range — keep in sync with `requires-python` in pyproject.toml.
PYREQ=">=3.12,<3.14"

printf '\n\033[38;5;173m▚ olywork\033[0m - installing the olywork CLI…\n\n'

if command -v uv >/dev/null 2>&1; then
  uv tool install --force --python "$PYREQ" "$SRC"
elif command -v pipx >/dev/null 2>&1; then
  PIPX_PY=""
  for py in python3.13 python3.12; do
    if command -v "$py" >/dev/null 2>&1; then PIPX_PY="$py"; break; fi
  done
  if [ -n "$PIPX_PY" ]; then
    pipx install --force --python "$PIPX_PY" "$SRC"
  else
    pipx install --force "$SRC"
  fi
elif command -v pip3 >/dev/null 2>&1; then
  pip3 install --user --upgrade "$SRC"
else
  echo "Need Python 3.12 or 3.13 and one of: uv (recommended), pipx, or pip3." >&2
  echo "Install uv:  https://docs.astral.sh/uv/getting-started/installation/" >&2
  exit 1
fi

CMD_NAME="olywork"
command -v olywork >/dev/null 2>&1 && CMD_NAME="olywork"

# point the CLI at this server (falls back silently on older CLIs)
$CMD_NAME config --base-url "$BASE" >/dev/null 2>&1 || true

# install the official olywork skill into every detected agent so it knows how to use olywork.
if $CMD_NAME skill bootstrap 2>/dev/null; then
  :
else
  SKILL_DIR="$HOME/.claude/skills/olywork"
  if mkdir -p "$SKILL_DIR" 2>/dev/null && curl -fsSL "$BASE/skill.md" -o "$SKILL_DIR/SKILL.md" 2>/dev/null; then
    printf '\033[32m✓\033[0m Installed the \033[1molywork\033[0m skill for Claude Code (%s)\n' "$SKILL_DIR"
  fi
fi

# One-shot authed setup when a token was passed
if [ -n "$TOKEN" ]; then
  if $CMD_NAME login --token "$TOKEN" >/dev/null 2>&1; then
    printf '\033[32m✓\033[0m Signed in.\n'
    $CMD_NAME mcp install 2>/dev/null || true
  else
    printf '\033[33m!\033[0m That token did not verify — run \033[1m%s login\033[0m to sign in.\n' "$CMD_NAME"
  fi
  printf '\n\033[32m✓\033[0m olywork is set up. Docs & tutorial:  %s/tutorial\n\n' "$BASE"
else
  printf '\n\033[32m✓\033[0m Installed \033[1molywork\033[0m. Next:\n'
  printf '    \033[38;5;173m%s login\033[0m      # sign in (GitHub or email) - first login registers you\n' "$CMD_NAME"
  printf '    \033[38;5;173m%s mcp install\033[0m  # optional: add olywork as an MCP server in your agents\n' "$CMD_NAME"
  printf '\nDocs & interactive tutorial:  %s/tutorial\n\n' "$BASE"
fi
