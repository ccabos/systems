# STPA Copilot — Agent Skill

A Claude Agent skill that guides a user through a structured analysis
of a social, economic, governance, or other non-technical institutional
system using the SE / product-line / STPA techniques from
`../../knowledge/`.

**Skill bundle entry point:** [`SKILL.md`](SKILL.md) — the system prompt loaded by Claude.ai when this folder is uploaded as a skill.

**Design specification:** [`SKILL-spec.md`](SKILL-spec.md) — the third-person specification of audience, procedure, and knowledge-file map that the prompt was derived from. Kept in the repo for reference; not loaded at runtime.

## Quick summary

The skill accepts two entry points:

- A user who wants to understand an institution from scratch (system
  analysis, top-down).
- A user who has a specific failure or problem inside an institution
  (problem diagnosis, bottom-up).

It walks them through an eight-step procedure (boundary →
decomposition → product-line positioning → control structure →
justificatory-rung tagging *(social systems only)* → STPA →
remedies → deliverable) and produces either a plain-language
decision memo or a full analysis report filed under
`../problems/<problem-name>/`.

Primary users are ordinary non-specialists with no SE or STPA
background. The skill is designed to work for them without prior study.

## Repository layout

```
agent-skill/
├── SKILL.md                        # System prompt (loaded by Claude.ai)
├── SKILL-spec.md                   # Original design specification
├── reference/                      # Bundled knowledge files (self-contained)
│   ├── se-techniques/              # 7 always-read technique files
│   ├── system-catalogues/
│   │   ├── social-systems/         # 4 cross-system + 10 per-system + 1 worked example
│   │   └── dev-frameworks/         # 5 cross-framework + 8 per-framework
│   ├── memo-template.md            # Decision memo template (TODO)
│   └── report-template.md          # Full analysis report template (TODO)
├── examples/                       # Worked examples (social, economic, governance)
└── scripts/                        # Python / shell helpers
```

**Upload-ready.** The `reference/` subfolder mirrors the relevant
subset of the project's `knowledge/` tree, so `SKILL.md` can read
everything it needs from inside the skill bundle. No filesystem
access outside `agent-skill/` is required.
