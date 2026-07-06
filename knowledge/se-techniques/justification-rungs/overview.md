# Justificatory Rungs — Overview

## The problem this technique addresses

STPA tells us which control actions are unsafe. It does not tell us
why a control action that *should* land does not — why the bishop's
sermon does not sway the empirically-minded congregant, why the
scientist's data does not move the believer, why the parliament's
resolution does not constrain the autocrat. In each case, the
control action is issued, transmitted, and received, but the
receiver does not accept it as a *reason* to change behaviour. The
control loop opens not because of a missing arrow but because the
two ends are operating on different standards for what a reason is.

These standards form a ladder. Each later rung adds a check that
earlier rungs lack:

- Rung 0 — raw coercion ("Do it or else").
- Rung 1 — authority, rhetoric, identity (charisma, tradition).
- Rung 2 — formal consistency (valid deduction from shared premises).
- Rung 3 — empirical testability (data can sink a neat theory).
- Rung 4 — cumulative evidence and consilience (results survive replication and triangulation).
- Rung 5 — meta-rational integration (knowing when each method breaks, combining methods under uncertainty).
- Rung 6 — normative legitimacy (claims survive open inclusive discourse and meet ethical criteria).

The seven rungs are detailed in `rungs.md`.

**Where the ladder comes from.** The seven-rung arrangement is this
project's, but every rung is an established position with its own
literature: rungs 0–1 are Weber's authority types [Weber1922] (with
Arendt's power/violence distinction separating rung 0 from rung 1
[Arendt1970]); rung 3 is Popperian falsifiability [Popper1959];
rung 4 is consilience and cumulative evidence [Wilson1998;
Lakatos1970]; rung 5 is post-normal science and decision-making
under Knightian uncertainty [FuntowiczRavetz1993; Knight1921];
rung 6 is Habermasian discourse ethics and deliberative democracy
[Habermas1981; Fishkin2009]. Toulmin's *argument fields* — the
observation that different domains legitimately use different
standards of backing [Toulmin1958] — is the licence for treating
the standard itself as a per-arrow variable rather than a global
constant. The full annotated lineage is in `references.md`;
citation keys resolve in `knowledge/references/bibliography.md`.
The synthesis should be read as a checklist over known positions,
not as a new theory of justification.

## When to use this technique

Reach for this technique when:

- the system is social, institutional, or policy-shaped
- a control structure has been drawn and the four standard
  diagnostic questions have been answered
- one or more loops appear formally complete — the arrows are
  there, the channels exist — yet behaviour does not converge as
  the architecture predicts.

In that case the failure is often *epistemic*: the rungs on the two
ends of the loop are mismatched, or the controller's process model
does not admit the rung the feedback arrives on.

## What the technique adds at each STPA step

| STPA step | Standard output | What rung tagging adds |
|-----------|----------------|------------------------|
| 1 — Define purpose | Losses, hazards, constraints | A new hazard family: *the system operates at a rung incompatible with its stated purpose* |
| 2 — Model control structure | Hierarchical diagram of controllers, controlled processes, control actions, feedback | A rung tag on every control action and every feedback channel; a "claimed rung vs operating rung" annotation on each controller |
| 3 — Identify UCAs | Four-type UCA enumeration | Three rung-mismatch UCA modes (`application-to-stpa.md`) |
| 4 — Identify loss scenarios | Causal factors per UCA | Process-model factors that explain why the controller cannot register feedback at the relevant rung |

## What the technique does not do

- It does not say which rung a system *ought* to operate at —
  except that systems claiming a higher rung must actually operate
  at it.
- It does not replace the four standard diagnostic questions or
  the three dangerous patterns. It adds a fifth question and a
  fourth pattern.
- It is not a scoring rubric. A system at rung 3 throughout is not
  necessarily "better" than one with mixed rungs — democracy is
  rung-mixed by design and works because of it. What matters is
  whether the rung *on each arrow* fits its function.

## Where the technique applies in this project

- Per-system rung tagging in
  `knowledge/system-catalogues/social-systems/cross-system/control-structure-profiles.md`.
- Cross-system comparison in
  `knowledge/system-catalogues/social-systems/cross-system/justification-rungs-by-system.md`.
- Worked example in
  `knowledge/system-catalogues/social-systems/religion/applied-se-analysis.md`.
- Book treatment in `projects/systems-introduction-book/docs/part1/justification-rungs.md` and the rung sections of Part IV.
