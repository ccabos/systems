# Justificatory Rungs

!!! info "Canonical reference"
    The normative statement of the seven-rung ladder, its three
    rung-mismatch patterns, and the seven hooks into STPA Steps 1–4
    are maintained as the project's knowledge base under
    `knowledge/se-techniques/justification-rungs/`. This chapter is
    the narrative introduction; the knowledge base is the reference.

## What this chapter adds to the book

Parts I and IV introduce STPA — the safety-and-control analysis at
the heart of this book. STPA tells us *which control actions are
unsafe*. It does not tell us *why a control action that should land
does not*. That second question is the everyday experience of social
systems: the bishop's sermon does not sway the empirically-minded
congregant, the scientist's data does not move the believer, the
parliament's resolution does not constrain the autocrat. In each
case the control action is issued, transmitted, and received — but
the receiver does not accept it as a *reason* to change behaviour.

The reason is that human beings act on different **standards** for
what counts as a decisive reason. There are seven of them in this
book's analysis. They form a ladder, and most of the catastrophic
failures of social systems are traceable to mismatches on that
ladder: between the two ends of a control loop, or between what a
controller *claims* and what it *operates on*.

## The seven rungs at a glance

| Rung | Standard | Where you meet it |
|------|----------|-------------------|
| 0 | Power / coercion ("do it or else") | Coups, monopolies, threats |
| 1 | Authority / rhetoric / identity | Slogans, scripture, "as a parent…" |
| 2 | Formal consistency | Math proofs, court syllogisms |
| 3 | Empirical testability | Randomised trials, falsification |
| 4 | Cumulative evidence and consilience | Meta-analyses, IPCC reports |
| 5 | Meta-rational integration | Risk engineering, AI-safety, complex-systems policy |
| 6 | Normative legitimacy / deliberative ethics | Constitutional courts, citizens' assemblies |

Each later rung adds a *check* that earlier rungs lack:

- **Rung 0 → Rung 1.** The receiver moves voluntarily, without a
  threat, because they recognise the source as legitimate. Rung 1
  has no check on truth or consistency — but it has stopped using
  raw force.
- **Rung 1 → Rung 2.** A consistency check appears: even an
  authority cannot make an inconsistent argument win. Contradictions
  lose. This is the first *internal* check.
- **Rung 2 → Rung 3.** An *external* check appears: data can sink a
  consistent theory if its premises do not match the world.
- **Rung 3 → Rung 4.** The check is broadened against single-study
  flukes, publication bias, and method artefacts. Findings have to
  hold up across replications and methods.
- **Rung 4 → Rung 5.** The receiver becomes able to step *outside*
  any single method, recognise its limits, and combine methods
  under uncertainty. Rung 5 is rare, fragile, and cognitively
  costly.
- **Rung 5 → Rung 6.** A second kind of question appears that no
  amount of rung-5 sharpening can answer: *what should we do?*
  Rung 6 is the check that surviving open inclusive discourse
  imposes on claims about *oughts*.

The full rung definitions and examples are in
`knowledge/se-techniques/justification-rungs/rungs.md`.

## The seven rungs in detail

Each rung admits four questions: what is the standard, where do you
meet it, what does the rung *add* over the previous one, and what
does it still *lack* — and one extra question that matters for
STPA: how does the rung *show up* in a control structure when
something goes wrong.

### Rung 0 — Power / coercion

The standard is "do it or else." Compliance is enforced by threat
of sanction, violence, or exclusion; there is no shared criterion
for what is true, valid, or fair. Two parties at rung 0 cannot
disagree productively — they can only enforce or submit. Examples
range from coups and occupation regimes to organised crime and
parental "because I said so."

What rung 0 *lacks*: any common standard at all. In an STPA
control structure this shows up as control actions that land
without persuasion and feedback that either flatters the controller
or is suppressed. Loss scenarios concentrate around the absence of
corrective feedback — the controller cannot be wrong because the
controller cannot be questioned.

