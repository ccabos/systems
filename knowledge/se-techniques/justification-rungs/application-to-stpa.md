# Applying Justificatory Rungs Inside STPA

This page is the integration spec: where in the four STPA steps the
rung dimension hooks in, what new artefacts it produces, and how it
interacts with the existing technique pages in `../stpa/` and
`../control-structures/`.

## Hook 1 — Step 1: a new hazard family

Standard STPA Step 1 produces losses, hazards, and constraints. The
rung dimension adds one hazard family that recurs across social
systems:

> **HX — Operating-rung mismatch.** The system claims a high
> justificatory rung in its stated purpose but operates at a
> markedly lower rung in practice.

This hazard always implicates losses around legitimacy and trust:
the gap between claimed and operating rung is empirically visible
to participants, and once visible it erodes the system's ability to
function at *any* rung.

The corresponding constraint is:

> **SCX.** The operating rung of every loop must match (or exceed)
> the rung the system claims publicly.

## Hook 2 — Step 2: tag every arrow

Step 2 of STPA produces a hierarchical control structure with
arrows for control actions (downward) and feedback (upward). The
rung extension tags **every arrow** with the rung at which it
actually operates, and **every controller box** with two extra
attributes:

| Attribute | Meaning |
|-----------|---------|
| Claimed rung | The rung the controller's stated authority depends on |
| Operating rung | The rung the controller actually uses to issue control actions and accept feedback |

Tagging is mechanical once you ask the right question for each arrow:
*"At what rung does the receiver have to operate to register this
signal?"*

In a religion's control structure, the bishop-to-clergy arrow
typically operates at rung 1 (authority). The clergy-to-bishop
feedback arrow may *nominally* operate at rung 1 (filial reports)
but is *expected* by external observers to operate at rung 3
(empirical reports of pastoral state). The mismatch is structural,
not accidental.

## Hook 3 — Step 2: add a per-controller process-model field

Each controller in standard STPA has a process model — its internal
representation of the controlled process. The rung extension adds
two fields to every process model:

- **Acceptable command rungs.** What rungs of control action the
  controller believes the controlled process will obey.
- **Acceptable feedback rungs.** What rungs of feedback the
  controller will register as informative versus dismiss as
  illegitimate.

These two fields are often different on the same controller, and
the gap between them often *is* the loss scenario.

## Hook 4 — Step 3: three new UCA modes

Standard STPA enumerates UCAs across four types: not provided,
provided when hazardous, provided too early/late, provided too
long/short. The rung extension adds three modes that cut across all
four types:

### UCA-R1 — Over-rung command

The controller issues a control action at a rung the receiver
cannot decode. Rung 4 ("the meta-analysis shows…") delivered to a
rung-1 audience produces no behavioural change; the audience cannot
process the input as a reason. The command fails *silently* — the
controller may believe it has been issued, executed, and obeyed.

### UCA-R2 — Under-rung command

The controller issues a control action at a rung the receiver
rejects as illegitimate. Rung 1 ("trust me") delivered to a rung-4
audience produces *active rejection* — the audience treats the
attempt as an insult to its standards. The command fails *noisily*,
often eroding the controller's standing.

### UCA-R3 — Asymmetric loop

The control action and the feedback channel on the same loop
operate at different rungs. The controller can issue commands the
receiver accepts but cannot register the feedback the receiver is
qualified to send (or vice versa). The loop is structurally broken:
information flows but does not correct.

UCA-R3 is the most common rung-mismatch UCA in social systems and
the hardest to remedy because the controller's process model
*already classifies* the higher-rung feedback as out-of-band.

## Hook 5 — Step 4: process-model causal factors

Standard STPA Step 4 catalogues why a UCA could occur: wrong
process model, missing feedback, faulty actuator, unexpected
state, external disturbance. The rung extension adds two specific
process-model failures:

- **Acceptance-rung filter.** The controller's process model
  defines a maximum acceptable feedback rung; anything higher is
  classified as hostile, irrelevant, or incomprehensible. Examples:
  doctrinal authorities classifying empirical contradiction as
  heresy; charismatic leaders classifying evidence-based critique
  as betrayal.
- **Issuance-rung overconfidence.** The controller's process model
  assumes the receiver accepts a higher rung than it does, so
  control actions are issued at the wrong rung and fail silently.
  Examples: technocrats issuing rung-4 policy explanations to a
  rung-1 electorate.

Both failures yield specific structural remedies (see
`dangerous-mismatches.md`).

## Hook 6 — Cross-cutting: a fifth diagnostic question

The four diagnostic questions in
`../control-structures/diagnostic-questions.md` are extended by:

> **5. Rung match.** *At what rungs do the loop's control action
> and feedback operate, and is the loop symmetric? Does the
> controller's claimed rung match its operating rung?*

A satisfactory answer names the rungs on each arrow, identifies
mismatches, and shows whether the loop's *function* requires
symmetry (most operational loops do) or deliberate asymmetry (some
democratic loops do).

## Hook 7 — Cross-cutting: a fourth dangerous pattern

The three dangerous patterns in
`../control-structures/dangerous-patterns.md` are extended by **Rung
Asymmetry**:

> **Symptom.** Stable downward control at rung 1 with
> structurally filtered upward feedback. The system maintains
> behavioural compliance while losing the ability to register
> corrective signals.
>
> **Generic remedy.** Raise the operating rung of the feedback
> channel — typically by inserting an independent rung-3 channel
> (audit, inspection, mandatory reporting) parallel to the
> existing rung-1 channel. The new channel must reach the
> controller's process model directly, not through the rung-1
> filter.

Most of the canonical remedies in
`knowledge/system-catalogues/social-systems/cross-system/remedies-case-studies.md`
can be re-read as rung-elevation moves: SOX (rung 1 → rung 3 in
financial feedback), Bundeswehr Wehrbeauftragter (rung 0/1 → rung 3
in conduct feedback), Vatican II's lay councils (rung 1 → rung 1+2
in doctrinal feedback).
