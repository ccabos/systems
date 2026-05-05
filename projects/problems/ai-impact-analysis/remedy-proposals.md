# Remedy proposals

_Companion to `analysis.md`. Each remedy is referenced from the Step 4
loss scenario(s) it addresses. Remedies are proposed; tractability and
time horizon are honest estimates for current (2026) political and
institutional conditions, not normative recommendations._

Notation:

- **Pattern** — which `dangerous-mismatches.md` pattern the remedy
  closes (A: rung-elevation; B: claim/operation alignment; C: domain-
  appropriate rung containment), or "cadence" for cadence-matched
  controls, or "new-controller" for additions to the structure.
- **Cost** — order-of-magnitude resource cost (low / medium / high)
  considering both fiscal cost and political capital.
- **Tractability** — likelihood of adoption in a 5-year window given
  current institutional incumbents (low / medium / high).
- **Time horizon** — time from political adoption to material effect
  on the controlled process.

## R-1 — Reservation requirements on leading-edge supply

**Addresses:** LS-1 (UCA-46, 50, 52, 53).

**Mechanism:** A statutory or regulatory rule that reserves a
minimum fraction (e.g. 10–20 %) of leading-edge GPU/accelerator
output and hyperscale capacity for non-frontier customers,
defined by capability tier or revenue threshold. The reservation
is enforceable against contracts that would otherwise foreclose
this fraction.

**Pattern:** cadence-matched controls (the rule binds at r2 with
r3 cadence, matching the contract cycle that creates the
foreclosure).

**Cost:** medium fiscal (audit and enforcement); medium political
(opposed by hyperscalers, supported by smaller labs and startup
ecosystem).

**Tractability:** medium. Analogous to common-carrier rules in
telecoms; conceptually familiar to regulators.

**Time horizon:** 18–36 months from rule adoption to first effect;
3–5 years for full structural effect.

## R-2 — Merger-review reform to capture contract-level foreclosure

**Addresses:** LS-1 (UCA-11, 50).

**Mechanism:** Update merger-review thresholds and Section 2 (US)
/ DG-COMP enforcement guidance to recognise long-duration exclusive
compute-allocation contracts and bundled tying as conduct to be
reviewed regardless of M&A status. Statutory authority to
investigate and order divestiture of contractual entitlements.

**Pattern:** Pattern C — domain-appropriate rung containment (route
foreclosure events, currently r3-private, into the r2/r4 antitrust
forum). Closes M5.

**Cost:** medium fiscal; high political (challenges entrenched
M&A-only paradigm).

**Tractability:** low–medium. US FTC has signalled interest;
challenged in courts; partial PRC and EU analogues exist.

**Time horizon:** 3–7 years (rule + litigation + remedy).

## R-3 — Expedited capability-jump merger review window

**Addresses:** LS-1 (UCA-49, 12).

**Mechanism:** Statutory authority for antitrust authorities to
impose a temporary review hold on long-duration compute and capacity
contracts during defined "capability-jump windows" (declared by
CTRL-2e on the basis of FB-1). Holds expire automatically after
review.

**Pattern:** cadence-matched controls.

**Cost:** low fiscal; high political (opposed as government overreach
into private contracts).

**Tractability:** low. Novel authority.

**Time horizon:** 5–10 years.

## R-4 — Mandatory pre-deployment evaluation by independent body

**Addresses:** LS-2 (UCA-14, 15, 36, 39).

**Mechanism:** Statutory requirement that capability-tier models be
evaluated by an independent body (US AISI, UK AISI, EU AI Office, or
joint successor) before public release above a defined threshold.
The body has classified-access authority where needed; results above
threshold are publishable in standardised form.

