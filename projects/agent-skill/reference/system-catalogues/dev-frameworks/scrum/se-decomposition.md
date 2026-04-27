# Scrum — SE Decomposition

Extracted from `projects/systems-introduction-book/docs/part3/frameworks.md`
§2.4. IDs use the `S*` prefix as in the source.

## Goals (SG)

- **SG1** — Deliver valuable, working product increments frequently
- **SG2** — Maximize adaptability to changing requirements and emerging understanding
- **SG3** — Empower self-organizing teams to find the best solutions
- **SG4** — Enable continuous improvement through inspect-and-adapt cycles

## Requirements (SR)

- **SR1** — Fixed-length iterations (Sprints, typically 1–4 weeks)
- **SR2** — Prioritized Product Backlog maintained by a single Product Owner
- **SR3** — Cross-functional team with all skills needed to deliver an increment
- **SR4** — No scope changes during a Sprint
- **SR5** — Working software as the primary measure of progress
- **SR6** — Regular retrospectives to improve the process

## Functions (SF)

- **SF1** — Backlog refinement — clarify, estimate, prioritize upcoming work
- **SF2** — Sprint Planning — select backlog items, define Sprint Goal
- **SF3** — Daily coordination — Daily Scrum, impediment removal
- **SF4** — Increment delivery — develop, integrate, test within the Sprint
- **SF5** — Sprint Review — demonstrate increment to stakeholders, collect feedback
- **SF6** — Sprint Retrospective — inspect process, define improvements

## Logical Architecture (SL)

- **SL1** — Product Discovery Subsystem — Product Owner, Backlog, stakeholder feedback
- **SL2** — Sprint Execution Subsystem — Dev Team, Sprint Backlog, Daily Scrum
- **SL3** — Integration & Quality Subsystem — Definition of Done, testing within Sprint
- **SL4** — Continuous Improvement Subsystem — Retrospective, impediment tracking

## Physical Implementation (SP)

- **SP1** — Product Backlog (Jira, Azure DevOps, physical board), user stories
- **SP2** — Sprint Board (Kanban-style task board), burndown chart
- **SP3** — Scrum roles: Product Owner, Scrum Master, Development Team
- **SP4** — Sprint ceremonies: Planning, Daily, Review, Retro (timeboxed meetings)
- **SP5** — Definition of Done document, increment artifact
