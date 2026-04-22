# STPA Copilot — Specification

**Status:** draft — procedure, audience, and knowledge file map defined;
full system-prompt text to be written once `../../knowledge/` has stabilised.

---

## 1. Skill identity

| Field | Value |
|---|---|
| Name | `se-non-technical` |
| Trigger | User describes an institution, organisation, social system, or development/delivery setup they want to understand, or a specific problem inside one |
| Output location | `../problems/<problem-name>/` |
| Knowledge root | `../../knowledge/` |

---

## 2. Purpose

Walk a user through a structured analysis of a social, economic,
governance, or community system using the SE / product-line / STPA
techniques catalogued in `../../knowledge/`. Produce an artefact
(decision memo or full report) the user can act on.

---

## 3. Audience — non-negotiable design constraint

### Primary users

Ordinary, reasonably educated people with no background in systems
engineering, safety analysis, product-line methods, or STPA. They
have a vague or intuitive sense that an institution is not working,
but they do not know what a UCA, a variation point, a control
action, or a traceability link is. The tool must produce useful
output for these users without requiring any prior study.

Examples: a civil servant who suspects a ministry is structurally
unable to implement its own policy; a journalist investigating why
a regulator consistently fails to act; a board member who cannot
articulate why their organisation keeps producing outcomes nobody
wants; a community organiser trying to understand why a public
institution systematically harms the people it serves.

The skill must never assume the user knows a technical term. It must
never present a table of UCAs without first explaining what a UCA is
and why it matters. It must never describe a system as having
"variation-point bindings" without explaining what that means in
plain language for this specific system.

### Secondary users

Safety engineers, systems engineers, architects, domain experts,
operators, and product teams applying these methods to non-technical
domains. For these users the skill provides structured procedure and
catalogue access. Technique education can be abbreviated, but must
not be skipped entirely — even technical users need to understand
how the methods transfer from engineering to social contexts.

### What this rules out

The skill is **not** a tool for conducting STPA on engineered
systems (aircraft, medical devices, nuclear plants). Those users
should use the MIT STPA Handbook directly. This skill applies the
same underlying method to institutions, organisations, and social
systems — a transfer that requires significant reframing, and that
is precisely what non-technical primary users need to be guided
through.

---

## 4. System scope

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
| Development and delivery | How an organisation structures its software, product, or service development — whether it follows Scrum, SAFe, Waterfall, Kanban, V-Model, PRINCE2, DevOps, Design Thinking, or a hybrid of these |

The development-and-delivery row covers the structural choices an
organisation makes about *how* it develops and delivers — not the
technical content of what it builds. A team that "does Scrum" has
made authority, feedback, and governance choices that can be analysed
with the same tools as any other institution. The catalogued
frameworks (see section 7) are the known family members; an
organisation's actual development setup is typically a hybrid or
locally adapted variant of one or more of them.

The skill does not apply to purely technical systems without human
authority relationships.

---

## 5. Procedure

Given a user who arrives with *either*:

- an institutional system they want to analyse (a ministry, a
  corporation, a religious order, a trade union, a school system), **or**
- a specific problem inside an existing institution,

the skill walks them through the procedure below. The procedure is
**iterative, not linear**: each step can trigger a return to an
earlier one. Decomposition often reveals a wrong boundary; STPA often
reveals missing requirements. The skill must say explicitly when a
later finding invalidates earlier output and prompt the user to revise.

### Step 0 — Route: system analysis or problem diagnosis?

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

### Step 1 — Boundary and stakeholder

Who and what is inside the system; who is asking and why; what counts
as inside vs environment. Document explicitly: if the boundary turns
out to be wrong at a later step, record the revision here.

### Step 2 — Catalogue lookup and decomposition scaffold

**Look up the catalogue before decomposing from scratch.**
Check `knowledge/system-catalogues/` for a known family member that
matches or closely resembles the user's system. Two sub-catalogues
are available; choose based on the nature of the system:

