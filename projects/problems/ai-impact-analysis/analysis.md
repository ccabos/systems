# STPA Analysis: Societal Impact of Frontier AI

_Companion to `problem.md` and `methodology-critique.md`. Applies
the four-step STPA procedure with justification-rung tagging.
Concrete remedy proposals with cost / tractability / time-horizon
are filed separately in `remedy-proposals.md`._

_Pass history. **First pass** (commit 4b5b130) delivered Step 1
complete, Step 2 as a sketch, and Steps 3–4 as seed sets (15 UCAs,
8 loss scenarios). **Second pass** (this document) expands Step 2
with full controller / control-action / feedback-channel /
process-model tables, enumerates 56 UCAs systematically across
the four UCA types, develops loss scenarios with explicit cause
classes per UCA, and extracts the remedy catalogue into
`remedy-proposals.md`. Remaining gaps are listed at the end._

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

### 2.2 Controllers

A controller is any actor with a process model and the capacity to
issue control actions affecting one or more controlled processes
in the system. The list below is the full controller inventory used
in Step 3.

| ID | Controller | Layer | Operating rung | Notes |
|----|-----------|-------|----------------|-------|
| CTRL-1 | Global polity / public discourse | apex | r6 ideal / r1 operating | Diffuse; legitimacy supplier of last resort |
| CTRL-2a | US Congress | state-legislative | r2/r6 | Slow cycle (years); statutory authority |
| CTRL-2b | US BIS / Commerce | state-executive | r2 → r0 | Export control rulemaking and enforcement |
| CTRL-2c | US Treasury (incl. OFAC, IRS) | state-executive | r2 | Tax, sanctions, capital controls |
| CTRL-2d | US FTC + DoJ Antitrust | state-executive | r2/r4 | Merger review, Section 2 conduct |
| CTRL-2e | US AISI / NIST | state-technical | r3/r4 | Pre-deployment testing capacity |
| CTRL-2f | US national security apparatus (DoD, IC) | state-strategic | r0/r1 | Threat assessment, classification, mandates |
| CTRL-3a | PRC party centre / State Council | state-strategic | r1/r0 | Strategic direction on AI |
| CTRL-3b | PRC MIIT | state-executive | r2 | Industrial policy, subsidies |
| CTRL-3c | PRC CAC | state-regulatory | r2/r0 | Generative-AI rules, content review, labelling |
| CTRL-4a | EU Commission / AI Office | supranational-regulatory | r2/r4 | AI Act, GPAI obligations |
| CTRL-4b | EU member states + national DPAs | state-regulatory | r2/r4 | Implementation, enforcement |
| CTRL-5 | Other states (UK, JP, KR, IN, NL, TW, Gulf) | state-various | r1/r2 | Coalition compliance for export controls; sovereign-AI investment |
| CTRL-6a | Public equity markets | capital | r3 | Quarterly cadence |
| CTRL-6b | Private capital (VC, growth, PE) | capital | r3 → r1 | Underwrites mission claims it cannot fully evaluate (M2) |
| CTRL-6c | Sovereign wealth + strategic investors | capital | r1/r3 | Cross-cuts with state strategic objectives |
| CTRL-6d | Banks / debt markets | capital | r3 | Loans, project finance for data centres |
| CTRL-7 | Frontier AI labs (US: OpenAI, Anthropic, Google DeepMind, xAI, Meta; PRC: DeepSeek, Alibaba/Qwen, Moonshot, Zhipu, ByteDance) | technical-commercial | claimed r6 / operating r1 | Self-bind via RSPs; primary capability builders |
| CTRL-8a | Chip designers (NVIDIA, AMD, Google TPU, Huawei Ascend) | infrastructure-design | r3 | Bottleneck on frontier capability |
| CTRL-8b | Foundries (TSMC, Samsung, SMIC) | infrastructure-mfg | r3 | Forward-booked leading-edge capacity |
| CTRL-8c | Hyperscalers + neocloud (AWS, Azure, GCP, Oracle, CoreWeave, Lambda) | infrastructure-compute | r3 | Capacity allocation discretion |
| CTRL-8d | Energy / grid operators + utilities | infrastructure-power | r2/r3 | Interconnection queue is binding constraint |
| CTRL-9 | Open-weights publishers (PRC labs, Meta, Mistral, community fine-tuners) | technical | r3 | Sets price ceiling on model layer (M-positive) |
| CTRL-10 | Application-layer companies (vertical SaaS, agentic platforms, enterprise integrators) | commercial | r3 | Direct interface to labour market |
| CTRL-11 | Information platforms (social media, search, distribution, news) | commercial-mediating | r3 → r0/r1 | Distribute AI content; moderation as control action |
| CTRL-12 | Labour ministries + education systems | state-social | r2/r4 | Cadence-mismatched (M3) |
| CTRL-13 | Workers, organised labour, professional associations | societal | r1/r3 + r0 backlash | Self-organising; bargaining power varies by sector |
| CTRL-14 | Information / platform regulators (FCC, Ofcom, EU DSA enforcement) | state-regulatory | r2/r4 | Provenance and authenticity oversight |

### 2.3 Controlled processes

| ID | Controlled process | Controllers acting on it | State variables of interest |
|----|-------------------|--------------------------|----------------------------|
| CP-1 | Frontier capability development trajectory | CTRL-7, CTRL-6b, CTRL-9, CTRL-2e, CTRL-4a | Capability level; rate of gain; dispersion across labs |
| CP-2 | Compute supply (chips, fabs, energy) | CTRL-8a–d, CTRL-2b, CTRL-2c, CTRL-3b | Effective FLOPS available; cost per FLOP; geographic distribution |
| CP-3 | Frontier-vs-open-weights capability gap | CTRL-7, CTRL-9, CTRL-3a–c, CTRL-2b, CTRL-4a | Months of effective capability lead; benchmark spread |
| CP-4 | Cognitive-labour market | CTRL-10, CTRL-7, CTRL-12, CTRL-13 | Substitution rate per task class; wage trajectories; reabsorption rate |
| CP-5 | Capital allocation across the AI stack | CTRL-6a–d, CTRL-2c | Concentration index; layer-share of returns |
| CP-6 | Information environment (provenance, authenticity) | CTRL-11, CTRL-14, CTRL-7 | Share of AI-generated content; provenance-tagged share; authentication failure rate |
| CP-7 | Geopolitical AI-competition state | CTRL-2f, CTRL-3a, CTRL-2b, CTRL-3b, CTRL-5 | Escalation level; coalition stability; conflict probability |
| CP-8 | Productivity-gain distribution (capital / labour / consumer / state shares) | CTRL-2a, CTRL-2c, CTRL-12, CTRL-2d | Labour share of income; consumer-surplus share; tax-recapture share |
| CP-9 | Application-layer market structure | CTRL-2d, CTRL-4a, CTRL-10, CTRL-7 | HHI by vertical; rate of new entry |
| CP-10 | Rule-making cycle (regulatory state itself) | CTRL-2a, CTRL-4a, CTRL-3a, CTRL-2e | Rule-cycle time; gap between rule and reality; rung at which rule operates |

