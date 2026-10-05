---
name: html-report-style
description: Create or update self-contained, offline Chinese HTML reports, analysis documents, plans, reviews, and architecture documentation using the Claude Code official documentation visual style. Use when the reader needs a conclusion, a review draft or questions to answer; add interaction only where the reader must operate something. Not for explainer videos or full web apps; ordinary conversational answers do not require a file.
metadata:
  short-description: Chinese HTML reports matching Claude Code Docs
---

# HTML Report Style

Produce Chinese-first, offline HTML reports matching the typography and reading layout of https://code.claude.com/docs/zh-CN/claude-directory. Use the official Chinese page as the typography reference for Chinese reports. This reference supplies visual design, not an official report-generation skill. Preserve the report's own product name and evidence.

## Output choice

The default output is one offline Chinese HTML report built from the template. Each rung below costs more to make and to check than the one before; take the lowest one that serves the reader's task. `references/output-ladder-and-prose.md` maps this to Karpathy's understanding ladder and lists boundary cases.

- **Conversation:** answer ordinary questions, status checks and yes/no questions in chat. Create no file.
- **Report (default):** when the reader needs a conclusion, a review draft or questions to answer, create the static offline report.
- **Interaction:** only for a part the reader must operate to understand, such as changing an input, filtering many rows or exploring a large map. State every conclusion, key number and representative case in static HTML that stays readable with JavaScript off. Keep controls offline and inside the visual contract. A full web app (server, login, live data, shared state) is outside this skill.
- **Video:** explainer videos (narrated animation, 3Blue1Brown-style, synthetic voice) are outside this skill. Do not script, render or embed one; say so and offer the report with diagrams.

An explicit user format choice, such as Markdown, overrides the HTML default. Video and full web apps stay out of scope.

## Starting point

Read `references/habitat-html-report-template.html` before creating a report. This historical filename now contains the Claude documentation template and is the single reusable skeleton. Do not recreate the previous engineering dashboard styling.

Public distribution does not bundle third-party font binaries. Create an offline starter using locally supplied fonts you have permission to use:

```powershell
python <skill-root>/scripts/create_report.py --output <destination.html> --title "报告标题" --font-dir <local-font-directory>
```

If original fonts are unavailable, explicitly use `--system-fonts` and disclose that font fidelity is reduced. Font filenames and source URLs are listed in `assets/fonts/manifest.json`; do not claim the public repository includes the font files.

Replace the example article, navigation, category, description, and metadata with the actual report. Keep the embedded font block intact. The script refuses to overwrite an existing file. For existing reports, port the template's styles and document shell while preserving content and stable anchors.

Use the user's output directory or the repository's appropriate docs location. Keep Markdown optional. Use Chinese by default; retain literal paths and code.

## Visual contract

Read `references/claude-docs-visual-spec.md` when changing the design or checking fidelity. Copy measured CSS values from the template instead of a verbal approximation.

- Plain warm-white page `#FDFDF7`; dark mode `#090909`. Body text `#3E3E3E` / `#9E9E9E`. No page-wide graph grid, gradient hero, decorative shadows, giant titles, or mandatory KPI cards.
- Original **Anthropic Sans** for body/navigation, **Anthropic Serif Display** regular for headings, **paperMono** for code. For original-font mode, embed locally supplied bytes with inline data URLs, never CDN dependencies. System-font mode is an explicit fallback and must not be described as matching the original fonts.
- Headings: normal letter spacing, word spacing `.1em`, weight 400. h1 36/40px (30/36px below 640px), h2 24/32px, h3 20/28px. Body 16px, paragraphs 26.4px line height; prose container 28px. Navigation 14/24px, tables 14/20px. Inline code 14/21px, padding 2px 8px, corners 6px.
- Preserve the official Chinese page's complete font stacks: headings `"Anthropic Serif Display", Georgia, "Times New Roman", Times, serif`; body/navigation `"Anthropic Sans", system-ui, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`. Do not insert SimSun, Noto Serif CJK SC, Source Han Serif SC, or other guessed CJK fonts. The earlier explicit Songti fallback visibly changed the Chinese headings. Computed font-family describes a stack, not proof of the font rendering each Chinese glyph; compare actual same-text Chinese rendering in the same browser. Keep semantic `lang="zh-CN"` and document any browser/language fallback differences instead of claiming cross-platform pixel identity.
- Sticky 112px two-row header, desktop 288px left rail, approximately 817px reading column inside an 864px main container. The reference is a wide page **without a right-hand TOC**; do not automatically add a third column.
- Navigation uses 12px corners and restrained active backgrounds. Headings and whitespace organize prose; do not wrap every section in a bordered card.
- Below 1024px the rail becomes a working menu; article has roughly 20px side gutters. Tables/code scroll inside their containers without widening the page.

