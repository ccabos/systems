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

---

## 2. Step 2 — Model the control structure

### 2.1 The four loops

Religion's control structure follows the universal four-level
social-system pattern (see
`../../../se-techniques/control-structures/overview.md`). The four
loops are forced by the SE decomposition's R4 authority requirement
and the candidate-loop justification is in
`projects/systems-introduction-book/docs/part4/religion-stpa.md` §3.2.

| Loop | Controller (SE ID) | Controlled Process | Authority source | Primary control actions |
|------|-------------------|-------------------|------------------|-------------------------|
| 1 | Central Authority (P5, P6) | Clergy (P3) | R4 + claimed divine mandate | Doctrine (F1, F4), canon law (F3), appointment/removal |
| 2 | Clergy (P3) | Congregation (P4) | R4 delegated | Preaching (F1), sacraments (F5), pastoral rules (F2), discipline |
| 3 | Congregation (P4) | Individual | R5, R6 | Social norms, inclusion/exclusion, reputation |
| 4 | Individual (self) | Own behaviour | Internalised R1–R3 | Self-regulation, conscience, confession, prayer |

### 2.2 Per-arrow rung tags

Per the rung extension to STPA Step 2 (see
`../../../se-techniques/justification-rungs/application-to-stpa.md`),
every control action and every feedback channel is tagged with the
rung at which it actually operates.

| Loop | Control action rung | Feedback rung | Loop symmetry |
|------|--------------------|---------------|---------------|
| 1 (Authority → Clergy) | Rung 1 (sacred + institutional authority) | Rung 1 (filial reports from appointees) | Symmetric at rung 1 |
| 2 (Clergy → Congregation) | Rung 1 (pastoral authority, sacrament gatekeeping) | Rung 1 (confession, attendance, donation) | Symmetric at rung 1 |
| 3 (Congregation → Individual) | Rung 1 (social norms, peer pressure) | Rung 1 (gossip, reputation, observed compliance) | Symmetric at rung 1 |
| 4 (Individual self-regulation) | Internalised rung 1 (conscience formed by R1–R3) | Rung 1 (self-examination filtered through doctrine) | Symmetric at rung 1 |

### 2.3 The structural mismatch

The four loops are *internally* rung-symmetric, which is why the
system functions stably for centuries. The catastrophic failure
mode is **external**: rung-3 reality (abuse evidence, scientific
findings, demographic data on harm) is *generated* outside the
hierarchy and tries to enter Loop 1's feedback channel. The
controller's process model has no slot for rung-3 input — it
classifies rung-3 evidence as rung-1 hostility (heresy,
persecution, betrayal) and filters it out.

This is **Pattern A — Asymmetric Loop** from
`../../../se-techniques/justification-rungs/dangerous-mismatches.md`,
combined with **Pattern B — Claimed-Rung Inflation** (the system
claims rung 6 sacralised ultimate legitimacy while operating at
rung 1).

### 2.4 Process models — claimed vs operating rungs

| Controller | Claimed rung | Operating rung | Acceptable feedback rungs |
|------------|--------------|---------------|--------------------------|
| Central Authority | 6 (sacralised ultimate legitimacy) | 1 (clerical authority) | 1 only — rung-3+ feedback rejected as hostile |
| Clergy | 1 (delegated sacred authority) | 1 | 1 (confession, complaints from rung-1 sources only) |
| Congregation | 1 (shared faith, tradition) | 1 | 1 (peer signals; rung-3 outside critique dismissed) |
| Individual | 1 (internalised) | 1 | 1 (doubt classified as temptation) |

The acceptable-feedback-rung column is the structural cause of
most loss scenarios in §4.

---

## 3. Step 3 — Identify unsafe control actions

Standard four-type UCA enumeration plus the three rung-mismatch
modes from `../../../se-techniques/justification-rungs/application-to-stpa.md`.

### 3.1 Loop 1 — Central Authority → Clergy

