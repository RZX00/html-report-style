import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from figure_embed import figures_html

class FiguresTest(unittest.TestCase):
    def test_offline_svg_and_reject_external_content(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); svg=root/'figure.svg'; manifest=root/'figures.json'
            item={'file':'figure.svg','title':'A < B','alt':'Flow','caption':'Example','source':'Illustrative'}
            manifest.write_text(json.dumps([item]),encoding='utf-8')
            svg.write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><path d="M0 0L10 10"/></svg>',encoding='utf-8')
            html=figures_html(manifest)
            self.assertIn('data:image/svg+xml;base64,',html)
            self.assertIn('A &lt; B',html)
            for content in ['<script>alert(1)</script>','<image href="https://example.com/a.png"/>','<path onclick="x()"/>','<style>@import "https://example.com/a.css";</style>']:
                svg.write_text('<svg xmlns="http://www.w3.org/2000/svg">'+content+'</svg>',encoding='utf-8')
                with self.assertRaises(ValueError):figures_html(manifest)

    def test_plot_exports_and_uncertainty_validation(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            for kind,csv in [('line','x,y,yerr\n1,2,0.5\n2,3,0.8\n'),('scatter','x,y\n1,2\n2,3\n'),('bar','x,y\nA,2\nB,3\n'),('box','A,B\n1,2\n3,4\n'),('heatmap','label,A,B\nX,1,2\nY,3,4\n')]:
                data=root/(kind+'.csv');data.write_text(csv,encoding='utf-8');out=root/(kind+'.svg')
                cmd=[sys.executable,str(ROOT/'scripts/plot_data.py'),str(data),str(out),'--kind',kind,'--title','Example','--xlabel','X','--ylabel','Y','--source','Simulated test']
                if kind=='line':
                    bad=subprocess.run(cmd,capture_output=True)
                    self.assertNotEqual(bad.returncode,0);self.assertFalse(out.exists())
                    cmd+=['--error-label','Synthetic error']
                subprocess.run(cmd,check=True,capture_output=True)
                self.assertIn('<svg',out.read_text(encoding='utf-8'))
                meta=json.loads(out.with_suffix('.provenance.json').read_text())
                self.assertEqual(meta['rows'],2)
                manifest=root/'figures.json';manifest.write_text(json.dumps([{'file':out.name,'title':kind,'alt':kind,'caption':'Test','source':'Simulated'}]),encoding='utf-8')
                self.assertIn('data:image/svg+xml',figures_html(manifest))
                before=out.read_bytes()
                repeated=subprocess.run(cmd,capture_output=True)
                self.assertNotEqual(repeated.returncode,0);self.assertEqual(before,out.read_bytes())

if __name__=='__main__':unittest.main()
