# Scientific data and plotting

Use standard plotting tools for research figures, not hand-drawn bars or fabricated sample points. `scripts/plot_data.py` supports line, scatter, bar, box and heatmap using CSV + Matplotlib. Install with `python -m pip install -r requirements-plot.txt`. Other scientific plots can be authored directly with Matplotlib/Seaborn when the data calls for them.

For line/scatter/bar CSV requires x,y columns; optional yerr is a nonnegative symmetric uncertainty magnitude. Numeric x is required for line/scatter; bar x may be a category. The tool does not calculate confidence intervals or choose an uncertainty definition for you. Pass --error-label when using yerr (e.g. “95% CI, bootstrap 2000 replicates”). Line x values are used in file order; order them deliberately. Bars use a zero baseline.

For box plots CSV columns are numeric sample groups, each row an observation. For heatmaps first column contains row labels; remaining headers name numeric columns. This small helper requires complete finite numeric data. Clean missing data explicitly and disclose exclusions rather than silently dropping observations.

```sh
python scripts/plot_data.py measurements.csv figure.svg --kind scatter --title "Latency versus load" --xlabel "Requests / second" --ylabel "Latency (ms)" --source "Load test 2026-09-07; n=24" --error-label "SD across five repeats"
```

Use .svg for scalable export or .png (300 dpi) for raster. Unicode text requires an installed font that covers its glyphs; --font can select it. Missing-glyph warnings fail generation rather than silently producing squares. Paths preserve existing outputs; use another output name for a revision.

Every plot receives an adjacent .provenance.json recording source label, CSV SHA-256, plotting parameters, library version, sample/row count and error definition. Keep CSV and methodology accessible with the report. Caption must state:

- What was measured, units, sample count, date and origin.
- What points, colors, lines and error bars mean.
- Any aggregation, filtering, normalization or log scales.
- What the data supports and what remains uncertain. Correlation alone is not causal evidence.

Avoid dual y-axes unless necessary and clearly justified. Don't crop bar baselines or use a diverging heatmap without a meaningful center. Use fixed comparable scales for comparisons. Color must not be the only label; use text, symbols or patterns. In reports, accompany key numeric findings with HTML data tables.

Examples under examples/ are explicitly simulated teaching data, not measured product performance. Validate real research results with a domain-appropriate workflow; the helper validates data shape, not scientific correctness.
