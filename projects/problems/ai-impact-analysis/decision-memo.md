# Decision memo: sequenced implementation plan for the 22 remedies

_Companion to `analysis.md` and `remedy-proposals.md`. Converts the
22 proposals into a sequenced plan, names the entry points where a
non-state actor (analyst, philanthropy, lab, civil society) can
move first, and identifies decision points where intermediate
outcomes determine which downstream remedy becomes available._

This memo does not advocate. It identifies a structural sequence
implied by the dependency graph in the remedy set, and the
controllers each step requires. A stakeholder with different goals
or constraints would re-order the same set differently — but the
dependencies (R-18 before R-16; R-20 before R-19 enforcement; R-7
and R-12 sharing the same benchmark) are not optional.

## Remedy dependency graph

```
                            R-14 (open-weights gap as policy var)
                              │
                              ▼
R-18 (track 1.5)  ──►  R-15 (targeted misuse-risk regime)
   │                          │
   ▼                          ▼
R-16 (verification regime) ◄─ R-17 (geographic fab diversification)


R-20 (provenance measurement)
   │
   ▼
R-19 (mandatory provenance)


R-7 (auto-stabilisers indexed to displacement) ─┐
                                                 ├─► same benchmark required
R-12 (EITC indexed to displacement) ────────────┘
   │
   ▼
R-8 (cohort-specific transitions) ──► R-9 (portable benefits)


R-1 (reservation requirements) ──► R-3 (capability-jump review)
   │
   ▼
R-2 (merger-review reform for contract foreclosure)


R-4 (mandatory pre-deployment evaluation)
   │
   ├─► R-5 (structural separation of safety governance)
   │
   └─► R-6 (statutory PBC-class with mission constraints)


R-10 (productivity-indexed dividend) ◄── R-11 (VAT on inference)
                                              │
                                              ▼
                                         R-13 (sovereign-wealth)


R-21 (rules indexed to moving benchmark) ──► R-22 (recalibration authority)
```

## Phase 1 — months 1–18: measurement and feedback channels

The fastest gains come from measurement: closing the feedback-
channel gaps in the control structure so that subsequent rule-making
operates on r3 evidence rather than r1 narrative.

**Entry remedies (no statutory change required for first version):**

- **R-14** — publish a quarterly frontier-vs-open-weights gap
  assessment. *Entry point:* AISI / NIST / EU AI Office can
  initiate as a non-binding publication. *Decision point at month
  12:* if any major rule-making (CA-1 or CA-10) cited the gap,
  the channel is live; if not, statutory mandate becomes the
  next move.
- **R-20** — aggregate provenance-failure measurement. *Entry
  point:* national statistics offices, academic consortia, or a
  philanthropy-funded measurement body. *Decision point at month
  18:* baseline established → R-19 mandate becomes specific.
- **R-7 / R-12 shared benchmark** — task-displacement index.
  *Entry point:* BLS / Eurostat / OECD existing labour data + AI
  task-mapping research. *Decision point at month 18:* benchmark
  is public and stable enough to use as a statutory trigger.
- **R-18** — track-1.5 AI-infrastructure dialogue. *Entry point:*
  existing US–China Track II forums, Wilson Centre, EastWest
  Institute, NTI, similar PRC counterparts. *Decision point at
  month 18:* shared technical vocabulary exists for what
  AI-infrastructure verification could mean.

**Why these first.** Each of the four creates the empirical input
later remedies rely on. They are also the four lowest-cost
fastest-tractability proposals in the set; failure of any one
costs little and tells the planner something useful.

## Phase 2 — months 12–48: rules built on the new feedback channels

Once the measurement channels of Phase 1 are operating, rule-making
can index to them.

**Statutory or regulatory action (US / EU primary, allies follow):**

- **R-19** mandatory provenance, indexed to R-20 measurement.
- **R-1** reservation requirements on leading-edge supply.
- **R-15** targeted misuse-risk regime for open weights, indexed
  to R-14.
- **R-21** capability-tier rules indexed to a moving benchmark,
  with sunset clauses.
- **R-22** standing AI-impact assessment with statutory
  recalibration authority.
- **R-12** EITC expansion indexed to the displacement benchmark.
- **R-7** automatic stabiliser triggers indexed to the displacement
  benchmark.
- **R-4** mandatory pre-deployment evaluation by AISI-class body
  (the statutory authority that makes Phase 1 R-14 binding rather
  than advisory).

**Entry points for non-state actors.** The statutory work happens
inside legislatures, but non-state actors shape it through:

- Drafting model-bill language that legislatures can adopt
  (Aspen, Brookings, AI Policy Institute, GFI).
- Litigation that forces existing antitrust authority onto
  contract-level foreclosure (private antitrust actions; state
  AGs).
