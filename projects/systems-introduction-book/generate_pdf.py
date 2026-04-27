#!/usr/bin/env python3
"""Generate a single PDF of the Systems Thinking book from the MkDocs markdown sources."""

import glob
import io
import os
import re
import sys
import logging
import markdown
from fpdf import FPDF
from fpdf.fonts import FontFace, TextStyle
from PIL import Image as PILImage

# Suppress fpdf2's noisy HTML parser warnings
logging.getLogger("fpdf.html").setLevel(logging.ERROR)

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(REPO_DIR, "docs")
INTERACTIVE_DIR = os.path.join(DOCS_DIR, "interactive")
VENDOR_DIR = os.path.join(REPO_DIR, "vendor")
RENDERED_DIR = os.path.join(REPO_DIR, ".interactive_renders")

FONTS = {
    "Serif": "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
    "SerifB": "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
    "SerifI": "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf",
    "SerifBI": "/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf",
    "Sans": "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    "SansB": "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "SansI": "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf",
    "SansBI": "/usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf",
    "Mono": "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",
    "MonoB": "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf",
    "MonoI": "/usr/share/fonts/truetype/liberation/LiberationMono-Italic.ttf",
    "MonoBI": "/usr/share/fonts/truetype/liberation/LiberationMono-BoldItalic.ttf",
}

# Navigation from mkdocs.yml with hierarchy level:
#   0 = top-level (Home, Introduction, Part headings, About)
#   1 = chapter within a part
#   2 = worked example (sub-section)
NAV = [
    ("Home", "index.md", 0),
    ("Introduction", "introduction.md", 0),
    ("Part I -- Foundations", "part1/index.md", 0),
    ("What Is a System?", "part1/what-is-a-system.md", 1),
    ("The Five-Level SE Hierarchy", "part1/se-hierarchy.md", 1),
    ("Product Line Thinking", "part1/product-lines.md", 1),
    ("STPA and STAMP", "part1/stpa-introduction.md", 1),
    ("Justificatory Rungs", "part1/justification-rungs.md", 1),
    ("Part II -- Social Systems", "part2/index.md", 0),
    ("Religion", "part2/religion.md", 1),
    ("Kingdom & Republic", "part2/kingdom-republic.md", 1),
    ("Ten Social Systems Compared", "part2/ten-systems.md", 1),
    ("Verein (e.V.)", "part2/examples/verein.md", 2),
    ("Democracy", "part2/examples/democracy.md", 2),
    ("Theocracy", "part2/examples/theocracy.md", 2),
    ("Corporation", "part2/examples/corporation.md", 2),
    ("University", "part2/examples/university.md", 2),
    ("Military", "part2/examples/military.md", 2),
    ("Family", "part2/examples/family.md", 2),
    ("One-Party State", "part2/examples/one-party-state.md", 2),
    ("Part III -- Development Frameworks", "part3/index.md", 0),
    ("Eight Frameworks Decomposed", "part3/frameworks.md", 1),
    ("The Framework Platform", "part3/framework-platform.md", 1),
    ("Hybrid Architectures", "part3/hybrids.md", 1),
    ("Part IV -- STPA Applied", "part4/index.md", 0),
    ("STPA on Religion", "part4/religion-stpa.md", 1),
    ("Control Structures in Social Systems", "part4/control-structures.md", 1),
    ("Architectural Remedies", "part4/remedies.md", 1),
    ("About", "about.md", 0),
]


