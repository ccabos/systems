# Two Patterns Behind Changes That Never Arrive

The four patterns in `../control-structures/dangerous-patterns.md`
describe ways an operating loop fails. The two below describe ways a
*change* loop fails — cases where the operating loop is understood,
the remedy is correct, and nothing happens anyway.

Neither is a discovery of this project. Both are the control-structure
framing of results in the implementation literature, cited per pattern
below. Citation keys resolve in
`knowledge/references/bibliography.md`.

## Pattern 1 — The Actuator Void

**Symptom.** The controller issues a control action for which it holds
no actuator. The action is genuine, transmitted and received, and
reaches an actor who cannot execute it because the lever belongs to
somebody else. Nothing in the loop is missing except the ability to
move it.

**Instances observed.** A head of government pledging faster building
and plant permits that are decided by municipal authorities under
state law, with statutory consultation rights attached; a chief
executive announcing customer focus while the objectives scheme is set
jointly with the remuneration committee and the works council; a
ministry ordering digital services whose case-handling system is
contracted to a shared service provider it does not direct;
supranational directives that require member-state transposition
before they bind anyone.

**Generic remedy.** Either bind the actuator's owner into the loop —
a joint decision body, a statutory duty on the owner, a conditional
transfer — or re-aim the control action at a lever the controller
actually holds, and say publicly that this is what has been done.
Repeating the announcement more loudly is not a remedy; it is the
characteristic non-response to this pattern.

**Literature.** Pressman and Wildavsky's study of a federal programme
that dissolved across the clearance points between decision and
delivery is the founding case [PressmanWildavsky1973]. Lipsky's work
on street-level discretion explains why the last actuator in the chain
— the caseworker — is so often the decisive one [Lipsky1980].
Mazmanian and Sabatier systematise the conditions under which the
chain holds [MazmanianSabatier1983].

## Pattern 2 — The Horizon Mismatch

**Symptom.** The feedback on a control action returns after the
controller's tenure has ended. The loop is open, not because a channel
is missing but because nobody who issued the action is still there to
receive the signal.

**Instances observed.** Electoral terms of four to five years set
against training pipelines of three to six; quarterly reporting set
against a platform rebuild measured in years; a minister's tenure set
against the time a contested reform takes to clear the courts; a
project manager rotated out before the architecture decision they took
shows its consequences.

**Generic remedy.** Two moves, and they are needed together.

First, intermediate indicators that lie *on the same causal path* and
carry signal sooner — vacancies filled and cases cleared per examiner,
not a substitute for the outcome. Substitute measures are how this
remedy fails: a proxy adopted because it reports quickly is Pattern 3
of `../control-structures/dangerous-patterns.md`, and it converts a
horizon problem into a measurement problem.

Second, a commitment that outlives the tenure: statutory duties with
dates, funding committed beyond the term, an independent body holding
the mandate. This is the same requirement as the third remedy
precondition in `../control-structures/dangerous-patterns.md`,
approached from the other side — there it protects a finished reform
from the next controller, here it lets the current one act at all.

**Literature.** Meadows locates the power to change system structure
as a leverage point in its own right [Meadows1999], which is what a
short horizon effectively removes. The behavioural consequence — that
short-horizon controllers change the visible parts rather than the
slow rules, and produce institutions with the form but not the
function — is documented as isomorphic mimicry [Andrews2017;
MeyerRowan1977].

## Both patterns in one system

The corporation exhibits both, and the catalogue had recorded the
second before it had a name: the causal factor for UCA-C2 is that the
incentive structure's time horizon is shorter than that of the
decisions being made. Worked through in
`knowledge/system-catalogues/social-systems/corporation/change-loop-analysis.md`.

## Why these two

They correspond to the two ways a change loop can fail while the
operating-loop analysis is entirely correct:

| Pattern | What fails |
|---------|------------|
| Actuator Void | The controller cannot reach the lever |
| Horizon Mismatch | The controller cannot receive the feedback |

A third possibility — the controller reaches the lever, receives the
feedback, and the change still does not produce the outcome — is not
a change-loop failure. That is an operating-loop finding, and belongs
to the four patterns in `../control-structures/`.
