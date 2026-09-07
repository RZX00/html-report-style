"""Render editable Mermaid source to offline SVG using installed Mermaid CLI."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('input', type=Path)
    p.add_argument('output', type=Path)
    p.add_argument('--theme', choices=['light','dark'], default='light')
    p.add_argument('--mmdc', help='Path to an installed mmdc executable')
    a = p.parse_args()
    if a.output.exists() or a.output.suffix.lower() != '.svg':
        p.error('Choose a new .svg output path')
    cli = a.mmdc or shutil.which('mmdc')
    if not cli:
        p.error('Install @mermaid-js/mermaid-cli from npm, or pass --mmdc')
    source = a.input.resolve(strict=True)
    with tempfile.TemporaryDirectory() as d:
        config = Path(d) / 'config.json'
        bg,fg,border,line=('#191919','#deded6','#555550','#aaa99f') if a.theme=='dark' else ('#fdfdf7','#171717','#d1cfc5','#73726c')
        config.write_text(json.dumps({'theme':'base','securityLevel':'strict','htmlLabels':False,'flowchart':{'htmlLabels':False},'themeVariables':{'fontFamily':'Arial, sans-serif','darkMode':a.theme=='dark','background':bg,'primaryColor':bg,'primaryTextColor':fg,'primaryBorderColor':border,'lineColor':line,'textColor':fg,'secondaryColor':bg,'tertiaryColor':bg}}), encoding='utf-8')
        result = Path(d) / 'figure.svg'
        subprocess.run([str(cli), '-i', str(source), '-o', str(result), '-c', str(config), '-b', bg], check=True)
        data = result.read_bytes()
        if b'<svg' not in data:
            raise ValueError('Renderer did not produce SVG')
        a.output.parent.mkdir(parents=True, exist_ok=True)
        with a.output.open('xb') as f:
            f.write(data)
    print(a.output.resolve())

if __name__ == '__main__':
    main()
