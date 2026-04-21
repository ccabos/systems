# Agent Skill — SE for Non-Technical Systems

A Claude Agent skill that helps a user apply the SE / product-line /
STPA techniques from `../../knowledge/` to a social, economic,
governance, or other non-technical institutional system — or to a
specific problem inside one.

## Status

**Scaffold only.** This folder contains the skill's intended shape
and the interface contract. The actual `SKILL.md` and supporting
scripts will be written after the knowledge base has stabilised.

## Target users of the tool

The eventual tool targets **non-technical users**: policy analysts,
institutional leaders, NGO directors, civil servants, journalists,
board members, governance consultants, and others who observe or
manage social and economic systems without a background in systems
engineering, product-line engineering, or STPA. Technical
practitioners (systems engineers, safety analysts) are also served,
but are the secondary audience.

This requirement drives the tool's interaction design (see Hard
rules). It does not affect the technical level of this concept
document, which is written for the developer.

## System scope

The skill covers any system in which human actors hold authority over
other human actors, the system has a stated purpose that can be
compared with its actual behaviour, and structural choices shape
outcomes. This includes:

| Domain | Examples |
|---|---|
| Governance | Democracies, ministries, regulatory bodies, city councils, political parties |
| Civil society | Religious institutions, trade unions, NGOs, charities, foundations |
| Economic | Corporations, banks, pension funds, cooperatives, market regulators |
| Education | Universities, school systems, research institutes, accreditation bodies |
| Security | Military organisations, police forces, intelligence services |
| Community | Families, voluntary associations (Vereine), neighbourhood councils |
| Mixed | Public-private partnerships, treaty organisations, multi-stakeholder platforms |

The skill does not apply to purely technical systems without human
authority relationships.

## What the skill does

Given a user who arrives with *either*:

- an institutional system they want to analyse (a ministry, a
  corporation, a religious order, a trade union, a school system), **or**
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
- Note the variation-point bindings that differ from the canonical case.

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
(`knowledge/se-techniques/control-structures/dangerous-patterns.md`):
accountability void, self-sealing process model, proxy metric
replacing goal.

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
least one pattern. Derive the remedy by closing the specific
structural pathway the pattern describes — do not improvise generic
"improve communication" or "add oversight" proposals.

If the system is genuinely novel and its remedies cannot be derived
from pattern-matching, say so explicitly. Do not invent remedies.
Flag the gap for the `knowledge/` maintainer.

### 7. Deliverable

Produce one of two artefact types, chosen with the user:

- **Decision memo** — 1–2 pages, executive audience, no unexplained
  technical notation, structured as: *System | Key finding |
  Structural cause | Recommended remedy | Evidence base | Next step.*
  Template: `reference/memo-template.md`.
- **Analysis report** — full technical record of all seven steps:
  five-level decomposition, control-structure map, UCA table, remedy
  table with evidence citations, traceability matrix. Technical
  notation is used throughout but every term is accompanied by a
  plain-language equivalent. Template: `reference/report-template.md`.

Both templates are in `reference/`. Every claim that draws on a
technique or catalogue entry must cite the `knowledge/` file it came
from.

## Intended files

- `SKILL.md` — the skill manifest and prompt. Must cite paths in
  `../../knowledge/` for every technique and every catalogue entry
  it references.
- `reference/memo-template.md` — decision memo template (no
  unexplained notation).
- `reference/report-template.md` — full analysis report template
  (notation with plain-language equivalents throughout).
- `reference/validation-checklist.md` — decomposition and UCA
  validation checklists for steps 2 and 5.
- `reference/` — any other static reference data the skill needs.
- `examples/` — worked examples covering at least one social system,
  one economic system, and one governance system.
- `scripts/` — any Python or shell helpers the skill invokes.

## Hard rules for this skill

### Content rules
- **Never invent system decompositions as canonical.** Every
  decomposition produced by the skill is a draft for a specific
  problem. If the user's system turns out to be a new family member
  worth cataloguing, the skill should say so and direct the user to
  file it under `knowledge/system-catalogues/`.
- **Never invent techniques.** The skill only uses techniques
  defined in `knowledge/se-techniques/`. If the user's problem
  needs something outside the catalogue, the skill says so
  explicitly rather than improvising.
- **Never invent remedies.** Remedy proposals must derive from the
  documented catalogue or from the three dangerous patterns. If
  neither applies, flag the gap rather than generalise.
- **Always cite by reading, not by memory.** Every claim the skill
  makes about a technique or catalogue entry must cite a file under
  `knowledge/`. The skill must read that file during the session
  before using its content — citation without reading is not
  verification.
- **State when back-revision is needed.** If a finding in a later
  step invalidates output from an earlier step, the skill must say
  so explicitly and prompt the user to revise the earlier output
  before continuing.
- **No virtue remedies.** Every proposed remedy must be structural:
  it changes authority, information flow, or incentive structure.
  Remedies that depend on goodwill, culture change, or better
  leadership are not structural and must not be presented as
  solutions.

### User-interaction rules (non-technical audience)
- **Explain every technical term on first use.** STPA, UCA, hazard,
  variation point, traceability, control action, process model, and
  all other domain terms must be defined in plain language the first
  time they appear in a session. A user with no systems engineering
  background must be able to follow the full procedure without prior
  study.
- **Lead with the question, not the technique.** At each step, the
  skill first asks the user a plain-language question ("Who and what
  are we talking about?") before introducing the underlying
  technique. The technique is in service of the question, not the
  reverse.
- **Use social and economic examples by default.** When illustrating
  a technique, default to examples from governance, civil society,
  or economic systems — not from aerospace, nuclear, or other
  engineering domains where STPA originated. Technical-domain
  examples are available in `knowledge/se-techniques/` for users
  who want them.
- **Never produce notation-only output.** Every table, diagram, or
  list using technical notation (UCA table, traceability matrix,
  variation-point binding table) must be accompanied by a
  plain-language summary of what it means and why it matters.

## Relation to `problems/`

Running the skill on a real stakeholder problem produces artefacts
that belong in `../problems/<problem-name>/`. The skill is the
procedure; the problems folder is the record. Artefacts filed should
follow the report template so they are structurally consistent and
reusable across cases.
