# 安装说明（供 Agent 执行）

## 1 范围

本文件供 Agent 在用户要求安装 html-report-style 时执行。安装内容是一个技能目录 `html-report-style`；仓库不含官方字体文件。

## 2 术语和定义

2.1 技能目录：宿主读取技能的文件夹，其下每个子文件夹含一个 `SKILL.md`。

2.2 系统字体模式：运行 `scripts/create_report.py` 时加 `--system-fonts`，报告不嵌入字体，使用阅读设备上的系统字体。

## 3 前置条件

3.1 应先确认已安装 Git 和 Python 3：`git --version`；macOS / Linux 运行 `python3 --version`，Windows 运行 `python --version`。未安装时，应告知用户并停止，不应自行安装。

3.2 生成报告不需要第三方 Python 包。画科研图需要 matplotlib（`python -m pip install -r requirements-plot.txt`），渲染 Mermaid 需要 Node.js 和 `@mermaid-js/mermaid-cli`。这两项可选，用户需要图形时应先征得同意再安装，不应预先安装。

## 4 安装步骤

4.1 应先问清用户使用的宿主，按下表确定技能目录。

| 宿主 | 技能目录 |
|---|---|
| Claude Code | `~/.claude/skills/` |
| Codex 等读取 `~/.agents/skills/` 的 Agent | `~/.agents/skills/` |

注：旧版 README 把仓库克隆到 `~/.codex/skills/`，该路径本次没有重新测试。

4.2 应检查 `<技能目录>/html-report-style` 是否已存在。已存在时，应告知用户，不应覆盖或删除，因为其中可能有用户的修改，也可能是指向别处的链接；由用户决定更新还是换位置。

4.3 目标位置不存在时，应运行：

```bash
git clone https://github.com/RZX00/html-report-style.git <技能目录>/html-report-style
```

4.4 应告知用户：仓库不分发官方字体，默认用系统字体生成报告，字形与官方文档页面有差异。用户已有权使用的字体文件时，生成时改用 `--font-dir <字体目录>`；所需文件名和来源见 `assets/fonts/manifest.json`。

## 5 验证

5.1 应确认 `<技能目录>/html-report-style/SKILL.md` 存在。

5.2 宜在系统临时目录生成一份示例报告，确认脚本可运行；该命令不联网，输出文件已存在时会拒绝覆盖。

```bash
python <技能目录>/html-report-style/scripts/create_report.py --output <临时目录>/check.html --system-fonts
```

5.3 应提示用户开一个新会话，宿主在会话开始时加载技能。

5.4 应把第一句可用的话告诉用户，见 7。

## 6 卸载

6.1 应删除 `<技能目录>/html-report-style`。该目录是克隆目录，删除前应确认其中没有用户未提交的修改。

## 7 示例

<examples>
<example>
用户：帮我安装 html-report-style。
Agent：你用 Claude Code 还是 Codex？
用户：Claude Code。
Agent：（确认 `~/.claude/skills/html-report-style` 不存在，运行 `git clone`，在临时目录生成示例报告并报告路径）装好了，在 `~/.claude/skills/html-report-style`。仓库不带官方字体，报告用系统字体，字形和官方文档页面会有差异。开一个新会话，然后对我说：「用 html-report-style，把这份分析做成一份报告，保存为 ./report.html。」
</example>
</examples>
