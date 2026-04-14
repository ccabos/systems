# Agent Skill — SE for Non-Technical Systems

A Claude Agent skill that helps a user apply the SE / product-line /
STPA techniques from `../../knowledge/` to a new non-technical
system or a specific problem.

## Status

**Scaffold only.** This folder contains the skill's intended shape
and the interface contract. The actual `SKILL.md` and supporting
scripts will be written after the knowledge base has stabilised.

## What the skill is for

Given a user who arrives with *either*:

- an institutional system they want to analyse (a ministry, a
  charity, a religious order, a faculty, a team), **or**
- a specific problem inside an existing institution,

the skill should walk them through:

1. **Boundary and stakeholder** — who and what is inside the system;
   who is asking.
2. **Five-level SE decomposition** — goals, requirements, functions,
   logical architecture, physical implementation, with traceability.
3. **Product-line positioning** — which known system family this
   system belongs to, which platform elements apply, and which
   variation-point bindings it inherits.
4. **Control-structure sketch** — four diagnostic questions, search
   for the three dangerous patterns.
5. **STPA pass** (if warranted) — losses, hazards, UCAs, scenarios.
6. **Remedy proposals** — drawn from the catalogue of proven
   remedies, adapted to the specific context.
7. **Deliverable** — a decision memo or analysis report in the
   format the stakeholder needs.

## Intended files

- `SKILL.md` — the skill manifest and prompt. Must cite paths in
  `../../knowledge/` for every technique and every catalogue entry
  it references.
- `reference/` — any static reference data the skill needs (e.g. a
  minimal copy of the variation-point catalogue for offline use).
- `examples/` — worked examples of the skill's outputs for a few
  canonical cases.
- `scripts/` — any Python or shell helpers the skill invokes.

## Hard rules for this skill

- **Never invent system decompositions as canonical.** Every
  decomposition produced by the skill is a draft for a specific
  problem. If the user's system turns out to be a new family member
  worth cataloguing, the skill should say so and direct the user to
  file it under `knowledge/system-catalogues/`.
- **Never invent techniques.** The skill only uses techniques
  defined in `knowledge/se-techniques/`. If the user's problem
  needs something outside the catalogue, the skill should say so
  explicitly rather than improvise.
- **Always cite.** Every claim the skill makes about SE, PLE, or
  STPA must cite a file under `knowledge/` so that the user can
  verify and deepen the reasoning.

## Relation to `problems/`

Running the skill on a real stakeholder problem produces artefacts
that belong in `../problems/<problem-name>/`. The skill is the
procedure; the problems folder is the record.