def clean_markdown(text):
    """Pre-process markdown to remove MkDocs-specific syntax."""

    # Remove mermaid code blocks
    text = re.sub(r'```mermaid\n.*?```', '*[Diagram: see online version]*\n', text, flags=re.DOTALL)

    # Handle MkDocs admonitions: !!! type "title" / indented body
    def admonition_sub(m):
        title = m.group(2) or m.group(1).capitalize()
        body = m.group(3)
        body = re.sub(r'^    ', '', body, flags=re.MULTILINE)
        return f'\n> **{title}**\n>\n> {body}\n'
    text = re.sub(
        r'^!!! (\w+)(?: "([^"]*)")?\n((?:    .*\n?)+)',
        admonition_sub, text, flags=re.MULTILINE
    )

    # Replace links to docs/interactive/*.html with rendered PNG embeds
    # (must run BEFORE attribute-list stripping so the { .md-button } suffix
    # is consumed by the same regex).
    text = replace_interactive_links(text)

    # Remove MkDocs attribute lists: { .md-button }, { .lg }, etc.
    text = re.sub(r'\{[^}]*\.md-button[^}]*\}', '', text)
    text = re.sub(r'\{\s*[^}]*(?:width|loading|\.lg|\.middle)[^}]*\}', '', text)

    # Any remaining non-embedded interactive links fall through to plain text.
    text = re.sub(
        r'\[([^\]]*Interactive[^\]]*)\]\([^)]*\.html[^)]*\)',
        r'*[\1 -- see online version]*',
        text, flags=re.IGNORECASE
    )

    # Compact "Level | ID | Description" hierarchy tables into grouped bullet
    # lists (much denser than the default bordered-table rendering).
    text = compact_hierarchy_tables(text)

    # Convert internal .md links to plain text
    text = re.sub(r'\[([^\]]+)\]\([^)]*\.md[^)]*\)', r'\1', text)

    # Handle footnotes: [^1] references and [^1]: definitions
    # Keep them as inline text
    text = re.sub(r'\[\^(\d+)\]:', r'[Footnote \1]:', text)
    text = re.sub(r'\[\^(\d+)\]', r'[\1]', text)

    # Remove material icons
    text = re.sub(r':material-[a-z-]+:\{[^}]*\}', '', text)
    text = re.sub(r':material-[a-z-]+:', '', text)

    # Clean up multiple blank lines
    text = re.sub(r'\n{4,}', '\n\n\n', text)

    return text


def md_to_html(md_text):
    """Convert markdown to HTML suitable for fpdf2's write_html."""
    html = markdown.markdown(md_text, extensions=['tables', 'fenced_code'], output_format='html')
    return html


# ---------------------------------------------------------------------------
# Rendering interactive D3 pages to PNG via headless Chromium
# ---------------------------------------------------------------------------

_CHROMIUM_PATH = None
_D3_BODY = None


def find_chromium():
    """Locate a headless Chromium executable that Playwright can drive."""
    global _CHROMIUM_PATH
    if _CHROMIUM_PATH:
        return _CHROMIUM_PATH
    candidates = []
    for pat in (
        "/opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell",
        "/opt/pw-browsers/chromium-*/chrome-linux/chrome",
    ):
        candidates.extend(sorted(glob.glob(pat)))
    for c in candidates:
        if os.path.exists(c):
            _CHROMIUM_PATH = c
            return c
    return None


def _load_d3_body():
    global _D3_BODY
    if _D3_BODY is not None:
        return _D3_BODY
    d3_path = os.path.join(VENDOR_DIR, "d3.min.js")
    if os.path.exists(d3_path):
        with open(d3_path, "rb") as f:
            _D3_BODY = f.read()
    else:
        _D3_BODY = b""
    return _D3_BODY


def render_interactive_to_png(html_filename):
    """Render docs/interactive/<html_filename> to TWO PNG images using
    headless Chromium: one of the D3 graph view, one of the Table view.
    Returns (graph_png_path, table_png_path) or None on failure.

    Results are cached on disk under .interactive_renders/ and only
    re-generated when the HTML source is newer than the cached PNGs."""
    html_path = os.path.join(INTERACTIVE_DIR, html_filename)
    if not os.path.exists(html_path):
        return None

    os.makedirs(RENDERED_DIR, exist_ok=True)
    base = os.path.splitext(html_filename)[0]
    graph_png = os.path.join(RENDERED_DIR, base + ".graph.png")
    table_png = os.path.join(RENDERED_DIR, base + ".table.png")

    src_mtime = os.path.getmtime(html_path)
    if (
        os.path.exists(graph_png)
        and os.path.exists(table_png)
        and os.path.getmtime(graph_png) >= src_mtime
        and os.path.getmtime(table_png) >= src_mtime
    ):
        return (graph_png, table_png)

    chromium = find_chromium()
    if not chromium:
        print(f"  No Chromium found; cannot render {html_filename}")
        return None

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("  playwright not installed; cannot render interactive pages")
        return None

    d3_body = _load_d3_body()

    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(executable_path=chromium)
            try:
                context = browser.new_context(
                    viewport={"width": 1200, "height": 1800},
                    device_scale_factor=2,
                )
                page = context.new_page()

                def handle_route(route):
                    url = route.request.url
                    if d3_body and "d3" in url and url.endswith(".js"):
                        route.fulfill(
                            status=200,
                            content_type="application/javascript",
                            body=d3_body,
                        )
                    elif "fonts.googleapis" in url or "fonts.gstatic" in url:
                        route.fulfill(status=200, content_type="text/css", body=b"")
                    else:
                        try:
                            route.continue_()
                        except Exception:
                            route.abort()

                page.route("**/*", handle_route)
                page.goto("file://" + os.path.abspath(html_path))
                try:
                    page.wait_for_selector(".gc svg g", timeout=15000)
                except Exception:
                    pass
                page.wait_for_timeout(400)

                # Graph view
                page.evaluate(
                    "showV('graph', document.querySelectorAll('.tab')[0])"
                )
                page.wait_for_timeout(300)
                page.locator(".gc").first.screenshot(path=graph_png)

                # Table view
                page.evaluate(
                    "showV('table', document.querySelectorAll('.tab')[1])"
                )
                page.wait_for_timeout(300)
                page.locator(".tc").first.screenshot(path=table_png)
            finally:
                browser.close()
    except Exception as e:
        print(f"  Render failed for {html_filename}: {e}")
        return None

    print(f"  Rendered: {base}.graph.png + {base}.table.png")
    return (graph_png, table_png)


