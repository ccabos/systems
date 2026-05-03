# STPA first pass: Societal Impact of Frontier AI

_Companion to `problem.md` and `methodology-critique.md`. Applies
the four-step STPA procedure with justification-rung tagging. This
is an **explicit first pass**: Step 1 is complete; Step 2 is
sketched at the logical-architecture level; Steps 3 and 4 are
seeded with representative UCAs and loss scenarios rather than
exhaustively enumerated._

---

## STPA Step 1 — Define Purpose of the Analysis

### 1.1 Losses

Losses are unacceptable outcomes the stakeholders want to avoid,
stated in stakeholder language. The losses here are framed at the
level of the global economic and political system, not at the level
of any single firm or country.

| ID | Loss |
|----|------|
| L1 | **Sustained mass cognitive-worker displacement** — a cohort of cognitive workers (10s to 100s of millions globally) loses earning capacity faster than the economy reabsorbs them, producing a multi-decade unemployment overhang concentrated in early-career and mid-career knowledge workers |
| L2 | **Concentration of economic power into a small number of compute-and-frontier-model providers** — a handful of firms (≤10 globally) become structurally able to set terms for access to the productivity gains of AI, with no effective competitive or regulatory check |
| L3 | **Concentration of political power into the same firms or their state patrons** — control over the AI substrate translates into agenda-setting power over media, elections, regulation, and policy, eroding pluralistic governance |
| L4 | **Loss of the open-weights commoditisation pressure valve** — the open-weights ecosystem fails (regulatory suppression, capability stagnation, geopolitical bifurcation) and the model layer concentrates as much as the infrastructure layer |
| L5 | **Loss of broad welfare gains from AI-driven productivity** — the productivity surplus is captured almost entirely by capital and a small labour elite, with consumers and median labour seeing little benefit |
| L6 | **Geopolitical conflict triggered by AI-infrastructure competition** — physical conflict (kinetic, cyber, sanctions-and-counter-sanctions escalation) over chips, fabs, talent, or model access |
| L7 | **Erosion of epistemic infrastructure** — the information environment degrades to the point that collective decision-making (markets, elections, deliberation) loses reliability faster than AI restores it |
| L8 | **Generational equity failure** — AI-era productivity gains accrue to existing capital holders and senior workers; new entrants to the knowledge economy face permanently degraded prospects, fracturing the inter-generational mobility that legitimates the current economic order |

### 1.2 Hazards

Hazards are system states that, in a worst-case environment, would
lead to a loss. Stated as system conditions.

| ID | Hazard | Linked losses |
|----|--------|---------------|
| H1 | A small number of firms (≤10) own the binding-constraint inputs to frontier AI (chips, energy, fabs, leading-edge models) without effective external accountability | L2, L3, L5 |
| H2 | The substitution-vs-complementarity balance shifts faster than retraining and reabsorption institutions can respond | L1, L8 |
| H3 | Productivity gains accrue to capital owners without redistribution mechanisms transmitting them to consumers or labour | L5, L8 |
| H4 | The frontier-vs-open-weights capability gap collapses to ≤6 months *and* the open-weights ecosystem is then suppressed by regulation or capability stagnation | L2, L4 |
| H5 | Frontier AI labs operate at rung-1 mission-driven authority while their funding, capability disclosure, and deployment decisions affect rung-6 collective outcomes | L3, L7 |
| H6 | National AI-infrastructure competition crosses the threshold from sanctions-and-export-control coercion into kinetic or cyber conflict | L6 |
| H7 | Information environments saturate with AI-generated content faster than provenance, authentication, and verification systems can scale | L7 |
| H8 | Capability deployment cycles (months) decouple from labour, education, and welfare-policy cycles (years to decades) | L1, L8 |

### 1.3 System-level constraints

Each constraint is the inversion of a hazard — a "must" statement
that prevents the hazard.

