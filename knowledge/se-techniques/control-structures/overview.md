# Control Structures — Overview

A **control structure** is a hierarchical arrangement of
controllers, controlled processes, control actions, and feedback
channels. The concept is the central object of STAMP/STPA (see
`../stamp/overview.md` and `../stpa/overview.md`), but it is
useful on its own as a diagnostic lens: once you have a system's
control structure, a small number of generic questions will
reveal most of its failure modes.

## The universal control pattern

Across the non-technical systems studied in this project, control
structures have a common four-level shape:

| Level | Role |
|-------|------|
| **Supreme Authority** | Issues doctrine, law, strategy, or policy |
| **Intermediate Controllers** | Interpret and transmit downward; aggregate and filter upward |
| **Local Community** | Enforces norms through social mechanisms; primary source of ground-truth feedback |
| **Individual** | Internalises norms; self-regulates; ultimate recipient of system outcomes |

What varies across systems is *who* occupies each level, *what
mechanisms* connect them, and *how honest* the upward flow is.
The pattern itself is invariant.

## The five diagnostic questions

Every control structure can be interrogated with the same five
questions. They are listed here and expanded in
`diagnostic-questions.md`. Question 5 applies only to social
systems.

1. **Feedback richness** — how many independent channels carry
   information upward, and how accurately do they represent the
   state of the controlled process?
2. **Self-sealing tendency** — can the process model at the top
   be corrected by information from below, or does it filter out
   contradictory signals?
3. **Accountability voids** — where is the controller also the
   interested party, so that independent oversight is
   structurally prevented?
4. **Circuit breakers** — what mechanisms can interrupt an
   escalating harmful loop before it causes irreversible damage?
5. **Rung match** *(social systems)* — at what justificatory
   rungs do the loop's control action and feedback operate, and
   is the loop symmetric? See `../justification-rungs/`.

## What this technique adds

The SE hierarchy says *what the system is*. STPA says *what
specific control actions could be unsafe*. The control-structure
technique sits between them: it turns the logical architecture
into a control diagram and applies a fixed checklist (the five
questions above, the four dangerous patterns in
`dangerous-patterns.md`) that catches the most common failure
modes without a full STPA pass.

It is the quick-diagnosis layer: if one of the five questions
returns a bad answer, or one of the four patterns is present, a
full STPA analysis is warranted.

## Where it is applied in this project

- Technique definitions and generic remedies live in this folder.
- The justificatory-rung extension for social systems lives in
  `../justification-rungs/`.
- Per-system control-structure profiles for the ten social
  systems live in
  `knowledge/system-catalogues/social-systems/cross-system/control-structure-profiles.md`.
- Per-system remedy case studies (Basic Law, SOX, Mitbestimmung,
  Vatican II, pre-registration, Bundeswehr model) live in
  `knowledge/system-catalogues/social-systems/cross-system/remedies-case-studies.md`.
