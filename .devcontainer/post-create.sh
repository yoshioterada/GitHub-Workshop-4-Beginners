#!/usr/bin/env bash
set -euo pipefail

log() {
  printf "[post-create] %s\n" "$1"
}

log "Start provisioning workspace"

if command -v npm >/dev/null 2>&1; then
  log "Installing markdownlint-cli"
  npm install --global markdownlint-cli@0.39.0 >/dev/null 2>&1 || log "npm install skipped"
fi

if command -v pip >/dev/null 2>&1 && [ -f requirements.txt ]; then
  log "Installing Python dependencies"
  pip install -r requirements.txt
fi

if git config --global user.name >/dev/null 2>&1; then
  :
else
  log "Configuring git user"
  git config --global user.name "codespaces-user"
  git config --global user.email "codespaces@example.com"
fi

if command -v markdownlint >/dev/null 2>&1; then
  log "Running markdownlint"
  markdownlint docs/**/*.md || log "markdownlint completed with warnings"
fi

log "Post-create tasks finished"