# Regex for [label](interactive/x.html) with optional { ... } attrs
_INTERACTIVE_LINK_RE = re.compile(
    r'\[([^\]]+)\]\(([^)]*interactive/[^)]+\.html)\)(?:\s*\{[^}]*\})?'
)


def replace_interactive_links(text):
    def _sub(m):
        alt = m.group(1).strip()
        filename = os.path.basename(m.group(2))
        result = render_interactive_to_png(filename)
        if not result:
            return "*[{} -- see online version]*".format(alt)
        graph_png, table_png = result
        return (
            "\n\n![{} — graph]({})\n\n"
            "![{} — table]({})\n\n"
        ).format(alt, graph_png, alt, table_png)
    return _INTERACTIVE_LINK_RE.sub(_sub, text)


# ---------------------------------------------------------------------------
# Compact rendering of "Level | ID | Description" hierarchy tables
# ---------------------------------------------------------------------------

_HIER_HEADER_RE = re.compile(
    r'^\s*\|\s*\*{0,2}Level\*{0,2}\s*\|\s*\*{0,2}ID\*{0,2}\s*\|\s*\*{0,2}Description\*{0,2}\s*\|\s*$',
    re.IGNORECASE,
)
_HIER_SEP_RE = re.compile(r'^\s*\|[-:\s|]+\|\s*$')


def compact_hierarchy_tables(text):
    """Find `| Level | ID | Description |` markdown tables and rewrite them as
    compact grouped bullet lists — one heading per level, one line per item.
    This avoids the borders, per-row level repetition, and table-wrap
    overhead that inflate the PDF."""
    lines = text.split('\n')
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if _HIER_HEADER_RE.match(line) and i + 1 < len(lines) and _HIER_SEP_RE.match(lines[i + 1]):
            j = i + 2
            rows = []
            while j < len(lines) and lines[j].strip().startswith('|'):
                rows.append(lines[j])
                j += 1
            groups = {}
            order = []
            for row in rows:
                cells = [c.strip() for c in row.strip().strip('|').split('|')]
                if len(cells) < 3:
                    continue
                lvl = re.sub(r'\*+', '', cells[0]).strip().rstrip('.')
                if not lvl:
                    continue
                if lvl not in groups:
                    groups[lvl] = []
                    order.append(lvl)
                groups[lvl].append((cells[1], cells[2]))
            if not groups:
                out.append(line)
                i += 1
                continue
            out.append('')
            for lvl in order:
                out.append('**{}**'.format(lvl))
                out.append('')
                for ident, desc in groups[lvl]:
                    # Plain paragraphs avoid fpdf2's bullet rendering bugs
                    # (oversized/coloured bullet, list broken across pages).
                    out.append('**{}** \u2014 {}'.format(ident, desc))
                    out.append('')
            i = j
            continue
        out.append(line)
        i += 1
    return '\n'.join(out)