**Pattern:** Pattern A — rung-elevation of the feedback channel
(parallel r3 channel that bypasses the lab's r1 wrapping in CH4).

**Cost:** medium fiscal (build out testing infrastructure);
medium–high political (industry resistance to mandatory access).

**Tractability:** medium. UK and US AISIs exist; their statutory
authority is the limiting variable. EU AI Act provides a partial
template.

**Time horizon:** 18–36 months from statutory authority to first
binding evaluation.

## R-5 — Structural separation of safety governance from commercial governance

**Addresses:** LS-2 (UCA-32, 33, 41, 42, 43).

**Mechanism:** Require that lab safety frameworks be governed by a
body separate from the commercial board, with binding (not advisory)
authority over deployment thresholds. Members appointed by a
mechanism not controlled by capital. Frameworks publicly committed
and amended only by published process. Enforceable PBC mission
constraints, not advisory trust-and-safety boards.

**Pattern:** Pattern B — close the claim/operation gap (raise the
operation rather than lower the claim).

**Cost:** medium fiscal (legal restructuring); medium–high political
(opposed by capital that loses the cadence lever).

**Tractability:** low–medium. Partial precedents in PBC structures
of Anthropic and others; depends on whether structural protections
are enforceable rather than rhetorical.

**Time horizon:** 5–10 years for industry-wide effect; specific labs
can move faster unilaterally.

## R-6 — Capital-structure mission constraints with statutory enforcement

**Addresses:** LS-2 (UCA-32, 33).

**Mechanism:** A statutory class of "AI public-benefit corporation"
with mission constraints enforceable by the state attorney general
or analogous public agent (not only by shareholders). Tax or
regulatory benefits conditional on adoption.

**Pattern:** Pattern B + new-controller.

**Cost:** medium.

**Tractability:** medium in US (Delaware statutory tradition); harder
elsewhere.

**Time horizon:** 3–7 years.

## R-7 — Task-displacement-indexed automatic stabilisers

**Addresses:** LS-3 (UCA-37, 56, 57, 60, 62).

**Mechanism:** Unemployment insurance, retraining credits, and
income support indexed to a published task-displacement benchmark
(BLS / EU equivalent / OECD), not to headline employment. Triggers
fire when the benchmark crosses thresholds without further
legislative action — closing the M3 cadence mismatch by removing
the rung-3/4 confirmation requirement per cycle.

**Pattern:** cadence-matched controls (automatic), new-controller
(benchmark-publishing body).

**Cost:** medium–high fiscal (depends on threshold calibration);
medium political (familiar UI architecture, novel index).

**Tractability:** medium. Operationally similar to existing UI
extensions during recessions; index construction is the technical
bottleneck.

**Time horizon:** 24–48 months.

## R-8 — Cohort-specific transitions for early-career cognitive workers

**Addresses:** LS-3 (UCA-61, 63), L8 specifically.

**Mechanism:** Targeted programmes — wage subsidies, retraining
credits, apprenticeship guarantees — for the cohort of
early-career cognitive workers most exposed to substitution. Funded
through R-10 / R-11 mechanisms.

**Pattern:** new-controller (a cohort-tracking authority that no
existing labour ministry has).

**Cost:** medium.

**Tractability:** medium. Partial analogue: post-WWII GI Bill;
dislocated-worker programmes.

**Time horizon:** 24–60 months.

## R-9 — Portable benefits independent of employer

**Addresses:** LS-3 (UCA-56, 63).

**Mechanism:** Healthcare, retirement, and skill-credit
portability that does not depend on continuous employment with a
single employer. Reduces the cost to workers of moving across the
substitution boundary.

**Pattern:** new-controller (or existing controller scope expansion).

**Cost:** medium–high.

**Tractability:** medium. Bipartisan US support exists in principle;
implementation contested.

**Time horizon:** 5–10 years.

## R-10 — Productivity-indexed dividend

**Addresses:** LS-4 (UCA-8, 9, 35, 63).

**Mechanism:** A per-capita dividend funded by a tax indexed to
aggregate AI-driven productivity gain (measured at the sector or
firm level). Distinguishes itself from generic UBI by being
explicitly tied to the surplus from which it is funded — a
transmission channel rather than a redistribution programme.

**Pattern:** new-controller / new-channel.

**Cost:** high fiscal; high political.

**Tractability:** low. Closest analogue is Alaska Permanent Fund
(natural-resource-indexed dividend); no peer for productivity.

**Time horizon:** 10+ years.

## R-11 — Value-added tax on AI inference with hypothecated dividend

**Addresses:** LS-4 (UCA-8, 9, 11, 12).

**Mechanism:** A modest VAT or excise on AI inference (per token or
per compute unit), hypothecated to a public dividend or sovereign
fund. Lower bar than R-10 because it taxes the visible economic
flow rather than imputed productivity gain.

**Pattern:** new-controller / new-channel.

**Cost:** medium fiscal; high political (industry opposition).

**Tractability:** low–medium. Easier than R-10; harder than ordinary
tax adjustments.

**Time horizon:** 5–10 years.

## R-12 — Expanded EITC indexed to displacement benchmark

**Addresses:** LS-3 / LS-4 boundary (UCA-9, 60, 63).

**Mechanism:** Earned-income tax credit (or peer-country equivalent)
expanded with a top-up indexed to the same task-displacement
benchmark used in R-7. Targets workers in the affected occupations
without requiring proof of individual displacement.

**Pattern:** existing-controller scope expansion.

**Cost:** medium fiscal; low–medium political.

**Tractability:** medium–high. EITC is established; expansion is
operationally familiar.

**Time horizon:** 12–36 months.

## R-13 — Sovereign-wealth participation in AI infrastructure

**Addresses:** LS-4 (UCA-11, 12, 35).

**Mechanism:** Public equity participation in AI infrastructure
(compute, energy) through sovereign wealth funds, with returns
flowing to a public dividend or general revenue. Norway / GIC /
Mubadala / Singapore Temasek precedents in adjacent sectors.

**Pattern:** new-controller (or existing-controller scope expansion
where SWFs exist).

**Cost:** high upfront capital deployment; medium political.

**Tractability:** medium where SWFs already exist; low elsewhere
(US lacks one at federal level).

**Time horizon:** 5–10 years; capital deployment can be faster but
governance and dividend mechanism is the slow part.

## R-14 — Open-weights gap as published policy variable

**Addresses:** LS-5 (UCA-2, 55).

**Mechanism:** A statutory or regulatory requirement that an
identified body (CTRL-2e / CTRL-4a / NIST / EU AI Office) publish a
quarterly assessment of the frontier-vs-open-weights capability gap
on standardised benchmarks, and that any rule affecting open-weights
release explicitly weigh impact on this gap as a documented input.

**Pattern:** Pattern C — domain-appropriate rung containment (forces
the regulator's process model to include the price-setting variable).
Closes the process-model failure named in LS-5.

**Cost:** low.

**Tractability:** medium. Operationally similar to existing
benchmark-tracking obligations; politically novel.

**Time horizon:** 12–24 months.

## R-15 — Targeted misuse-risk regime for open weights that preserves the price-setting mechanism

**Addresses:** LS-5 (UCA-2, 55).

**Mechanism:** Restrict specific identified misuse-risk capabilities
(CBRN uplift; defined cyber-offence categories) at the model release
boundary, while explicitly preserving the open-weights ecosystem
below those thresholds. Avoids the all-or-nothing regulation that
would suppress the price-ceiling.

**Pattern:** Pattern C.

**Cost:** medium.

**Tractability:** medium. Threshold-design is the technical bottleneck.

**Time horizon:** 24–48 months.

## R-16 — Independent inspection / observation regime for AI infrastructure

**Addresses:** LS-6, LS-7 (UCA-4–6, 17–24, 30, 31, 48; PRC mirror UCA-20–21).

**Mechanism:** A multilateral verification regime for AI-
infrastructure deployments (compute clusters above a threshold,
training runs above a FLOP threshold). Analogues: IAEA
safeguards, OPCW chemical-weapons inspection, Open Skies (now
defunct but precedent). Operates at r3 (verification) bypassing
the r1 strategic-claim filter on both sides.

**Pattern:** Pattern A bilaterally.

**Cost:** high fiscal (institution build); very high political.

**Tractability:** very low in current geopolitical climate.
Conditions for tractability: reciprocal access; technical
specification of what can be verified without revealing weights;
trusted neutral body.

**Time horizon:** 10+ years for any binding regime; voluntary
confidence-building precursor (track 1.5) is achievable in 3–5
years.

## R-17 — Geographic diversification of fab capacity

**Addresses:** LS-6 (UCA-48).

**Mechanism:** Coordinated public investment (US CHIPS Act, EU Chips
Act, JP / KR analogues) sustained over a decade to bring leading-
edge fab capacity outside Taiwan to a strategically meaningful
fraction. Already in progress; the question is sustained political
commitment across electoral cycles.

**Pattern:** controlled-process state change (move CP-2 to a less
chokepoint-vulnerable state).

**Cost:** very high fiscal (~$100B+ globally, multi-year);
medium political (bipartisan in US; less so in some allies).

**Tractability:** medium. CHIPS Act exists but is contested;
implementation lags; PRC indigenous capacity advances in parallel.

**Time horizon:** 10+ years to material effect.

## R-18 — Track 1.5 AI-infrastructure confidence-building

**Addresses:** LS-6 (preparation step for R-16).

**Mechanism:** Ongoing semi-official dialogues between US, PRC,
EU, and other AI-state experts on infrastructure-level confidence-
building measures. No binding authority; produces shared technical
language and small reciprocal transparency steps.

**Pattern:** rung-elevation precursor (creates the shared
vocabulary R-16 needs).

**Cost:** low.

**Tractability:** medium-high; some dialogues exist (e.g.
US–China Track II).

**Time horizon:** 1–3 years for first work product; 5+ years
for any reciprocal transparency.

## R-19 — Mandatory provenance at capture / transmission layer

**Addresses:** LS-8 (UCA-58, 59, 64, 65).

**Mechanism:** Mandate provenance signals (cryptographic
attestation, C2PA, equivalent) at the capture (camera, OS)
and transmission (model output API) layers, not at the platform
layer. Standardised, redundant, and verifiable. Voluntary regimes
(C2PA opt-in) move to mandatory regimes in defined contexts
(news, election content, paid advertising).

**Pattern:** controlled-process state change (move CP-6 to a
state where provenance is the default).

**Cost:** medium fiscal (standards work); medium political
(industry resistance).

**Tractability:** medium. C2PA and equivalents have industry
adoption; mandatory regimes have legislative momentum in EU
and several US states.

**Time horizon:** 24–48 months.

## R-20 — Aggregate provenance-failure measurement

**Addresses:** LS-8 (UCA-65; closes FB-10 weakness).

**Mechanism:** A statutory body publishes a quarterly measurement
of aggregate provenance-failure rate on a sampled basis across
major information platforms. Provides the missing FB-10 channel
that regulators and the public need to evaluate R-19's
effectiveness.

**Pattern:** new-feedback-channel.

**Cost:** low–medium.

**Tractability:** medium. Sampling methodology is the technical
bottleneck; political bottleneck is platform compliance.

**Time horizon:** 24–36 months.

## R-21 — Capability-tier rules indexed to a moving benchmark with sunset

**Addresses:** LS-9 (UCA-1, 27, 28, 29).

**Mechanism:** AI legislation and regulation drafted with rules
keyed to a moving capability benchmark (computed by CTRL-2e /
CTRL-4a) rather than a fixed FLOP / dollar threshold. Sunset
clauses force re-passage if the regulator does not recalibrate.

**Pattern:** cadence-matched controls.

**Cost:** low fiscal; medium political (departs from fixed-threshold
legal tradition).

**Tractability:** medium. Some EU AI Act mechanisms gesture this
direction; full implementation novel.

**Time horizon:** 3–7 years for embedded rules; faster for new
legislation drafted from scratch.

## R-22 — Standing AI-impact assessment with statutory recalibration authority

**Addresses:** LS-9 (UCA-27, 28, 29).

**Mechanism:** A standing body (could be CTRL-2e / CTRL-4a expanded)
with statutory authority to recalibrate capability-tier thresholds
without primary legislation, subject to a defined notice-and-comment
process. Closes the M3-mirror at the regulatory cadence boundary.

**Pattern:** new-controller / cadence-matched controls.

**Cost:** medium fiscal; medium–high political (delegated authority
is contentious).

**Tractability:** low–medium. Closest US analogue: SEC rule-making;
EU analogue: Commission delegated acts. Politically more contested
than either.

**Time horizon:** 5–7 years.

---

## Sequencing notes

A full sequenced implementation plan belongs in a `decision-memo.md`
that does not yet exist. Pending that, this section flags the
obvious sequencing constraints visible in the remedy set:

- **Fast (12–36 months):** R-1, R-7, R-12, R-14, R-19, R-20. These
  are operationally familiar and use existing institutional
  infrastructure.
- **Medium (3–7 years):** R-2, R-4, R-5, R-6, R-9, R-11, R-13, R-15,
  R-21, R-22. These require new statutes or substantial regulatory
  reform but draw on identifiable precedents.
- **Slow (10+ years):** R-3, R-10, R-16, R-17. These are politically
  hardest, structurally most novel, or constrained by physical /
  industrial cycles.
- **Precondition / preparatory:** R-18 is a precursor to R-16; R-14
  and R-20 are measurement preconditions for R-15 and R-19
  respectively; R-7 cannot be calibrated without the same task-
  displacement benchmark used in R-12.
- **Adversarial coupling:** R-2 and R-1 are jointly more effective
  than either alone (R-1 prevents new foreclosure; R-2 unwinds
  existing foreclosure); R-19 without R-20 is unverifiable.
- **Geopolitical sensitivity:** R-15, R-16, R-17, R-18 cannot be
  unilateral; their tractability depends on coalition state.
- **Coverage:** the 22 remedies collectively address all nine LS;
  the highest-leverage single remedy is R-4 (touches LS-2 directly
  and LS-1 / LS-8 indirectly via the feedback-channel it creates).

A third pass would convert these notes into a sequenced plan with
dependencies, decision points, and reversibility analysis per
remedy.
