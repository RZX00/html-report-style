"""Create an offline report starter with original fonts. Never overwrite files."""
import argparse
import base64
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FONTS = [
    ("Anthropic Sans", "AnthropicSans-Text-Regular-Static.otf", "400"),
    ("Anthropic Sans", "AnthropicSans-Text-Medium-Static.otf", "500"),
    ("Anthropic Sans", "AnthropicSans-Text-Semibold-Static.otf", "600"),
    ("Anthropic Sans", "AnthropicSans-Text-Bold-Static.otf", "700"),
    ("Anthropic Serif Display", "AnthropicSerif-Display-Regular-Static.otf", "400"),
    ("paperMono", "PaperMono-Variable.woff2", "100 800"),
]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--title", default="文档与报告样式参考")
    fonts = parser.add_mutually_exclusive_group()
    fonts.add_argument("--font-dir", type=Path, default=ROOT / "assets" / "fonts", help="Directory containing locally supplied original fonts")
    fonts.add_argument("--system-fonts", action="store_true", help="Use installed fallback fonts; appearance will differ from the reference")
    args = parser.parse_args()
    rules = []
    for family, filename, weight in ([] if args.system_fonts else FONTS):
        font_path = args.font_dir / filename
        if not font_path.is_file():
            parser.error(f"Missing font {filename}. Supply --font-dir with fonts you may use, or choose --system-fonts.")
        data = font_path.read_bytes()
        fmt, mime = ("woff2", "font/woff2") if filename.endswith("woff2") else ("opentype", "font/otf")
        if not data.startswith(b"wOF2" if fmt == "woff2" else b"OTTO"):
            raise ValueError(f"Invalid font: {filename}")
        encoded = base64.b64encode(data).decode("ascii")
        rules.append(f'@font-face{{font-family:"{family}";src:url(data:{mime};base64,{encoded}) format("{fmt}");font-weight:{weight};font-style:normal;font-display:swap;}}')
    template = (ROOT / "references" / "habitat-html-report-template.html").read_text(encoding="utf-8")
    output = template.replace("/* EMBED_FONT_FACES */", "\n".join(rules)).replace("{{TITLE}}", escape(args.title))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(output)
    print(args.output.resolve())

if __name__ == "__main__":
    main()