| ID | Constraint | Inverts |
|----|-----------|---------|
| C1 | Ownership of binding-constraint AI inputs must be subject to effective external accountability proportional to the systemic power those inputs confer | H1 |
| C2 | The pace of substitution-driving capability deployment must not exceed the absorptive capacity of retraining and reabsorption institutions, *or* those institutions must be redesigned to match the new pace | H2 |
| C3 | Productivity gains from AI must be transmitted to consumers (via competitive prices) or labour (via wages) or the public (via taxation) — at least one of the three channels must function | H3 |
| C4 | An open-weights tier with credible capability proximity to the frontier (gap ≤12 months) must remain accessible as a price-setting mechanism on the model layer | H4 |
| C5 | Decisions by frontier labs that affect rung-6 collective outcomes (capability disclosure, deployment thresholds, model-access policy) must be subject to rung-appropriate governance, not merely lab-internal authority | H5 |
| C6 | National competition over AI infrastructure must remain below the threshold of kinetic or escalating-cyber conflict | H6 |
| C7 | The information environment must be equipped with provenance and authentication infrastructure scaled to AI-generated content volume | H7 |
| C8 | Labour, education, and welfare institutions must operate on a cycle commensurate with the capability deployment cycle, *or* automatic stabilisers must absorb the cadence mismatch | H8 |

---

## STPA Step 2 — Model the Control Structure

This step is sketched at the logical-architecture level. A full Step
2 would draw the diagram graphically; here it is presented as a
hierarchy of controllers and the principal control actions and
feedback channels between them, with rung tags on each arrow.

Notation: each control action and feedback channel is tagged with
the rung at which it operates (`r0`–`r6`). Where a channel is
nominally one rung but operates at another, both are shown
(`claimed:r6 / operating:r1`). For the rungs framework, see
`knowledge/se-techniques/justification-rungs/rungs.md`.

### 2.1 Logical controller hierarchy

```
                  ┌──────────────────────────────────┐
                  │  Global polity / public discourse│ (rung 6 ideal)
                  └──────────────┬───────────────────┘
                                 │ control: norms, legitimacy
                                 │ feedback: backlash, elections, mass opinion
                ┌────────────────┼────────────────┐
                │                │                │
        ┌───────▼─────┐  ┌───────▼─────┐  ┌───────▼─────┐
        │ US govt     │  │ PRC govt    │  │ EU + others │
        │ (BIS, FTC,  │  │ (MIIT,      │  │ (EU Comm,   │
        │  Treasury,  │  │  CAC, party │  │  AI Office, │
        │  Congress)  │  │  centre)    │  │  member sts)│
        └──┬──┬──┬────┘  └──┬──┬───────┘  └──┬──────────┘
           │  │  │          │  │             │
   export  │  │  │  industrial policy        │ regulation
   ctrls   │  │  │  & capital steering       │ (AI Act etc)
   r0/r2   │  │  │  r0/r1/r2                 │ r2/r4
           │  │  └────────────┐              │
           │  │ procurement   │              │
           │  │ r2            │              │
           │  ▼               ▼              ▼
        ┌──────────────────────────────────────────┐
        │   Capital markets (PE, public equity,    │
        │   sovereign wealth, strategic investors) │   (operating r3/r4 on
        └──────────┬───────────────────────────────┘    rung-1 mission claims)
                   │ funding rounds, equity, debt
                   │ r3 (financial returns)
                   ▼
   ┌────────────────────────────────────────────────────────────┐
   │           Frontier AI labs (US + PRC, ≤10 globally)        │
   │           — claimed mission rung r1 + r6 (safe AGI)        │
   │           — operating rung r1 (founder/exec authority)     │
   └──┬─────────────────┬────────────────┬──────────────────────┘
      │                 │                │
      │ compute         │ model           │ products /
      │ purchase r3     │ releases r3     │ APIs r3
      ▼                 ▼                 ▼
   ┌──────────┐  ┌─────────────────┐  ┌────────────────────┐
   │ Compute  │  │ Open-weights    │  │ Application layer  │
   │ infra:   │  │ ecosystem       │  │ (vertical SaaS,    │
   │ chips,   │  │ (price-setter   │  │ agentic platforms, │
   │ fabs,    │  │ on model layer) │  │ enterprise)        │
   │ energy,  │  │                 │  │                    │
   │ DCs      │  │                 │  │                    │
   └────┬─────┘  └────────┬────────┘  └─────────┬──────────┘
        │                 │                     │
        │ chips r3        │ free download r3    │ deployment r3
        │ energy r3       │                     │
        ▼                 ▼                     ▼
   ┌──────────────────────────────────────────────────────────┐
   │  Workers and consumers in the cognitive-knowledge economy │
   │  (controlled process — substitution / complementarity     │
   │  effects experienced here)                                │
   └──────────────────────────────────────────────────────────┘
                          │
                          │ feedback: wages, employment, prices,
                          │ political opinion
                          │ r3/r4 (slow), r0 (when it escapes
                          │       to backlash)
                          ▼
                   (back to global polity)
```

