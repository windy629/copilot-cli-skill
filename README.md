# copilot-cli-skill

OpenClaw skill that wraps the GitHub Copilot CLI (`copilot`) so OpenClaw agents can call Copilot CLI programmatically.

Contents
- SKILL.md — skill description and usage notes
- scripts/run-copilot.sh — shell wrapper that runs `copilot` and returns JSON (exit/stdout/stderr)
- scripts/run-copilot-programmatic.py — Python helper with timeout support that returns JSON

Quickstart
1. Install Copilot CLI: https://docs.github.com/copilot/how-tos/copilot-cli
2. Ensure `copilot` is on PATH and authenticated (e.g., `copilot auth login`).
3. From an OpenClaw-capable agent or skill, call the wrapper:
   - Shell: `/home/km/.openclaw/workspace/skills/copilot-cli-skill/scripts/run-copilot.sh chat "Explain this code" --json`
   - Python: `python3 /home/km/.openclaw/workspace/skills/copilot-cli-skill/scripts/run-copilot-programmatic.py --timeout 30 -- chat "Explain this code" --json`

Security
- Commands executed by these scripts run with the same privileges as the OpenClaw process. Do NOT expose to untrusted user input.
- Prefer argument-array programmatic calls (see run-copilot-programmatic.py) to avoid shell injection.

License
MIT — see LICENSE