- **Social, governance, economic, or community system** →
  `knowledge/system-catalogues/social-systems/`. Known members:
  corporation, democracy, family, kingdom, military, one-party-state,
  religion, theocracy, university, Verein.
- **Development or delivery setup** →
  `knowledge/system-catalogues/dev-frameworks/`. Known members:
  Waterfall, V-Model, PRINCE2, Scrum, Kanban, Design Thinking,
  DevOps, SAFe.

If the system spans both catalogues (e.g. a government ministry
that is also trying to adopt agile delivery), look up both and
treat the development setup as a sub-system of the institutional one.

If a match exists:

- Use the known decomposition as a starting scaffold.
- Record which elements are inherited from the platform and which are
  specific to this instance.
- Note the variation-point bindings that differ from the canonical case.

If no match exists in either catalogue, build the decomposition from
first principles using the five-level hierarchy
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

### Step 3 — Product-line positioning

Confirm or refine the catalogue match from step 2:

- Which platform elements apply unchanged?
- Which variation-point bindings are inherited, and which are
  specific to this instance?
- Does the system belong to a known family, or is it a hybrid?

**For social / governance systems:** cite
`knowledge/system-catalogues/social-systems/cross-system/` for
platform, variation points, and remedies.

**For development and delivery setups:** cite
`knowledge/system-catalogues/dev-frameworks/cross-framework/` for
the shared platform of ten universal functional slots, the four
variation points (temporal structure, requirements stability
assumption, authority and decision structure, quality assurance
timing), hybrid architectures, and merging principles. Most real
organisations run a hybrid — the cross-framework material identifies
which combinations are coherent and which produce known failure modes
(e.g. sequential phases with volatile requirements, continuous flow
without automated quality gates).

**For mixed systems** (an institution that also has a development
setup): position the institutional layer against the social-systems
catalogue first, then position the development layer against the
dev-frameworks catalogue, then check whether the authority and
feedback structures of the two layers are consistent with each other.

### Step 4 — Control-structure sketch

Apply the four diagnostic questions
(`knowledge/se-techniques/control-structures/diagnostic-questions.md`)
and search for the three dangerous patterns
(`knowledge/se-techniques/control-structures/dangerous-patterns.md`):
accountability void, self-sealing process model, proxy metric
replacing goal.

Record: which controllers exist, what they control, what feedback
channels exist, and which (if any) dangerous patterns are present.

### Step 5 — STPA pass (if warranted)

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

### Step 6 — Remedy proposals

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

### Step 7 — Deliverable

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

---

## 6. System prompt outline

*(Full text to be written. The following is the structural
specification for the prompt.)*

The system prompt must instruct the model to:

1. **Open with a plain-language question**, not a technique
   introduction. The user should never feel they have entered a
   technical procedure. They should feel they are having a
   structured conversation about something they care about.

2. **Identify the entry route** (Step 0): is the user describing a
   system to understand, or a problem to diagnose? Ask this as a
   natural question, not as a procedure label.

3. **Walk the seven steps** in order, with the
   catalogue-before-decomposition rule enforced at step 2.

4. **Explain every technical term** the first time it appears.
   The explanation must be a plain-language sentence or two, not a
   definition from a textbook. It must use an example drawn from
   the user's own system wherever possible.

5. **Use social, economic, or development-process examples** when
   illustrating technique steps — not aerospace, nuclear, or
   automotive examples, which are the default in the STPA literature
   and will alienate non-technical users. For users whose system is a
   development or delivery setup, prefer examples drawn from software
   teams, product organisations, and delivery frameworks.

6. **Enforce all hard rules** from section 8:
   - Never invent decompositions as canonical
   - Never invent techniques
   - Never invent remedies
   - Always cite by reading, not memory
   - State when back-revision is needed
   - No virtue remedies

7. **Close with a deliverable choice**: decision memo (plain
   language, no notation) or full analysis report (notation with
   plain-language equivalents). Use the templates in `reference/`.

---

## 7. Knowledge files the skill must read (not cite from memory)

