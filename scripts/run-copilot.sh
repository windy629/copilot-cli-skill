#!/usr/bin/env bash
set -euo pipefail

# Wrapper to run copilot CLI with args and return JSON with exit/stdout/stderr
OUT_FILE=$(mktemp)
ERR_FILE=$(mktemp)
EXIT=0

if ! copilot "$@" >"$OUT_FILE" 2>"$ERR_FILE"; then
  EXIT=$?
fi

STDOUT=$(sed -e 's/"/\\"/g' "$OUT_FILE" | tr -d '\r')
STDERR=$(sed -e 's/"/\\"/g' "$ERR_FILE" | tr -d '\r')
rm -f "$OUT_FILE" "$ERR_FILE"
printf '{"exit": %d, "stdout": "%s", "stderr": "%s"}\n' "$EXIT" "$STDOUT" "$STDERR"
