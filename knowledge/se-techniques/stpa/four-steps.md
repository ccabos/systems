# The Four Steps of STPA

STPA is a four-step procedure. Each step takes the previous step's
output as input and produces a new artefact.

| Step | Name | What It Produces |
|------|------|------------------|
| 1 | Define Purpose of the Analysis | Losses, Hazards, System-level Constraints |
| 2 | Model the Control Structure | Hierarchical diagram of controllers, control actions, feedback, process models |
| 3 | Identify Unsafe Control Actions | Systematic enumeration of UCAs across the four UCA types |
| 4 | Identify Loss Scenarios | Causal analysis explaining why each UCA could occur |

## Step 1 — Define Purpose

Fix three things:

- **Losses.** Unacceptable outcomes the stakeholders want to
  avoid. Losses are stated in stakeholder language, not engineering
  language: "loss of life," "loss of public trust," "loss of
  legitimate succession," "loss of financial solvency."
- **Hazards.** System states that, in a worst-case environment,
  would lead to a loss. Hazards are stated as system conditions:
  "the executive acts without legitimate authority," "funds leave
  the treasury without audit trail."
- **System-level Constraints.** Must-statements that prevent each
  hazard: "the executive must only act within its legitimate
  authority," "funds must not leave the treasury without audit
  trail."

Step 1's output is small (a few losses, a handful of hazards, one
constraint per hazard) but the later steps all depend on getting
it right.

## Step 2 — Model the Control Structure

Draw the system as a hierarchy of **controllers** and
**controlled processes**, connected by **control actions**
(downward) and **feedback** (upward). Each controller has a
**process model** — its internal representation of the state of
the thing it is controlling.

In social systems, controllers are offices, ministries, boards,
assemblies; controlled processes are populations, budgets,
programmes, members; control actions are decisions, orders,
appointments, budgets; feedback is reports, audits, complaints,
elections.

The control structure should be at the level of the logical
architecture from the SE decomposition — not the level of
individual physical actors.

## Step 3 — Identify Unsafe Control Actions

For every control action in the structure, ask the four UCA
questions (see `unsafe-control-actions.md`). Each UCA is written
as a specific hazardous condition: "Parliament does not withdraw
confidence when the executive acts unconstitutionally →
H1."

The output of Step 3 is a table: control action × UCA type →
hazard reference.

## Step 4 — Identify Loss Scenarios

For each UCA, ask *why* it could occur. Possible causes are
organised around the control loop:

- The controller's **process model** is wrong (wrong beliefs
  about the state of the controlled process).
- The **feedback** channel is missing, delayed, or corrupted.
- The **control action** is executed incorrectly by the actuator.
- The **controlled process** has changed state unexpectedly.
- An **external disturbance** defeats the controller.

Each loss scenario suggests a remedy: fix the process model, fix
the feedback, fix the actuator, etc. Step 4 is where STPA becomes
constructive — it points at specific design changes in the
control structure.