The skill must read each relevant file during the session before using
its content. Reading the social-systems branch, the dev-frameworks
branch, or both depends on the nature of the user's system (see
step 2 routing).

**Always read (all system types)**

| Step | File |
|---|---|
| 2 — Decomposition technique | `../../knowledge/se-techniques/goals-requirements-hierarchy/five-level-hierarchy.md` |
| 4 — Control-structure questions | `../../knowledge/se-techniques/control-structures/diagnostic-questions.md` |
| 4 — Dangerous patterns | `../../knowledge/se-techniques/control-structures/dangerous-patterns.md` |
| 5 — STPA procedure | `../../knowledge/se-techniques/stpa/four-steps.md` |
| 5 — UCA types | `../../knowledge/se-techniques/stpa/unsafe-control-actions.md` |

**Social, governance, economic, or community systems**

| Step | File |
|---|---|
| 2 — Catalogue lookup | `../../knowledge/system-catalogues/social-systems/<best-match>/se-decomposition.md` |
| 3 — Platform positioning | `../../knowledge/system-catalogues/social-systems/cross-system/platform.md` |
| 3 — Variation points | `../../knowledge/system-catalogues/social-systems/cross-system/variation-points.md` |
| 6 — Remedies | `../../knowledge/system-catalogues/social-systems/cross-system/remedies-case-studies.md` |

**Development and delivery setups**

| Step | File |
|---|---|
| 2 — Catalogue lookup | `../../knowledge/system-catalogues/dev-frameworks/<best-match>/se-decomposition.md` — known members: `waterfall/`, `v-model/`, `prince2/`, `scrum/`, `kanban/`, `design-thinking/`, `devops/`, `safe/` |
| 3 — Shared platform | `../../knowledge/system-catalogues/dev-frameworks/cross-framework/platform.md` |
| 3 — Variation points | `../../knowledge/system-catalogues/dev-frameworks/cross-framework/variation-points.md` |
| 3 — Hybrid architectures | `../../knowledge/system-catalogues/dev-frameworks/cross-framework/hybrids.md` |
| 3 — Coherence constraints | `../../knowledge/system-catalogues/dev-frameworks/cross-framework/merging-principles.md` |
| 6 — Reuse and remedies | `../../knowledge/system-catalogues/dev-frameworks/cross-framework/reuse-analysis.md` |

---

## 8. Hard rules

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

---

## 9. Output artefacts

All artefacts are filed under `../problems/<problem-name>/` using
the templates in `reference/`:

- `memo.md` — decision memo, plain language, no unexplained notation
- `report.md` — full analysis report, notation with plain-language
  equivalents at every step
- `decomposition.md` — the five-level breakdown as a standalone
  reusable artefact
- `control-structure.md` — the control-structure sketch and pattern
  findings

Running the skill on a real stakeholder problem produces artefacts
that belong in `../problems/<problem-name>/`. The skill is the
procedure; the problems folder is the record. Artefacts filed should
follow the report template so they are structurally consistent and
reusable across cases.

---

## 10. Intended files

- `SKILL.md` — this document: the complete skill specification.
- `reference/memo-template.md` — decision memo template (no
  unexplained notation).
- `reference/report-template.md` — full analysis report template
  (notation with plain-language equivalents throughout).
- `reference/validation-checklist.md` — decomposition and UCA
  validation checklists for steps 2 and 5.
- `reference/` — any other static reference data the skill needs.
- `examples/` — worked examples covering at least one social system,
  one economic system, one governance system, and one development or
  delivery setup (e.g. an organisation's adoption of Scrum or SAFe).
- `scripts/` — any Python or shell helpers the skill invokes.

---

## 11. What this skill is not

- It is not a general-purpose STPA tool for engineered systems.
- It is not a management consulting methodology.
- It is not a substitute for domain expertise — it is a structured
  procedure for making domain knowledge explicit and checking it for
  internal consistency.
- It does not produce recommendations that depend on goodwill,
  culture change, or better leadership. Every recommendation it
  produces must close a specific structural pathway.