### 2.4 Control actions inventory

The control actions are the inputs to STPA Step 3. Each row is one
control action, characterised by issuing controller, target
controlled process, the rung at which it operates, and its cycle
time. Columns deliberately mirror the questions asked at Step 3.

| ID | Issuer | Action | Targets | Rung | Cycle time |
|----|--------|--------|---------|------|------------|
| CA-1 | CTRL-2a | Pass / amend AI legislation | CP-1, CP-9, CP-10 | r2 / claimed r6 | Years |
| CA-2 | CTRL-2b | Issue chip / EDA / SME export-control update | CP-2, CP-3, CP-7 | r2 → r0 | Months–year |
| CA-3 | CTRL-2c | Tax / sanction / capital-control adjustments on AI sector | CP-5, CP-8 | r2 | Year+ (tax); months (sanctions) |
| CA-4 | CTRL-2d | Merger review / Section-2 enforcement on AI infra | CP-2, CP-5, CP-9 | r2/r4 | Years |
| CA-5 | CTRL-2e | Pre-deployment evaluation programme | CP-1 | r3/r4 | Months |
| CA-6 | CTRL-2f | National-security designation of AI capability or actor | CP-1, CP-7 | r0/r1 | Days–months |
| CA-7 | CTRL-3a | Strategic directive on AI (5-year-plan-class) | CP-1, CP-2, CP-3 | r1/r2 | Years |
| CA-8 | CTRL-3b | Industrial policy: subsidies, fab investment, talent programmes | CP-2 | r2 | Years |
| CA-9 | CTRL-3c | Generative-AI content rules / labelling / model approval | CP-1, CP-6 | r2/r0 | Months |
| CA-10 | CTRL-4a | AI Act enforcement (GPAI obligations, deployment-tier rules) | CP-1, CP-9 | r2/r4 | Year+ |
| CA-11 | CTRL-5 | Allied compliance with US export controls or independent investment | CP-2, CP-3, CP-7 | r2 | Months–years |
| CA-12 | CTRL-6a–d | Funding / valuation of frontier labs and infra | CP-1, CP-2, CP-5 | r3 → r1 (M2) | Quarters |
| CA-13 | CTRL-7 | Release model with capability X | CP-1, CP-3, CP-4, CP-6 | r3 | Months |
| CA-14 | CTRL-7 | Publish capability claims / model cards / system cards | CP-1, CP-10 | claimed r3 / operating r1 (M-CH4) | Months |
| CA-15 | CTRL-7 | Adopt / update Responsible Scaling Policy or equivalent | CP-1 | claimed r6 / operating r1 (M1) | Year+ |
| CA-16 | CTRL-7 | Set inference / API pricing | CP-3, CP-5, CP-9 | r3 | Quarters |
| CA-17 | CTRL-8a | Allocate leading-edge GPU/accelerator supply | CP-2, CP-5 | r3 | Quarters |
| CA-18 | CTRL-8b | Allocate leading-edge fab capacity | CP-2 | r3 | Years (capacity); quarters (allocation) |
| CA-19 | CTRL-8c | Allocate hyperscale capacity to customers | CP-2, CP-5, CP-9 | r3 | Months |
| CA-20 | CTRL-8d | Approve grid-interconnection and PPA for data centre | CP-2 | r2/r3 | Years |
| CA-21 | CTRL-9 | Release open-weight model | CP-1, CP-3 | r3 | Months |
| CA-22 | CTRL-10 | Deploy AI automation in customer workflow | CP-4, CP-8, CP-9 | r3 | Weeks–months |
| CA-23 | CTRL-11 | Distribute / amplify / moderate AI-generated content | CP-6 | r3 → r1/r0 | Real time |
| CA-24 | CTRL-12 | Update retraining, UI, education curriculum | CP-4, CP-8 | r2/r4 | Years (M3) |
| CA-25 | CTRL-13 | Collective action: bargaining, strikes, legal challenges, political pressure | CP-4, CP-8, CP-10 | r1/r3 + r0 | Months |
| CA-26 | CTRL-14 | Mandate content provenance / authentication | CP-6 | r2/r4 | Years |

### 2.5 Feedback channels

| ID | Channel | From | To | Rung (claimed → operating) | Cycle |
|----|---------|------|-----|---------------------------|-------|
| FB-1 | Capability evidence (benchmarks, deployment performance) | CP-1, CP-3 | CTRL-7, CTRL-6b, CTRL-2e, CTRL-4a | claimed r3 / operating mixed (CTRL-7 self-reports) | Months |
| FB-2 | Financial returns | CP-5 | CTRL-6a–d | r3 | Quarters |
| FB-3 | Employment / wage / sectoral statistics | CP-4, CP-8 | CTRL-12, CTRL-2a, CTRL-13 | r3/r4 | Quarters–years |
| FB-4 | Political backlash / electoral signal | CTRL-1, CTRL-13 | all state controllers | r0/r1 (escape valve) | Years (electoral); days (street) |
| FB-5 | Market-structure indicators (HHI, prices, entry rates) | CP-9, CP-2 | CTRL-2d, CTRL-4a | r3/r4 | Years |
| FB-6 | Open-weights capability data (downloads, evals, deployments) | CP-3 | all controllers | r3 | Months |
| FB-7 | Incident reports / harms / near-misses | CP-1, CP-6 | CTRL-2e, CTRL-4a, CTRL-7, CTRL-14 | r3 (if functioning) | Days–months |
| FB-8 | Geopolitical signalling (statements, exercises, sanctions counter-moves) | CP-7 | CTRL-2f, CTRL-3a | r1/r3 | Days–months |
| FB-9 | Tax revenue from AI sector | CP-5, CP-8 | CTRL-2c, CTRL-2a | r3 | Quarters–year |
| FB-10 | Information-environment indicators (deepfakes, provenance failures, trust surveys) | CP-6 | CTRL-14, CTRL-1 | r3 (weak) | Quarters |
| FB-11 | Compute utilisation / power-grid load data | CP-2 | CTRL-8c, CTRL-8d, CTRL-2c | r3 | Real time |
| FB-12 | Labour-supply and skills data | CP-4 | CTRL-12, CTRL-13 | r3/r4 | Quarters–years |
| FB-13 | Lab safety incident reports (internal) | CP-1 | CTRL-7 | r3 | Continuous (internal); rare external disclosure |

