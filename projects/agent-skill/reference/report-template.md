# Analysis Report Template

> **How to use.** Replace every italic placeholder with content for
> the user's case. The report is the technical record of the full
> eight-step procedure: decomposition, control-structure map, rung
> tagging, STPA pass, remedies, and traceability. Use technical
> notation freely **but always with a plain-language equivalent**
> alongside (no notation-only output). Cite the `reference/...`
> file behind every technique step and every catalogue claim.

---

# Analysis Report — *<short, concrete title naming the system>*

**Prepared for:** *<stakeholder role>*
**Prepared by:** *<your name or role>*
**Date:** *<month and year>*
**Procedure:** STPA Copilot eight-step procedure (`SKILL.md`).
**Companion artefact:** `memo.md` *(short executive form of this report).*

---

## 0. Entry route

*Was this a system analysis (top-down: understand an institution
from scratch) or a problem diagnosis (bottom-up: investigate a
specific failure)? One paragraph stating the route and which
sections were emphasised because of it.*

---

## 1. Boundary and stakeholder

*Who and what is inside the system; who is outside; who is asking
this question and why. Note any boundary revisions made later in
the analysis and explain what triggered them.*

| Element | Inside | Outside |
|---------|--------|---------|
| Actors | *…* | *…* |
| Artefacts | *…* | *…* |
| Information flows | *…* | *…* |

---

## 2. Catalogue lookup and SE decomposition

### 2.1 Catalogue match

*Which family in `reference/system-catalogues/` does this system
match? Cite the matching `se-decomposition.md`. If no match,
explain what is novel and flag the candidate new family member.*

### 2.2 Five-level decomposition

*Plain-language sentence introducing the levels: goals, requirements,
functions, logical architecture, physical implementation. Cite
`reference/se-techniques/goals-requirements-hierarchy/five-level-hierarchy.md`.*

**Goals (G).**

- **G1** — *…*
- **G2** — *…*

**Requirements (R).**

- **R1** — *…*
- **R2** — *…*

**Functions (F).**

- **F1** — *…*
- **F2** — *…*

**Logical Architecture (L).**

- **L1** — *…*
- **L2** — *…*

**Physical Implementation (P).**

- **P1** — *…*
- **P2** — *…*

### 2.3 Validation

*Brief statement that the four validation checks have been run:
goals are outcomes (not solutions); requirements are necessary
and sufficient; every function traces to a requirement;
traceability links are consistent. List any gaps the user
explicitly accepted.*

---

## 3. Product-line positioning

| Aspect | Value |
|--------|-------|
| Catalogue family | *known family member name* |
| Inherited platform elements | *…* |
| Variation-point bindings | *…* |
| Hybrid? | *yes/no, with which families* |

*One paragraph in plain language explaining what this positioning
means: which structural choices are inherited from a known family,
which are specific to this instance. Cite the relevant
`reference/system-catalogues/<branch>/cross-*/platform.md` and
`variation-points.md`.*

---

## 4. Control-structure sketch

*Diagram or text rendering of controllers, controlled processes,
control actions (downward), feedback channels (upward), and process
models. The diagram must be accompanied by a plain-language
summary.*

### 4.1 The five diagnostic questions

*Cite `reference/se-techniques/control-structures/diagnostic-questions.md`.*

| Question | Answer |
|----------|--------|
| 1. Feedback richness | *…* |
| 2. Self-sealing tendency | *…* |
| 3. Accountability voids | *…* |
| 4. Circuit breakers | *…* |
| 5. Rung match *(social systems)* | *…* |

### 4.2 Dangerous patterns present

*Cite `reference/se-techniques/control-structures/dangerous-patterns.md`.*

- *Accountability Void — yes/no, with evidence*
- *Self-Sealing Process Model — yes/no, with evidence*
- *Proxy Metric Replacing Goal — yes/no, with evidence*
- *Rung Asymmetry (social systems) — yes/no, with evidence*

---

## 5. Justificatory-rung tagging *(social systems only)*

*If engineered system: write "Not applicable: every loop in this
system operates at rung 3-4 throughout; rung tagging adds no
information." and skip to §6.*

*Cite `reference/se-techniques/justification-rungs/rungs.md` and
`reference/se-techniques/justification-rungs/dangerous-mismatches.md`.*

### 5.1 Per-arrow rung tags

| Loop | Control action rung | Feedback rung | Loop symmetry |
|------|--------------------|---------------|---------------|
| *…* | *…* | *…* | *…* |

### 5.2 Per-controller rung profile

| Controller | Claimed rung | Operating rung | Acceptable feedback rungs |
|------------|--------------|---------------|--------------------------|
| *…* | *…* | *…* | *…* |

### 5.3 Mismatch patterns present

- *Pattern A — Asymmetric Loop — yes/no, with evidence*
- *Pattern B — Claimed-Rung Inflation — yes/no, with evidence*
- *Pattern C — Cross-Loop Rung Imposition — yes/no, with evidence*

