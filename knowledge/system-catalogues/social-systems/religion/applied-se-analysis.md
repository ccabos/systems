# Religion — Applied SE Analysis (STPA + Justificatory Rungs)

Canonical STPA analysis of religion as a social system. Integrates
the **justificatory-rung** dimension throughout (see
`../../../se-techniques/justification-rungs/`).

The narrative version is in
`projects/systems-introduction-book/docs/part4/religion-stpa.md`;
this file is the structured reference.

## 0. Inputs

- SE decomposition: `se-decomposition.md` (this folder)
- STPA technique: `../../../se-techniques/stpa/`
- Control-structure technique: `../../../se-techniques/control-structures/`
- Justificatory rungs technique: `../../../se-techniques/justification-rungs/`
- Religion's row in cross-system control-structure profile:
  `../cross-system/control-structure-profiles.md` (Religion §)
- Religion's row in cross-system rung comparison:
  `../cross-system/justification-rungs-by-system.md`
- Religion's remedies: `../cross-system/remedies-case-studies.md` §3

## Sections to follow

1. Step 1 — Define purpose (losses, hazards, constraints)
2. Step 2 — Model the control structure (loops + rung tags)
3. Step 3 — Identify unsafe control actions (4 types + 3 rung-mismatch modes)
4. Step 4 — Identify loss scenarios (causal factors with rung filter)
5. Cross-cutting structural findings
6. Why rung mismatch is the dominant structural driver
7. Pointers to remedies

---

## 1. Step 1 — Define purpose

### 1.1 Losses

Each loss is the negation of a system goal from `se-decomposition.md`.
LX is added to capture rung-related legitimacy loss, which the
standard goal set does not surface explicitly.

| ID | Loss | Negates |
|----|------|---------|
| L1 | Individuals suffer existential despair, alienation, or loss of meaning *because of* the religious system | G1 |
| L2 | The system produces, enables, or conceals immoral behaviour (abuse, violence, corruption, exploitation) | G2 |
| L3 | Social destruction — division, persecution, hatred, or war between groups | G3 |
| L4 | Psychological damage — trauma, guilt, fear, or mental illness inflicted on individuals | G4 |
| L5 | Loss of institutional legitimacy — trust and authority needed to function are forfeited | All |
| L6 | Suppression of truth — scientific knowledge, critical thinking, or individual conscience is suppressed | G1, G2 |
| **LX** | **Rung-claim collapse** — the gap between the system's claimed justificatory rung (sacred / ultimate legitimacy) and its operating rung (clerical authority) becomes empirically visible to participants, accelerating L5 | All |

Each loss is the *negation* of a goal — the defining feature of
STPA applied to social systems. Hazards are not external threats
but self-inflicted contradictions where the system's own control
actions produce outcomes opposite to its stated purpose.

### 1.2 Hazards

| ID | Hazard | Losses |
|----|--------|--------|
| H1 | Doctrine becomes unfalsifiable and self-sealing — no internal mechanism can correct doctrinal errors | L1, L2, L6 |
| H2 | Authority structure becomes unaccountable — no effective oversight of those who interpret and enforce norms | L2, L4, L5 |
| H3 | In-group/out-group mechanism escalates to dehumanisation of outsiders | L3 |
| H4 | Moral legislation becomes absolutist — no allowance for context, conscience, or evolving understanding | L1, L2, L4 |
| H5 | Pastoral care relationship is exploited — power asymmetry enables abuse | L2, L4, L5 |
| H6 | Missionary function prioritises expansion over welfare of converts or target populations | L2, L3 |
| H7 | Financial resources are extracted from vulnerable populations without accountability | L2, L5 |
| H8 | Ritual performance becomes coercive — participation is compelled, not voluntary | L1, L4 |
| **HX** | **Operating-rung mismatch** — the system claims rung 6 (sacralised ultimate legitimacy) but operates at rung 1 (clerical authority); rung-3 corrective feedback (empirical reality of abuse, science, institutional performance) cannot enter the apex's process model | L1, L2, L5, L6, LX |

### 1.3 System-level constraints

Each hazard implies a constraint the system must maintain to prevent it.

| ID | Constraint | Prevents |
|----|-----------|----------|
| SC1 | Doctrine must include mechanisms for self-correction, reinterpretation, and engagement with external knowledge | H1 |
| SC2 | Authority figures must be subject to transparent oversight, accountability, and removal procedures | H2 |
| SC3 | In-group/out-group distinctions must not extend to denial of outsiders' human dignity or rights | H3 |
| SC4 | Moral legislation must preserve space for individual conscience and contextual judgement | H4 |
| SC5 | Pastoral relationships must have safeguards: codes of conduct, mandatory reporting, external recourse | H5 |
| SC6 | Missionary activity must respect the autonomy and existing culture of target populations | H6 |
| SC7 | Financial management must be transparent, audited, and separated from spiritual authority | H7 |
| SC8 | Ritual participation must be voluntary, with no material or social penalty for non-participation | H8 |
| **SCX** | **Rung match.** Either lower the public claim to match operation (rung-1 clerical authority, honestly stated) or insert independent rung-3 feedback channels that route around the rung-1 hierarchy (audit, mandatory reporting, lay safeguarding) | HX |