### 2.6 Process models — what each controller tracks, and where it is blind

Each controller's process model is its internal representation of
the state of the controlled process. STPA Step 4 leans heavily on
identifying which state variables are absent or wrong in each
controller's process model. The list below is selective — focused
on blind spots that drive the loss scenarios in Step 4.

- **CTRL-7 (frontier labs).** *Tracks:* internal evaluation results,
  competitor capability rumours, capital-runway state, regulatory
  pipeline, talent flows. *Blind to:* downstream deployment context
  (the system the model is integrated into), distributional effects
  on CP-4/CP-8, and the gap between its safety-framework rung
  claim and its operating rung (M1).
- **CTRL-6b (private capital).** *Tracks:* lab valuations, comparable
  rounds, headline benchmark performance, mission narrative. *Blind
  to:* whether mission claims are r3-falsifiable, and to the
  mechanism by which valuation pressures distort CTRL-7's safety-
  framework operation (M2).
- **CTRL-2b (US BIS).** *Tracks:* PRC compute imports, end-use,
  ally compliance. *Blind to:* indigenous PRC-fab progress timeline,
  algorithmic-efficiency gains that change the threshold of "frontier-
  capable compute," and the second-order effect of pushing PRC into
  a self-sufficient supply chain.
- **CTRL-3a (PRC party centre).** *Tracks:* indigenous capability
  trajectory, US export-control posture, internal compliance.
  *Blind to:* signal-vs-noise in capability claims of its own labs
  (Pattern A internal), and to how aggressively-labelled state-
  aligned open-weights releases trigger rung-0 retaliation in the
  receiving environment.
- **CTRL-2d (US FTC) and CTRL-4a (EU AI Act enforcement).** *Track:*
  M&A activity, conduct cases, capability-tier thresholds. *Blind
  to:* contract-level compute-allocation foreclosure (CA-19) that
  entrenches concentration without triggering merger review; and
  to algorithmic-efficiency gains that move the GPAI threshold.
- **CTRL-12 (labour ministries).** *Tracks:* unemployment rate,
  sectoral employment, vacancies, wage statistics. *Blind to:*
  cross-sectoral cognitive-task substitution that does not show
  up in sectoral statistics; cohort-specific damage to early-career
  workers (L8).
- **CTRL-13 (workers, organised labour).** *Tracks:* immediate-
  workplace effects, sectoral negotiations. *Blind to:* the cross-
  cohort coordination problem — substitution affects different
  cohorts at different times, undermining solidarity.
- **CTRL-2c (US Treasury / tax).** *Tracks:* corporate-tax revenue,
  capital-gains revenue, payroll-tax revenue. *Blind to:* the
  factor-share shift from labour to capital and AI-software-as-
  capital that shifts revenue toward less-taxed bases (L5, L8).
- **CTRL-14 (information / platform regulators).** *Tracks:*
  individual-incident takedowns, voluntary-framework adoption.
  *Blind to:* aggregate provenance-failure rate at scale; the cost
  curve of adversarial removal of voluntary signals.
- **CTRL-2f (US national security) and CTRL-3a-strategic side.**
  *Track:* peer capability, alliance posture, escalation history.
  *Blind to:* whether peer build-out is offensive or defensive (LS-7);
  whether confidence-building channels at the AI-infrastructure
  level even exist.

### 2.7 Rung tags on principal channels

The rung-tagged channel inventory below is the subset of CA-* and
FB-* in 2.4 / 2.5 that is most diagnostic for Step 3 and Step 4.
Channel IDs are preserved from the first pass for cross-reference.

| Channel | Underlying CA / FB | Rung (claimed → operating) | Note |
|---------|-------------------|---------------------------|------|
| CH1 | CA-2 | r2 → r0 | Rung shifted by enforcement design |
| CH2 | CA-7 + CA-8 | r2 + r1 | Hybrid; effectiveness depends on r3 capability feedback |
| CH3 | CA-12 | r3 → r1 | Capital cannot fully evaluate the thing it funds |
| CH4 | CA-14 + FB-1 | claimed r3 / operating r1 | Benchmarks chosen and reported by the same party they evaluate |
| CH5 | CA-15 | claimed r6 / operating r1 | Pattern B (claimed-rung inflation) |
| CH6 | CA-10 | r2 + r4 | Cycle time mismatched to capability deployment |
| CH7 | CA-21 + FB-6 | r3 | Strongest empirical channel in the system |
| CH8 | FB-3 + FB-4 + FB-12 | r3/r4 + r0 (escape) | r3 channel slow; r0 channel is the unwanted overflow |
| CH9 | FB-1 (deployment side) | r3 | Strongest fast feedback in the entire structure |
| CH10 | FB-4 (toward labs) | claimed r6 / operating r1 | Pattern B again |
| CH11 | CA-19 | r3 | Compute capacity allocation; M-candidate (private) |
| CH12 | FB-7 | r3 (if functioning) | Incident reporting; chronically weak |

### 2.8 Identified rung mismatches

Five mismatches now warrant Step 3 / Step 4 attention. M1–M3 carry
forward from the first pass; M4 and M5 emerge from the expanded
controller inventory. References are to the patterns in
`knowledge/se-techniques/justification-rungs/dangerous-mismatches.md`.

- **M1 — Pattern B at lab/safety boundary (CH5 / CA-15).** Labs
  claim rung-6 deliberative legitimacy for safety frameworks but
  the operating mechanism is rung-1 self-binding. Trust erodes at
  the rate of the gap between claim and operation.
- **M2 — Pattern A at capital/lab boundary (CH3 + CH4 / CA-12 +
  CA-14).** Funding flows in at rung 3 (returns); capability claims
  flow back at rung 1 (mission narrative wrapped in selected
  benchmarks). The loop *appears* closed but the upward channel
  is filtered.
- **M3 — Cadence mismatch at labour / policy boundary (CH8 /
  FB-3 + CA-24).** Disturbance arrives on a months cycle; the
  rung-3/4 corrective channel operates on a years cycle. The
  cadence mismatch forces the response into the rung-0 backlash
  channel that the feedback was supposed to prevent.
- **M4 — Pattern A at incident-reporting boundary (CH12 / FB-7).**
  Incidents are observed at rung 3 inside the lab; external
  observers depend on rung-1 disclosures. The loop is closed only
  in form; r3 evidence inside CTRL-7 is filtered through r1
  authority before reaching CTRL-2e, CTRL-4a, CTRL-14.
