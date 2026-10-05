"""Prepare the exported viewer for direct, self-contained GitHub Pages loading."""
from pathlib import Path
from urllib.request import urlopen

root = Path(__file__).resolve().parents[1]
page = (root / 'source/standalone-export.html').read_text(encoding='utf-8')
vendor = root / 'vendor'
vendor.mkdir(exist_ok=True)
resources = {
    'https://cdn.jsdelivr.net/npm/three@0.160.1/build/three.min.js': 'three-0.160.1.min.js',
    'https://unpkg.com/@floating-ui/core@1.7.3/dist/floating-ui.core.umd.min.js': 'floating-ui-core-1.7.3.js',
    'https://unpkg.com/@floating-ui/dom@1.7.4/dist/floating-ui.dom.umd.min.js': 'floating-ui-dom-1.7.4.js',
    'https://unpkg.com/lucide@1.17.0/dist/umd/lucide.js': 'lucide-1.17.0.js',
}
for url, name in resources.items():
    target = vendor / name
    if not target.exists():
        with urlopen(url, timeout=40) as response:
            target.write_bytes(response.read())
    page = page.replace(url, 'vendor/' + name)
page = page.replace("script-src 'unsafe-inline'", "script-src 'self' 'unsafe-inline'")
page = page.replace("img-src blob:", "img-src 'self' blob:")
page = page.replace('../assets/', 'assets/')
page = page.replace('<title>Store Measured</title>', '<title>Shofankom 3D Store</title>')
page = page.replace('__CODEX_VISUALIZATION_WIDGET_STATE__', '{}')
start = page.index('let renderer;')
end = page.index("renderer.domElement.style.display='block';", start) + len("renderer.domElement.style.display='block';")
page = page[:start] + (root / 'source/renderer-compat.js').read_text(encoding='utf-8') + page[end:]
(root / 'index.html').write_text(page, encoding='utf-8')
print('Prepared direct viewer with locally hosted dependencies')
