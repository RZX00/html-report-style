import re
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
# Anything the page would load at runtime; <a href> navigation links are stripped before the check.
RUNTIME_LOAD=re.compile(r'''\s(?:src|srcset|href)\s*=\s*(?!["']?(?:data:|#))|url\(\s*(?!["']?(?:data:|#))|@import|\bfetch\(''')

class ReportTest(unittest.TestCase):
    def test_default_report_is_offline_chinese_html(self):
        with tempfile.TemporaryDirectory() as d:
            for name,extra in [('plain.html',[]),('figures.html',['--figures-json',str(ROOT/'examples/figures.json')])]:
                out=Path(d)/name
                subprocess.run([sys.executable,str(ROOT/'scripts/create_report.py'),'--output',str(out),'--system-fonts',*extra],check=True,capture_output=True)
                html=out.read_text(encoding='utf-8')
                self.assertIn('<html lang="zh-CN">',html)
                page=re.sub(r'<a\b[^>]*>','',html)
                found=RUNTIME_LOAD.search(page)
                self.assertIsNone(found,f'{name}: {found and page[found.start():found.start()+80]}')

if __name__=='__main__':unittest.main()
