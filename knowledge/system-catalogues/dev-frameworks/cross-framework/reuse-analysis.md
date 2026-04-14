# Reuse Analysis Across Development Frameworks

Extracted from `projects/systems-introduction-book/docs/part3/frameworks.md`
§5. Classification of framework elements by how far they can be reused
across frameworks: freely, with adaptation, or not at all.

## Fully Reusable (Any Framework Can Adopt These)

| Element | Source | Why It's Universal |
|---------|--------|-------------------|
| **Version control** (Git) | DevOps / all modern | No framework is harmed by tracking changes. Even Waterfall benefits. |
| **Visual work tracking** (board) | Kanban | Making work visible helps regardless of temporal structure. A Waterfall team with a Kanban board is strictly better than one without. |
| **Retrospectives** | Scrum | Every framework benefits from periodic process reflection. PRINCE2 calls them "Lessons Learned"; the mechanism is identical. |
| **Definition of Done** | Scrum | An explicit quality checklist works in any context — Waterfall phase exits, Kanban done columns, PI increments. |
| **Automated testing** | DevOps | Automated tests reduce defects in any framework. A V-Model project with CI is strictly better than one without. |
| **User research / empathy** | Design Thinking | Understanding users before defining requirements improves outcomes regardless of whether you then plan sequentially or iterate. |

## Partially Reusable (Adopt with Adaptation)

| Element | Source → Target | Required Adaptation |
|---------|----------------|-------------------|
| **Sprint structure** | Scrum → Waterfall | Use iterations *within* phases: e.g., 2-week design sprints within the Design phase, each producing a reviewed design increment. Not full Scrum, but iterative refinement within a sequential frame. |
| **Business Case governance** | PRINCE2 → Scrum | Add a lightweight Business Case review at major milestones (e.g., every 3 Sprints). The Product Owner maintains it. Adds governance without killing agility. |
| **Architectural runway** | SAFe → Scrum | Single-team Scrum benefits from dedicating a fraction of backlog capacity to technical enablers. SAFe formalizes this; small teams can adopt the practice without the SAFe apparatus. |
| **CI/CD pipeline** | DevOps → V-Model | The V-Model's right arm (testing levels) can be automated as pipeline stages. Unit tests run on commit, integration tests nightly, system tests on merge to main. The V-Model's structure is *preserved* but *accelerated*. |
| **Empathize/Define phases** | Design Thinking → Scrum | Front-load a Design Thinking "Sprint Zero" before the first Scrum Sprint. Use empathy research and problem framing to populate the initial Product Backlog with validated user needs. |
| **WIP limits** | Kanban → Scrum | Scrum teams often overload Sprints. Adding explicit WIP limits to the Sprint Board (e.g., max 3 items in "In Progress") is pure Kanban transplanted into a Scrum iteration. Widely practiced, always beneficial. |
| **Portfolio Kanban** | SAFe → PRINCE2 | PRINCE2 manages individual projects but struggles with portfolio flow. A Lean Portfolio Kanban board showing all projects in stages (Funnel → Analyzing → Implementing → Done) adds flow visibility to PRINCE2's governance. |

## Structurally Incompatible

| Element | Source | Conflicts With | Why |
|---------|--------|---------------|-----|
| **No iterations** (pure flow) | Kanban | Scrum's Sprint commitment | Scrum's social contract depends on the timebox: the team commits for a fixed period. Removing the timebox removes the commitment mechanism. You get Kanban, which is fine — but it's no longer Scrum. |
| **Complete upfront requirements** | Waterfall | Scrum's emergent requirements | If you baseline all requirements before Sprint 1 and forbid changes, you've removed Scrum's adaptive mechanism. You have Waterfall with stand-up meetings. |
| **Hierarchical task assignment** | Waterfall PM | Scrum self-organization | If the PM assigns individual tasks within Sprints, the team loses ownership and the ability to self-optimize. This is the most common hybrid antipattern. |
| **Fixed scope + fixed date** | Waterfall contract | Any adaptive framework | Adaptive frameworks require that at least one of scope, date, or budget is variable. Fixing all three forces plan-driven execution regardless of what you call it. |
| **No documentation** | Extreme Agile interpretation | V-Model / PRINCE2 / regulated environments | Regulated domains (medical, automotive, aviation) *legally require* traceable documentation. "Working software over documentation" does not mean "no documentation." |
