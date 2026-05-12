#!/usr/bin/env python3
"""Render every docs/interactive/*.html explorer to two PNGs (graph + table).

The MkDocs PDF build (hooks.py) embeds these PNGs into the printed book
because WeasyPrint cannot execute the D3 client-side script. This script
populates the cache directory so the hook finds them. Call it from CI
before `mkdocs build` runs with ENABLE_PDF_EXPORT=1.

Standalone (no dependency on generate_pdf.py) so the PDF generation
pipeline keeps working even if fpdf2 / Pillow aren't installed.
"""

import glob
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
INTERACTIVE_DIR = os.path.join(HERE, "docs", "interactive")
VENDOR_DIR = os.path.join(HERE, "vendor")
RENDERED_DIR = os.path.join(HERE, ".interactive_renders")


def find_chromium():
    explicit = os.environ.get("WITH_PDF_CHROMIUM_PATH")
    if explicit and os.path.isfile(explicit):
        return explicit
    for pat in (
        "/opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell",
        "/opt/pw-browsers/chromium-*/chrome-linux/chrome",
    ):
        matches = sorted(glob.glob(pat))
        if matches:
            return matches[-1]
    import shutil
    return (
        shutil.which("chromium")
        or shutil.which("chromium-browser")
        or shutil.which("google-chrome")
    )


def load_d3_body():
    path = os.path.join(VENDOR_DIR, "d3.min.js")
    if os.path.exists(path):
        with open(path, "rb") as f:
            return f.read()
    return b""


def render_one(page, html_path, graph_png, table_png):
    page.goto("file://" + os.path.abspath(html_path))
    try:
        page.wait_for_selector(".gc svg g", timeout=15000)
    except Exception:
        pass
    page.wait_for_timeout(400)
    page.evaluate("showV('graph', document.querySelectorAll('.tab')[0])")
    page.wait_for_timeout(300)
    page.locator(".gc").first.screenshot(path=graph_png)
    page.evaluate("showV('table', document.querySelectorAll('.tab')[1])")
    page.wait_for_timeout(300)
    page.locator(".tc").first.screenshot(path=table_png)


def main():
    chromium = find_chromium()
    if not chromium:
        print("No Chromium executable found; skipping interactive renders.")
        return 0

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("playwright not installed; skipping interactive renders.")
        return 0

    os.makedirs(RENDERED_DIR, exist_ok=True)
    d3_body = load_d3_body()
    html_files = sorted(
        f for f in os.listdir(INTERACTIVE_DIR)
        if f.endswith(".html") and f != "_template.html"
    )
    if not html_files:
        print("No interactive HTMLs to render.")
        return 0

    print(f"Rendering {len(html_files)} interactive explorers via {chromium}")
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

            for name in html_files:
                base = os.path.splitext(name)[0]
                html_path = os.path.join(INTERACTIVE_DIR, name)
                graph_png = os.path.join(RENDERED_DIR, f"{base}.graph.png")
                table_png = os.path.join(RENDERED_DIR, f"{base}.table.png")
                src_mtime = os.path.getmtime(html_path)
                if (
                    os.path.exists(graph_png)
                    and os.path.exists(table_png)
                    and os.path.getmtime(graph_png) >= src_mtime
                    and os.path.getmtime(table_png) >= src_mtime
                ):
                    print(f"  cached: {base}")
                    continue
                try:
                    render_one(page, html_path, graph_png, table_png)
                    print(f"  rendered: {base}")
                except Exception as e:
                    print(f"  FAILED {base}: {e}")
        finally:
            browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