### Rung 1 — Authority / rhetoric / identity

A claim is decisive because of *who* makes it, *what tradition* it
comes from, or *what group* the listener identifies with. The
listener moves voluntarily, but without an obligation to check
truth or consistency. Examples: campaign slogans, scripture,
"as a parent…", brand loyalty, expert testimony where the listener
cannot evaluate the substance, charismatic leadership.

What rung 1 *adds* over rung 0: voluntary acceptance — the listener
moves without a sanction being threatened. What rung 1 *lacks*: any
internal check. Two contradictory rung-1 authorities cannot
adjudicate the contradiction without escalating to rung 0 (force)
or rung 2+ (some standard outside personal authority). In STPA
terms, rung-1 controllers treat *who said it* as the deciding
factor; feedback that comes from the wrong source is dismissed
regardless of content. The self-sealing process models catalogued
in the next chapter are most often rung-1 process models.

### Rung 2 — Formal consistency

A conclusion follows validly from premises both parties already
accept. The argument can be checked step by step; contradictions
lose. Examples: mathematical proofs, court syllogisms, formal
logic, rule-based bureaucratic decisions, legal reasoning within an
established code.

What rung 2 *adds* over rung 1: an *internal* check. Even an
authority cannot make an inconsistent argument win — a rung-2
challenge can defeat a rung-1 claim by exhibiting contradiction
within the claim's own premises. What rung 2 *lacks*: an *external*
check. Premises themselves are not tested against the world. Loops
that operate at rung 2 produce internally coherent decisions that
may diverge from external reality — the characteristic failure is
the system that "follows the rules" straight into harm.

### Rung 3 — Empirical testability

A hypothesis is decisive only if it survives tests against rivals
— controlled experiments, falsification, prediction against unseen
data. Examples: randomised trials, falsification in physical
sciences, A/B tests, engineering acceptance tests, audited
financial statements.

What rung 3 *adds*: an *external* check. Data can sink a neat
theory; premises themselves become accountable to observation. What
rung 3 *lacks*: protection against one-off flukes, publication
bias, p-hacking, and the small-N problem. A single positive trial
does not yet make a robust claim. Rung-3 feedback channels are
powerful but fragile — a single biased sample can defeat them — so
loops that operate at rung 3 require active maintenance of the
channel's integrity (independence of the auditor, pre-registration
of trials, replication budgets).

### Rung 4 — Cumulative evidence and consilience

A claim is decisive when results survive replication and line up
across multiple methods, populations, and disciplines.
Meta-analyses, systematic reviews, and cross-method triangulation
beat single studies. Examples: evidence-based medicine, IPCC
assessment reports, well-replicated psychology effects,
cross-discipline syntheses, regulatory science.

What rung 4 *adds*: robustness against flukes, biases, and method
artefacts. A finding that holds up across independent methods is
harder to explain away. What rung 4 *lacks*: a way to handle
situations in which the methods themselves are in dispute, or where
no single method applies, or where the question is partly
normative. Rung-4 feedback is slow but durable; systems that depend
on it (climate policy, drug regulation) have characteristic failure
modes around delay — the rung-4 signal arrives only after
irreversible action.

### Rung 5 — Meta-rational integration

A claim is decisive when the speaker can show *why* a method works,
*when it breaks*, and *how to combine multiple methods* under
uncertainty. The speaker steps outside any single formalism to
choose the right one for the question. Examples: risk engineering,
AI-safety research, complex-systems policy labs, integrated
assessment in climate policy, intelligence analysis at its best.

What rung 5 *adds*: an acknowledgement that no single method covers
all messy domains, and a discipline for choosing among methods
rather than defaulting to one. Rung 5 is where one becomes able to
talk sensibly about model failure, unknown unknowns, and the limits
of one's own evidence. What rung 5 *lacks*: any answer to *what
should be done* once the empirics are settled. Rung 5 sharpens
facts; it does not deliver oughts. Rung-5 controllers can hold
multiple feedback channels in superposition — a rung-3 RCT, a
rung-1 stakeholder intuition, a rung-2 legal constraint — and
weight them appropriately. This is rare, fragile, and cognitively
costly.