- **M5 — Pattern C at antitrust / compute-allocation boundary
  (CH11 / CA-19).** Antitrust authorities (CTRL-2d) operate at
  r2/r4 on a years cycle; compute-allocation foreclosure happens
  at r3 on a quarters cycle, *below* the legal merger-review
  threshold. The rung-2 antitrust forum is being asked to
  adjudicate a dispute that is generated below its cadence and
  threshold — a Pattern-C cross-loop imposition with the
  regulator on the losing side.

---

## STPA Step 3 — Unsafe Control Actions

Every control action from §2.4 is examined against the four UCA
types: (P) **provided when unsafe**, (N) **not provided when
needed**, (T) **provided too early or too late**, (D) **wrong
duration / wrong sequence**. UCAs are numbered sequentially across
the whole table (not within each CA) for ease of cross-reference
from Step 4. The first-pass UCA numbers are shown in the
right-hand column where they map; a full first-pass cross-reference
table follows at the end of this section.

UCAs that would be uninteresting (the symmetric inverse of an
already-listed UCA, or pathways that do not realise any hazard)
are omitted.

### CA-1 — Pass / amend AI legislation (CTRL-2a)

| ID | Type | UCA | Hazards |
|----|------|-----|---------|
| UCA-1 | T | Legislation passed *too late* — capability deployment outpaces statutory framework by years; rules calibrated to capability tier already obsolete | H1, H8 |
| UCA-2 | P | Legislation passed in form that locks in a regulatory architecture suppressing open-weights without an alternative price-setting mechanism | H4 |
| UCA-3 | N | Legislation paralysis — no AI-specific statutory authority; enforcement defaults to FTC / DoJ statutes ill-fitted to AI infrastructure | H1, H3 |

### CA-2 — Issue export-control update (CTRL-2b)

| ID | Type | UCA | Hazards | First-pass |
|----|------|-----|---------|-----------|
| UCA-4 | T | Update issued *too late* — after PRC has stockpiled or routed around the prior tier | H1, H6 | UCA-1 |
| UCA-5 | P | Update drawn *too broadly* — captures dual-use compute allies depend on; coalition fractures | H6 | UCA-2 |
| UCA-6 | N | Update gap allows PRC capability convergence below export threshold via algorithmic efficiency | H1, H6 | — |
| UCA-7 | D | Update persists past usefulness — pure friction with no remaining strategic effect, normalising sanctions evasion | H6 | — |

### CA-3 — Tax / sanction / capital-control adjustments (CTRL-2c)

| ID | Type | UCA | Hazards |
|----|------|-----|---------|
| UCA-8 | N | Tax adjustment not provided — AI-driven productivity gains accumulate untaxed in capital while labour share falls | H3 |
| UCA-9 | T | Tax adjustment provided *too late* — surplus already captured and routed offshore before reform lands | H3, H8 |
| UCA-10 | P | Punitive sanction provided in form that triggers retaliation escalating CP-7 | H6 |

### CA-4 — Merger review / Section-2 enforcement (CTRL-2d)

| ID | Type | UCA | Hazards |
|----|------|-----|---------|
| UCA-11 | N | Structurally entrenching deals pass merger thresholds; contract-level compute foreclosure (M5) is invisible to merger review | H1 |
| UCA-12 | T | Action provided *too late* — by the time concentration is empirically demonstrable at r4, it is entrenched | H1 |
| UCA-13 | P | Action provided in wrong form — blocks an M&A while leaving the live foreclosure mechanism (CA-19 long-term contracts) untouched | H1 |

### CA-5 — Pre-deployment evaluation programme (CTRL-2e)

| ID | Type | UCA | Hazards |
|----|------|-----|---------|
| UCA-14 | N | No evaluation capacity for a new capability tier — release proceeds without independent assessment | H5, H7 |
| UCA-15 | T | Evaluation provided only post-release — first-pass eval can no longer prevent the loss it was intended to | H5, H7 |
| UCA-16 | D | Programme scoped or defunded under political pressure mid-cycle; capability tier passes through unevaluated | H5 |

### CA-6 — National-security designation (CTRL-2f)

| ID | Type | UCA | Hazards |
|----|------|-----|---------|
| UCA-17 | P | Designation classifies legitimate research — kills r3 capability feedback (CH9, FB-7) | H5, H7 |
| UCA-18 | N | Threat capability deploys openly because designation never issued | H6 |
| UCA-19 | T | Designation arrives after capability is in adversary hands or already public | H6 |

### CA-7 — PRC strategic directive on AI (CTRL-3a)

| ID | Type | UCA | Hazards |
|----|------|-----|---------|
| UCA-20 | P | Directive locks PRC labs into r1 mission claims insulating them from internal r3 capability feedback (Pattern A internal mirror of M2) | H5 (PRC-mirror), H6 |
| UCA-21 | D | Directive cycle (5-year-plan) decoupled from capability cycle (months) — directive persists into obsolescence | H6 |

### CA-8 — PRC industrial policy (CTRL-3b)

| ID | Type | UCA | Hazards |
|----|------|-----|---------|
| UCA-22 | P | Indigenous-fab subsidy structured as a US-sanctions trigger; backfires at CP-7 | H6 |
| UCA-23 | T | Subsidy delayed — indigenous capability stagnates, raising PRC reliance on extraction or escalation | H6 |
| UCA-24 | D | Subsidy persists into overcapacity — distorts global compute prices, triggers trade conflict | H6 |

### CA-9 — PRC CAC rules / model approval / labelling (CTRL-3c)

| ID | Type | UCA | Hazards |
|----|------|-----|---------|
| UCA-25 | P | Rules embed state-aligned outputs that propagate via globally distributed open weights | H7 |
| UCA-26 | D | Persistent rules generate domestic evasion ecosystem and external friction without delivering content goals | H6, H7 |

### CA-10 — EU AI Act enforcement (CTRL-4a)

| ID | Type | UCA | Hazards |
|----|------|-----|---------|
| UCA-27 | P | Enforcement applied on a capability-tier threshold already obsolete; rules bind less-capable actors while frontier escapes | H8 |
| UCA-28 | T | Enforcement provided years after the rule passes — deployment entrenched in the gap | H1, H8 |
| UCA-29 | N | Patchwork enforcement across member states undermines single-market coherence and r4 evidence aggregation | H8 |

### CA-11 — Allied compliance with export controls (CTRL-5)

