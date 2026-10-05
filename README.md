# HTML Report Style

生成中文优先、可离线查看的 HTML 报告，视觉参考 [Claude Code 官方中文文档](https://code.claude.com/docs/zh-CN/claude-directory)。适用于分析、规划、评审和架构说明。

独立社区 Skill，与 Anthropic 官方无隶属关系。模板保留自己的报告品牌，不包含官方网站的账号、搜索或 AI 助手服务。

## 使用

需要 Python 3.9+，无第三方 Python 依赖。

将仓库克隆到 Codex 的 Skill 目录：

```sh
git clone https://github.com/RZX00/html-report-style.git ~/.codex/skills/html-report-style
```

如果该位置已有安装，先检查原目录，勿覆盖已有修改。也可以克隆到任意目录，让 Agent 读取其中的 `SKILL.md`。

没有官方字体时，用系统字体生成可用的离线报告：

```sh
python scripts/create_report.py --output output/report.html --title "分析报告" --system-fonts
```

需要匹配原站英文字体时，先在本地准备你有权使用的字体文件，再运行：

```sh
python scripts/create_report.py --output output/report.html --title "分析报告" --font-dir /path/to/fonts
```

文件名和原始公开来源见 [字体清单](assets/fonts/manifest.json)。仓库不重新分发官方字体，也不包含内嵌这些字体的示例报告。字体的使用、嵌入和分发遵循其权利人的条款；本仓库不授予第三方字体权利。

生成后让 Agent 按 `SKILL.md` 替换示例正文、目录和元信息。脚本不会覆盖已有输出文件。内嵌字体的生成文件无需联网；系统字体模式的外观取决于本机字体，不能保证与原站一致。

## 输出选择与正文写法

默认产出一份离线中文 HTML 报告，用于给出结论、送审，或列出需要读者回答的问题。普通对话直接回答，不生成文件。只有读者必须自己操作才能看懂的部分才加交互。关闭 JavaScript 时，结论仍须可读。讲解视频和完整 Web 应用不在本 Skill 范围。

正文按约八成 ASD-STE100 受控写作：一句一事，先定义术语，结论先行，事实、推断、未知分开写。完整规则、反例与改写示例见 [输出选择与受控正文](references/output-ladder-and-prose.md)。

## 图形与科研数据

按信息选择表格、ASCII、Mermaid、SVG、可缩放画布和科研图表；不要求每份报告塞满图形。完整规范见 [图形选择指南](references/visualization-guide.md) 和 [科研绘图规范](references/scientific-figures.md)。

```sh
# 可选：科研绘图依赖
python -m pip install -r requirements-plot.txt
python scripts/plot_data.py examples/simulated.csv output/trend.svg --kind line --title "Simulated example" --xlabel "Step" --ylabel "Value" --source "Simulated teaching data, n=5" --error-label "Illustrative error magnitudes"

# 可选：Mermaid 构建依赖；报告运行时无需 Node 或网络
npm install -g @mermaid-js/mermaid-cli
python scripts/render_mermaid.py examples/flow.mmd output/flow.svg

# 将有来源和说明的 SVG/PNG 嵌入报告
python scripts/create_report.py --output output/visual-report.html --system-fonts --figures-json examples/figures.json
```

图形支持放大、缩小、拖动、适应窗口和下载。静态图在关闭 JavaScript 或打印时仍可阅读。科学图表保留原始配色和独立数据来源记录。示例 CSV 是模拟数据，不代表任何产品测量结果。

## 文件结构

- `SKILL.md`：报告生成与验证规则。
- `references/habitat-html-report-template.html`：可复用页面模板；文件名沿用历史命名。
- `references/claude-docs-visual-spec.md`：实测样式、来源和适配差异。
- `scripts/create_report.py`：将字体嵌入独立 HTML 的生成脚本。
- `agents/openai.yaml`：Codex 展示信息。

支持深浅色、章节目录、代码复制、可选文件详情组件，以及手机布局。中文标题保留官方中文页的字体栈，不额外强制宋体。不同系统的中文字体回退仍可能不同，不承诺整页像素完全一致。

### 图形深浅色适配

使用 `--theme dark` 为 Mermaid 和科研图生成深色版本，在清单中通过 `dark_file` 指定。背景、文字与坐标轴适配主题，数据颜色和热力图色阶保持一致；下载跟随当前主题，打印采用浅色版本。自有 SVG 示例提供配套深色文件。
