# Systems — Applying Systems Engineering to Non-Technical Systems

A research project on whether the methods engineers use to design safe,
reliable, goal-directed systems can be applied with benefit to
non-technical systems — political regimes, religions, corporations,
universities, families, development processes, and others.

## Repository layout

This repository is split into two top-level trees:

```
systems/
├── knowledge/     # The systematic foundation — the evidence base
└── projects/      # Derived artefacts that draw on knowledge/
```

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the rules that keep them
separate.

### `knowledge/`

The evidence base the project draws upon. Dry, exhaustive, and
listing-heavy on purpose. It holds:

- `foundations/` — what a system is
- `se-techniques/` — SE skills (SE hierarchy, product lines, STPA, …)
- `system-catalogues/` — case studies of real systems
  - `social-systems/` — religions, polities, organisations, families…
  - `dev-frameworks/` — Waterfall, V-Model, PRINCE2, Scrum, Kanban,
    Design Thinking, DevOps, SAFe
- `references/` — bibliography and glossary

More catalogues will be added under `system-catalogues/` as scope grows.

### `projects/`

Derived artefacts:

- `systems-introduction-book/` — a readable book introducing the ideas
  for readers unfamiliar with SE. Published as a MkDocs site and a PDF.
- `problems/` — problem-driven application area. One folder per
  concrete problem; each folder has a `problem.md` at its root.
- `agent-skill/` — an AI agent skill to apply SE to a new system or
  problem.
- `textbook/` — placeholder for a future derived textbook.

## The book

The readable book is published at
[https://ccabos.github.io/systems/](https://ccabos.github.io/systems/)
and distributed as a PDF
([`projects/systems-introduction-book/Systems_Thinking_Book.pdf`](projects/systems-introduction-book/Systems_Thinking_Book.pdf)).

To build it locally:

```bash
cd projects/systems-introduction-book
pip install mkdocs mkdocs-material pymdown-extensions
mkdocs serve    # local preview at http://127.0.0.1:8000
mkdocs build    # static site in ./site
python generate_pdf.py
```

## Historical state

The monolithic book layout that existed before this restructure is
preserved under the `Release` tag.

## License

Personal research and documentation project.
