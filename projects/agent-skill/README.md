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

the skill walks them through the procedure below. The procedure is
**iterative, not linear**: each step can trigger a return to an
earlier one. Decomposition often reveals a wrong boundary; STPA often
reveals missing requirements. The skill must say explicitly when a
later finding invalidates earlier output and prompt the user to revise.

## Step 0 — Route: system analysis or problem diagnosis?

Before anything else, the skill determines which of two traversal
strategies applies:

- **System analysis** — the user wants to understand an institution
  from scratch. Proceed top-down: goals → requirements → structure →
  control → safety.
- **Problem diagnosis** — the user has a specific failure or concern
  inside an existing institution. Proceed bottom-up: identify which
  requirement is being violated or which control action is unsafe,
  trace the causal path upward, then scope the decomposition to the
  relevant portion of the system.

The two paths rejoin at step 4. Steps 1–3 differ in emphasis and
depth depending on the route chosen.

## Steps

### 1. Boundary and stakeholder
Who and what is inside the system; who is asking and why; what counts
as inside vs environment. Document explicitly: if the boundary turns
out to be wrong at a later step, record the revision here.

### 2. Catalogue lookup and decomposition scaffold

**Look up the catalogue before decomposing from scratch.**
Check `knowledge/system-catalogues/` for a known family member that
matches or closely resembles the user's system. If a match exists:

- Use the known decomposition as a starting scaffold.
- Record which elements are inherited from the platform and which are
  specific to this instance.
- Note the variation-point bindings that differ from the canonical
  case.

If no match exists, build the decomposition from first principles
using the five-level hierarchy
(`knowledge/se-techniques/goals-requirements-hierarchy/`), then flag
that a new family member may be worth cataloguing.

**Five-level SE decomposition** — goals, requirements, functions,
logical architecture, physical implementation, with full traceability
links between levels.

**Validation pass (mandatory before proceeding).**
Before moving to step 3, check:

- Are all goals genuinely goals (outcomes the system exists to
  produce) rather than hidden solutions or process descriptions?
- Are requirements necessary and sufficient to achieve the goals?
- Does every function trace to at least one requirement?
- Are traceability links consistent (no orphan nodes, no
  contradictory allocations)?

Record any failures. Do not proceed until the decomposition passes
the validation checklist or the user explicitly accepts a known gap.

### 3. Product-line positioning

Confirm or refine the catalogue match from step 2:

- Which platform elements apply unchanged?
- Which variation-point bindings are inherited, and which are
  specific to this instance?
- Does the system belong to a known family, or is it a hybrid?

If the system is a hybrid, cite
`knowledge/system-catalogues/*/cross-*/` for the applicable
cross-system analysis.

### 4. Control-structure sketch

Apply the four diagnostic questions
(`knowledge/se-techniques/control-structures/diagnostic-questions.md`)
and search for the three dangerous patterns
(`knowledge/se-techniques/control-structures/dangerous-patterns.md`).

Record: which controllers exist, what they control, what feedback
channels exist, and which (if any) dangerous patterns are present.

### 5. STPA pass (if warranted)

**Warranted when all three of the following hold:**

1. The user's concern involves potential for harmful outcomes (not
   merely inefficiency or performance shortfall).
2. The system has identifiable authority relationships — some actors
   can issue control actions that others are structurally expected to
   obey.
3. Feedback channels exist (or are conspicuously absent) between
   controlled processes and controllers.

If STPA is warranted, follow the four steps in
`knowledge/se-techniques/stpa/four-steps.md`: losses → hazards →
unsafe control actions → causal scenarios.

**Validation pass after UCAs.** Before moving to step 6, verify that
each UCA traces back to a specific causal factor in the control
structure, not just to human error or bad intentions.

### 6. Remedy proposals

Draw remedies from
`knowledge/system-catalogues/*/cross-*/remedies-case-studies.md`.

**For systems that match a known catalogue entry:** use the specific
remedies documented for that system family, adapted to the instance.

**For novel systems or unmatched UCAs:** fall back to the three
dangerous patterns. Each UCA identified in step 5 must map to at
least one pattern (accountability void, self-sealing process model,
proxy metric replacing goal). Derive the remedy by closing the
specific structural pathway the pattern describes — do not improvise
generic "improve communication" or "add oversight" proposals.

If the system is genuinely novel and its remedies cannot be derived
from pattern-matching, say so explicitly. Do not invent remedies.
Flag the gap for the `knowledge/` maintainer.

### 7. Deliverable

Produce one of two artefact types, chosen with the user:

- **Decision memo** — 1–2 pages, executive audience, structured as:
  *System | Key finding | Structural cause | Recommended remedy |
  Evidence base | Next step.* Template: `reference/memo-template.md`.
- **Analysis report** — full technical report with all seven steps
  documented, traceability matrix, UCA table, remedy table with
  evidence citations. Template: `reference/report-template.md`.

Both templates are in `reference/`. Every claim in the deliverable
that draws on a technique or catalogue entry must cite the
`knowledge/` file it came from.

## Intended files

- `SKILL.md` — the skill manifest and prompt. Must cite paths in
  `../../knowledge/` for every technique and every catalogue entry
  it references.
- `reference/memo-template.md` — decision memo template.
- `reference/report-template.md` — full analysis report template.
- `reference/validation-checklist.md` — decomposition and UCA
  validation checklists for steps 2 and 5.
- `reference/` — any other static reference data the skill needs
  (e.g. a minimal copy of the variation-point catalogue for offline
  use).
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
- **Never invent remedies.** Remedy proposals must derive from the
  documented catalogue or from the three dangerous patterns. If
  neither applies, flag the gap rather than generalise.
- **Always cite by reading, not by memory.** Every claim the skill
  makes about SE, PLE, or STPA must cite a file under `knowledge/`.
  The skill must read that file during the session before using its
  content — citation without reading is not verification.
- **State when back-revision is needed.** If a finding in a later
  step invalidates output from an earlier step, the skill must say
  so explicitly and prompt the user to revise the earlier output
  before continuing.

## Relation to `problems/`

Running the skill on a real stakeholder problem produces artefacts
that belong in `../problems/<problem-name>/`. The skill is the
procedure; the problems folder is the record. Artefacts filed should
follow the report template so they are structurally consistent and
reusable.
