# Choose a visual by the reader's question

Keep the Claude Docs reading layout. Use as many figures as the explanation needs, not a quota. Each important figure needs a conclusion, an explanation of how to read it, and a source. Never invent values to fill a chart.

| Question | Form | Notes |
| --- | --- | --- |
| What is the exact value or difference? | Table / comparison matrix | Units in headers, align numbers, show missing values explicitly. Keep an HTML table alongside important charts. |
| What is the small hierarchy? | ASCII in pre/code | File trees and short chains; use monospace, label arrows. Avoid dense ASCII for large relationships. |
| What happens in what order? | Mermaid flowchart / sequence / state diagram | Keep editable .mmd source; render to SVG at build time. |
| Who owns what / how do layers connect? | Annotated SVG | Use assets/figures/architecture.svg as a starting point. Explicit boundaries, labeled arrows, readable legends. |
| How do I explore a large map? | SVG in pan/zoom viewport | Use the figure viewer; text explanation must work without interaction. Canvas is reserved for genuinely large/dynamic data, not the default. |
| How do values change? | Line / scatter | Show axis names and units; don't imply continuity across unrelated categories. |
| How do categories compare? | Bar / table | Zero baseline for bars; indicate negative values, show raw counts when needed. |
| What is the distribution? | Box plot / histogram | Report sample counts; avoid replacing distributions with means alone. |
| What varies across two dimensions? | Heatmap | Label both dimensions and color scale; use a perceptually ordered palette. |
| How uncertain is an estimate? | Points/lines with explicit error bars | State whether bars are SD, SE or CI, and how computed. Do not infer uncertainty from a single value. |

## Offline Mermaid

Install optional build dependency from npm: `npm install -g @mermaid-js/mermaid-cli`.
Render using `python scripts/render_mermaid.py input.mmd output.svg`.
The wrapper uses a docs-colored base theme, strict security, and SVG text rather than HTML labels. It preserves the source file and fails if the CLI fails. It never falls back to a decorative fake diagram. Fonts use the browser's installed stack during rendering.

Inspect the rendered diagram: syntactically valid Mermaid can still overlap or have unreadable labels. For many nodes split by responsibility or offer an overview plus detailed figures. Retain the .mmd alongside the output for editing; do not fetch Mermaid scripts at report runtime.

## Reusable SVG

`assets/figures/architecture.svg` and `assets/figures/lifecycle.svg` demonstrate boundaries, connectors, labels and restrained accent colors. Replace sample text and relationships with verified facts. SVG files have title/desc and a viewBox. Export scientific plots with SVG text converted to paths for consistent offline output; captions and data tables provide searchable information.

Static scientific figures keep their original light background in both report themes so color/contrast meanings do not change. Do not invert scientific images in dark mode. Use the viewer for large figures and provide download links; all base figures remain visible without JavaScript and print at full width.

## Report figure input

Pass `--figures-json path/to/figures.json` to create_report.py. JSON is a list of objects:

```json
[{"file":"architecture.svg","title":"Request ownership","alt":"Gateway passes the request to the API, which reads the database.","caption":"The API owns business processing; arrows show request direction.","source":"Reviewed architecture, revision abc123"}]
```

Paths are relative to the manifest. SVG and PNG are embedded as data URLs. Figures are wrapped in semantic figure/figcaption. Title, alt, caption and source are required; the source may explicitly say “illustrative / simulated”, never imply real measurements. The SVG validator is a bounded admission check, not a general-purpose sanitizer: only include trusted locally authored diagrams. It rejects scripts, HTML foreignObject, event handlers, external resources, DTDs and entities.

The reader can zoom, drag, scroll, reset to fit and download each figure. Wheel scrolling remains normal page/viewport scrolling. Mobile uses native touch scrolling; controls remain keyboard accessible. No editing canvas, graph database or external scripts are added.
