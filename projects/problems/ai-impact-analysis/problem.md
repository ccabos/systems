# Problem: Societal Impact of Frontier AI — Jobs, Welfare, Power Concentration

## Stakeholder

A non-aligned analyst seeking a systems-level understanding of how
the diffusion of frontier AI (LLM-class general-purpose systems and
their successors) will reshape the global economy and political
order over the next 3–10 years. The analyst has no operational
authority and seeks structural understanding, not policy advocacy.

The presenting question came from a chat conversation reproduced in
`chat-analysis.md`. This problem folder documents that analysis and
upgrades it from structured strategic thinking into a partial systems-
engineering treatment.

## Scope and boundary

**Inside the system under analysis:**

- AI labs at the frontier (OpenAI, Anthropic, Google DeepMind, xAI,
  Meta AI Research, and their Chinese counterparts including DeepSeek,
  Alibaba/Qwen, Moonshot/Kimi, Zhipu, ByteDance/Doubao).
- Compute infrastructure providers: chip designers (NVIDIA, AMD,
  Google TPU, Huawei Ascend), foundries (TSMC, Samsung, SMIC),
  hyperscale cloud (AWS, Azure, GCP, Oracle, CoreWeave), and the
  electrical-grid + data-centre layer that sits underneath.
- The application layer: vertical SaaS, agentic platforms, in-house
  enterprise deployments, consumer products.
- The labour market for cognitive work, with explicit attention to
  software engineering as the leading edge of substitution and
  complementarity effects.
- Capital markets allocating to the above.
- Governments as regulators and customers: US (BIS export controls,
  CHIPS Act), China (industrial policy, indigenous compute push),
  EU (AI Act), and the Gulf states / India / Japan as emerging
  AI-infrastructure investors.
- The open-weights ecosystem as a price-setting mechanism on the
  model layer.

**Outside the system (environment):**

- The internal politics of any single state actor (treated as
  constraints, not levers).
- Long-horizon questions of AGI alignment and existential risk
  (relevant context but out of scope for this 3–10 year analysis).
- AI's effects on warfare and autonomous weapons (out of scope;
  warrants a separate problem folder).
- Climate-policy interactions with AI energy demand (acknowledged
  as a constraint via the energy/grid bottleneck, not analysed).

## The presenting question

Given the rapidly falling cost of software production, the rising
power of Chinese open-weight models, and the concentration of capital
into a small number of US AI labs, what is the structural trajectory
of the system with respect to (a) employment and welfare, and (b)
concentration of economic and political power?

## Observed symptoms

- **Software-production cost collapse.** Agentic coding tools
  (Claude Code, Cursor, Codex, Devin, Aider) compress
  routine-implementation tasks from hours to minutes. Hiring patterns
  for entry-level engineers have softened in 2024–2026; senior-engineer
  productivity has risen.
- **Capex concentration.** Frontier training runs cost in the high
  hundreds of millions to low billions of US dollars per model. Fewer
  than ten organisations globally can sustain this cadence.
- **Open-weights pressure.** Chinese open-weight releases
  (DeepSeek-V3 / R1, Qwen 2.5/3, Kimi K2, GLM 4.x) reach within
  6–18 months of US frontier capability on most benchmarks at a small
  fraction of the inference cost, eroding pricing power on the
  model layer.
- **Infrastructure rents.** NVIDIA's gross margins remain at
  historically anomalous levels; TSMC's leading-edge capacity is
  forward-booked; hyperscaler capex is at multiples of historical
  norms. Energy and grid interconnection has become a binding
  constraint in several US regions.
- **Geopolitical decoupling.** US BIS export controls on advanced
  chips, EDA tools, and semiconductor manufacturing equipment
  (October 2022, October 2023, December 2024 expansions) have not
  prevented Chinese frontier-model progress but have accelerated
  Chinese investment in indigenous compute.
