# SAFe (Scaled Agile Framework) — SE Decomposition

Extracted from `projects/systems-introduction-book/docs/part3/frameworks.md`
§2.8. IDs use the `SA*` prefix as in the source.

## Goals (SAG)

- **SAG1** — Apply Agile principles at enterprise scale across multiple teams
- **SAG2** — Align strategy, portfolio investment, and team execution
- **SAG3** — Deliver integrated solutions across large, complex programs
- **SAG4** — Enable governance and predictability without sacrificing agility

## Requirements (SAR)

- **SAR1** — Agile Release Trains (ARTs) — long-lived teams-of-teams aligned to a value stream
- **SAR2** — Program Increments (PIs) — fixed ~10-week cadences with planning events
- **SAR3** — Portfolio-level Lean budgeting — fund value streams, not projects
- **SAR4** — Architectural runway — intentional technical foundation work
- **SAR5** — Built-in quality — TDD, CI/CD, peer review at every level
- **SAR6** — System demos and inspect-and-adapt at every PI boundary

## Functions (SAF)

- **SAF1** — PI Planning — face-to-face alignment of all teams in an ART on objectives
- **SAF2** — Team-level Scrum/Kanban execution within PIs
- **SAF3** — System integration — continuous integration across teams, system demo
- **SAF4** — Portfolio management — strategic themes, Lean business cases, epic approval
- **SAF5** — Architectural governance — define and maintain architectural runway
- **SAF6** — Inspect & Adapt — quantitative measurement, problem-solving workshop

## Logical Architecture (SAL)

- **SAL1** — Portfolio Subsystem — Lean Portfolio Management, strategic themes, epic Kanban
- **SAL2** — Program Subsystem — ART, Release Train Engineer, PI cadence
- **SAL3** — Team Subsystem — Scrum/Kanban teams within the ART
- **SAL4** — Technical Foundation Subsystem — architectural runway, enablers, CI/CD

## Physical Implementation (SAP)

- **SAP1** — PI Planning event (2-day, all-hands), Program Board, ROAM risk board
- **SAP2** — ART backlog, team backlogs, PI objectives, Jira/Rally/Azure DevOps
- **SAP3** — System demo, Inspect & Adapt workshop, business owners
- **SAP4** — Lean Portfolio Management tooling, portfolio Kanban, guardrails
