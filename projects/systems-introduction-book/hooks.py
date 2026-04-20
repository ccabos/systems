"""MkDocs hooks for the Systems Thinking book.

When ENABLE_PDF_EXPORT=1, the on_page_content hook replaces every
md-button link pointing to an interactive D3 HTML page with base64-
encoded graph + table screenshots so WeasyPrint can embed them without
needing to execute JavaScript.
"""

import base64
import os
import re

_RENDERS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            '.interactive_renders')


def _embed_png(name: str, suffix: str, label: str) -> str:
    path = os.path.join(_RENDERS_DIR, f'{name}.{suffix}.png')
    if not os.path.exists(path):
        return ''
    with open(path, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode()
    return (
        '<figure style="margin:1.2em 0;page-break-inside:avoid">'
        f'<img src="data:image/png;base64,{b64}" '
        f'alt="{name} {label}" '
        'style="max-width:100%;display:block;margin:0 auto">'
        '<figcaption style="text-align:center;font-size:0.8em;'
        f'color:#666;margin-top:0.3em">{name} — {label}</figcaption>'
        '</figure>'
    )


def on_page_content(html, page, config, files):
    if not os.environ.get('ENABLE_PDF_EXPORT'):
        return html

    def repl(m):
        full = m.group(0)
        # Only expand button-style links (md-button class)
        if 'md-button' not in full:
            return full
        href = m.group(1)
        name = os.path.splitext(os.path.basename(href))[0]
        imgs = _embed_png(name, 'graph', 'Graph') + _embed_png(name, 'table', 'Table')
        return imgs if imgs else full

    return re.sub(
        r'<a[^>]+href="([^"]*interactive/[^"]+\.html)"[^>]*>.*?</a>',
        repl,
        html,
        flags=re.DOTALL,
    )
