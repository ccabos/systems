# The Most Dangerous Structural Patterns

Across all ten social systems in the project's catalogue, four
control-structure patterns recur wherever the most serious harm
occurs. Each pattern has a corresponding remedy at the
control-structure level — not a remedy that relies on actors
behaving better, but one that restructures the control loop so
that the harmful state is no longer reachable. Patterns 1–3 are
domain-general; Pattern 4 (Rung Asymmetry) applies specifically
to social systems and is detailed in `../justification-rungs/`.

None of the first three patterns is a discovery of this project.
Each has a substantial literature of its own, cited per pattern
below; what this page adds is only the uniform control-structure
framing that lets the same remedy logic apply to all of them.
The principle behind that remedy logic — design so that structure,
not virtue, carries the load — is itself old: "ambition must be
made to counteract ambition" [Madison1788]. (Citation keys resolve
in `knowledge/references/bibliography.md`.)

## Pattern 1 — The Accountability Void

**Symptom.** The controller and the interested party are the
same entity. No external actor has authority to review the
decision.

**Instances observed.** Monarchs judging the Crown's own
claims; bishops investigating abuse by their own clergy;
commanding officers prosecuting conduct reflecting on their
commands; boards setting the pay of executives who helped
appoint them; peers reviewing competitors' research; parents
overseeing their own conduct toward children.

**Generic remedy.** Structurally separate the controller from
the interested party, and give the separating body genuine
authority — meaning budget, staffing, and decisional
independence that do not flow through the actor being
overseen. The separating body must also have the power to act
on its findings, not merely to report them.

**Literature.** The separation-of-powers argument in
[Madison1788] is the constitutional-design original. Power's
*The Audit Society* [Power1997] documents the failure mode of
half-remedies: oversight bodies that formally exist but whose
verification has become ritual — precisely the "cosmetic remedy"
this page warns against under Remedy preconditions.

## Pattern 2 — The Self-Sealing Process Model

**Symptom.** The top of the control structure populates its own
process model from sources it controls. Contradictory
information is excluded by doctrine, by incentive, or by
structure. The model diverges from reality while the authority
acts with increasing confidence.

**Instances observed.** Party leadership hearing only cadre
reports of success during the Great Leap Forward; military
high commands receiving operational reports filtered through
the same chain of command; doctrinal authorities declaring
empirical contradiction to be heresy; management populating
board agendas in ways that exclude dissenting operational
knowledge; family authority insulated by privacy norms.

**Generic remedy.** Establish independent information channels
with direct access to the apex of the hierarchy, reporting to
a body that sits outside the controlled chain of command. The
channel must be *direct* (no filtering intermediary) and
*protected* (the reporter must not be punishable by the actor
being reported on).

**Literature.** The term *self-sealing* is Argyris and Schön's:
their theory-in-use analysis shows how organisations protect
their governing assumptions from disconfirmation, and why fixing
it requires double-loop (assumption-revising) rather than
single-loop (error-correcting) learning [ArgyrisSchon1978].
Wilensky documented how hierarchy, specialisation, and
centralisation each systematically distort upward information
flow [Wilensky1967]; Janis described the small-group variant
[Janis1972]; Vaughan's Challenger study is the canonical field
case of a process model drifting from reality one accepted
anomaly at a time [Vaughan1996].

## Pattern 3 — The Proxy Metric

**Symptom.** The system measures something that is correlated
with its actual goal, attaches resources and careers to that
measure, and then watches as the system reorients toward
producing the measure rather than the goal.

**Instances observed.** Exam scores replacing education;
quarterly earnings replacing sustainable value; publication
counts replacing scientific knowledge; citation impact
replacing research quality; compliance reports replacing
operational readiness; electoral wins replacing democratic
health.

**Generic remedy.** Continuously examine what is being
measured and whether the feedback loop connects to the goal or
only to a proxy, and restructure the measurement accordingly.
Two structural defences work: (1) measure the goal directly
even when it is more expensive to do so; (2) decouple the
reward structure from the specific measure so that gaming the
measure does not produce the reward.

