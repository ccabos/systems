# Systems Introduction Book

A readable book introducing Systems Engineering and its application to
non-technical systems, aimed at readers who are not SE specialists.

## Audience

Readers who are curious about how structured engineering methods might
apply to social and organisational systems, but who have no formal SE
background. The book favours motivation and worked examples over
completeness. For the full evidence base (exhaustive decompositions,
comparison matrices, bibliography) see the repository-level
[`knowledge/`](../../knowledge/) tree.

## Scope

- A single narrative arc from "what is a system" through SE techniques
  to STPA applied to social systems.
- A handful of well-chosen worked examples rather than exhaustive
  coverage.
- Short tables that serve the narrative; long listings stay in
  `knowledge/`.

Out of scope: the problem-driven projects, the AI agent skill, and the
textbook — each lives in its own sibling directory under `projects/`.

## Build

```bash
cd projects/systems-introduction-book
pip install mkdocs mkdocs-material pymdown-extensions
mkdocs serve       # local preview at http://127.0.0.1:8000
mkdocs build       # static site in ./site
python generate_pdf.py
```

## Published

- Static site: [https://ccabos.github.io/systems/](https://ccabos.github.io/systems/)
- PDF: [`Systems_Thinking_Book.pdf`](Systems_Thinking_Book.pdf)