### Rung 6 — Normative legitimacy / deliberative ethics

A claim is decisive when it survives open, inclusive discourse and
meets normative criteria — fairness, reversibility,
universalisability, respect for the autonomy of the affected. Even
perfect facts and models do not tell us *oughts*; society still has
to justify rules to all affected by them. Examples: constitutional
courts, citizens' assemblies, Habermasian deliberative democracy,
well-functioning parliamentary deliberation, bioethics committees.

What rung 6 *adds*: a way to settle questions about what should be
done that cannot be reduced to fact — distribution, risk
acceptance, value tradeoffs, intergenerational duties. Rung 6 is
the only rung that handles *value pluralism* without smuggling one
party's values in as facts. What rung 6 *lacks*: speed and reach.
Rung-6 deliberation is slow, expensive, and does not scale to many
decisions per unit time, so most operational control stays at lower
rungs. The characteristic failure mode is *displacement*: when the
rung-6 channel is suppressed, the unresolved normative question
accumulates pressure that eventually escapes through rung 0
(revolution).

### What every controller carries on every loop

Drawing these rungs onto an STPA control structure means every
arrow gets a tag, and every controller acquires two extra
attributes: the rung at which it accepts *commands* from above and
the rung at which it accepts *feedback* from below. The two are
often different on the same controller, and that asymmetry is
where most rung-related failures live. The next section catalogues
the three patterns of mismatch.

## Why the ladder matters for STPA

STPA Step 2 produces a control structure: controllers issuing
control actions to controlled processes, with feedback returning.
For social systems, every arrow in that structure operates at *some
rung*. The bishop-to-priest arrow is rung 1 (sacred authority). The
scientist-to-policymaker arrow is rung 3 (empirical testability).
The court-to-parliament arrow is rung 2 (formal consistency)
backed by rung 6 (constitutional principle).

Tagging the rungs makes three failure modes visible:

### Same rung is necessary for transmission

If the controller speaks at a rung the receiver does not operate
on, the control action does not land. A scientist briefing a
charismatic authority at rung 3 ("the data shows…") to a rung-1
audience does not produce behavioural change — the audience cannot
process *data* as a reason. This failure mode is silent: the
controller may believe the action was issued, transmitted, and
obeyed.

### Same rung is not sufficient — and at low rungs it is dangerous

Two actors both at rung 1 transmit perfectly but have *no internal
check*. The system efficiently propagates whatever the upper
controller wants, and the same low-rung filter applies to feedback.
The corrective signal that would expose error is never registered
as evidence — it is registered as disloyalty, hostility, or sin.

This is the dominant failure mode of *Religion* (the Part IV
worked example): rung-1 control downward is honest and stable, but
rung-3 reality (abuse evidence, scientific findings, demographic
harm) tries to enter the upward channel and is reclassified as
rung-1 noise.

### Different rungs on the two arrows of one loop

The most subtle pattern: the *same loop* operates at different
rungs in each direction. The controller issues commands at rung 1
but expects feedback at rung 3. Or it issues commands at rung 3
but receives feedback only at rung 1. Either way the loop is
structurally broken: information flows but does not correct.

This is what the cross-system catalogue identifies in religion,
the unreformed military justice system, board-captured corporations,
and family systems where the privacy norm absorbs all upward
signal into a rung-1 filter.

## Three dangerous mismatches

The seven rungs admit many possible per-arrow combinations. Three
recur across the catalogued social systems and account for most of
the rung-related failures.

### Pattern A — Asymmetric loop

Rung-1 control downward, rung-3 (or higher) feedback expected
upward. The controller's process model rejects the higher-rung
feedback unless it arrives wrapped in rung-1 packaging — which
strips the empirical content.