- **Labour-market signals.** Software-engineer job postings down
  meaningfully from 2022 peaks; wage growth flat to negative in
  several cognitive-knowledge categories; productivity statistics
  have not yet shown the predicted aggregate boost (consistent with
  Solow's "everywhere but in the productivity statistics" lag).
- **Distributional signal.** Equity-market gains since 2023 have
  concentrated in a narrow set of AI-infrastructure and frontier-lab-
  adjacent firms; broader wage indices have not tracked the gains.

## Goals in tension

### Declared goals of major actors

| Actor | Declared goal |
|-------|---------------|
| US frontier labs | Reach AGI / transformative AI safely; capture commercial returns to fund the mission |
| Chinese frontier labs | Match US capability; commoditise the model layer; build indigenous compute supply chain |
| US government | Maintain US compute and model-layer lead; deny PRC access to advanced compute; manage labour-market disruption |
| Chinese government | Achieve strategic technological independence; deploy AI in productivity and state-capacity applications |
| EU | Regulate for safety, fairness, transparency; capture economic value where possible |
| Compute providers | Maximise hyperscale capex absorption; defend margin against commoditisation |
| Application companies | Build defensible products on a moving model substrate |
| Workers | Maintain wage levels and employment continuity across the transition |
| Capital | Identify and concentrate in winners; minimise exposure to losers |

### Goals in tension

1. **Frontier labs' commercial sustainability vs. open-weights
   commoditisation.** US labs need pricing power to fund frontier
   training; open weights set a price ceiling that erodes that
   pricing power. Labs respond by moving up the stack into product
   and integration, but that competes with their own customers.

2. **US export controls vs. global market access.** Denying PRC
   access to advanced compute is incompatible with maximising NVIDIA
   revenue; the US has chosen denial, accepting the revenue loss and
   accelerating Chinese indigenous capability as a side effect.

3. **Productivity gains vs. labour-share maintenance.** The same
   capability that raises aggregate output also reduces the
   bargaining power of substitutable cognitive workers. Without
   redistribution, productivity → capital, not labour.

4. **Speed of capability deployment vs. social-system absorption
   capacity.** Faster capability gains shorten the time available
   for retraining, institutional adaptation, and political
   negotiation of distributional outcomes.

5. **Frontier-lab autonomy vs. infrastructure-provider leverage.**
   Compute providers (NVIDIA, hyperscalers) capture an increasing
   share of the lab-revenue stack; labs are price-takers on compute
   and price-makers on inference, but the latter erodes faster than
   the former.

## Constraints

- **Physical:** semiconductor fab cycle time (3–5 years for a new
  leading-edge fab), grid-interconnection queue depth (years in
  several US regions), water and cooling for data centres.
- **Capital:** concentration of frontier training capital in a small
  number of investors; willingness of public markets to fund
  multi-year capex without near-term cash flows is bounded.
- **Algorithmic:** efficiency improvements at fixed capability
  appear to compound at roughly 3–4× per year, but this rate is not
  guaranteed forward.
- **Political:** US export controls require allied compliance
  (Netherlands, Japan, South Korea, Taiwan); enforcement is
  imperfect.
- **Legal:** copyright and data-use law remains unsettled in the US,
  EU, and elsewhere; outcomes will affect training-data economics.
- **Knowledge irreversibility:** model weights, once leaked, cannot
  be un-leaked; capability gains cannot be un-discovered.

## What has been tried

| Attempt | Outcome | Notes |
|---------|---------|-------|
| US chip export controls (2022–2024) | Slowed but did not stop PRC frontier progress; accelerated indigenous investment | Loss-scenario candidate: rung-0 coercive feedback to a controller (PRC) operating at rung-1 strategic-identity logic |
| Voluntary lab safety commitments (2023 White House, 2024 Seoul / Bletchley) | Limited operational effect; superseded by national regulation | Weak control loop — feedback is reputational, no enforcement |
| EU AI Act (in force 2024–2026, phased) | First comprehensive horizontal regulation; cost-of-compliance effects unclear | Rung-2/4 control action onto a system whose state changes faster than the regulatory cycle |
| Industry self-regulation via responsible-scaling policies (Anthropic, OpenAI, GDM) | Internal control loops without external verification; concentration of authority within labs | Self-sealing process model risk |
| Universal-basic-income pilots (Finland, Stockton, Kenya GiveDirectly) | Mixed evidence; politically marginal at scale | Pre-emptive distributional remedy not yet adopted by any major economy |
| Sector-specific retraining programmes (US Workforce Innovation, EU New Skills Agenda) | Historical effectiveness modest; no AI-era track record | Slow control loop versus a fast disturbance |

## Analytical approach

The analysis in this folder proceeds in four layers, each
deliberately distinct:

1. `chat-analysis.md` — the original chat-conversation analysis,
   preserved as a record of what *structured strategic thinking*
   produced before any SE method was applied. This is the baseline
   against which the SE upgrade is measured.

2. `methodology-critique.md` — an explicit, self-critical comparison
   of the chat analysis against the SE techniques catalogued in
   `knowledge/se-techniques/`. Honest about which steps were
   actually applied and which were merely gestured at with systems
   vocabulary.

3. `analysis.md` — full STPA analysis with justification-rung
   tagging. Step 1 (losses, hazards, constraints) complete; Step 2
   (control structure) with enumerated controllers, controlled
   processes, control actions, feedback channels, and process
   models; Step 3 with 65 UCAs across 26 control actions; Step 4
   with 9 loss scenarios covering all UCAs, with explicit five-class
   cause analysis.

4. `remedy-proposals.md` — 22 concrete remedy proposals (R-1
   through R-22) linked to the loss scenarios, each with cost /
   tractability / time-horizon and sequencing notes.

Sequence: critique first, then constructive SE work. The
sequence matters: claiming SE rigor without the artefacts is
exactly the rung-1 / rung-3 mismatch the rungs framework warns
against.

## Deliverables

- `problem.md` (this document) — framing and constraints.
- `chat-analysis.md` — the original chat-level analysis verbatim.
- `methodology-critique.md` — honest assessment of what was and
  was not systems engineering.
- `analysis.md` — STPA analysis: Step 1 losses/hazards/constraints,
  Step 2 enumerated control structure with rung tagging, Step 3
  with 65 UCAs, Step 4 with 9 loss scenarios.
- `remedy-proposals.md` — 22 remedies (R-1–R-22) with cost,
  tractability, time-horizon, and sequencing notes.

## Status

_second pass complete — chat analysis preserved, methodology
critique written, full STPA delivered (Step 2 enumerated, 65 UCAs
in Step 3, 9 loss scenarios in Step 4), and 22 remedy proposals
extracted. Remaining gaps for a third pass are listed at the end
of `analysis.md`: complete process-model coverage for the
remaining 4 controllers, more UCAs within sparsely-enumerated CAs,
graphical Step 2 diagram, and a sequenced `decision-memo.md`._