## Content and components

### Prose

Write body text about 80% of the way to ASD-STE100, the controlled English of aerospace maintenance manuals: keep the rules that make text easy to read and drop the rest. Read `references/output-ladder-and-prose.md` before writing body text; it has the Chinese adaptation, examples and a check list.

- One sentence carries one fact, action or judgement. End the sentence when the topic changes; do not chain clauses with commas.
- Define each term at first use, then use that one term for that one thing. Do not rotate synonyms or coin undefined labels.
- Lead with the conclusion and its scope, then give short evidence. Apply this to the report, each section and each paragraph.
- Keep facts, inferences and unknowns apart. A fact cites its source. An inference names the facts it rests on. An unknown says what would resolve it and whether it blocks the conclusion.
- Name the actor and use active voice. Write procedures as numbered imperative steps: one action per step, condition first, warning before the step.
- Default to the 80% level and avoid stiff regulation-style prose. Move closer to STE for procedures, warnings before destructive actions and text meant for translation. Never claim STE compliance: STE is defined for English with an approved dictionary.

### Visual selection and generation

Read `references/visualization-guide.md` when choosing or adding tables, ASCII, Mermaid, SVG, or a pan/zoom canvas. Read `references/scientific-figures.md` for numeric or research data. Choose representations by the reader's question; no fixed figure quota. Preserve prose conclusions and cite sources beside important visuals.

- Exact comparisons: semantic HTML tables/matrices. Small hierarchies: ASCII. Processes/states: Mermaid rendered to SVG with `scripts/render_mermaid.py`; retain editable .mmd source.
- Architecture and annotated relationships: adapt `assets/figures/architecture.svg` or `lifecycle.svg`. They are illustrative, never evidence about the user's system.
- Numeric distributions/trends/uncertainty: use `scripts/plot_data.py` or other standard scientific plotting tools; retain input data, units, sample count, uncertainty definition and provenance. Do not invent measurements. Install optional dependencies only when the chosen representation requires them.
- Large maps: use the offline figure viewport (zoom, drag, fit, export). Canvas rendering is optional for unusually large/dynamic data; SVG is the default so printing, offline viewing and export stay simple.
- Embed SVG/PNG with `create_report.py --figures-json <manifest>`; schema in the visualization guide. Include title, alt text, caption and source per figure. Viewer assets are inlined automatically. Inspect labels, legends, clipping, mobile overflow and downloads. Export scientific charts as SVG or 300-dpi PNG; generate light/dark variants with `--theme` and provide `dark_file` in the manifest. Adapt neutral backgrounds, labels and axes to the report theme while preserving data colors; never use a blanket inversion filter. Verify actual images in both themes, not only the surrounding page.

The figure mode augments the document template, not replaces its contents. Replace the starter's example prose with the real analysis and include corresponding HTML tables for key numeric results.

Choose sections from the actual topic: findings, explanation, responsibility table, evidence, unknowns, next steps. Do not pad reports with a fixed section list or invented metrics.

Use semantic headings, paragraphs, lists, tables and code blocks. Add inline SVG or offline HTML/CSS diagrams only when relationships benefit.

The template includes a file/detail explorer modeled on the referenced MEMORY.md panel. Use it only for file, component or ownership exploration; adapt labels and panes together. Retain pane content in the HTML. Its mobile stacked layout is an intentional report adaptation: the source hides its explorer below 700px. Remove the entire explorer for ordinary prose reports.

Keep only useful local controls: anchors, theme switch, mobile menu, copy buttons, optional explorer and figure viewer. Add other controls only for a part the reader must operate (see Output choice). Do not copy the official logo, account links, AI assistant, feedback submission or nonfunctional search into reports.

## Validation

Open the generated artifact in a browser. Check 1440px, 768px and 390px, both themes, anchors, menu, copy controls, optional explorer, and long table/code content. Verify font loading and no external resource dependencies. Use a clean browser for color comparisons; Dark Reader rewrites source colors.

Compare same-text Chinese and mixed Chinese/Latin headings and paragraphs against the Chinese reference, as well as English samples for Latin font fidelity. Report intentional and unverified differences honestly. Preserve no-JavaScript readability and reduced-motion/print behavior.

Reload the report with JavaScript disabled. The conclusion, key numbers, tables and figures must stay readable, and each interactive part must have its static result beside it. Re-read the body against the prose check list in `references/output-ladder-and-prose.md`.
