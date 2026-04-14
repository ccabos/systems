# STAMP — Overview

**STAMP** (Systems-Theoretic Accident Model and Processes), developed
by Nancy Leveson at MIT, is a model of how losses arise in complex
systems. It treats accidents not as the result of component failures
but as **emergent properties of inadequate control** — including
failures that occur between components that are each functioning
exactly as designed.

## The core claim

A traditional accident model asks *which component broke?* STAMP
asks *which control action was missing, wrong, mistimed, or
misapplied?* The underlying insight is that safety (and, more
generally, any system-level property) is an emergent phenomenon:
it exists in the *interactions* between controllers and controlled
processes, not in the individual parts.

This has a direct consequence: you cannot ensure a system-level
property by improving the reliability of its parts. You can only
ensure it by designing the control structure so that unsafe states
cannot persist.

## Why STAMP fits social systems

The model was developed for engineered safety-critical systems
(aviation, medical devices, nuclear plants), but it is unusually
well-suited to non-technical systems for one reason: in social
systems, the most devastating outcomes typically occur not because
the system has "broken" but because its control mechanisms are
operating exactly as designed — just in a way that produces harm.

- Inquisitions operate exactly as designed.
- Financial-crisis-producing incentives operate exactly as
  designed.
- Abuse cover-ups operate exactly as designed.
- Failed reform programmes operate exactly as designed.

A component-failure model has nothing to say about these cases. A
control-structure model has a lot to say — specifically, it asks
what feedback was missing, what control action was inappropriate,
and what process model the controller was working from.

## What STAMP provides

STAMP is a conceptual model, not a procedure. It gives three
things:

1. **A vocabulary** — controller, controlled process, control
   action, feedback, process model.
2. **An accident definition** — a loss caused by inadequate
   control.
3. **A design stance** — systems are kept safe by the structure of
   their control loops, not the reliability of their components.

The analytical procedure built on top of STAMP is STPA. See
`../stpa/overview.md`.

## References

See `references.md` for the primary Leveson sources.
