# Five-Level SE Hierarchy — How It Works

The mechanics of applying the Goals → Requirements → Functions →
Logical Architecture → Physical Implementation hierarchy. For level
definitions see `five-level-hierarchy.md`.

## Traceability rules

Every item in the hierarchy must be connected:

- Every Goal links to at least one Requirement.
- Every Requirement links to at least one Function.
- Every Function links to at least one Logical Architecture element.
- Every Logical Architecture element links to at least one Physical
  Implementation.
- A child can have multiple parents (many-to-many is valid).
- **No orphan nodes** — every item must be traceable upward to a
  goal and downward to an implementation.

These rules ensure:

- **Completeness** — every goal is implemented.
- **Necessity** — every implementation serves a goal.

When applied to social systems, the rules reveal a common pathology:
physical implementations that have lost their connection to any goal
("we do this because we've always done it") and goals that have no
implementation ("we believe in this but have no mechanism to achieve
it").

## ID conventions

Each system uses a short system-specific prefix followed by the level
letter and a number:

- `K*` = kingdom (KG1, KR1, KF1, KL1, KP1)
- `R*` = republic / democracy (RG1, RR1, RF1, RL1, RP1)
- `T*` = theocracy
- `O*` = one-party state
- `C*` = corporation
- `U*` = university
- `M*` = military
- `F*` = family
- `V*` = verein (social systems) / V-Model (dev frameworks — namespace
  collision scoped by catalogue)
- `W*`, `P*`, `S*`, `KB*`, `DT*`, `DO*`, `SA*` = dev frameworks

The prefix is local to the decomposition. Cross-system references
always name the system to disambiguate (e.g. "kingdom's KG1"
vs. "democracy's RG1").

## Order of decomposition

The standard top-down order is:

1. **Draw the boundary** (see
   `knowledge/foundations/boundaries-and-environment.md`). Decide
   what is in the system and what is outside. State the boundary
   explicitly before writing anything else.
2. **List the goals.** Aim for 3–6. Separate declared from operative
   goals where they diverge; the operative goals are what the STPA
   analysis will need later.
3. **Derive requirements.** For each goal, ask: what must be true
   for this goal to be achievable? Write each answer as a must-
   statement. Some requirements will serve multiple goals.
4. **Derive functions.** For each requirement, ask: what operations
   does the system perform to satisfy this? Write as active verbs.
5. **Group functions into logical subsystems.** Prefer cohesion:
   functions that share data or control flow go in the same
   subsystem.
6. **Assign physical implementations.** For each logical subsystem,
   list the concrete people, buildings, documents, and processes
   that realise it.
7. **Check traceability.** Every P links upward to at least one L;
   every L to at least one F; every F to at least one R; every R to
   at least one G. No orphans.

The order is top-down in presentation, but in practice analysts move
up and down the levels as new information forces revisions. The
finished decomposition should satisfy the traceability rules
regardless of how it was constructed.

## Skipping levels is a pathology

Skipping a level — for example, jumping from goals directly to
physical implementation — produces systems that "work" but are
fragile, incoherent, and resistant to change. Two typical
manifestations:

- **Goal → Physical shortcuts.** "We need to improve education, so
  we'll build more universities" — without deriving requirements
  (who gets educated, in what, how), functions (teaching, research,
  credentialing), or logical architecture (what subsystems interact).
  The buildings get built and the goal is no closer.
- **Physical → Goal reverse-justification.** "We have this ministry,
  therefore it must serve some goal" — a mechanism looking for a
  purpose. Usually a sign that the physical element has outlived the
  goal it was originally built to serve.

Full traceability catches both pathologies: the first fails because
there are orphan P's not linked upward; the second fails because
there are orphan G's not linked downward.

## Recursion

Every logical subsystem is itself a system. You can decompose any
L-level element into its own G / R / F / L / P. The **recursion
boundary** (how far to decompose) is a modelling choice — see
`knowledge/foundations/boundaries-and-environment.md`.

In practice the project uses a single level of recursion:
system → subsystem. Further recursion is done only when a subsystem
becomes the focus of a dedicated analysis (e.g. a national
constitutional court analysed as a system in its own right).
