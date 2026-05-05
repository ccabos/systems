"""MkDocs hooks for the Systems Thinking book.

When ENABLE_PDF_EXPORT=1, two things happen:

1. on_page_content replaces every md-button link pointing to an
   interactive D3 HTML page with base64-encoded graph + table
   screenshots so WeasyPrint can embed them without needing to
   execute JavaScript.

2. on_page_content also pre-renders every ``` ```mermaid``` ``` block
   to a base64-embedded PNG via the bundled mmdc + Chromium toolchain.
   The mkdocs-with-pdf plugin's own JS-renderer hook is broken on
   modern bs4 (`tag.text` setter removed), and WeasyPrint cannot
   execute the Mermaid client-side script either, so without this
   step the PDF would print Mermaid source as preformatted text.

   Rendered PNGs are cached in `.mermaid_renders/` keyed by SHA-256
   of the source so subsequent builds reuse them. (We use PNG rather
   than inline SVG because WeasyPrint mishandles Mermaid's
   markerUnits="userSpaceOnUse" arrow markers, producing huge black
   arrowhead blobs; server-side Chromium rasterisation is faithful.)
"""

import base64
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile

_HERE = os.path.dirname(os.path.abspath(__file__))
_RENDERS_DIR = os.path.join(_HERE, '.interactive_renders')
_MERMAID_CACHE = os.path.join(_HERE, '.mermaid_renders')


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


def _expand_interactive_buttons(html: str) -> str:
    def repl(m):
        full = m.group(0)
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


# --- Mermaid pre-rendering -------------------------------------------------

# Pattern produced by pymdownx.superfences's mermaid custom_fence.
# Material renders blocks as: <pre class="mermaid"><code>...source...</code></pre>
_MERMAID_BLOCK = re.compile(
    r'<pre class="mermaid">\s*<code>(?P<src>[\s\S]*?)</code>\s*</pre>',
    re.IGNORECASE,
)

# HTML entities the SuperFences renderer emits inside the source. We need
# the original Mermaid syntax back before feeding it to mmdc.
_HTML_UNESCAPE = {
    '&amp;': '&',
    '&lt;': '<',
    '&gt;': '>',
    '&quot;': '"',
    '&#39;': "'",
}


def _decode_html(s: str) -> str:
    for k, v in _HTML_UNESCAPE.items():
        s = s.replace(k, v)
    return s


def _find_mmdc() -> str | None:
    """Locate mermaid-cli. Prefers WITH_PDF_MMDC env, then PATH, then a
    common npm-installed location used by the build job."""
    explicit = os.environ.get('WITH_PDF_MMDC')
    if explicit and os.path.isfile(explicit):
        return explicit
    found = shutil.which('mmdc')
    if found:
        return found
    for candidate in (
        '/tmp/m/node_modules/.bin/mmdc',
        os.path.join(_HERE, 'node_modules/.bin/mmdc'),
    ):
        if os.path.isfile(candidate):
            return candidate
    return None


def _find_chromium() -> str | None:
    explicit = os.environ.get('WITH_PDF_CHROMIUM_PATH')
    if explicit and os.path.isfile(explicit):
        return explicit
    # Playwright-managed install
    import glob
    matches = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')
    if matches:
        return sorted(matches)[-1]
    return shutil.which('chromium') or shutil.which('chromium-browser') or shutil.which('google-chrome')


def _render_mermaid_to_png(source: str) -> str | None:
    """Render `source` to a PNG image via mmdc + Chromium and return an
    HTML <figure> wrapping a base64 data: URI. Returns None if the
    toolchain is unavailable or the render fails; the caller falls back
    to leaving the original block in place.

    PNG (rather than inline SVG) because WeasyPrint mishandles Mermaid's
    arrow-marker definitions (markerUnits="userSpaceOnUse" combined with
    viewBox produces oversized arrowheads in the PDF). Server-side
    rasterisation by Chromium produces a faithful image.
    """
    os.makedirs(_MERMAID_CACHE, exist_ok=True)
    key = hashlib.sha256(source.encode('utf-8')).hexdigest()
    cached_html = os.path.join(_MERMAID_CACHE, f'{key}.html')
    if os.path.exists(cached_html):
        with open(cached_html, encoding='utf-8') as f:
            return f.read()

    mmdc = _find_mmdc()
    chromium = _find_chromium()
    if not mmdc or not chromium:
        return None

    with tempfile.TemporaryDirectory() as tmp:
        src_path = os.path.join(tmp, 'in.mmd')
        out_path = os.path.join(tmp, 'out.png')
        cfg_path = os.path.join(tmp, 'puppeteer.json')
        mmcfg_path = os.path.join(tmp, 'mmconfig.json')
        with open(src_path, 'w', encoding='utf-8') as f:
            f.write(source)
        with open(cfg_path, 'w', encoding='utf-8') as f:
            json.dump({'executablePath': chromium, 'args': ['--no-sandbox']}, f)
        with open(mmcfg_path, 'w', encoding='utf-8') as f:
            json.dump({
                'flowchart': {'useMaxWidth': False},
                'themeVariables': {'fontFamily': 'DejaVu Sans, sans-serif'},
            }, f)
        try:
            subprocess.run(
                [mmdc, '-i', src_path, '-o', out_path,
                 '--puppeteerConfigFile', cfg_path,
                 '-c', mmcfg_path,
                 '--backgroundColor', 'white',
                 '--scale', '2'],   # 2× DPI for crisp print rendering
                check=True, capture_output=True, timeout=60,
            )
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            return None
        with open(out_path, 'rb') as f:
            png_bytes = f.read()

    b64 = base64.b64encode(png_bytes).decode()
    wrapped = (
        '<figure class="mermaid-pdf" '
        'style="margin:1.2em 0;page-break-inside:avoid;text-align:center">'
        f'<img src="data:image/png;base64,{b64}" '
        'alt="Mermaid diagram" '
        'style="max-width:100%;height:auto">'
        '</figure>'
    )

    with open(cached_html, 'w', encoding='utf-8') as f:
        f.write(wrapped)
    return wrapped


def _replace_mermaid_blocks(html: str) -> str:
    def repl(m: re.Match) -> str:
        src = _decode_html(m.group('src')).strip()
        rendered = _render_mermaid_to_png(src)
        return rendered if rendered is not None else m.group(0)

    return _MERMAID_BLOCK.sub(repl, html)


def on_page_content(html, page, config, files):
    if not os.environ.get('ENABLE_PDF_EXPORT'):
        return html
    html = _expand_interactive_buttons(html)
    html = _replace_mermaid_blocks(html)
    return html
