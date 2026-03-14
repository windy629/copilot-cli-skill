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


---

# 中文说明

copilot-cli-skill 是一个供 OpenClaw 使用的技能，封装了 GitHub Copilot CLI（`copilot`）的调用，方便 agent 程序化地运行 Copilot CLI 的命令（如 chat、suggest、agents 等），并以 JSON 返回结果。

包含内容
- SKILL.md — 技能描述与使用注意事项
- scripts/run-copilot.sh — Shell 包装脚本，运行 `copilot`，并返回 JSON（exit/stdout/stderr）
- scripts/run-copilot-programmatic.py — Python 辅助脚本，支持超时并以 JSON 返回

快速开始
1. 安装 Copilot CLI：请参考 https://docs.github.com/copilot/how-tos/copilot-cli
2. 确保 `copilot` 在 PATH 中并已认证（例如运行 `copilot auth login`）。
3. 在 OpenClaw 的 agent 或技能中调用封装脚本：
   - Shell: `/home/km/.openclaw/workspace/skills/copilot-cli-skill/scripts/run-copilot.sh chat "解释这段代码" --json`
   - Python: `python3 /home/km/.openclaw/workspace/skills/copilot-cli-skill/scripts/run-copilot-programmatic.py --timeout 30 -- chat "解释这段代码" --json`

安全说明
- 这些脚本以 OpenClaw 进程的权限运行命令。不要将不受信的输入直接传给它们，避免命令注入风险。
- 尽量使用参数数组的程序化调用（见 run-copilot-programmatic.py）以减少 shell 注入风险。

许可证
MIT — 见 LICENSE