---

## 6. STPA pass

*If STPA is not warranted (no harmful-outcome potential, no
identifiable authority relationships, no feedback channels), state
that explicitly and skip to §7. Otherwise cite
`reference/se-techniques/stpa/four-steps.md`.*

### 6.1 Step 1 — Losses, hazards, constraints

| ID | Loss | Negates goal |
|----|------|--------------|
| L1 | *…* | G1 |

| ID | Hazard | Related losses |
|----|--------|----------------|
| H1 | *…* | L1 |

| ID | Constraint | Prevents hazard |
|----|-----------|-----------------|
| SC1 | *…* | H1 |

### 6.2 Step 2 — Control structure

*Reference §4 above; do not duplicate the diagram. State any
refinements made during the STPA pass.*

### 6.3 Step 3 — Unsafe Control Actions

*Cite `reference/se-techniques/stpa/unsafe-control-actions.md`.*

| ID | Type | UCA | Hazard |
|----|------|-----|--------|
| UCA-1 | not provided / provided / timing / duration | *…* | H1 |

*Plus, for social systems, the three rung-mismatch UCA modes:*

| ID | Mode | UCA | Hazard |
|----|------|-----|--------|
| UCA-R1 | over-rung command | *…* | *…* |
| UCA-R2 | under-rung command | *…* | *…* |
| UCA-R3 | asymmetric loop | *…* | *…* |

### 6.4 Step 4 — Loss scenarios

*One sub-block per UCA, listing causal factors. Standard categories
(flawed process model, missing feedback, faulty actuator, unexpected
process state, external disturbance) plus the rung-acceptance
filter for social systems.*

**LS-1 — *<short scenario name>* — UCA-1 → H1 → L1**

| Causal factor | Mechanism |
|---------------|-----------|
| *…* | *…* |

### 6.5 Validation

*Brief statement that every UCA has been traced to a structural
causal factor (not merely human error or bad intentions).*

---

## 7. Remedy proposals

*Cite the `remedies-case-studies.md` file behind every recommended
remedy. Each remedy must close a specific structural pathway —
no virtue remedies (no "improve communication," "add training,"
"better leadership").*

| ID | Remedy | Closes UCA | Pattern type | Evidence base |
|----|--------|------------|--------------|---------------|
| Rx1 | *…* | UCA-1 | accountability void / self-sealing / proxy / rung asymmetry | *cited reference/ file* |

*For social systems with rung-mismatch UCAs, identify which remedies
are rung-elevation moves (parallel rung-3 channel routed around the
rung-1 hierarchy). Cite the §6 rung-elevation table in
`reference/system-catalogues/social-systems/cross-system/remedies-case-studies.md`.*

*If any UCA could not be matched to a catalogued remedy or pattern,
flag it explicitly here as a known gap rather than inventing a fix.*

---

## 8. Traceability matrix

| Goal | Requirement | Function | Loss | Hazard | UCA | Remedy |
|------|-------------|----------|------|--------|-----|--------|
| G1 | R1 | F1 | L1 | H1 | UCA-1 | Rx1 |

*Each row demonstrates that a goal is connected through requirement,
function, loss, hazard, and UCA to a specific remedy. Empty cells
indicate a structural break in the chain — flag those explicitly.*

---

## 9. Open questions and known gaps

- *Anything the analysis could not settle within the catalogued
  techniques and remedies.*
- *Any place the system is genuinely novel and may warrant a new
  catalogue entry under `knowledge/system-catalogues/`.*
- *Any back-revision pending: a finding in a later step that
  invalidates an earlier step's output, with the user's decision
  to defer the revision recorded.*

---

## 10. Citation summary

*Flat list of every `reference/...` file actually cited above,
grouped:*

**Techniques.**
- `reference/se-techniques/goals-requirements-hierarchy/five-level-hierarchy.md`
- `reference/se-techniques/control-structures/diagnostic-questions.md`
- `reference/se-techniques/control-structures/dangerous-patterns.md`
- `reference/se-techniques/justification-rungs/rungs.md`
- `reference/se-techniques/justification-rungs/dangerous-mismatches.md`
- `reference/se-techniques/stpa/four-steps.md`
- `reference/se-techniques/stpa/unsafe-control-actions.md`

**Catalogue.**
- `reference/system-catalogues/<branch>/<best-match>/se-decomposition.md`
- `reference/system-catalogues/<branch>/cross-*/platform.md`
- `reference/system-catalogues/<branch>/cross-*/variation-points.md`
- `reference/system-catalogues/<branch>/cross-*/remedies-case-studies.md`
- *(For social systems:)* `reference/system-catalogues/social-systems/cross-system/justification-rungs-by-system.md`
- *(For dev frameworks:)* `reference/system-catalogues/dev-frameworks/cross-framework/hybrids.md`, `merging-principles.md`, `reuse-analysis.md`

*Drop entries that were not actually cited; do not pad the list.*