- Coalition-building among open-weights-dependent application
  companies whose business is foreclosed by R-1's absence.

**Decision point at month 36.** Have at least three of the eight
been adopted? If yes, Phase 3 is structurally feasible. If not,
the remaining gaps reveal which controllers were actually
unwilling, and Phase 3 design must route around them.

## Phase 3 — months 36–84: structural remedies

The harder structural remedies require the political capital that
Phase 1 and Phase 2 generate, and the empirical record that
shows whether the easier remedies were sufficient.

**Structural remedies (5–7 year horizon):**

- **R-2** merger-review reform for contract-level foreclosure.
- **R-5** structural separation of safety governance from
  commercial governance.
- **R-6** statutory PBC-class with mission constraints
  enforceable by public agent.
- **R-8** cohort-specific transition programmes for early-career
  cognitive workers.
- **R-9** portable benefits independent of employer.
- **R-11** VAT on inference with hypothecated dividend.
- **R-13** sovereign-wealth participation in AI infrastructure
  (SWF jurisdictions only; US separately if it adopts one).

**Decision points at month 60.** Has the M3 cadence mismatch
been substantially closed by Phase 2 R-7 + R-12? If yes, R-8 and
R-9 are accelerants rather than emergency measures. If no, they
move forward in priority.

## Phase 4 — months 60–144: the slow remedies

The four 10+ year remedies cannot be substantially shortened.
They are listed here for sequencing rather than fast action.

- **R-3** expedited capability-jump merger review window.
  Politically novel; awaits the political space Phase 2 creates.
- **R-10** productivity-indexed dividend. Awaits R-11 to build
  the operational substrate.
- **R-16** independent inspection / observation regime for AI
  infrastructure. Awaits R-18 vocabulary and R-17 chip
  diversification (so verification has somewhere to look that
  is not already monopolised).
- **R-17** geographic fab diversification. Already in progress
  via CHIPS Act and EU Chips Act; the question is sustained
  political commitment across electoral cycles.

## Reversibility analysis

Most of the proposed remedies are reversible at moderate cost
within their first cycle:

- **Reversible at low cost:** R-14, R-18, R-20, R-7 (trigger
  thresholds adjustable), R-12.
- **Reversible at medium cost:** R-1, R-4, R-15, R-19, R-21, R-22.
- **Reversible at high cost:** R-5, R-6, R-13, R-17 (fab capex
  is sunk).
- **Irreversible in practical terms within decade:** R-16 (once
  established, withdrawal would itself signal an escalation
  posture), R-10 (once established as a household income source).

A risk-averse stakeholder would weight Phase 1 and Phase 2
preferentially. A loss-averse stakeholder considering tail risks
(LS-6 kinetic escalation; LS-3 mass cohort displacement) would
weight R-16 and R-7 more heavily despite their costs.

## Coalition dependencies

Several remedies require coalitions that do not currently exist:

- **R-1, R-2** require open-weights labs + non-frontier application
  companies + small cloud providers acting together against
  hyperscaler / frontier-lab interests.
- **R-4, R-5, R-6** require capital actors who *prefer* mission
  constraints (long-horizon mission-aligned funds, public
  pension funds, certain sovereign wealth funds) acting against
  capital actors who prefer cadence.
- **R-7, R-8, R-9, R-12** require labour, education ministries,
  and centre-left coalitions that exist but have not yet
  converged on AI as their organising issue.
- **R-16, R-17, R-18** require diplomatic capital across blocs
  that the current crisis cycle erodes faster than it accumulates.

The sequencing above assumes coalitions form roughly on schedule;
where they do not, alternative routes through the dependency graph
are available but less efficient.

## What this memo does not do

- **Does not advocate.** Identifies a structural sequence; does
  not argue that any particular remedy is normatively justified
  beyond the LS it addresses.
- **Does not quantify cost.** Estimates in `remedy-proposals.md`
  are order-of-magnitude. Detailed costing belongs in a
  jurisdiction-specific analysis.
- **Does not prioritise across loss scenarios.** A planner who
  rates LS-6 (kinetic conflict) above LS-3 (cohort displacement)
  would re-weight R-16 and R-7 differently than this memo
  implies. The dependency graph constrains the ordering, not
  the weighting.
- **Does not address allocation across jurisdictions.** US, EU,
  and PRC face different feasible subsets of these remedies; a
  multilateral version of this memo would map each remedy to
  the jurisdictions that can realistically adopt it.

A fourth pass would address these by producing a stakeholder-
specific decision memo (e.g. "what should a US foundation
allocate $50M to over five years, given these 22 remedies"),
which would in turn require the costing and quantification flagged
in `analysis.md` as third-pass gaps not yet closed.
