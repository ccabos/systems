# From SE Decomposition to STPA

The five-level SE hierarchy (see
`../goals-requirements-hierarchy/`) and STPA are complementary: a
completed SE decomposition gives STPA most of what it needs for
Steps 1 and 2. This page lists the translation rules.

## The translation rules

| SE level | Feeds into STPA as |
|----------|--------------------|
| Goals (G) | **Losses** — each loss is the negation of a goal |
| Requirements (R) | **System-level Constraints** — must-statements become safety constraints |
| Functions (F) | **Control actions** — the active verbs become the things a controller does |
| Logical Architecture (L) | **Control structure** — subsystems become controllers and controlled processes |
| Physical Implementation (P) | **Actors** — the concrete people, offices, and documents that issue the control actions |

## How the mapping works in practice

### Goals → Losses

A goal of "ensure territorial integrity" becomes the loss "loss of
territorial integrity." A goal of "generate sustainable profit"
becomes the loss "loss of solvency." This mechanical negation is
often enough; sometimes a single goal maps to several distinct
losses (a goal of "legitimate succession" maps to both "contested
succession" and "unconstitutional seizure of power").

### Requirements → Constraints

Requirements are already phrased as must-statements, so they are
already in the shape STPA wants for constraints. The only
adjustment is to rephrase them so that each constraint prevents a
specific hazard rather than enabling a specific goal.

### Logical Architecture → Control Structure

The subsystems from the L-level become the nodes of the STPA
control structure. The control actions between them are the
functions that cross subsystem boundaries. This is why STPA works
at the logical level, not the physical level: the control
structure should be stable across changes of personnel, building,
or document form.

### Physical Implementation → Actors

The P-level says which concrete actor issues each control action.
This matters for Step 4 (loss scenarios), because the causal
factors behind an unsafe control action are often actor-specific:
a judge's process model is informed by different sources than a
general's.

## What STPA adds that the SE decomposition does not

The SE decomposition tells you *what the system is*. STPA tells
you *what could go wrong*. Three things are new:

1. **Feedback channels.** The SE decomposition lists functions;
   STPA also demands the reverse channel — how the controller
   learns about the state of the controlled process.
2. **Process models.** STPA requires that each controller's
   internal beliefs about the state of the controlled process be
   made explicit, because most UCAs are traceable to a wrong
   process model.
3. **The four UCA questions.** A function list says *what the
   system does*; the UCA questions say *what it could fail to do,
   or do wrongly* — in four systematic categories.

For social systems, a fourth thing is new and is **not** delivered
by the SE decomposition: the **justificatory rung** of each control
action and feedback channel. The SE level lists the function
(*what is done*) and the L/P levels say *who does it*, but neither
says *on what standard the receiver will accept it*. Rung tagging
is its own elicitation activity, performed during STPA Step 2. See
`../justification-rungs/application-to-stpa.md`.

## The project's workflow

In this project, the workflow is:

1. Decompose the system through the SE hierarchy (see
   `../goals-requirements-hierarchy/how-it-works.md`).
2. Translate G, R, L, P into STPA Step 1 and Step 2 artefacts
   using the rules above.
3. Run Steps 3 and 4 to produce UCAs and loss scenarios.
4. Match each UCA to a pattern in the remedy catalogue (see
   `../remedies/`).

The worked examples of this workflow for the ten social systems
live in the per-system folders under
`knowledge/system-catalogues/social-systems/<system>/stpa-analysis.md`
(where present).