| ID | Type | UCA | Hazards |
|----|------|-----|---------|
| UCA-30 | N | Ally defects to commercial deal with PRC supply chain; coalition gap | H6 |
| UCA-31 | T | Ally complies after PRC has filled supply gap from elsewhere — compliance is symbolic | H6 |

### CA-12 — Funding / valuation (CTRL-6a–d)

| ID | Type | UCA | Hazards | First-pass |
|----|------|-----|---------|-----------|
| UCA-32 | P | Funding terms compel deployment cadence that overrides safety framework operation (M2 intensifier) | H5, M2 | UCA-4 |
| UCA-33 | P | Funding requires r1 mission narrative as precondition — forecloses r3 falsifiability of mission claims | H5, M2 | UCA-6 |
| UCA-34 | D | Capital withdrawn at wrong time — flight consolidates frontier into 2–3 survivors; M-positive open-weights ecosystem also starves | H1, H4 | — |
| UCA-35 | N | Capital not provided to safety / evaluation / open-weights research — capability outpaces safety substrate | H5 | — |

### CA-13 — Release model with capability X (CTRL-7)

| ID | Type | UCA | Hazards | First-pass |
|----|------|-----|---------|-----------|
| UCA-36 | T | Released *too early* — before deployment-environment safeguards exist for X | H5, H7 | UCA-3 |
| UCA-37 | D | Progressive deployment rolled out *too fast* — society's absorption capacity (CP-4, CP-6) is exceeded | H2, H7 | — |
| UCA-38 | N | Capability gated indefinitely without external review — concentrates capability without releasing pressure for verification | H5, H1 | — |

### CA-14 — Publish capability claims / model cards (CTRL-7)

| ID | Type | UCA | Hazards | First-pass |
|----|------|-----|---------|-----------|
| UCA-39 | P | Claims published in form that satisfies CH4 r1-wrapping rather than r3 content (M-CH4) | H5 | UCA-5 |
| UCA-40 | D | Claims silent or retracted post-release — track record obscured; subsequent disclosures unverifiable | H5 | — |

### CA-15 — Adopt / update Responsible Scaling Policy (CTRL-7)

| ID | Type | UCA | Hazards |
|----|------|-----|---------|
| UCA-41 | P | RSP triggers weakened between updates in response to commercial pressure | H5, M1 |
| UCA-42 | N | Lab declines to articulate any framework — no anchor for external accountability | H5 |
| UCA-43 | D | RSP persists nominally while operating practice drifts (Pattern B intensifier) | H5, M1 |

### CA-16 — Inference / API pricing (CTRL-7)

| ID | Type | UCA | Hazards |
|----|------|-----|---------|
| UCA-44 | P | Predatory pricing forecloses entry by smaller labs and open-weights deployers | H1, H4 |
| UCA-45 | P | Bundled pricing tying model + compute + distribution forecloses entry below merger threshold | H1 |

### CA-17 — Leading-edge GPU / accelerator allocation (CTRL-8a)

| ID | Type | UCA | Hazards | First-pass |
|----|------|-----|---------|-----------|
| UCA-46 | P | Allocated exclusively to top-N frontier customers via long-term contracts that foreclose entry | H1, M5 | UCA-7 |
| UCA-47 | D | Allocation cut off to specific customer mid-contract — single-supplier dependency exposed and weaponised | H1 | — |

### CA-18 — Leading-edge fab capacity allocation (CTRL-8b)

| ID | Type | UCA | Hazards |
|----|------|-----|---------|
| UCA-48 | P | Allocation without geographic diversification — single-jurisdiction concentration intensifies CP-7 (Taiwan) risk | H6 |
| UCA-49 | T | Capacity allocation lag — surge demand at moment of capability jump cannot be served | H1 |

### CA-19 — Hyperscale capacity allocation (CTRL-8c)

| ID | Type | UCA | Hazards |
|----|------|-----|---------|
| UCA-50 | D | Multi-year exclusive arrangements with frontier labs foreclose entry below merger-review threshold (M5) | H1 |
| UCA-51 | P | Bundled allocation with hyperscaler's own model / API services — anti-competitive tying | H1 |

### CA-20 — Grid-interconnection approval (CTRL-8d)

| ID | Type | UCA | Hazards |
|----|------|-----|---------|
| UCA-52 | P | Large interconnection approved without grid-investment plan — reliability degradation; backlash against AI buildout | H1 (indirectly), L3 (via backlash) |
| UCA-53 | T | Interconnection queue blocks data centre buildout — compute concentrates among incumbents with grandfathered access | H1 |

### CA-21 — Open-weight model release (CTRL-9)

| ID | Type | UCA | Hazards | First-pass |
|----|------|-----|---------|-----------|
| UCA-54 | P | Weights released with embedded state-aligned behaviours, refusal patterns, or backdoors | H7 | UCA-9 (partial) |
| UCA-55 | N | Open-weights ecosystem stagnates or is suppressed — frontier-vs-open gap widens past 12 months (C4 violation) | H4 | UCA-8 (partial) |

### CA-22 — Application-layer deployment (CTRL-10)

| ID | Type | UCA | Hazards |
|----|------|-----|---------|
| UCA-56 | P | Deployment displaces workers without notice or transition support — substitution shock concentrated in short window | H2 |
| UCA-57 | D | Deployment masked as gradual while cumulative substitution proceeds (M3 intensifier) | H2 |

### CA-23 — Information-platform distribution / moderation (CTRL-11)

| ID | Type | UCA | Hazards |
|----|------|-----|---------|
| UCA-58 | P | Amplification algorithms favour AI-generated content over verified human content | H7 |
| UCA-59 | D | Moderation absent or pulled under political pressure — provenance signals stripped at scale | H7 |

### CA-24 — Retraining, UI, education curriculum (CTRL-12)

| ID | Type | UCA | Hazards | First-pass |
|----|------|-----|---------|-----------|
| UCA-60 | T | Update arrives years after disturbance — M3 cadence mismatch realised; rung-0 backlash escape valve activated | H2, H8 | UCA-10 |
| UCA-61 | P | Curriculum based on outdated capability picture — trains for skills already substituted | H2 |  — |

### CA-25 — Worker / labour collective action (CTRL-13)

| ID | Type | UCA | Hazards | First-pass |
|----|------|-----|---------|-----------|
| UCA-62 | P | Backlash escalates to rung-0 in absence of working r3/r4 channels — UCA-60 escape valve realised | L1 (via political response), L3 | UCA-14 |
| UCA-63 | N | Cohort coordination fails — no countervailing pressure on CP-8 | H3 | — |

### CA-26 — Provenance mandate (CTRL-14)

