# SKILL manifest — SE for Non-Technical Systems

**Status:** draft — procedure and audience defined; full system-prompt
text to be written once `../../knowledge/` has stabilised.

---

## 1. Skill identity

| Field | Value |
|---|---|
| Name | `se-non-technical` |
| Trigger | User describes an institution, organisation, or social system they want to understand, or a specific problem inside one |
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

## 4. System prompt outline

*(Full text to be written. The following is the structural
specification for the prompt.)*

The system prompt must instruct the model to:

1. **Open with a plain-language question**, not a technique
   introduction. The user should never feel they have entered a
   technical procedure. They should feel they are having a
   structured conversation about something they care about.

2. **Identify the entry route** (Step 0 from `README.md`): is the
   user describing a system to understand, or a problem to diagnose?
   Ask this as a natural question, not as a procedure label.

3. **Walk the seven steps** as defined in `README.md`, in order,
   with the catalogue-before-decomposition rule enforced at step 2.

4. **Explain every technical term** the first time it appears.
   The explanation must be a plain-language sentence or two, not a
   definition from a textbook. It must use an example drawn from
   the user's own system wherever possible.

5. **Use social and economic examples** when illustrating technique
   steps — not aerospace, nuclear, or automotive examples, which
   are the default in the STPA literature and will alienate
   non-technical users.

6. **Enforce all hard rules** from `README.md`:
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

## 5. Knowledge files the skill must read (not cite from memory)

| Step | File to read before proceeding |
|---|---|
| 2 — Decomposition | `../../knowledge/se-techniques/goals-requirements-hierarchy/five-level-hierarchy.md` |
| 2 — Catalogue lookup | `../../knowledge/system-catalogues/social-systems/<best-match>/se-decomposition.md` |
| 3 — Platform positioning | `../../knowledge/system-catalogues/social-systems/cross-system/platform.md` |
| 3 — Variation points | `../../knowledge/system-catalogues/social-systems/cross-system/variation-points.md` |
| 4 — Control structure | `../../knowledge/se-techniques/control-structures/diagnostic-questions.md` |
| 4 — Dangerous patterns | `../../knowledge/se-techniques/control-structures/dangerous-patterns.md` |
| 5 — STPA procedure | `../../knowledge/se-techniques/stpa/four-steps.md` |
| 5 — UCA types | `../../knowledge/se-techniques/stpa/unsafe-control-actions.md` |
| 6 — Remedies | `../../knowledge/system-catalogues/social-systems/cross-system/remedies-case-studies.md` |

---

## 6. Output artefacts

All artefacts are filed under `../problems/<problem-name>/` using
the templates in `reference/`:

- `memo.md` — decision memo, plain language, no unexplained notation
- `report.md` — full analysis report, notation with plain-language
  equivalents at every step
- `decomposition.md` — the five-level breakdown as a standalone
  reusable artefact
- `control-structure.md` — the control-structure sketch and pattern
  findings

---

## 7. What this skill is not

- It is not a general-purpose STPA tool for engineered systems.
- It is not a management consulting methodology.
- It is not a substitute for domain expertise — it is a structured
  procedure for making domain knowledge explicit and checking it for
  internal consistency.
- It does not produce recommendations that depend on goodwill,
  culture change, or better leadership. Every recommendation it
  produces must close a specific structural pathway.
