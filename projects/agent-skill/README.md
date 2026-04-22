# STPA Copilot — Agent Skill

A Claude Agent skill that guides a user through a structured analysis
of a social, economic, governance, or other non-technical institutional
system using the SE / product-line / STPA techniques from
`../../knowledge/`.

**Full specification:** [`SKILL.md`](SKILL.md)

## Quick summary

The skill accepts two entry points:

- A user who wants to understand an institution from scratch (system
  analysis, top-down).
- A user who has a specific failure or problem inside an institution
  (problem diagnosis, bottom-up).

It walks them through a seven-step procedure (boundary → decomposition
→ product-line positioning → control structure → STPA → remedies →
deliverable) and produces either a plain-language decision memo or a
full analysis report filed under `../problems/<problem-name>/`.

Primary users are ordinary non-specialists with no SE or STPA
background. The skill is designed to work for them without prior study.

## Repository layout

```
agent-skill/
├── SKILL.md                        # Complete specification (start here)
├── reference/
│   ├── memo-template.md            # Decision memo template
│   ├── report-template.md          # Full analysis report template
│   └── validation-checklist.md     # Step 2 and step 5 checklists
├── examples/                       # Worked examples (social, economic, governance)
└── scripts/                        # Python / shell helpers
```
