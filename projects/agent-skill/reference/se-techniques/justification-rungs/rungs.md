# The Seven Rungs

Each rung defines what counts as a *decisive reason* — the standard
a control action or a feedback signal must meet to move the
receiver. Later rungs include all the checks of the earlier rungs
plus one new one. Skipping rungs is possible (a constitutional court
operates at rung 6 without first passing through rung 5), but
skipping is rare and unstable.

## Rung 0 — Power / coercion

**Standard.** "Do it or else." Compliance is enforced by threat of
sanction, violence, or exclusion. There is no shared criterion for
what is true, valid, or fair; the only criterion is the
distribution of force.

**Where you meet it.** Coups, monopolistic threats, occupation
regimes, organised crime, parental "because I said so," workplace
intimidation.

**What this rung lacks.** Any common standard at all. Two parties
at rung 0 cannot disagree productively; they can only enforce or
submit.

**STPA signature.** Control action lands without persuasion;
feedback either flatters the controller or is suppressed. Loss
scenarios concentrate around the absence of corrective feedback.

## Rung 1 — Authority / rhetoric / identity

**Standard.** A claim is decisive because of *who* makes it, *what
tradition* it comes from, or *what group* the listener identifies
with. Persuasion happens, but without an obligation to check truth
or consistency.

**Where you meet it.** Campaign slogans, scripture, "as a parent…,"
brand loyalty, expert testimony where the listener cannot evaluate
the substance, charismatic leadership.

**What rung 1 adds over rung 0.** Voluntary acceptance — the
listener moves without a sanction being threatened. The listener
moves because the source is recognised as legitimate, not because
the conclusion has been independently checked.

**What rung 1 lacks.** Any internal check. Two contradictory rung-1
authorities cannot adjudicate the contradiction without escalating
to rung 0 (force) or rung 2+ (some standard outside personal
authority).

**STPA signature.** Controller's process model treats *who said it*
as the deciding factor. Feedback that comes from the wrong source
is dismissed regardless of content. Self-sealing process models
(see `../control-structures/dangerous-patterns.md`) are most often
rung-1 process models.

## Rung 2 — Formal consistency

**Standard.** A conclusion follows validly from premises both
parties already accept. The argument can be checked step by step;
contradictions lose.

**Where you meet it.** Mathematical proofs, court syllogisms,
formal logic, rule-based bureaucratic decisions, legal reasoning
within an established code.

**What rung 2 adds over rung 1.** An *internal* check: even an
authority cannot make an inconsistent argument win. A rung-2
challenge can defeat a rung-1 claim by exhibiting contradiction
within the claim's own premises.

**What rung 2 lacks.** An *external* check. Premises themselves
are not tested against the world. A perfectly consistent system
may still be wrong if its premises are wrong.

**STPA signature.** Loops that operate at rung 2 produce internally
coherent decisions that may diverge from external reality. The
characteristic failure is the system that "follows the rules"
straight into harm.

## Rung 3 — Empirical testability

**Standard.** A hypothesis is decisive only if it survives tests
against rivals — controlled experiments, falsification, prediction
against unseen data.

**Where you meet it.** Randomised trials, falsification in physical
sciences, A/B tests, engineering acceptance tests, audited
financial statements.

**What rung 3 adds over rung 2.** An *external* check: data can
sink a neat theory. Premises themselves become accountable to
observation.

**What rung 3 lacks.** Protection against one-off flukes,
publication bias, p-hacking, and the small-N problem. A single
positive trial does not yet make a robust claim.

**STPA signature.** Rung-3 feedback channels are powerful but
fragile — they can be defeated by a single biased sample. Loops
that operate at rung 3 require active maintenance of the channel's
integrity.

## Rung 4 — Cumulative evidence and consilience

**Standard.** A claim is decisive when results survive replication
and line up across multiple methods, populations, and disciplines.
Meta-analyses, systematic reviews, and cross-method triangulation
beat single studies.

**Where you meet it.** Evidence-based medicine, IPCC assessment
reports, well-replicated psychology effects, cross-discipline
syntheses, regulatory science.

**What rung 4 adds over rung 3.** Robustness against flukes,
biases, and method artefacts. A finding that holds up across
independent methods is harder to explain away than one method's
single result.

**What rung 4 lacks.** A way to handle situations in which the
methods themselves are in dispute, or where no single method
applies, or where the question is partly normative.

**STPA signature.** Rung-4 feedback is slow but durable. Systems
that depend on rung-4 feedback (climate policy, drug regulation)
have characteristic failure modes around delay — the rung-4 signal
arrives only after irreversible action.

## Rung 5 — Meta-rational integration

**Standard.** A claim is decisive when the speaker can show *why*
a method works, *when it breaks*, and *how to combine multiple
methods* under uncertainty. The speaker steps outside any single
formalism to choose the right one for the question.

**Where you meet it.** Risk engineering, AI safety research,
complex-systems policy labs, integrated assessment in climate
policy, intelligence analysis at its best.

**What rung 5 adds over rung 4.** An acknowledgement that no
single method covers all messy domains, and a discipline for
choosing among methods rather than defaulting to one. Rung 5 is
where one becomes able to talk sensibly about model failure,
unknown unknowns, and the limits of one's own evidence.

**What rung 5 lacks.** Any answer to *what should be done* once
the empirics are settled. Rung 5 sharpens facts; it does not
deliver oughts.

**STPA signature.** Rung-5 controllers can hold multiple feedback
channels in superposition — a rung-3 RCT, a rung-1 stakeholder
intuition, a rung-2 legal constraint — and weight them
appropriately. This is rare, fragile, and cognitively costly.

## Rung 6 — Normative legitimacy / deliberative ethics

**Standard.** A claim is decisive when it survives open, inclusive
discourse and meets normative criteria — fairness, reversibility,
universalisability, respect for the autonomy of the affected. Even
perfect facts and models do not tell us oughts; society still has
to justify rules to all affected by them.

**Where you meet it.** Constitutional courts, citizens'
assemblies, Habermasian deliberative democracy, well-functioning
parliamentary deliberation, bioethics committees.

**What rung 6 adds over rung 5.** A way to settle questions about
what should be done that cannot be reduced to fact — distribution,
risk acceptance, value tradeoffs, intergenerational duties. Rung 6
is the only rung that handles *value pluralism* without smuggling
one party's values in as facts.

**What rung 6 lacks.** Speed and reach. Rung-6 deliberation is
slow, expensive, and does not scale to many decisions per unit
time. Most operational control therefore stays at lower rungs.

**STPA signature.** Rung-6 feedback channels are typically
*infrequent* but *high-impact* — constitutional crises, landmark
cases, generational reforms. Their characteristic failure mode is
displacement: when the rung-6 channel is suppressed, the unresolved
normative question accumulates pressure that eventually escapes
through rung 0 (revolution).

## What every controller has on every loop

Drawing these rungs onto an STPA control structure means every
arrow gets a tag. Many failures become visible immediately:

- A controller that issues control actions at rung 1 but expects
  feedback at rung 4 is structurally deaf — the feedback arrives
  but the controller's process model rejects it.
- A controlled process that has internalised rung 3 norms cannot
  be moved by rung-1 commands except through rung-0 fallback
  (coercion).
- A loop that nominally operates at rung 6 but actually operates
  at rung 1 is the *democratic-deficit* pattern.

The three patterns of mismatch are catalogued in
`dangerous-mismatches.md`.