### 2.2 Rung tags on principal channels

| # | Channel | Rung (claimed → operating) | Note |
|---|---------|---------------------------|------|
| CH1 | US export controls → PRC compute access | r2 (regulatory rule) → r0 (coercive denial) | Rung shifted by enforcement design |
| CH2 | PRC industrial policy → indigenous compute | r2 (rule) + r1 (national mission) | Hybrid; effectiveness depends on r3 capability feedback |
| CH3 | Capital markets → frontier labs (funding) | r3 (financial returns) → r1 (mission belief required to underwrite) | Capital cannot fully evaluate the thing it funds |
| CH4 | Frontier labs → public (capability claims, model cards) | claimed r3 (benchmarks) / operating r1 (lab authority) | Benchmarks chosen and reported by the same party they evaluate |
| CH5 | Lab safety frameworks (RSPs, voluntary commitments) → public | claimed r6 (deliberative) / operating r1 (lab self-binding) | Pattern B (claimed-rung inflation) |
| CH6 | EU AI Act → labs and deployers | r2 (rule) + r4 (evidence-based risk tiering) | Cycle time mismatched to capability deployment |
| CH7 | Open-weights releases → application layer | r3 (download, run, measure) | Strongest empirical channel in the system |
| CH8 | Worker displacement → policymakers | r3/r4 (statistics) + r0 (backlash) | r3 channel slow; r0 channel is the unwanted overflow |
| CH9 | Lab → user (product use) | r3 (works or doesn't) | Strongest fast feedback in the entire structure |
| CH10 | Public discourse → labs | claimed r6 (legitimacy) / operating r1 (PR, narrative) | Pattern B again |

### 2.3 Identified rung mismatches (preliminary)

Three mismatches are immediately visible and warrant Step 3 / Step
4 attention. References are to the patterns in
`knowledge/se-techniques/justification-rungs/dangerous-mismatches.md`.

- **M1 — Pattern B at lab/safety boundary (CH5).** Labs claim
  rung-6 deliberative legitimacy for safety frameworks but the
  operating mechanism is rung-1 self-binding. Trust erodes at the
  rate of the gap between claim and operation.
- **M2 — Pattern A at capital/lab boundary (CH3 + CH4).** Funding
  flows in at rung 3 (returns); capability claims flow back at
  rung 1 (mission narrative wrapped in selected benchmarks). The
  loop *appears* closed but the upward channel is filtered. This
  is the classic asymmetric loop and the structural reason for
  recurring valuation–reality dislocations in the AI sector.
- **M3 — Cadence mismatch at labour/policy boundary (CH8).**
  Disturbance arrives on a months cycle; the rung-3/4 corrective
  feedback channel operates on a years cycle. The cadence
  mismatch causes rung-3/4 feedback to arrive irrelevantly late,
  forcing the response into the rung-0 backlash channel that the
  feedback was supposed to prevent. Not strictly one of the three
  catalogued patterns; closest to Pattern A with delay as the
  dominant failure mode.

---

## STPA Step 3 — Unsafe Control Actions (seed set)

For a complete Step 3, every control action in the structure would
be examined against the four UCA types (action provided when
unsafe; not provided when needed; provided too early/late; provided
for wrong duration). What follows is a representative seed set —
the UCAs most directly connected to the identified hazards.

| ID | Controller | Control action | UCA | Type | Linked hazards |
|----|-----------|----------------|-----|------|----------------|
| UCA-1 | US BIS | Issues chip export-control update | Issued *too late* — after PRC has stockpiled or routed around the prior tier | Late | H1 (indirectly), H6 |
| UCA-2 | US BIS | Issues chip export-control update | Issued *too broadly* — captures dual-use compute that allies depend on, fracturing the coalition needed for enforcement | Wrong | H6 |
| UCA-3 | Frontier lab | Releases a model with capability X | Released *before* deployment-environment safeguards exist for X | Early | H5, H7 |
| UCA-4 | Frontier lab | Raises funding round at valuation V | Accepted at a V that compels deployment behaviours incompatible with stated safety mission (Pattern B intensifier) | Wrong | H5 |
| UCA-5 | Frontier lab | Publishes model card / capability claims | Published in form that satisfies CH4's r1-wrapping rather than CH4's r3-content | Wrong | H5 |
| UCA-6 | Capital allocator | Funds frontier training round | Funds at terms that make the lab's r1 mission narrative a precondition of capital, foreclosing rung-3 falsifiability | Wrong | H5, M2 |
| UCA-7 | Compute infrastructure provider | Allocates capacity | Allocates exclusively to a small number of frontier customers in long-term contracts that foreclose entry by smaller actors | Wrong | H1 |
| UCA-8 | US/EU regulator | Imposes restrictions on open-weight model release | Imposed in a way that suppresses the open-weights price-setting mechanism without replacing it | Wrong | H4, indirectly H1 |
| UCA-9 | PRC government | Continues open-weight releases | Continues *too long* — until release of weights with state-aligned behaviours embedded becomes a vector for influence at scale | Wrong duration | H7 |
| UCA-10 | Labour ministries / education systems | Updates retraining and curriculum | Updated *too slowly* — on a multi-year cycle while disturbance arrives on a multi-month cycle (M3) | Late | H2, H8 |
| UCA-11 | Tax authorities | Adjusts taxation of AI-driven productivity | Not provided — productivity gains accumulate untaxed in capital while labour share falls | Not provided | H3, L5, L8 |
| UCA-12 | Antitrust authorities | Acts on AI-infrastructure concentration | Not provided in time — concentration becomes structurally entrenched before action | Late | H1 |
| UCA-13 | Information-platform regulator | Mandates content provenance / authentication | Not provided at scale — voluntary frameworks persist while AI content saturates | Not provided | H7 |
| UCA-14 | Public discourse / electorate | Withdraws legitimacy from a lab or sector | Withdrawn via r0 backlash because r3/r4 channels failed to land in time (M3 escape valve) | Wrong | L3, indirectly L1 |
| UCA-15 | National security apparatus | Treats peer-state AI capability as casus belli | Provided when the underlying conflict could have been mediated at lower rungs — H6 realised | Wrong | L6 |

This is a seed set, not exhaustive. A complete pass would generate
40–80 UCAs across all controllers and the four UCA types.

---

## STPA Step 4 — Loss Scenarios (seed set)

For each UCA, ask *why* it could occur. Causes organise around the
control loop: process model wrong; feedback missing/delayed/
corrupted; control action incorrectly executed; controlled process
state changed unexpectedly; external disturbance.

Below, one or two loss scenarios per high-priority UCA, with a
linked candidate remedy.

### LS-1 (from UCA-3, UCA-5) — Lab releases a capability-jump model that the deployment ecosystem cannot safely absorb

- **Process-model failure.** Lab's process model treats "passes
  internal evals" as sufficient for "safe to release." External
  deployment context (downstream users, applications, integrations)
  is not in the process model.
- **Feedback failure.** CH4 carries r1-wrapped capability claims;
  external r3 evaluation is not in the loop before release.
- **Remedy class.** Pattern A remedy (rung-elevation of the feedback
  channel): independent pre-release evaluation by a body whose
  existence is not contingent on the lab. UK AISI, US AISI, EU AI
  Office testing programmes are early instances; their statutory
  authority and independence determine whether they actually
  bypass CH4's filter.

### LS-2 (from UCA-4, UCA-6, M2) — Capital structure forces deployment behaviours incompatible with mission

- **Process-model failure.** Investors' process model treats lab
  mission claims as r3-evaluable when they are r1 commitments;
  diligence cannot resolve the gap.
- **Controller incentive failure.** Fund returns require deployment
  cadence; cadence overrides safety frameworks at scale.
- **Remedy class.** Lower the claim (Pattern B remedy): structural
  separation of safety governance from commercial governance;
  long-horizon-aligned capital structures (PBC governance with
  enforceable mission constraints, not advisory).

### LS-3 (from UCA-7, UCA-12, H1) — Compute-layer concentration becomes structurally entrenched

- **Controlled process state.** Long-term capacity contracts and
  vertical-integration acquisitions move the system to a state in
  which entry by new compute providers is foreclosed.
- **Feedback delay.** Antitrust evidence operates at r4 cumulative
  timescales (years); concentration entrenches at r3 contract
  timescales (quarters).
- **Remedy class.** Cadence-matched controls: ex-ante non-
  discrimination requirements on hyperscale capacity allocation;
  mandatory reservation of a fraction of leading-edge fab output
  for non-frontier customers.

### LS-4 (from UCA-8, H4) — Open-weights price-setting mechanism is regulated away

- **Process-model failure.** Regulator treats open weights primarily
  as a misuse risk; does not model them as the price-setting
  mechanism on the model layer.
- **External disturbance.** Geopolitical pressure to "match" PRC
  open-weights restrictions drives unilateral US/EU restrictions.
- **Remedy class.** Domain-appropriate rung containment (Pattern C
  remedy): routing open-weights questions to a forum that holds
  both the misuse-risk and price-setting considerations in
  superposition (rung-5 integration).

### LS-5 (from UCA-10, M3, H2) — Labour reabsorption fails because cadence is mismatched

- **Cadence failure.** Disturbance and corrective channel operate
  on incompatible cycles.
- **Process-model failure.** Labour ministries' process models
  treat AI-driven displacement as a sectoral shock when it is a
  cross-sectoral cognitive-task shock.
- **Remedy class.** Automatic stabilisers that activate without
  requiring rung-3/4 confirmation per cycle: AI-impact-indexed
  unemployment insurance, sectoral retraining credits indexed to
  task-displacement benchmarks rather than headline employment.

### LS-6 (from UCA-11, H3, L5) — Productivity surplus accrues to capital with no transmission to labour or consumers

- **Controlled process state.** Capital share rises; labour share
  falls; consumer prices may or may not fall depending on market
  structure (LS-3).
- **Controller absent.** No controller in the current structure
  is positioned to act on cross-sectoral productivity-gain capture.
- **Remedy class.** New controller: a transmission mechanism
  (productivity-indexed dividend, value-added tax on AI inference
  with hypothecated dividend, expanded EITC indexed to task-
  displacement, sovereign-wealth participation in AI infrastructure
  with public dividend).

### LS-7 (from UCA-1, UCA-2, UCA-15, H6) — Compute / chip competition escalates to kinetic conflict

- **Process-model failure.** Each national security apparatus models
  the other side's compute build-out as preparation for adversarial
  use; the alternative model (defensive build-out for self-
  sufficiency) is filtered out.
- **Feedback failure.** Confidence-building channels at the AI-
  infrastructure level do not exist; the only available channels
  are coercive (sanctions, export controls) and rhetorical (state
  speeches).
- **Remedy class.** Pattern-A remedy: independent inspection or
  observation regime for AI-infrastructure deployments, of the
  kind that has worked for other dual-use technologies (IAEA, OPCW,
  Open Skies). Rare and slow; prerequisite is willingness to
  accept rung-3 verification on rung-1 strategic claims.

### LS-8 (from UCA-13, H7) — Information environment saturates with unauthenticated AI content

- **Controlled process state.** Volume of AI-generated content
  exceeds the capacity of human and automated authentication.
- **Feedback failure.** Provenance signals exist (C2PA, watermarking)
  but adoption is voluntary and adversarial actors strip them.
- **Remedy class.** Mandatory provenance at the platform / device
  layer; rung-3 verification standards backed by rung-2 regulation;
  acceptance that watermarking alone is insufficient and provenance
  must move to the capture or transmission layer.

---

## What changed from the chat analysis

Of the chat analysis's headline conclusions, the SE pass:

| Chat conclusion | SE-pass status |
|-----------------|----------------|
| "Software work bifurcates by judgment intensity" | Survives; reframed as the substitution-vs-complementarity profile underlying H2 / L1. Not a top-level loss in itself. |
| "Infrastructure layer captures more durable rents" | Survives; reframed as H1 with UCA-7, UCA-12 and LS-3 specifying the actual concentration mechanisms. |
| "Open weights set a price ceiling" | Survives; reframed as constraint C4 with UCA-8 and LS-4 specifying how the constraint can be violated. |
| "Joblessness vs. welfare is a policy choice" | Survives; reframed as H3 and H8 with UCA-10, UCA-11 and LS-5, LS-6 specifying the structural transmission mechanisms. |
| "2×2 scenario matrix on (open-weights gap) × (redistribution)" | Replaced. The 2×2 was a forecasting tool; the SE artefacts above identify *interventions* per identified UCA, which is the constructive form of the same insight. |

The SE pass also surfaces material the chat analysis missed:

- **The capital → lab asymmetric loop (M2).** The chat analysis
  treated capital flows as an undifferentiated input. The rung-tagged
  control structure shows it as a Pattern-A asymmetric loop and
  predicts a specific failure mode (LS-2) that the chat analysis
  missed.
- **The lab/safety claimed-rung inflation (M1).** The chat analysis
  treated industry self-regulation as ineffective without naming the
  mechanism. The rungs framework names it as Pattern B and points at
  the specific structural remedy.
- **Cadence mismatch as a distinct failure class (M3).** The chat
  analysis hand-waved this as "speed of capability vs. speed of
  institutional adaptation". The SE pass identifies it as the
  structural cause of the rung-0 backlash escape valve (UCA-14)
  that political backlash represents.
- **L6, L7 — geopolitical conflict and epistemic-infrastructure
  losses.** The chat analysis essentially missed these. The losses-
  and-hazards step forced their inclusion.

---

## What this first pass does not yet do

- Step 2 is sketched as ASCII rather than as a proper diagram. A
  full Step 2 would draw the controllers and arrows graphically.
- The UCA enumeration in Step 3 is a seed set (~15 UCAs) rather
  than a complete pass (40–80 UCAs).
- Step 4 loss scenarios are one or two per high-priority UCA, not
  the full causal-chain enumeration each UCA admits.
- Remedies are proposed at the *class* level (Pattern A elevation,
  Pattern B claim/operation closure, cadence-matched controls,
  etc.) rather than as concrete policy proposals.
- No `remedy-proposals.md` has been written; remedy classes appear
  inline in Step 4 above. A second pass would extract them into
  their own file with cost / tractability / time-horizon analysis.

A second pass would address these in turn. This first pass is
sufficient to demonstrate that the SE method produces structurally
different artefacts from the chat-level analysis and points at
specific structural interventions that the chat analysis missed.