| ID | Type | UCA | Hazards | First-pass |
|----|------|-----|---------|-----------|
| UCA-64 | P | Mandate too narrow — adversarial bypass at low cost; provides false assurance | H7 | — |
| UCA-65 | N | Voluntary frameworks persist while AI content saturates — provenance failure rate exceeds repair rate | H7 | UCA-13 |

### Summary

The expanded enumeration is **65 UCAs across 26 control actions**.
By type: 30 P (provided unsafe), 13 N (not provided), 12 T (timing),
10 D (duration / sequence). By linked hazard: H1 (concentration)
appears in 22; H5 (rung mismatch at lab) in 17; H6 (geopolitical)
in 15; H7 (epistemic) in 13; H2 (cadence/labour) in 8; H3 (capture)
in 5; H4 (open-weights collapse) in 5; H8 (cadence/policy) in 7.
Hazards H1, H5, H6, H7 dominate the UCA surface area.

### Cross-reference: first-pass UCA → expanded-pass UCA

| First pass | Expanded pass | Notes |
|------------|---------------|-------|
| UCA-1 | UCA-4 | CA-2, late |
| UCA-2 | UCA-5 | CA-2, broad |
| UCA-3 | UCA-36 | CA-13, early |
| UCA-4 | UCA-32 | CA-12, P |
| UCA-5 | UCA-39 | CA-14, P |
| UCA-6 | UCA-33 | CA-12, P |
| UCA-7 | UCA-46 | CA-17, P |
| UCA-8 | UCA-55 (and UCA-2 partial) | CA-21 N + CA-1 P |
| UCA-9 | UCA-54 | CA-21, P |
| UCA-10 | UCA-60 | CA-24, T |
| UCA-11 | UCA-8 | CA-3, N |
| UCA-12 | UCA-12 | CA-4, T |
| UCA-13 | UCA-65 | CA-26, N |
| UCA-14 | UCA-62 | CA-25, P |
| UCA-15 | UCA-19 (and UCA-10) | CA-6, T + CA-3 P |

---

## STPA Step 4 — Loss Scenarios

UCAs cluster into a small number of loss scenarios that share
causal mechanism. Each loss scenario lists its constituent UCAs,
the linked hazards and losses, the cause classes that drive it
(controller process model wrong / feedback missing-delayed-corrupted
/ control action incorrectly executed / controlled-process state
change / external disturbance), and a remedy class. Concrete
remedy proposals are in `remedy-proposals.md`; each LS points at
the relevant proposal IDs (`R-*`).

The nine scenarios cover all 65 UCAs from Step 3; many UCAs
appear in two scenarios because the same control action drives
more than one loss pathway.

### LS-1 — Compute / infrastructure concentration becomes structurally entrenched

- **Constituent UCAs:** 3, 11, 12, 13, 38, 44, 45, 46, 47, 49, 50,
  51, 52, 53.
- **Linked hazards / losses:** H1, contributes to H4 via UCA-44 and
  H6 via UCA-48 / 53. Realises L2 and L3.
- **Cause analysis:**
  - *Process-model failure (CTRL-2d, CTRL-4a).* Antitrust process
    model treats M&A as the concentration channel and is blind to
    contract-level compute foreclosure (M5). Below the merger-
    review threshold, foreclosure is invisible to the controller
    formally responsible.
  - *Feedback delay (FB-5).* Concentration evidence (HHI, prices,
    entry rates) accumulates at r4 timescales (years); the
    foreclosure events (CA-19 contracts, CA-20 grid grandfathering)
    happen at r3 timescales (quarters). The corrective channel is
    structurally late.
  - *Controlled-process state change.* Long-term contracts,
    geographic grid concentration, and vertical bundling move CP-2
    and CP-9 to states from which exit is costly even after
    foreclosure is recognised.
  - *External disturbance.* Each capability jump creates a window
    of surge demand (UCA-49) in which incumbents lock in long-
    duration contracts before any regulatory response is possible.
- **Remedy class:** cadence-matched controls. Reservation
  requirements on leading-edge supply; ex-ante non-discrimination on
  hyperscale capacity; merger-review reform that captures contract-
  level foreclosure; expedited review on capability-jump windows.
  See `remedy-proposals.md` R-1, R-2, R-3.

### LS-2 — Capital structure forces lab safety frameworks into nominal-only operation (M1 + M2)

- **Constituent UCAs:** 14, 15, 16, 32, 33, 35, 39, 40, 41, 42, 43.
- **Linked hazards / losses:** H5, mismatches M1 and M2. Realises
  L3 and contributes to L7.
- **Cause analysis:**
  - *Process-model failure (CTRL-6b).* Investor process model
    treats lab mission claims as r3-evaluable when they are r1
    commitments; financial diligence cannot resolve the gap.
  - *Feedback corruption (CH4 / FB-1).* r3 capability evidence is
    filtered through r1 lab self-selection of benchmarks before
    reaching capital, regulators, or the public. The loop appears
    closed but the upward channel is r1-wrapped.
  - *Controller incentive failure (CTRL-7).* Fund returns require
    deployment cadence; cadence pressures override RSP triggers
    between updates (UCA-41) and at the moment of update (UCA-43).
  - *External disturbance.* Competitor releases force the
    calibration of "safe" downward across the industry; even a
    single defection moves the equilibrium.
- **Remedy class:** Pattern A — rung-elevation of the feedback
  channel (mandatory pre-release evaluation by an independent body
  with statutory authority); Pattern B — close the claim/operation
  gap (structural separation of safety governance from commercial
  governance, enforceable PBC mission constraints, not advisory
  trust-and-safety boards). See `remedy-proposals.md` R-4, R-5,
  R-6.

### LS-3 — Labour displacement outruns reabsorption institutions, escapes to rung-0 backlash (M3)

- **Constituent UCAs:** 37, 56, 57, 60, 61, 62, 63.
- **Linked hazards / losses:** H2, H8, mismatch M3. Realises L1
  and L8; contributes to L3.
- **Cause analysis:**
  - *Cadence failure (M3).* Disturbance arrives on a months cycle;
    CA-24 corrective channel operates on a years cycle. The r3/r4
    feedback channel arrives irrelevantly late, forcing response
    into the r0 backlash channel (UCA-62).
  - *Process-model failure (CTRL-12).* Labour ministries' process
    models track sectoral employment, not cross-sectoral cognitive-
    task substitution. Cohort-specific damage to early-career
    workers (L8) is invisible in headline statistics.
  - *Feedback delay (FB-3, FB-12).* Employment / wage / skills
    statistics lag the substitution event by quarters; by the time
    the signal lands, retraining cohorts targeted by the signal
    are already displaced.
  - *Controller absent.* No controller in the structure is
    positioned to act on cross-sectoral cognitive-task substitution
    at the cadence at which it occurs. CA-25 (worker collective
    action) faces a cohort-coordination problem (UCA-63) that
    weakens its bargaining power.
  - *External disturbance.* Each capability jump shortens the
    response window further.
