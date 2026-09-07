"""Embed trusted local SVG/PNG figures and their evidence captions."""
import base64
from html import escape
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

def image_uri(path):
    path=Path(path); data=path.read_bytes()
    if path.suffix.lower()=='.svg':
        source=data.decode('utf-8-sig')
        if re.search(r'<!DOCTYPE|<!ENTITY',source,re.I): raise ValueError('SVG DTD/entity not allowed')
        svg=ET.fromstring(source)
        if svg.tag.split('}')[-1]!='svg': raise ValueError('Not SVG')
        for node in svg.iter():
            tag = node.tag.split('}')[-1].lower()
            if tag in ['script','foreignobject','iframe','object','embed','animate','set']:
                raise ValueError('Active/embedded SVG content is not allowed')
            for key,value in node.attrib.items():
                key=key.split('}')[-1].lower()
                embedded_png = False
                if tag == 'image' and key == 'href' and value.startswith('data:image/png;base64,'):
                    embedded_png = base64.b64decode(value.split(',',1)[1]).startswith(b'\x89PNG\r\n\x1a\n')
                if key.startswith('on') or (key in ['href','src'] and not value.startswith('#') and not embedded_png):
                    raise ValueError('SVG event or external reference not allowed')
        if re.search(r'@import',source,re.I) or any(not value.strip().strip('\"\'').startswith('#') for value in re.findall(r'url\(([^)]*)\)',source,re.I)):
            raise ValueError('SVG external CSS resource not allowed')
        mime='image/svg+xml'
    elif path.suffix.lower()=='.png' and data.startswith(b'\x89PNG\r\n\x1a\n'):
        mime='image/png'
    else: raise ValueError('Only SVG and PNG are supported')
    uri=f'data:{mime};base64,'+base64.b64encode(data).decode('ascii')
    return uri

def figures_html(manifest):
    manifest=Path(manifest)
    items=json.loads(manifest.read_text(encoding='utf-8-sig'))
    if not isinstance(items,list): raise ValueError('Figure manifest must be a list')
    figures=[]
    for index,item in enumerate(items,1):
        for field in ['file','title','alt','caption','source']:
            if not isinstance(item.get(field),str) or not item[field].strip(): raise ValueError(f'Figure {index}: missing {field}')
        path=manifest.parent/item['file']
        uri=image_uri(path)
        dark_uri=image_uri(manifest.parent/item['dark_file']) if item.get('dark_file') else uri
        dark_name=Path(item.get('dark_file',item['file'])).name
        title=escape(item['title']); alt=escape(item['alt'],quote=True)
        figures.append(f'''<figure class="report-figure"><div class="figure-tools"><button type="button" data-zoom-out aria-label="缩小：{title}">−</button><button type="button" data-zoom-in aria-label="放大：{title}">＋</button><button type="button" data-zoom-fit aria-label="适应窗口：{title}">适应窗口</button><span class="figure-scale" aria-live="polite">100%</span><a data-figure-download data-light="{uri}" data-dark="{dark_uri}" data-light-name="{escape(path.name,quote=True)}" data-dark-name="{escape(dark_name,quote=True)}" href="{uri}" download="{escape(path.name,quote=True)}">下载图形</a></div><div class="figure-viewport" tabindex="0" role="region" aria-label="{title}，可滚动图形"><img data-light="{uri}" data-dark="{dark_uri}" src="{uri}" alt="{alt}" draggable="false"></div><figcaption><strong>图 {index} · {title}</strong><br>{escape(item['caption'])}<span class="figure-source">来源：{escape(item['source'])}</span></figcaption></figure>''')
    return '<section id="report-figures"><h2>图形与数据</h2>'+''.join(figures)+'</section>'