def strip_inline_tags_in_table_cells(html):
    """fpdf2's write_html raises NotImplementedError on any nested tag inside
    a <td> or <th> element (e.g. <em>, <strong>, <code>, <a>...). That error
    fires MID-RENDER, which corrupts output because write_html has already
    emitted partial content before raising. To stay safe we strip all inline
    tags inside table cells up front, keeping only their text."""
    def process_cell(m):
        tag = m.group(1)
        attrs = m.group(2)
        content = m.group(3)
        content = re.sub(r'<[^>]+>', '', content)
        return f'<{tag}{attrs}>{content}</{tag}>'
    return re.sub(
        r'<(td|th)((?:\s[^>]*)?)>(.*?)</\1>',
        process_cell,
        html,
        flags=re.DOTALL,
    )


def widen_long_column(html):
    """For tables with >=2 columns, give 60% width to whichever column has the
    most text content (sampled across the first few rows). The remaining 40% is
    split equally among the other columns. This handles tables where the long
    column is not always column 3."""

    def process_table(match):
        table_html = match.group(0)
        first_row_match = re.search(r'<tr[^>]*>.*?</tr>', table_html, flags=re.DOTALL)
        if not first_row_match:
            return table_html
        first_row = first_row_match.group(0)
        n = len(re.findall(r'<(?:th|td)\b', first_row))
        if n < 2:
            return table_html

        # Sample up to 6 rows to find which column carries the most text.
        all_rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_html, flags=re.DOTALL)
        col_lengths = [0] * n
        for row_html in all_rows[:6]:
            cells = re.findall(r'<(?:th|td)[^>]*>(.*?)</(?:th|td)>', row_html, flags=re.DOTALL)
            for i, cell in enumerate(cells[:n]):
                col_lengths[i] += len(re.sub(r'<[^>]+>', '', cell).strip())

        long_col = col_lengths.index(max(col_lengths))

        # Scale the long-column share down for wide tables so the other
        # columns stay wide enough to avoid mid-word line breaks.
        # n=2→60, n=3→60, n=4→40, n=5→35, n=6→30
        long_width = max(30, 60 - max(0, n - 3) * 10)
        remaining = 100 - long_width
        other_width = remaining // (n - 1)
        widths = [other_width] * n
        widths[long_col] = long_width
        widths[0] += 100 - sum(widths)  # absorb rounding drift into col 1

        cell_idx = [0]
        def replace_cell(m):
            tag = m.group(1)
            attrs = m.group(2)
            attrs = re.sub(r'\s*width\s*=\s*"[^"]*"', '', attrs)
            w = widths[cell_idx[0]]
            cell_idx[0] += 1
            return f'<{tag}{attrs} width="{w}%">'

        new_first_row = re.sub(r'<(th|td)((?:\s[^>]*)?)>', replace_cell, first_row)
        return table_html.replace(first_row, new_first_row, 1)

    return re.sub(r'<table[^>]*>.*?</table>', process_table, html, flags=re.DOTALL)


def convert_ul_to_paragraphs(html):
    """Replace <ul>…</ul> blocks with plain <p>• item</p> paragraphs.

    fpdf2's built-in <li> renderer draws a filled disc in a hardcoded red
    colour regardless of li_prefix_color kwargs in some versions. Converting
    to plain paragraphs gives us full control over bullet colour and size."""
    def replace_list(m):
        items = re.findall(r'<li[^>]*>(.*?)</li>', m.group(1), flags=re.DOTALL)
        return '\n'.join(f'<p>\u2022\u00a0{item.strip()}</p>' for item in items)
    return re.sub(r'<ul[^>]*>(.*?)</ul>', replace_list, html, flags=re.DOTALL)


HTML_TAG_STYLES = {
    # Override fpdf2's default Courier-based pre/code styles with a Unicode
    # font so ASCII box-drawing characters (┌ └ ├ │ ─) render correctly.
    "pre": TextStyle(font_family="LibMono", t_margin=4 + 7 / 30),
    "code": FontFace(family="LibMono"),
}


