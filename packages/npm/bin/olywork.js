#!/usr/bin/env node
// @olywork/olywork — npm launcher for the olywork CLI (a Python tool).
// Finds an installed `olywork`; if missing, installs it via the registry's
// installer (https://olywork.com/install.sh), then execs it.
'use strict';

const { spawnSync } = require('node:child_process');
const { existsSync } = require('node:fs');
const os = require('node:os');
const path = require('node:path');

const BASE = process.env.OLYWORK_BASE_URL || process.env.OLYWORK_BASE_URL || 'https://olywork.com';
const args = process.argv.slice(2);

function findOlywork() {
  const probe = spawnSync(process.platform === 'win32' ? 'where' : 'which', ['olywork'], {
    encoding: 'utf8',
  });
  if (probe.status === 0 && probe.stdout.trim()) return probe.stdout.trim().split('\n')[0];
  // common install location not always on npm's PATH
  const local = path.join(os.homedir(), '.local', 'bin', 'olywork');
  if (existsSync(local)) return local;
  return null;
}

function run(bin) {
  const res = spawnSync(bin, args, { stdio: 'inherit' });
  process.exit(res.status === null ? 1 : res.status);
}

let bin = findOlywork();
if (bin) run(bin);

if (process.platform === 'win32') {
  console.error('olywork is a Python CLI. Install it with:');
  console.error('  uv tool install olywork');
  console.error('(get uv: https://docs.astral.sh/uv/getting-started/installation/)');
  process.exit(1);
}

console.error(`olywork not found — installing from ${BASE} ...`);
const install = spawnSync('sh', ['-c', `curl -fsSL ${BASE}/install.sh | sh`], {
  stdio: 'inherit',
});
if (install.status !== 0) {
  console.error('\nAutomatic install failed. Install manually:');
  console.error(`  curl -fsSL ${BASE}/install.sh | sh`);
  process.exit(install.status === null ? 1 : install.status);
}

bin = findOlywork();
if (!bin) {
  console.error('\nInstalled, but `olywork` is not on PATH. Add ~/.local/bin to your PATH and retry.');
  process.exit(1);
}
run(bin);
