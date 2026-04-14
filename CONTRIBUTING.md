# Contributing

This repository has two top-level trees that serve different purposes.
Knowing which one you are editing is the single most important rule.

## `knowledge/` — the systematic foundation

- Allowed to be dry, exhaustive, and listing-heavy.
- Completeness and reusability matter more than narrative flow.
- Every hierarchical SE decomposition lives here. It is the canonical
  source — never duplicate a decomposition into a project.
- One folder per system / technique / topic. Each folder has an
  `overview.md` as its entry point.
- Citations go next to the claim, in a local `sources.md` or in
  `knowledge/references/bibliography.md`.

## `projects/` — derived artefacts

- Allowed to be selective, narrative, and opinionated.
- A project may reference or excerpt from `knowledge/`, but must not
  become the canonical home for any evidence.
- Each project has its own `README.md` stating its audience, scope,
  and out-of-scope.
- The `projects/systems-introduction-book/` project publishes a static
  MkDocs site and a PDF. Any change to it must keep `mkdocs build` and
  `python generate_pdf.py` working.

## Commits

- Small, focused commits. One logical change per commit.
- Commit messages explain the *why*, not just the *what*.