| ID | Type | UCA | Hazard |
|----|------|-----|--------|
| UCA-1 | Not provided | Authority does NOT update doctrine when scientific evidence invalidates cosmological claims | H1, HX |
| UCA-2 | Not provided | Authority does NOT remove or discipline clergy credibly accused of abuse | H2, H5 |
| UCA-3 | Provided | Authority ISSUES doctrine that dehumanises outsiders (infidels, heretics, apostates) | H3 |
| UCA-4 | Provided | Authority EXCOMMUNICATES or PUNISHES members who raise legitimate doctrinal questions | H1, H4 |
| UCA-5 | Provided | Authority APPOINTS clergy on doctrinal loyalty rather than pastoral competence or moral character | H2, H5 |
| UCA-6 | Too late | Authority CORRECTS a doctrinal error only after centuries of harm (Galileo, 1633→1992) | H1, H6 |
| UCA-7 | Too long | Authority MAINTAINS absolutist moral prohibition long after ethical understanding has evolved | H4 |
| UCA-8 | Not provided | Authority does NOT establish transparent financial auditing | H7 |

### 3.2 Loop 2 — Clergy → Congregation

| ID | Type | UCA | Hazard |
|----|------|-----|--------|
| UCA-9 | Provided | Clergy USES pastoral relationship to sexually, emotionally, or financially exploit | H5 |
| UCA-10 | Provided | Clergy PREACHES hatred or contempt toward out-groups | H3 |
| UCA-11 | Provided | Clergy WITHHOLDS sacraments or pastoral care as punishment for questioning doctrine | H1, H4, H8 |
| UCA-12 | Not provided | Clergy does NOT provide pastoral support during genuine crisis (grief, mental illness, abuse) because the doctrinal frame has no model for the problem | H4 |
| UCA-13 | Provided | Clergy DEMANDS financial contributions through spiritual coercion (prosperity gospel, indulgences, obligatory tithing) | H7 |
| UCA-14 | Too long | Clergy MAINTAINS shunning long after the person has suffered disproportionate social death | H4, L3 |
| UCA-15 | Not provided | Clergy does NOT report abuse to civil authorities, instead handling it "internally" | H2, H5 |

### 3.3 Loop 3 — Congregation → Individual

| ID | Type | UCA | Hazard |
|----|------|-----|--------|
| UCA-16 | Provided | Congregation SHUNS member who expresses doubt, questions doctrine, or leaves the faith | H1, H4, H8 |
| UCA-17 | Provided | Congregation ENFORCES social conformity on matters of personal conscience (dress, diet, relationships, career) | H4, H8 |
| UCA-18 | Not provided | Congregation does NOT intervene when they observe clergy abusing a member | H2, H5 |
| UCA-19 | Provided | Congregation PRESSURES children into public faith commitments before meaningful consent | H8 |
| UCA-20 | Too early | Congregation LABELS children as sinful, damned, or spiritually deficient at developmentally inappropriate age | H4 |

### 3.4 Loop 4 — Individual self-regulation

| ID | Type | UCA | Hazard |
|----|------|-----|--------|
| UCA-21 | Provided | Individual SUPPRESSES doubt, curiosity, or moral intuition because "doubt = sin" is internalised | H1, H6 |
| UCA-22 | Provided | Individual REMAINS in an abusive religious environment because they believe leaving = damnation | H4, H5 |
| UCA-23 | Not provided | Individual does NOT seek professional mental health support; the framework teaches faith should suffice | H4 |
| UCA-24 | Provided | Individual REJECTS medical treatment for self or dependents based on doctrinal prohibition | H4, L1 |
| UCA-25 | Too long | Individual CONTINUES religious practices that cause measurable psychological harm beyond any devotional purpose | H4 |

### 3.5 Rung-mismatch UCAs (cross-loop)

These cut across Loops 1–4 and are not captured by the four
standard UCA types. See
`../../../se-techniques/justification-rungs/application-to-stpa.md`.

| ID | Mode | UCA | Hazard |
|----|------|-----|--------|
| UCA-R1 | Over-rung command | Authority issues doctrinal commands at rung 1 (sacred authority) to a population now operating at rung 3 (empirical, evidence-based reasoning) — commands fail silently as believers privately disregard them while remaining nominally observant | HX, H1 |
| UCA-R2 | Under-rung command | Authority issues a rung-1 statement on a question the audience expects to be answered at rung 3 (medical, scientific, factual) — provokes active rejection and erodes legitimacy | HX, L5 |
| UCA-R3 | Asymmetric loop | Authority issues commands at rung 1 and *expects* feedback at rung 1 (clerical reports), but the corrective signal that exists (rung-3 abuse data, scientific evidence, demographic harm) cannot enter the controller's process model — the loop is open by design | HX, H1, H2, H5 |

UCA-R3 is the **dominant** UCA in this system. It generates most
of the loss scenarios in §4 not by being a single failure but by
being structurally embedded in every Loop-1 cycle.
