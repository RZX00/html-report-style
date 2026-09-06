---
name: html-report-style
description: Create or update self-contained Chinese HTML reports, analysis documents, plans, reviews, and architecture documentation using the Claude Code official documentation visual style. Use for substantial reports or HTML artifacts; ordinary conversational answers do not require a file.
metadata:
  short-description: Chinese HTML reports matching Claude Code Docs
---

# HTML Report Style

Produce Chinese-first, offline HTML reports matching the typography and reading layout of https://code.claude.com/docs/zh-CN/claude-directory. Use the official Chinese page as the typography reference for Chinese reports. This reference supplies visual design, not an official report-generation skill. Preserve the report's own product name and evidence.

## Starting point

Read `references/habitat-html-report-template.html` before creating a report. This historical filename now contains the Claude documentation template and is the single reusable skeleton. Do not recreate the previous engineering dashboard styling.

Public distribution does not bundle third-party font binaries. Create an offline starter using locally supplied fonts you have permission to use:

```powershell
python <skill-root>/scripts/create_report.py --output <destination.html> --title "报告标题" --font-dir <local-font-directory>
```

If original fonts are unavailable, explicitly use `--system-fonts` and disclose that font fidelity is reduced. Font filenames and source URLs are listed in `assets/fonts/manifest.json`; do not claim the public repository includes the font files.

Replace the example article, navigation, category, description, and metadata with the actual report. Keep the embedded font block intact. The script refuses to overwrite an existing file. For existing reports, port the template's styles and document shell while preserving content and stable anchors.

Use the user's output directory or the repository's appropriate docs location. Keep Markdown optional. Use Chinese by default; retain literal paths and code. Explicit user format choices override HTML defaults.

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

Lead with the useful conclusion and scope. Choose sections from the actual topic: findings, explanation, responsibility table, evidence, unknowns, next steps. Do not pad reports with a fixed section list or invented metrics.

Use semantic headings, paragraphs, lists, tables and code blocks. Include evidence and distinguish facts, inferences and unknowns. Add inline SVG or offline HTML/CSS diagrams only when relationships benefit.

The template includes a file/detail explorer modeled on the referenced MEMORY.md panel. Use it only for file, component or ownership exploration; adapt labels and panes together. Retain pane content in the HTML. Its mobile stacked layout is an intentional report adaptation: the source hides its explorer below 700px. Remove the entire explorer for ordinary prose reports.

Keep only useful local controls: anchors, theme switch, mobile menu, copy buttons, optional explorer. Do not copy the official logo, account links, AI assistant, feedback submission or nonfunctional search into reports.

## Validation

Open the generated artifact in a browser. Check 1440px, 768px and 390px, both themes, anchors, menu, copy controls, optional explorer, and long table/code content. Verify font loading and no external resource dependencies. Use a clean browser for color comparisons; Dark Reader rewrites source colors.

Compare same-text Chinese and mixed Chinese/Latin headings and paragraphs against the Chinese reference, as well as English samples for Latin font fidelity. Report intentional and unverified differences honestly. Preserve no-JavaScript readability and reduced-motion/print behavior.