class BookPDF(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_auto_page_break(auto=True, margin=20)
        self.add_font('LibSerif', '', FONTS["Serif"])
        self.add_font('LibSerif', 'B', FONTS["SerifB"])
        self.add_font('LibSerif', 'I', FONTS["SerifI"])
        self.add_font('LibSerif', 'BI', FONTS["SerifBI"])
        self.add_font('LibSans', '', FONTS["Sans"])
        self.add_font('LibSans', 'B', FONTS["SansB"])
        self.add_font('LibSans', 'I', FONTS["SansI"])
        self.add_font('LibSans', 'BI', FONTS["SansBI"])
        self.add_font('LibMono', '', FONTS["Mono"])
        self.add_font('LibMono', 'B', FONTS["MonoB"])
        self.add_font('LibMono', 'I', FONTS["MonoI"])
        self.add_font('LibMono', 'BI', FONTS["MonoBI"])
        self.toc_entries = []

    def header(self):
        if self.page_no() > 1:
            self.set_font('LibSans', '', 8)
            self.set_text_color(128, 128, 128)
            self.cell(0, 8, 'Systems Thinking -- From SE to STPA', align='C')
            self.ln(4)
            self.set_draw_color(200, 200, 200)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font('LibSans', '', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def add_title_page(self):
        self.add_page()
        self.ln(70)
        self.set_font('LibSerif', 'B', 26)
        self.set_text_color(63, 81, 181)  # Indigo
        self.cell(0, 14, 'Systems Thinking', align='C', new_x="LMARGIN", new_y="NEXT")
        self.set_font('LibSerif', '', 18)
        self.set_text_color(80, 80, 80)
        self.cell(0, 12, 'From SE to STPA', align='C', new_x="LMARGIN", new_y="NEXT")
        self.ln(15)
        self.set_font('LibSerif', 'I', 12)
        self.set_text_color(100, 100, 100)
        self.multi_cell(0, 7,
            'Applying Systems Engineering Decomposition,\n'
            'Product Line Thinking, and STPA\n'
            'to Social and Technical Systems',
            align='C')
        self.ln(30)
        self.set_font('LibSans', '', 12)
        self.set_text_color(60, 60, 60)
        self.cell(0, 8, 'C. Cabos', align='C', new_x="LMARGIN", new_y="NEXT")
        self.ln(40)
        self.set_font('LibSans', '', 9)
        self.set_text_color(140, 140, 140)
        self.cell(0, 5, 'https://ccabos.github.io/systems/', align='C', new_x="LMARGIN", new_y="NEXT")

    def add_toc(self, toc_data):
        """Add table of contents with pre-computed page numbers."""
        self.add_page()
        self.set_font('LibSerif', 'B', 20)
        self.set_text_color(63, 81, 181)
        self.cell(0, 15, 'Table of Contents', align='L', new_x="LMARGIN", new_y="NEXT")
        self.ln(3)
        self.set_draw_color(63, 81, 181)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(8)

        for title, page_num, level in toc_data:
            if level == 0:
                self.set_font('LibSans', 'B', 11)
                self.set_text_color(40, 40, 40)
                indent = 0
            elif level == 1:
                self.set_font('LibSans', '', 10)
                self.set_text_color(70, 70, 70)
                indent = 8
            else:
                self.set_font('LibSans', '', 10)
                self.set_text_color(100, 100, 100)
                indent = 16

            self.set_x(15 + indent)
            title_w = 155 - indent
            self.cell(title_w, 7, title, new_x="RIGHT")
            self.cell(20, 7, str(page_num), align='R', new_x="LMARGIN", new_y="NEXT")

    def place_image(self, img_path, alt_text=""):
        """Embed an image centered on the current (or next) page. Handles
        downscaling, format conversion, and page breaks so callers don't
        have to worry about layout."""
        if not img_path or not os.path.exists(img_path):
            return
        try:
            with PILImage.open(img_path) as pil_img:
                iw, ih = pil_img.size

                # Downscale oversized images for reasonable PDF size
                max_px = 1800
                if iw > max_px or ih > max_px:
                    pil_img.thumbnail((max_px, max_px), PILImage.LANCZOS)
                    iw, ih = pil_img.size

                if pil_img.mode in ("RGBA", "P", "LA"):
                    bg = PILImage.new("RGB", pil_img.size, (255, 255, 255))
                    if pil_img.mode == "P":
                        pil_img = pil_img.convert("RGBA")
                    bg.paste(pil_img, mask=pil_img.split()[-1] if "A" in pil_img.mode else None)
                    pil_img = bg
                elif pil_img.mode != "RGB":
                    pil_img = pil_img.convert("RGB")

                buf = io.BytesIO()
                pil_img.save(buf, format="JPEG", quality=82, optimize=True)
                buf.seek(0)

            aspect = ih / iw
            max_w = 170  # mm
            w = min(max_w, iw * 0.264583)
            h = w * aspect
            available = self.h - self.get_y() - 30
            if h > available:
                max_h = 240
                if h > max_h:
                    h = max_h
                    w = h / aspect
                self.add_page()
            x = (210 - w) / 2
            self.image(buf, x=x, w=w)
            self.ln(3)
            if alt_text:
                self.set_font("LibSans", "I", 8)
                self.set_text_color(100, 100, 100)
                self.cell(0, 4, alt_text, align="C", new_x="LMARGIN", new_y="NEXT")
                self.set_text_color(30, 30, 30)
            self.ln(4)
        except Exception as e:
            print(f"    Image error ({os.path.basename(img_path)}): {e}")

    def render_section(self, nav_title, md_content, level=0):
        """Render a section and return its starting page number."""
        self.add_page()
        page_num = self.page_no()
        self.toc_entries.append((nav_title, page_num, level))

        cleaned = clean_markdown(md_content)
        html = md_to_html(cleaned)
        html = strip_inline_tags_in_table_cells(html)
        html = widen_long_column(html)
        html = convert_ul_to_paragraphs(html)

        self.set_font('LibSerif', '', 11)
        self.set_text_color(30, 30, 30)

        # Split the HTML on <img> tags so we can handle them with place_image
        segments = re.split(r'(<img\s[^>]+/?>)', html)
        for segment in segments:
            if not segment:
                continue
            img_match = re.match(r'<img\s[^>]*src="([^"]+)"[^>]*/?>', segment)
            if img_match:
                img_path = img_match.group(1)
                alt_match = re.search(r'alt="([^"]*)"', segment)
                alt_text = alt_match.group(1) if alt_match else ""
                self.place_image(img_path, alt_text)
                continue

            # Remove any stray img tags inside text segments
            segment = re.sub(r'<img[^>]*/?>', '', segment)
            if not segment.strip():
                continue

            # Important: do NOT wrap write_html in a fallback that re-renders
            # the whole segment — write_html commits output incrementally, so
            # a retry would duplicate everything that rendered before the
            # error. Just log and continue; strip_inline_tags_in_table_cells
            # already removes the common offender.
            self.set_font('LibSerif', '', 11)
            self.set_text_color(30, 30, 30)
            try:
                self.write_html(segment, tag_styles=HTML_TAG_STYLES)
            except Exception as exc:
                print(f"    write_html error in '{nav_title}': {exc}")

        return page_num


def load_sections():
    """Load all section content from markdown files."""
    sections = []
    for nav_title, filename, level in NAV:
        filepath = os.path.join(DOCS_DIR, filename)
        if not os.path.exists(filepath):
            print(f"  Warning: {filepath} not found, skipping")
            continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        sections.append((nav_title, content, level))
    return sections


def build_pdf(sections, include_toc_data=None):
    """Build the PDF. If include_toc_data is provided, insert TOC after title page."""
    pdf = BookPDF()
    pdf.set_title("Systems Thinking -- From SE to STPA")
    pdf.set_author("C. Cabos")

    pdf.add_title_page()

    if include_toc_data:
        pdf.add_toc(include_toc_data)

    for i, (nav_title, content, level) in enumerate(sections):
        print(f"  [{i+1:2d}/{len(sections)}] {nav_title}")
        pdf.render_section(nav_title, content, level)

    return pdf


def main():
    print("Loading sections...")
    sections = load_sections()

    # Pass 1: Build without TOC to measure page numbers
    print("\nPass 1: Measuring page layout...")
    pdf1 = build_pdf(sections)

    # TOC will take ~1 page (28 entries at 7mm = 196mm, fits on 1 page)
    toc_pages = 1
    adjusted_toc = [
        (title, page_num + toc_pages, level)
        for title, page_num, level in pdf1.toc_entries
    ]

    # Pass 2: Build with TOC
    print("\nPass 2: Generating final PDF with table of contents...")
    pdf2 = build_pdf(sections, include_toc_data=adjusted_toc)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Systems_Thinking_Book.pdf")
    pdf2.output(output_path)
    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"\n  PDF generated: {output_path}")
    print(f"  Total pages: {pdf2.pages_count}")
    print(f"  File size: {size_mb:.1f} MB")


if __name__ == "__main__":
    main()
