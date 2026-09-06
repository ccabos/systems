# Change Loops — Overview

Every technique catalogued before this one models the **operating
loop**: a controller issues control actions, a controlled process
responds, feedback returns. None of them models the loop you traverse
in order to *change* the operating loop.

The two differ in what they act on:

| Loop | Controller | Controlled process | Feedback |
|------|-----------|--------------------|----------|
| **Operating** | the institution's controllers | the world — applications decided, patients treated, students taught | outcomes, continuously |
| **Change** | whoever wants the institution to behave differently | the institution's own rules | the altered outcomes, much later |

The change loop's controlled process is a **rule**, and written rules
are connections in physical form (see
`knowledge/foundations/system-definition.md`). That is what makes this
a distinct object rather than a figure of speech: the operating loop
acts *through* the system's connections, the change loop acts *on*
them.

## The assumption that institutions break

STPA assumes a controller holds the control actions it issues. For an
autopilot this is true — it commands the elevator directly. For
institutions it is false for exactly the reform-relevant actions. A
head of government does not hold building law, staffing levels, or a
municipal authority's case handling. A chief executive does not hold
the objectives scheme alone.

A change loop is therefore characteristically a loop in which the
controller must first pass through *other* controllers who hold the
actuator. Analysing one means naming those holders, which is the step
that ordinary reform talk skips.

## What is recorded per lever

Four properties of the lever and one of the controller:

1. **Actuator ownership** — who signs. Not who is responsible, who
   signs.
2. **Change latency** — from decision to the rule being in force:
   legislative passage, budget cycle, consultation period.
3. **Effect latency** — from the rule being in force to an observable
   change in outcomes: training pipelines, staff turnover, system
   rollout.
4. **Resistance** — who loses a competence, a budget, or a certainty.
   Every rule change takes something from someone.
5. **Controller tenure** — an electoral term, a board period, a
   posting. A property of the controller, not of the lever, but the
   analysis is meaningless without it.

Separating (2) from (3) is not pedantry. Funding training places has a
change latency near zero and an effect latency of years; changing a
statutory deadline is the reverse. They are different blockages and
they take different remedies, and an analysis that reports one figure
cannot tell them apart.

Latencies are orders of magnitude, not measurements. "One to three
years" is a bracket. The guard against dressing them up as data is in
`../linear-algebra/false-precision-trap.md`.

## The derived quantity

Change latency plus effect latency, set against controller tenure:

> Where the effect horizon is longer than the tenure, the controller
> never sees the feedback from its own control action. The loop is
> open — not because an arrow is missing, but because the controller
> is gone before the signal returns.

This has a consequence that is worth stating as a prediction rather
than an observation. Every controller in the chain optimises for
signals that return inside its own horizon. Short latency and visible
output belong to the *parts* — a new agency, new staff, a new portal.
Long latency and invisible output belong to the *rules*. So a
structure of short-tenure controllers will reliably produce
part-changes offered as rule-changes, which is what the state-capability
literature calls isomorphic mimicry [Andrews2017]. The change loop
derives that behaviour from loop structure instead of recording it as
an empirical regularity.

## Why this is not new territory

The change loop has a place in sources the project already cites, and
two it did not.

- Meadows ranks "the power to add, change, evolve, or self-organize
  system structure" as her fourth-strongest leverage point, above the
  rules themselves [Meadows1999]. That is this loop, named as a
  leverage point.
- Ashby's requisite variety applies here as much as to the operating
  loop [Ashby1956]: a reformer must command as much variety as the
  rule being changed. This is the precise reason nobody at the top
  knows all the levers.
- Pressman and Wildavsky's *Implementation* [PressmanWildavsky1973] is
  the founding study of the gap between a decision and its effect,
  built on the count of clearance points a programme must pass.
- Lipsky's street-level bureaucracy [Lipsky1980] establishes that the
  last translation step — the caseworker's discretion — often
  dominates the outcome, which is why effect latency is not merely
  administrative delay.

There is also a mirror inside the project. The third remedy
precondition in `../control-structures/dangerous-patterns.md` requires
that a remedy survive a change of leadership. That is the *protective*
half of the same insight: it defends a completed reform against the
next controller. The change loop is the *diagnostic* half — whether
the controller can reach the reform at all, and whether it will still
be there when the effect arrives.

## What this technique adds

Control structures say how an operating loop fails. STPA says which
control actions in it are unsafe. Neither asks whether a proposed
change can reach the operating loop in the first place. That is this
technique's only question, and it is the one that decides whether an
analysis ends in a remedy or in an announcement.

It also makes an existing column measurable. The replaceability
hierarchy in `knowledge/foundations/system-definition.md` carries an
"effort to change" column whose entries are qualitative. Ownership,
the two latencies, and resistance are what stand behind that column.

## Where it is applied

- `lever-inventory.md` — the method, with a constructed permitting
  case worked through.
- `knowledge/system-catalogues/social-systems/corporation/change-loop-analysis.md`
  — the first application to a catalogued system. It finds that for
  the corporation's governance levers the actuator's owner and the
  change's loser are the same actor, and that all three architectural
  remedies in the catalogue were consequently installed from outside
  the firm.

One system is not a result about institutions in general. A
cross-system view in the style of
`knowledge/system-catalogues/social-systems/cross-system/control-structure-profiles.md`
is worth building once a second system has been worked to the same
depth.
