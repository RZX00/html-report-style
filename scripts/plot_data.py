"""Plot complete CSV data with explicit labels and source provenance."""
import argparse
import csv
import hashlib
import io
import json
import math
import re
from pathlib import Path
import warnings

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('input', type=Path)
    p.add_argument('output', type=Path)
    p.add_argument('--kind', choices=['line','scatter','bar','box','heatmap'], required=True)
    for name in ['title','xlabel','ylabel','source']:
        p.add_argument('--'+name, required=True)
    p.add_argument('--error-label')
    p.add_argument('--font', default='DejaVu Sans')
    a = p.parse_args()
    provenance = a.output.with_suffix('.provenance.json')
    if a.output.exists() or provenance.exists() or a.output.suffix.lower() not in ['.svg','.png']:
        p.error('Choose a new .svg or .png path, including its provenance sidecar')
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    raw = a.input.read_bytes()
    rows = list(csv.DictReader(io.StringIO(raw.decode('utf-8-sig'))))
    if not rows or None in rows[0]:
        p.error('CSV needs a header and complete observations')
    def number(value):
        n = float(value)
        if not math.isfinite(n):
            raise ValueError('Non-finite value')
        return n
    plt.rcParams.update({'font.family':a.font, 'font.size':11, 'svg.fonttype':'path','axes.spines.top':False,'axes.spines.right':False})
    fig, ax = plt.subplots(figsize=(8,4.8),layout='constrained')
    fig.set_facecolor('#fdfdf7'); ax.set_facecolor('#fdfdf7')
    try:
        if a.kind in ['line','scatter','bar']:
            x = [r['x'] if a.kind=='bar' else number(r['x']) for r in rows]
            y = [number(r['y']) for r in rows]
            err = [number(r['yerr']) for r in rows] if 'yerr' in rows[0] else None
            if err is not None and (not a.error_label or any(e < 0 for e in err)):
                raise ValueError('yerr requires nonnegative magnitudes and --error-label')
            if a.kind=='bar': ax.bar(x,y,yerr=err,color='#d97757',capsize=4)
            else: ax.errorbar(x,y,yerr=err,fmt='o-' if a.kind=='line' else 'o',color='#4a7fb5',capsize=4,label=a.error_label)
            if err is not None: ax.text(.01,.98,a.error_label,transform=ax.transAxes,va='top',fontsize=9)
            ax.grid(axis='y',alpha=.18); ax.set_axisbelow(True)
        elif a.kind=='box':
            columns=list(rows[0]); values=[[number(r[k]) for r in rows] for k in columns]
            ax.boxplot(values,tick_labels=[f'{k}\n(n={len(rows)})' for k in columns],patch_artist=True,boxprops={'facecolor':'#ead2c5'})
        else:
            columns=list(rows[0]); values=[[number(r[k]) for k in columns[1:]] for r in rows]
            if len(columns)<2: raise ValueError('Heatmap needs row labels and numeric columns')
            im=ax.imshow(values,aspect='auto',cmap='cividis')
            ax.set_xticks(range(len(columns)-1),columns[1:]); ax.set_yticks(range(len(rows)),[r[columns[0]] for r in rows])
            fig.colorbar(im,ax=ax,label='Value')
        ax.set(title=a.title,xlabel=a.xlabel,ylabel=a.ylabel)
        fig.text(.01,-.02,a.source,fontsize=8,color='#5e5d59')
        buffer=io.BytesIO()
        with warnings.catch_warnings():
            warnings.filterwarnings('error',message='Glyph .* missing from font')
            fig.savefig(buffer,format=a.output.suffix[1:].lower(),dpi=300,bbox_inches='tight')
    except (ValueError,KeyError,TypeError,UserWarning) as e:
        p.error(str(e))
    finally:
        plt.close(fig)
    meta={'source':a.source,'data_sha256':hashlib.sha256(raw).hexdigest(),'rows':len(rows),'kind':a.kind,'title':a.title,'xlabel':a.xlabel,'ylabel':a.ylabel,'error_definition':a.error_label,'matplotlib':matplotlib.__version__}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    data = buffer.getvalue()
    if a.output.suffix.lower()=='.svg':
        # Matplotlib's standard SVG DTD is unnecessary for offline embedding.
        data = re.sub(br'<!DOCTYPE[^>]*>', b'', data)
    with a.output.open('xb') as f: f.write(data)
    with provenance.open('x',encoding='utf-8') as f: json.dump(meta,f,ensure_ascii=False,indent=2)
    print(a.output.resolve())

if __name__=='__main__': main()
