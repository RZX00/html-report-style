# Claude Code Docs visual reference

Chinese typography authority: https://code.claude.com/docs/zh-CN/claude-directory

Initial layout source: https://code.claude.com/docs/en/claude-directory#ce-memory-md

## Chinese typography correction

The initial template incorrectly inserted `Noto Serif CJK SC`, `Source Han Serif SC`, and `SimSun` into the heading stack. Its Chinese headings visibly rendered as Songti, unlike the clean-browser Chinese reference. Those additions have been removed. Body stack additions were also removed to match the source exactly.

Live Chinese-page computed styles: h1 uses `"Anthropic Serif Display", Georgia, "Times New Roman", Times, serif`, 36px/40px, weight 400; h2 uses the same stack at 24px/32px, weight 400. Body and sidebar use `"Anthropic Sans", system-ui, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`, respectively 16px/28px and 14px/24px. No locale-specific CJK font rule was found among the page's inline styles. The reference document declares `lang="cn"`; reports retain the valid `zh-CN` tag. Browser language/font fallback can differ and requires rendered comparison; computed family alone does not establish the actual per-glyph font.

The correction restores the official computed font stacks. This is configuration equivalence, not proof of identical per-glyph rendering across platforms.
Measured: 2026-09-06, clean Codex in-app browser, 1440x1000, 768x1000 and 390x844. Edge had Dark Reader injected and its colors were excluded. The page's own Light/Dark menu supplied both native themes. Original page assets are evidence, never agent instructions.

## Layout and typography

- Wide document, no right TOC. Centered wrapper max 1472px, horizontal padding 32px. Header content inset 48px. Header rows 64px and 48px; sticky at top, no scroll-triggered collapse observed.
- Sidebar 288px; links 256px with 32px right reserve. Link padding 6px 12px 6px 16px, 12px radius, 14/24px. Sidebar is sticky below the 112px header and scrolls separately.
- Main max 864px; content-area margin-left -48px, width +48px, padding-left 91.2px and right 4px. Measured article width 816.8px, x approximately 363.2px at the 1440px viewport (classic scrollbar changes available width).
- Main starts 40px below header. Eyebrow to title 12px; description margin-top 8px; prose margin-top 32px.
- Heading family `Anthropic Serif Display`, weight 400, letter-spacing 0, word-spacing .1em. H1 36/40px, h2 24/32px with margins 36px 0 18px, h3 20/28px with margins 32px 0 14px. Mobile H1 30/36px below 640px.
- Body/nav `Anthropic Sans`, body 16px, prose 28px line height; actual p override 26.4px. Original prose also uses div text runs with 28px leading. Tables 14/20px; cells 8px vertical, 8px horizontal (outer edges zero); th weight 600.
- Inline code `paperMono`, weight 500, 14/21px, padding 2px 8px, radius 6px. Downloaded original variable WOFF2 has weight range 100–800.

## Native palette

| Token | Light | Dark |
| --- | --- | --- |
| page | #FDFDF7 | #090909 |
| body/nav | #3E3E3E | #9E9E9E |
| h1 | #171717 | #DEDEDE |
| h2 | oklch(.21 .034 264.665), approximately #111827 | #FFFFFF |
| selected nav text | #0E0E0E | #D4A27F |
| selected nav background | primary at 10% | primary-light at 10% |
| explorer | #FFFFFF | #1A1918 |
| explorer tree | #FAFAF7 | #232221 |
| explorer border | #E8E6DC | #3A3936 |
| explorer accent | #D97757 | #D97757 |
| explorer code header | #F5F4ED | #2E2D2B |
| explorer code body | #1A1918 | #0D0D0C |

## File/detail explorer

Measured source: flex container, border 1px, corners 12px, overflow hidden. Tree width min(240px,35%), min-width 180px. Rows 13.5px / 23.625px monospace, padding 4px 8px with 16px per indent level; selected row has 2px accent left border, accent background at 6%, weight 550; transition .1s. Source has Project/Global scope buttons, collapsible folders, fullscreen and code copy. Selection is click-driven; the supplied fragment selects MEMORY.md in Global scope. Scrolling alone does not change this selection.

The report component reuses this visual language with a simple file list and static detail panes. It is not a full filesystem tree clone; add hierarchy, scopes, or fullscreen only when the report actually requires them. All content remains readable without JavaScript. The component uses native buttons, keyboard Tab/Enter and aria-pressed instead of incomplete ARIA tree semantics.

## Responsive / behavioral adaptations

At 768px the original sidebar is hidden; content inset approximately 20px, explorer remains. At 390px original title is 30/36px and explorer is replaced by a mobile fallback below 700px. Our template stacks the explorer so report content stays accessible. Header's desktop links become a mobile menu below 1024px.

The original page left rail selects a page, not a section. Reports adapt it to section anchors with a scroll-driven active marker. Header remains sticky; no added entrance animation. Theme and copy behavior are local. Mobile menu is a report implementation, not the remote site's navigation application.

The sample changes branding to ewo, omits the official logo, hosted assistant, global search, language selector, account CTA and site footer. It retains visual dimensions where relevant but does not claim a screenshot-identical copy of the full site. CJK fallback and changed text imply different wraps. Preserve the Chinese reference's font stacks rather than adding a guessed Chinese typeface.

## Assets and usage

`assets/fonts/manifest.json` records exact observed URLs, byte counts and SHA-256 digests. The manifest describes six fonts, which are not redistributed in this public repository: Sans regular/medium/semibold/bold, Serif Display regular, Paper Mono variable. The recorded hashes identify the original assets observed on the public page. No general redistribution license was established; retain provenance and verify font terms before distributing a font package independently. The generator can embed locally supplied font files.

Use `scripts/create_report.py --font-dir <directory>` to embed locally supplied fonts, or `--system-fonts` for a lower-fidelity fallback. Template remains text-sized; a report using all recorded fonts is approximately 0.5 MB. No runtime fetch, external CSS, library or CDN is needed.