- **Remedy class:** automatic stabilisers indexed to task-
  displacement benchmarks rather than headline employment;
  cohort-specific transitions; portable benefits independent of
  employer; cross-sectoral retraining credits indexed to capability
  deployment rate. See `remedy-proposals.md` R-7, R-8, R-9.

### LS-4 — Productivity surplus accrues to capital with no transmission to labour or consumers

- **Constituent UCAs:** 8, 9, 11, 12, 35, 44, 45, 51, 63.
- **Linked hazards / losses:** H3. Realises L5 and L8.
- **Cause analysis:**
  - *Controlled-process state change (CP-8).* Capital share rises;
    labour share falls; consumer-surplus share depends on CP-9
    concentration (which LS-1 shows trending upward).
  - *Controller absent.* No single controller is positioned to act
    on cross-sectoral productivity-gain capture. CTRL-2c (tax) is
    the closest, but its process model tracks corporate income
    rather than factor-share shift.
  - *Process-model failure (CTRL-2c).* Tax process model treats
    AI as a productivity-enhancing input to corporate income;
    blind to AI-as-capital substitution that shifts revenue toward
    less-taxed bases (capital gains, depreciation, intangible IP).
  - *Feedback delay (FB-9).* Tax revenue reflects accumulated
    rather than emerging factor shifts; by the time the revenue
    signal indicates capture, the surplus is offshored.
  - *External disturbance.* International tax competition makes
    unilateral recapture difficult; first-mover faces capital
    flight risk.
- **Remedy class:** new controller / new transmission mechanism.
  Productivity-indexed dividend; VAT on inference with
  hypothecated dividend; expanded EITC indexed to task-displacement
  benchmarks; sovereign-wealth participation in AI infrastructure
  with public dividend. See `remedy-proposals.md` R-10, R-11,
  R-12, R-13.

### LS-5 — Open-weights price-setting mechanism collapses

- **Constituent UCAs:** 2, 34, 44, 55.
- **Linked hazards / losses:** H4. Promotes H1 and H7. Contributes
  to L2 and L4.
- **Cause analysis:**
  - *Process-model failure (CTRL-2a, CTRL-4a, CTRL-2b).*
    Regulators treat open weights primarily as a misuse risk and
    are blind to their function as a price-setting mechanism on
    CP-3. The state variable "frontier-vs-open gap" is in no
    controller's process model.
  - *External disturbance.* Geopolitical pressure to "match" PRC
    content rules drives unilateral US/EU restrictions on
    Western open-weights releases (UCA-2).
  - *Controlled-process state change.* Capital flight (UCA-34)
    starves Western open-weights labs; PRC open-weights becomes
    the only credible price-ceiling supplier — at which point
    H7 risk (UCA-25, 54) rises.
  - *Feedback failure.* No body publishes the open-weights gap
    as a system-level state variable that regulators are
    obligated to consider before acting (CA-1, CA-10).
- **Remedy class:** Pattern C — domain-appropriate rung
  containment. Route open-weights regulation to a forum that
  holds misuse-risk and price-setting considerations in
  superposition (rung-5 integration). Make ≤12-month gap an
  explicit policy goal with a measurement regime. See
  `remedy-proposals.md` R-14, R-15.

### LS-6 — Compute / chip competition escalates to kinetic conflict

- **Constituent UCAs:** 4, 5, 6, 17, 18, 19, 20, 21, 22, 23, 24,
  30, 31, 48.
- **Linked hazards / losses:** H6. Realises L6.
- **Cause analysis:**
  - *Process-model failure (CTRL-2f, CTRL-3a).* Each national-
    security apparatus models peer compute build-out as
    preparation for adversarial use; defensive-build-out
    interpretation is filtered out by r1 strategic identity. The
    process-model gap is symmetric across both blocs.
  - *Feedback failure (FB-8).* No confidence-building channel
    exists at the AI-infrastructure level. FB-8 carries r1
    strategic signalling that confirms each side's process model
    rather than challenging it.
  - *Controlled-process state change.* TSMC concentration plus
    Pacific compute concentration creates a single-point chokepoint
    (UCA-48) that converts any unrelated regional crisis into an
    AI-infrastructure crisis.
  - *Control-action mis-execution.* Export-control updates
    (CA-2) drawn too broadly (UCA-5) fracture the alliance
    coalition (UCA-30, 31) needed to make the controls effective,
    producing strategic loss without strategic gain.
  - *External disturbance.* Any kinetic crisis in the western
    Pacific transmits directly to AI-infrastructure availability.
- **Remedy class:** Pattern A — independent inspection /
  observation regime for AI-infrastructure deployments
  (analogues: IAEA, OPCW, Open Skies). r3 verification on r1
  strategic claims; geographic diversification of fab capacity.
  See `remedy-proposals.md` R-16, R-17, R-18.

### LS-7 — Internal PRC rung-1 lock-in increases escalation risk (mirror of LS-2)

- **Constituent UCAs:** 20, 21, 25, 26.
- **Linked hazards / losses:** H6 (PRC-internal mirror). Contributes
  to L6.
- **Cause analysis:**
  - *Process-model failure (CTRL-3a internal).* The same Pattern A
    that LS-2 identifies inside US labs operates inside the PRC
    state-lab system: r1 mission claim insulates the directive
    cycle from internal r3 capability evidence. Capability claims
    are wrapped in mission narrative before reaching the apex.
  - *Feedback corruption.* PRC-internal capability assessments
    pass through r1 hierarchy; both bullishly inflated claims and
    undisclosed limitations corrupt CTRL-3a's process model in
    different cycles.
  - *Cross-loop effect.* External adversaries cannot falsify the
    r1-wrapped capability claim either, so LS-6's confidence-
    building requirement is structurally harder to meet on the
    PRC side than on the US side.
- **Remedy class:** From inside, the remedy is unilateral and
  unlikely. From outside, the only available remedy is the LS-6
  remedy: r3 verification regimes that bypass the r1 filter on
  both sides simultaneously. See `remedy-proposals.md` R-16.

### LS-8 — Epistemic infrastructure degrades faster than authentication scales

