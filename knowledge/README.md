# Knowledge

The systematic foundation of this research project. This tree collects
the raw material that every derived artefact in `projects/` draws upon.
It is allowed to be dry, exhaustive, and listing-heavy — the goal is
completeness and reusability, not narrative flow.

## Structure

```
knowledge/
├── foundations/          1. What is a system?
├── se-techniques/        3–5. SE skills: catalog, how they work, technical examples
├── system-catalogues/    2, 6. Case studies of real-world systems
│   ├── social-systems/     — religions, polities, organisations, families…
│   └── dev-frameworks/     — software development process frameworks
└── references/           bibliography and glossary
```

More catalogues will be added under `system-catalogues/` as the scope
widens (e.g. biological systems, infrastructure systems, legal systems).

## Conventions

- One folder per system / technique / topic.
- Each folder has an `overview.md` as the entry point.
- Hierarchical SE decompositions are **canonical here**, never in a
  project. A project (e.g. the book) may *reference* or *excerpt* them.
- Sources and citations live next to the claim they support, in a
  `sources.md` (per folder) or the global `references/bibliography.md`.
