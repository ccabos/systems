# Development Framework Variation Points

Extracted from `projects/systems-introduction-book/docs/part3/frameworks.md`
§4. The four primary variation points identified across the eight
decomposed frameworks, plus their interaction constraints.

## VP1 — Temporal Structure of Work

*Interface:* The framework needs a way to organize work in time.

| Variant | Used By |
|---------|---------|
| **Sequential phases** — complete each phase before the next | Waterfall, V-Model |
| **Fixed-length iterations (Sprints/PIs)** — timeboxed cycles of plan-execute-review | Scrum, SAFe |
| **Continuous flow** — no iterations, work pulled as capacity permits | Kanban, DevOps |
| **Exploratory loops** — free-form cycling between stages based on learning | Design Thinking |
| **Staged authorization** — work proceeds in authorized stages of variable length | PRINCE2 |

This is the *primary* variation point — it cascades most strongly into
logical architecture and physical implementation.

## VP2 — Requirements Stability Assumption

*Interface:* The framework needs an assumption about how stable
requirements are.

| Variant | Used By |
|---------|---------|
| **Requirements are knowable upfront** — invest heavily in elicitation and baselining | Waterfall, V-Model, PRINCE2 |
| **Requirements emerge through delivery** — learn by building and showing | Scrum, Design Thinking |
| **Requirements are a backlog to be refined** — prioritized list, progressively elaborated | Scrum, SAFe, Kanban |
| **Requirements are hypotheses** — validated or invalidated through user testing | Design Thinking, DevOps (A/B testing) |

This variation point has the deepest philosophical implications. It
determines whether the framework treats uncertainty as a *problem to
be eliminated* (plan-driven) or a *reality to be navigated* (adaptive).

## VP3 — Authority & Decision Structure

*Interface:* The framework needs to define who makes which decisions.

| Variant | Used By |
|---------|---------|
| **Hierarchical PM authority** — project manager plans and controls, team executes | Waterfall, PRINCE2 |
| **Product Owner + self-organizing team** — PO decides *what*, team decides *how* | Scrum |
| **Shared team authority** — team collectively manages flow, no prescribed roles | Kanban |
| **Multi-level governance** — portfolio → program → team hierarchy | SAFe, PRINCE2 |
| **Facilitator-led collaboration** — design facilitator guides, cross-functional group decides | Design Thinking |
| **Automated pipeline authority** — the CI/CD pipeline enforces quality gates | DevOps |

## VP4 — Quality Assurance Timing

*Interface:* The framework needs to define when and how quality is
verified.

| Variant | Used By |
|---------|---------|
| **End-phase testing** — test after build is complete | Waterfall |
| **Symmetric test planning** — design each test level during corresponding design phase | V-Model |
| **Continuous within iteration** — test within every Sprint, Definition of Done | Scrum, SAFe |
| **Continuous automated** — test on every commit, automated pipeline gates | DevOps |
| **User validation** — test with real users using prototypes | Design Thinking |
| **Flow-integrated** — quality checks as explicit board columns | Kanban |

## Interactions and constraints

Just as with social systems, not all combinations are coherent:

- **VP1 = sequential phases** requires **VP2 = requirements knowable
  upfront.** If requirements are volatile and you've committed to a
  sequential plan, you'll deliver the wrong thing. This is Waterfall's
  well-known failure mode.
- **VP1 = continuous flow** requires **VP4 = continuous automated
  testing.** Without automated quality gates, continuous flow produces
  continuous defects. This is why Kanban without CI/CD produces chaos.
- **VP2 = requirements are hypotheses** requires **VP4 = user
  validation.** If you treat requirements as hypotheses but never test
  them with users, you've gained nothing over a plan-driven approach.
- **VP3 = hierarchical PM authority** is in tension with **VP1 =
  fixed iterations + self-organizing teams.** A project manager who
  dictates task assignments within a Sprint undermines Scrum's core
  mechanism. This is the "Scrum-but" antipattern.
- **VP3 = multi-level governance** requires explicit interfaces
  between levels. SAFe works when the portfolio → program → team
  boundaries are clear; it collapses into bureaucracy when every
  decision escalates.