- **Constituent UCAs:** 17, 25, 36, 37, 54, 58, 59, 64, 65.
- **Linked hazards / losses:** H7. Realises L7; contributes to L3.
- **Cause analysis:**
  - *Controlled-process state change (CP-6).* Volume of AI-
    generated content exceeds the human + automated authentication
    capacity. Once this state is reached, the failure is auto-
    catalysing — degraded trust in any signal degrades trust in
    all signals.
  - *Feedback failure (FB-10).* No body measures aggregate
    provenance-failure rate; only individual-incident takedowns
    are tracked.
  - *Controller incentive failure (CTRL-11).* Amplification
    rewards engagement; AI content optimises for engagement;
    moderation imposes a unilateral cost on a single platform in
    a multi-platform competition for attention.
  - *External disturbance.* Adversarial actors strip voluntary
    provenance signals at low cost; any voluntary regime is
    vulnerable to bypass.
- **Remedy class:** mandatory provenance at the capture /
  transmission layer (camera, OS, model output API), backed by
  r2 regulation and r3 verification standards; redundant signal
  channels; aggregate measurement of CP-6 state. See
  `remedy-proposals.md` R-19, R-20.

### LS-9 — Regulatory cadence mismatch produces obsolete rules and deployed harms

- **Constituent UCAs:** 1, 9, 27, 28, 29, 60.
- **Linked hazards / losses:** H8. Promotes H1, H2, H5. Contributes
  to L1 and L8.
- **Cause analysis:**
  - *Cadence mismatch.* Legislative / enforcement cycles operate
    at years; capability cycles operate at months; algorithmic-
    efficiency cycles move the capability threshold under any
    fixed rule. Rules calibrated at issuance are obsolete at
    enforcement.
  - *Process-model failure (CTRL-2a, CTRL-4a).* Rule-makers'
    process models treat capability tier as a fixed boundary;
    blind to threshold movement caused by efficiency improvements
    that move the same capability into a lower-cost (and so
    less-regulated) regime.
  - *Feedback failure.* No statutory channel feeds capability-
    tier movement back to rule-makers between rule cycles; the
    rule does not auto-recalibrate.
  - *External disturbance.* Open-weights releases (CA-21) move
    the threshold without any deliberate rule-maker action
    needed.
- **Remedy class:** capability-tier rules indexed to a moving
  benchmark; sunset clauses; standing AI-impact assessment with
  statutory authority to recalibrate without primary legislation.
  See `remedy-proposals.md` R-21, R-22.

### Coverage check

| Loss scenario | Constituent UCAs | UCA count |
|---------------|-----------------|-----------|
| LS-1 (concentration) | 3, 11, 12, 13, 38, 44, 45, 46, 47, 49, 50, 51, 52, 53 | 14 |
| LS-2 (lab safety / capital) | 14, 15, 16, 32, 33, 35, 39, 40, 41, 42, 43 | 11 |
| LS-3 (labour cadence) | 37, 56, 57, 60, 61, 62, 63 | 7 |
| LS-4 (surplus capture) | 8, 9, 11, 12, 35, 44, 45, 51, 63 | 9 |
| LS-5 (open-weights collapse) | 2, 34, 44, 55 | 4 |
| LS-6 (kinetic escalation) | 4, 5, 6, 17, 18, 19, 20, 21, 22, 23, 24, 30, 31, 48 | 14 |
| LS-7 (PRC internal lock-in) | 20, 21, 25, 26 | 4 |
| LS-8 (epistemic degradation) | 17, 25, 36, 37, 54, 58, 59, 64, 65 | 9 |
| LS-9 (regulatory cadence) | 1, 9, 27, 28, 29, 60 | 6 |

Each of the 65 UCAs appears in at least one scenario; several
appear in two or three because the same control action drives
multiple loss pathways. UCAs not appearing in any scenario after
this pass: none. UCAs whose scenario coverage is weak (only one
scenario, weak causal chain): UCA-7 (export-control persistence
without recalibration) — folded into LS-6 but not strongly
developed; UCA-10 (sanction-as-escalation) — folded into LS-6;
UCA-26 (PRC content rules persisting) — folded into LS-7 with
modest causal development. A third pass would strengthen these.

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

## What this second pass leaves for a third pass

The second pass closes most of the gaps the first pass listed:

| Gap from first pass | Status after second pass |
|---------------------|--------------------------|
| Step 2 sketched as ASCII | Step 2 now has full enumerated tables: 14 controllers, 10 controlled processes, 26 control actions, 13 feedback channels, 10 process-model entries, 12 rung-tagged channels, 5 rung mismatches |
| 15 UCAs (seed) | 65 UCAs (P: 30, N: 13, T: 12, D: 10), grouped by control action |
| 8 loss scenarios with single-cause sketches | 9 loss scenarios with explicit five-class cause analysis; coverage check shows all 65 UCAs accounted for |
| Remedies at class level only | 22 concrete remedy proposals extracted into `remedy-proposals.md` with cost / tractability / time-horizon |

Remaining gaps for a third pass:

- **Process-model articulation (§2.6) covers 10 of 14 controllers.**
  Missing: CTRL-2a, CTRL-3b, CTRL-3c, CTRL-5, CTRL-8a, CTRL-8b,
  CTRL-9, CTRL-10. Adding these would surface UCAs not yet
  enumerated.
- **UCA enumeration is non-exhaustive within each CA.** Some CAs
  generated only 2 UCAs because the symmetric inverses were
  uninteresting; others (CA-1, CA-12) could plausibly support more.
- **Coverage of UCAs 7, 10, 26 in Step 4 is weak.** Folded into
  LS-6 / LS-7 with limited causal development; merit standalone
  scenarios.
- **Cross-bloc symmetry analysis is incomplete.** LS-2 (US lab /
  capital Pattern A) and LS-7 (PRC internal Pattern A) are
  identified as mirrors but the structural symmetry is not
  systematically developed into a single bilateral remedy framework.
- **No quantification.** STPA does not require numerical models, but
  a third pass could attach order-of-magnitude estimates to cycle
  times, UCA frequencies, and remedy costs.
- **No graphical Step 2 diagram.** The §2.1 ASCII overview is
  sufficient for the controllers shown; a graphical diagram would
  scale better.
- **No worked sequencing of remedies.** `remedy-proposals.md` lists
  proposals with tractability and time horizon but does not yet
  produce a sequenced implementation plan (which would belong in a
  separate `decision-memo.md` if a stakeholder commissioned it).

This second pass is sufficient to demonstrate that the SE method
produces structurally different artefacts from chat-level analysis
and points at 22 specific structural interventions, each linked by
explicit causal chain to identified hazards and losses.
