# Kanban — SE Decomposition

Extracted from `projects/systems-introduction-book/docs/part3/frameworks.md`
§2.5. IDs use the `KB*` prefix as in the source (to distinguish from
kingdom's `K*` prefix in the social-systems catalogue).

## Goals (KBG)

- **KBG1** — Optimize the flow of value delivery by making work and bottlenecks visible
- **KBG2** — Minimize lead time and maximize throughput
- **KBG3** — Enable evolutionary, incremental process improvement

## Requirements (KBR)

- **KBR1** — Visualize the entire workflow on a shared board
- **KBR2** — Limit Work in Progress (WIP) at each workflow stage
- **KBR3** — Manage flow — measure lead time, cycle time, throughput
- **KBR4** — Make process policies explicit
- **KBR5** — Use feedback loops (reviews, standups, metrics) to improve
- **KBR6** — Start with what you do now — no prescribed roles or iterations

## Functions (KBF)

- **KBF1** — Work visualization — represent all items and their status
- **KBF2** — WIP limiting — enforce column limits, pull (don't push) work
- **KBF3** — Flow measurement — track cycle time, lead time, cumulative flow
- **KBF4** — Bottleneck identification — detect and resolve flow impediments
- **KBF5** — Continuous replenishment — pull new work when capacity is available
- **KBF6** — Process evolution — adjust policies based on flow data

## Logical Architecture (KBL)

- **KBL1** — Visualization Subsystem — board, columns, swim lanes, WIP limits
- **KBL2** — Flow Management Subsystem — metrics, policies, SLAs
- **KBL3** — Improvement Subsystem — feedback cadences, experiments, policy evolution

## Physical Implementation (KBP)

- **KBP1** — Kanban board (physical or digital: Jira, Trello, Azure DevOps)
- **KBP2** — WIP limit signs, pull policies, class-of-service definitions
- **KBP3** — Cumulative flow diagram, lead time histogram, throughput chart
- **KBP4** — Cadences: standup, replenishment, delivery planning, retrospective
