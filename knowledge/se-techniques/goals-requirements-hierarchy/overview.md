# Five-Level SE Hierarchy — Overview

The five-level decomposition used throughout this project.

Systems engineering decomposes any system — technical or social —
into five levels of abstraction. Each level answers a different
question, and each item at one level traces to items at the next
level down, forming a directed acyclic graph with full traceability.

The five levels and their IDs:

| Level | Prefix | Question Answered |
|-------|--------|------------------|
| **Goals** | G | *Why does this system exist?* |
| **Requirements** | R | *What must be true?* |
| **Functions** | F | *What does the system do?* |
| **Logical Architecture** | L | *How is it organized?* |
| **Physical Implementation** | P | *What is it made of?* |

For the level-by-level definition see `five-level-hierarchy.md`. For
the mechanics of applying it (traceability rules, IDs, order of
decomposition) see `how-it-works.md`.

## Why five levels?

The five levels are not arbitrary. They correspond to the fundamental
decisions that any system designer — whether an engineer or a
lawmaker — must make, in order:

1. **Purpose before structure.** You cannot design a system without
   knowing what it is for (Goals).
2. **Constraints before mechanisms.** You cannot choose mechanisms
   without knowing the constraints they must satisfy (Requirements).
3. **Functions before grouping.** You cannot group things into
   subsystems without knowing what functions need to exist
   (Functions).
4. **Logical before physical.** You should decide how subsystems
   interact before choosing which specific technologies, people, or
   buildings implement them (Logical → Physical).

Skipping a level — for example, jumping from goals directly to
physical implementation — produces systems that "work" but are
fragile, incoherent, and resistant to change. This is as true of a
parliament as it is of a software architecture.

## Where this technique is used

- In every entry under `knowledge/system-catalogues/` — each system
  and each development framework is decomposed with this hierarchy.
- As the analytical backbone for cross-system comparison: the
  platform/variation-point analysis in
  `system-catalogues/social-systems/cross-system/` and
  `system-catalogues/dev-frameworks/cross-framework/` both depend on
  the fact that all systems were decomposed using the same five
  levels.
- As the ontological match for the working definition in
  `knowledge/foundations/system-definition.md`: goals / connections /
  parts in the replaceability hierarchy map directly onto G / (F+L) / P.