**Literature.** This pattern is known as Goodhart's law
[Goodhart1975] and, independently and more generally, Campbell's
law [Campbell1979]; Strathern's formulation — "when a measure
becomes a target, it ceases to be a good measure" — is the one
usually quoted [Strathern1997]. Muller catalogues contemporary
cases and boundary conditions (metrics fail worst where judgment
is displaced rather than informed) [Muller2018]. The second
structural defence above is a direct application of Campbell's
own recommendation to decouple indicators from consequences.

## Pattern 4 — Rung Asymmetry (social-systems extension)

**Symptom.** The downward control action and the upward feedback
on the same loop operate at different **justificatory rungs**. The
controller transmits commands at rung 1 (authority, tradition) but
the corrective signals it would need to register arrive — or are
expected to arrive — at rung 3 or higher (empirical, audited,
replicated). The controller's process model classifies the
higher-rung feedback as out-of-band and filters it out.

**Instances observed.** Doctrinal authorities receiving abuse
reports as rung-1 hostility rather than rung-3 evidence;
autocracies receiving independent press reports as rung-1 treason
rather than rung-3 ground truth; family systems receiving
children's developmental signals as rung-1 defiance rather than
rung-3 health data; single-party leaderships receiving cadre
dissent as rung-1 disloyalty.

**Generic remedy.** Insert an independent feedback channel that
operates at rung 3 (or higher) and routes around the rung-1
filter. The new channel must (a) reach the controller's process
model directly, (b) operate independently of the rung-1 hierarchy
that filters out higher rungs, and (c) have authority to act on
its findings. Concrete instances: mandatory external audit;
independent ombudspersons with statutory access; pre-registered
studies; constitutional courts that can hear rung-3 evidence
against rung-1 sovereign claims. Most of the canonical remedies in
`knowledge/system-catalogues/social-systems/cross-system/remedies-case-studies.md`
can be re-read as rung-elevation moves of this kind.

**Literature.** The rung vocabulary is this project's, but the
ingredients are established: Weber's authority types for rung 0–1
[Weber1922], Habermasian discourse for rung 6 [Habermas1981], and
Hirschman's *voice* for what the blocked upward channel carries
[Hirschman1970]. The closest empirical treatment of the
claimed/operating gap is "isomorphic mimicry" in state-capability
research [Andrews2017]. See `../justification-rungs/references.md`
for the full lineage.

The pattern catalogue is complete only when this fourth pattern is
included; without it, social-systems STPA misses the dominant
failure mode of hierarchical institutions. Two further rung
mismatches (Claimed-Rung Inflation, Cross-Loop Rung Imposition)
are catalogued in `../justification-rungs/dangerous-mismatches.md`.

## Why these four

The four patterns are not a random list. They correspond one
to one with the four ways a social-system control loop can fail
at the structural level:

| Pattern | Which part of the loop fails |
|---------|------------------------------|
| Accountability Void | The oversight role is merged with the acting role |
| Self-Sealing Process Model | The feedback channel is captured by the actor it is supposed to report on |
| Proxy Metric | The reference signal no longer tracks the true goal |
| Rung Asymmetry | Control and feedback operate on different epistemic standards |

Any complete control-structure review should explicitly check
for all four. The patterns are what a full STPA analysis tends
to find repeatedly; listing them up front short-circuits the
discovery phase for cases that are already obvious.

## Remedy preconditions

Every remedy at the control-structure level has three
preconditions that, when missing, render the remedy
cosmetic:

1. **Independence must be financial as well as formal.** A
   separating body funded through the actor it is overseeing
   is not independent.
2. **Authority must include consequences.** A body that can
   find fault but cannot enforce must not be counted as a
   circuit breaker.
3. **The remedy must survive leadership change.** If the fix
   can be undone by the next executive, it is a policy, not a
   structural remedy. This is the protective half of a two-sided
   problem: it defends a finished remedy against the next
   controller. The diagnostic half — whether the current
   controller can reach the remedy at all, and whether it will
   still be in office when the effect arrives — is
   `../change-loops/`.

These preconditions apply to every worked remedy in
`knowledge/system-catalogues/social-systems/cross-system/remedies-case-studies.md`.
