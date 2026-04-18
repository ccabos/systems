# Claude Instructions for Systems Book

This project is a book on systems engineering, product line thinking, and STPA applied to social and technical systems.

## Technology
- MkDocs with Material theme
- GitHub Pages via GitHub Actions
- Content in Markdown under docs/

## PDF build
`generate_pdf.py` produces `Systems_Thinking_Book.pdf`. Before running
it, install the PDF pipeline dependencies — they are not the same set
as the MkDocs deps:

```bash
pip install -r requirements-pdf.txt
python -m playwright install chromium   # unless /opt/pw-browsers/ is already populated
```

The script finds a pre-installed Chromium at
`/opt/pw-browsers/chromium{,_headless_shell}-*/chrome-linux/` before
falling back to the Playwright-managed install.

## Structure
- Part I: Foundations (SE hierarchy, product lines, STPA)
- Part II: Social systems (10 systems compared, product line analysis)
- Part III: Development frameworks (8 frameworks, hybrid architectures)
- Part IV: STPA applied (religion analysis, control structures, remedies)

## Style
- Academic but accessible
- Tables for SE decompositions
- Mermaid diagrams for control structures where possible
- Admonitions for key findings and examples
- Cross-references between chapters using relative links
