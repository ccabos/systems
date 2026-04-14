# STPA — Overview

**STPA** (System-Theoretic Process Analysis) is the hazard
analysis technique built on the STAMP accident model (see
`../stamp/overview.md`). Where STAMP tells you *what* an accident
is (a loss caused by inadequate control), STPA tells you *how* to
find the places where inadequate control could occur, before the
loss happens.

## What STPA produces

A complete STPA analysis produces four kinds of artefact:

1. **Losses** — unacceptable outcomes the stakeholders want to
   avoid (loss of life, loss of trust, loss of legitimacy, loss of
   funds).
2. **Hazards** — system states that could lead to a loss.
3. **Control structure** — a hierarchical diagram of controllers,
   controlled processes, control actions, and feedback channels.
4. **Unsafe Control Actions (UCAs)** and **loss scenarios** — a
   systematic enumeration of how each control action could be
   unsafe, and the causal factors that would make each UCA
   actually occur.

## The procedure

The procedure is four steps, described in `four-steps.md`. Each
step takes the output of the previous step as input. The last step
is the one that produces design recommendations: by identifying
the causal factors behind each unsafe control action, STPA tells
you what to change in the control structure (not in the
components) to prevent the loss.

## Relation to the SE hierarchy

STPA does not duplicate the five-level SE decomposition — it
consumes it. A completed SE decomposition gives STPA most of what
it needs for Step 1 (losses and constraints) and Step 2 (control
structure). The integration rules are in `from-se-to-stpa.md`.

## Relation to remedies

STPA is the *hazard analysis* side of the technique. The matching
*remedy* catalogue — the specific design patterns that prevent
common UCAs in social systems — lives under
`knowledge/se-techniques/remedies/`. Together they form the
analyse-then-fix pair used throughout the project's Part IV work.