*Generic remedy:* insert an independent rung-3 channel that
parallels (does not replace) the rung-1 channel and reaches the
apex of control directly. Mandatory external audit, independent
ombudspersons, pre-registered studies, and constitutional courts
hearing rung-3 evidence against rung-1 sovereign claims are all
implementations.

### Pattern B — Claimed-rung inflation

The system publicly claims a high rung (rung 6 deliberation,
rung 4 cumulative evidence) but operates at rung 0/1. The
catastrophic systems of the twentieth century — one-party states
claiming "people's democracy," theocracies claiming sacralised
ultimate legitimacy — are inflations of this kind.

*Generic remedy:* close the gap. Either lower the claim to match
operation, or raise the operation to match the claim. The first is
rare because high claims confer near-term legitimacy; the second
is what most catalogued architectural remedies attempt.

### Pattern C — Cross-loop rung imposition

A controller legitimate at one rung in its own loop tries to
extend that rung's authority into adjacent loops where a different
rung is appropriate. Rung-1 religious authority claiming
jurisdiction over rung-3 scientific questions; rung-3 scientific
authority ruling on rung-6 normative questions; markets pricing
questions whose decisive considerations sit at rung 6.

*Generic remedy:* domain-appropriate rung containment via
subsidiarity rules and standing forums for the rung the question
requires.

The full catalogue is in
`knowledge/se-techniques/justification-rungs/dangerous-mismatches.md`.

## Claimed rung vs operating rung

Every controller has *two* rungs. The **claimed rung** is the
standard the controller's public legitimacy appeals to — what the
system tells participants and outsiders it operates on. The
**operating rung** is the standard at which control actions and
feedback actually run.

The gap between the two is itself a diagnostic. The widest gaps
produce the most catastrophic failures, because participants
experience the gap empirically and the system's legitimacy collapses
faster than the system can correct.

Across the ten social systems in this book's catalogue, the gaps
distribute as follows:

| System | Claimed rung | Operating rung | Gap |
|--------|--------------|---------------|-----|
| Kingdom | 1 | 0/1 | Small |
| Republic | 6 | 3–6 mixed | Variable; opens with capture |
| Theocracy | 6 (sacralised) | 1 | Large |
| One-Party State | 6 | 0/1 | Extreme |
| Corporation | 3 | 1–3 mixed | Moderate |
| University | 3–4 | 1–3 mixed | Moderate |
| Military | 1+2+6 (modern) | 0/1 | Small in tradition; widens under stress |
| Religion | 1+6 (sacralised) | 1 | Large |
| Family | Variable | Variable | The gap is the diagnostic |
| Verein | 6 | 6+2 | Smallest |

The full per-system analysis is in
`knowledge/system-catalogues/social-systems/cross-system/justification-rungs-by-system.md`.

## A normative caveat

STPA in its original form is deliberately neutral about which
controllers are "better" — it describes control loops without
ranking them. The rung ladder is openly normative: rung 6 sits
above rung 0 in a way that rung 0 cannot reciprocate. We flag this
explicitly rather than smuggle it in.

The ladder is a useful add-on *for social systems where epistemic
standards matter*. It is not a generic STPA tool. Engineering
systems mostly operate at rung 3–4 throughout, the rungs do not
mismatch, and the ladder adds nothing. Use this technique where
the question being asked is *whether the loop's rung fits its
function* — not where the question is purely informational.

## Forward references

- The technique is applied to the religion case study in
  [STPA on Religion](../part4/religion-stpa.md). Religion is the
  cleanest example of Pattern A asymmetric-loop failure.
- The dangerous patterns and their remedies generalise across all
  ten social systems — see
  [Control Structures in Social Systems](../part4/control-structures.md)
  and [Architectural Remedies](../part4/remedies.md).
- The full canonical reference is at
  `knowledge/se-techniques/justification-rungs/`.
