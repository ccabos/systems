# Agent Skill — Structural Analysis for Social, Economic, and Institutional Systems

A Claude Agent skill that helps a user understand why an institution,
organisation, or social system behaves the way it does — and what
would have to change for it to behave differently.

The skill applies structured analysis techniques drawn from
`../../knowledge/`. It does not require the user to know any of those
techniques in advance. The skill explains what it is doing and why
at every step, in plain language, before using any technical notation.

## Status

**Scaffold only.** This folder contains the skill's intended shape
and the interface contract. The actual `SKILL.md` and supporting
scripts will be written after the knowledge base has stabilised.

## Who this is for

### Primary users — non-technical practitioners

The skill is designed first for people who observe, manage, or are
affected by social, economic, or governance systems and have noticed
something is wrong — but do not have a technical background in
systems engineering or safety analysis. This includes:

- Policy analysts and civil servants diagnosing why a programme
  keeps failing despite repeated reform attempts
- Institutional leaders (directors, rectors, generals, bishops,
  executives) trying to understand structural dysfunctions they
  inherited
- NGO directors, community organisers, and social entrepreneurs
  analysing why an institution systematically produces outcomes
  opposite to its stated mission
- Journalists, researchers, and educators studying how social
  systems work and why they fail
- Legal professionals, governance consultants, and auditors
  assessing whether an institution's structure can produce the
  accountability it claims to provide
- Board members, trustees, and supervisory bodies evaluating
  whether control mechanisms are real or cosmetic

**No prior knowledge is required.** The skill will not assume
familiarity with systems engineering, product-line engineering, STPA,
or any other technique. Every term is explained in plain language
when it is first used. Notation and jargon are tools for precision,
not barriers to entry.

### Secondary users — technical practitioners

Systems engineers, safety analysts, organisational researchers, and
others who already know SE or STPA techniques and want to apply them
to social, economic, or governance domains — rather than to
engineered artefacts — are also well served by this skill. For these
users, the skill provides a structured procedure and a catalogue of
known systems, rather than technique explanation.

### System scope

The skill covers any system in which:

- Human actors hold authority over other human actors
- The system has a stated purpose that can be compared with its
  actual behaviour
- Structural choices (who answers to whom, who decides what, what
  information flows where) shape outcomes

This includes — but is not limited to:

| Domain | Examples |
|---|---|
| Governance | Democracies, ministries, city councils, regulatory bodies, political parties |
| Civil society | Religious institutions, trade unions, NGOs, charities, foundations |
| Economic | Corporations, banks, pension funds, cooperatives, market regulators |
| Education | Universities, school systems, research institutes, accreditation bodies |
| Security | Military organisations, police forces, intelligence services |
| Community | Families, voluntary associations (Vereine), neighbourhood councils |
| Mixed | Public-private partnerships, treaty organisations, multi-stakeholder platforms |

The skill does not apply to purely technical systems with no human
authority relationships (e.g. a software algorithm, a mechanical
device). For those, standard systems engineering without this skill
is more appropriate.

---

## What the skill does

Given a user who arrives with *either*:

- a system they want to understand (a ministry, a corporation, a
  religious order, a trade union, a school system), **or**
- a specific problem inside an existing institution (repeated
  policy failure, systematic abuse, governance collapse, captured
  regulator),

the skill walks them through the procedure below. The procedure is
**iterative, not linear**: each step can trigger a return to an
earlier one. What is found in a later step often reveals that an
assumption made in an earlier step was wrong. The skill must say so
explicitly and prompt the user to revise, rather than silently
continuing with an invalidated foundation.

---

## Step 0 — What kind of question is this?

Before anything else, the skill determines which of two strategies
applies:

- **Understand a system** — the user wants to understand how an
  institution is structured and why it behaves as it does. Proceed
  top-down: start from what the system exists to achieve, work down
  through what it must do, how it is organised, and what could go
  wrong.

- **Diagnose a problem** — the user has a specific failure or harm
  already in view. Proceed bottom-up: start from the observed
  outcome, identify which of the system's own rules or authority
  relationships produced it, and work upward to find the structural
  root cause.

The two paths join at step 4. Steps 1–3 differ in emphasis and depth
depending on the route chosen.

---

## Steps

### 1. Boundary and stakeholders

*Plain language: Who and what are we talking about?*

Establish:

- What is inside this system and what is outside it (environment)?
- Who has authority within it, and who is affected by it from
  outside?
- Who is asking this question and why — what decision or action
  will the analysis inform?

The boundary is a working assumption, not a fact. Record it
explicitly. If a later step reveals it is wrong, revise it here.

---

### 2. What the system is supposed to do — and how it actually works

*Plain language: What is this system for, and how is it organised?*

The skill builds a structured picture of the system across five
layers. Each layer is explained to the user before being filled in:

| Layer | Plain language | Technical name |
|---|---|---|
| 1 — Purpose | What outcomes does this system exist to produce? What would count as success? | Goals |
| 2 — Obligations | What must the system do (and not do) in order to achieve those outcomes? | Requirements |
| 3 — Activities | What does the system actually do — what are its core activities and processes? | Functions |
| 4 — Organisation | How are those activities allocated — which roles, units, or bodies carry out which functions? | Logical architecture |
| 5 — People and assets | Who and what physically carries out the work — specific offices, people, buildings, infrastructure? | Physical implementation |

Each layer traces to the one above: every activity must connect to
an obligation, every obligation to a purpose. Gaps and
contradictions in those connections are findings, not problems to
skip.

**Before the catalogue:** The skill first checks
`knowledge/system-catalogues/` for a known system of the same type.
If a democracy, a corporation, a university, a military, a religious
institution, a family, a voluntary association, or another catalogued
type is a close match, it serves as a starting scaffold — saving the
user from building from scratch and surfacing known patterns
immediately.

**Validation pass (mandatory before proceeding).**
Before moving to step 3, the skill checks:

- Are all stated purposes genuinely the system's purposes — or are
  some of them actually disguised instructions about how to operate?
- Do the obligations follow from the purposes — or are some of them
  inherited from a previous era and no longer connected to anything?
- Does every activity connect to at least one obligation?
- Are there any activities that connect to nothing, or obligations
  that no activity fulfils?

These are not rhetorical questions. Gaps here are the structural
source of many institutional failures. Record them. Do not proceed
until each gap is either resolved or explicitly acknowledged.

---

### 3. Where does this system fit — and what does that tell us?

*Plain language: Is this a known type of institution? What do we
already know about institutions like this?*

The catalogue
(`knowledge/system-catalogues/`) contains detailed structural
analyses of ten social systems and eight development frameworks.
If the user's system belongs to a known type — or is a variant or
hybrid — the skill:

- Identifies which structural features are typical for this type
  and which are specific to this instance
- Surfaces the known failure modes and control-structure pathologies
  documented for this family
- Notes where this instance deviates from the standard pattern and
  whether the deviation creates or reduces risk

For technical users: this is the product-line positioning step
(variation-point bindings against the platform defined in
`knowledge/system-catalogues/*/cross-*/`).

If the system is genuinely novel, the skill says so, builds the
analysis from first principles, and flags that a new catalogue entry
may be warranted.

---

### 4. Who controls whom — and does the control actually work?

*Plain language: Who tells whom what to do? Does information flow
back to the people making decisions? And where does the structure
break down?*

The skill maps the system's authority relationships: who can direct
whose behaviour, what instructions they can issue, and what
information is supposed to flow back to inform the next decision.

It then applies four diagnostic questions (from
`knowledge/se-techniques/control-structures/diagnostic-questions.md`):

1. Does the controller have an accurate model of what the controlled
   process is actually doing?
2. Do the control actions reach the process and have the intended
   effect?
3. Does feedback actually travel back to the controller — or is it
   filtered, delayed, or suppressed?
4. Does the controller have the authority and capacity to act on
   what the feedback tells them?

The skill then checks for three structural failure patterns
(`knowledge/se-techniques/control-structures/dangerous-patterns.md`):

- **Accountability void** — the body that should be held
  responsible for an outcome is the same body that controls whether
  accountability is applied
- **Self-sealing process model** — the decision-maker's picture of
  reality cannot be corrected by information from the people doing
  the actual work
- **Proxy metric replacing goal** — the institution is optimising
  for a measurable proxy (publication count, quarterly profit, voter
  approval rating) rather than the actual outcome it exists to
  produce

These patterns appear in democracies, corporations, religious
institutions, universities, and militaries alike. Finding them is
not a criticism of the people involved — it is a finding about the
structure.

---

### 5. Harm analysis (if the question involves harmful outcomes)

*Plain language: Can this system's own rules and authority
relationships produce serious harm — and if so, how?*

This step applies when:

1. The user's concern involves potential for serious harm (not
   just inefficiency or poor performance): abuse, corruption,
   financial ruin, political repression, public health damage,
   injustice
2. The system has clear authority relationships — some actors can
   issue instructions that others are structurally obligated to
   follow
3. Information flows (or fails to flow) between those doing the
   work and those making the decisions

If all three conditions hold, the skill works through four questions
drawn from the STPA method (System-Theoretic Process Analysis —
`knowledge/se-techniques/stpa/four-steps.md`). The method is
explained in plain terms as the skill applies it:

| Step | Plain language | Technical term |
|---|---|---|
| 1 — Losses | What are the worst outcomes this system must never produce? (Death, systematic abuse, institutional collapse, large-scale injustice) | Losses |
| 2 — Dangerous states | In what situations is the system in a state where those outcomes become likely — regardless of what happens next? | Hazards |
| 3 — Harmful instructions | In what situations does the system's own authority structure issue instructions — or fail to issue them — in a way that moves the system toward those dangerous states? | Unsafe Control Actions (UCAs) |
| 4 — How it happens | What specific combination of structural factors causes those harmful instructions to be issued? | Causal scenarios |

*For users unfamiliar with STPA:* the key insight is that harmful
outcomes in well-organised institutions usually do not result from
rogue individuals acting against the system — they result from the
system's own authority structure operating as designed. The analysis
looks for the structural conditions that make harm a predictable
consequence, not an accident.

**Validation pass after step 3 (harmful instructions).** Each
harmful instruction identified must trace to a specific structural
cause — a gap in feedback, a conflict of interest built into the
authority hierarchy, an absent check. "Human error" and "bad
intentions" are not structural causes. If an analysis cannot find a
structural cause, the harmful instruction has not been properly
characterised.

---

### 6. What would have to change?

*Plain language: What structural changes — not exhortations — would
close the pathways to harm?*

Remedies are drawn from
`knowledge/system-catalogues/*/cross-*/remedies-case-studies.md`.
The catalogue documents interventions that have been implemented in
practice and whose effects have been observed — constitutional court
structures, mandatory reporting laws, co-determination
requirements, pre-registration of research, independent military
inspection, audit independence rules.

**For systems that match a known catalogue entry:** specific
documented remedies are used, adapted to the instance.

**For novel systems or unmatched harmful instructions:** the skill
falls back to the three structural patterns. Each harmful instruction
must map to at least one pattern. The remedy closes the specific
structural pathway — it does not add generic "better governance" or
"more oversight." What body needs to be separated from what other
body? What information path needs to be opened or closed? What
decision needs to move from whom to whom?

If the system is genuinely novel and no remedy can be derived from
pattern-matching, the skill says so. It does not invent remedies.

**The skill does not ask people to be more virtuous.** Remedies that
depend on good intentions are not structural remedies. A remedy is
structural when it changes the cost, authority, or information
structure — so that the incentive points in a different direction
regardless of who holds the role.

---

### 7. Deliverable

*Plain language: What does the user walk away with?*

Produce one of two artefact types, chosen with the user based on
their audience:

- **Briefing note / decision memo** — 1–2 pages for a senior
  audience (board, minister, director), written in plain language
  with no technical notation. Sections: *What this system is for |
  What the analysis found | The structural cause | What would need
  to change | Evidence from comparable cases | Recommended next
  step.* Template: `reference/memo-template.md`.

- **Full analysis report** — complete structured record of all
  seven steps, including the five-layer breakdown, authority-
  structure map, harmful-instruction table (with plain-language
  descriptions alongside any technical notation), remedy table with
  evidence citations, and traceability. For governance reviews,
  research, or institutional reform processes. Template:
  `reference/report-template.md`.

Both templates are in `reference/`. Technical notation (STPA terms,
SE hierarchy labels) is included in the full report but always
accompanied by plain-language equivalents. The briefing note
contains no unexplained jargon.

---

## Intended files

- `SKILL.md` — the skill manifest and prompt. Must cite paths in
  `../../knowledge/` for every technique and every catalogue entry
  it references.
- `reference/memo-template.md` — briefing note / decision memo
  template (plain language, no notation).
- `reference/report-template.md` — full analysis report template
  (notation with plain-language equivalents throughout).
- `reference/validation-checklist.md` — decomposition and harmful-
  instruction validation checklists for steps 2 and 5.
- `reference/` — any other static reference data the skill needs.
- `examples/` — worked examples for a few canonical cases, covering
  at least one social system, one economic system, and one
  governance system.
- `scripts/` — any Python or shell helpers the skill invokes.

---

## Hard rules for this skill

- **Explain before using.** Every technical term (STPA, UCA, hazard,
  variation point, traceability, and all others) must be explained
  in plain language the first time it appears in a session. A user
  who has never heard of systems engineering must be able to follow
  the entire analysis without prior study.
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
  makes about a technique or a catalogue entry must cite a file
  under `knowledge/`. The skill must read that file during the
  session before using its content — citation without reading is not
  verification.
- **State when back-revision is needed.** If a finding in a later
  step invalidates output from an earlier step, the skill must say
  so explicitly and prompt the user to revise the earlier output
  before continuing.
- **Do not ask people to be more virtuous.** Every proposed remedy
  must be structural: it changes authority, information flow, or
  incentive structure. Remedies that depend on goodwill, culture
  change, or better leadership are not structural and must not be
  presented as solutions.

---

## Relation to `problems/`

Running the skill on a real stakeholder problem produces artefacts
that belong in `../problems/<problem-name>/`. The skill is the
procedure; the problems folder is the record. Artefacts filed should
follow the report template so they are structurally consistent and
reusable across cases.
