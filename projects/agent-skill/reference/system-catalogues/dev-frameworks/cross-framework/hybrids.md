# Three Hybrid Architectures

Extracted from `projects/systems-introduction-book/docs/part3/frameworks.md`
§6. Three principled hybrid configurations derived from the product-
line analysis. Each makes explicit binding decisions at all four
variation points (see `variation-points.md`) and specifies which
elements are reused from which source framework.

## Hybrid A — "Governed Agile"

**Target context:** Large organizations, regulated industries (medical
devices, automotive, maritime OT, defense), contractual delivery
commitments. The problem: pure Scrum lacks governance; pure PRINCE2
lacks adaptability.

**Binding decisions:**

| VP | Binding |
|----|---------|
| VP1: Temporal Structure | **Staged iterations** — PRINCE2 stages, each containing multiple Scrum Sprints |
| VP2: Requirements | **Progressive elaboration within a governed envelope** — high-level requirements baselined at project start (PRINCE2 PID), detailed requirements emerge per Sprint (Scrum backlog) |
| VP3: Authority | **Layered** — Project Board authorizes stages (PRINCE2); Product Owner prioritizes within stage (Scrum); team self-organizes within Sprint |
| VP4: QA Timing | **V-Model test levels automated in CI/CD pipeline** — unit tests on commit, integration tests nightly, system tests at Sprint boundary, acceptance tests at stage boundary |

**Reused elements:**

| From | Element |
|------|---------|
| PRINCE2 | Business Case, stage-gate authorization, management by exception, risk register |
| Scrum | Sprint cadence, Product Backlog, Sprint Review, Retrospective, self-organizing team |
| V-Model | Symmetric test planning — test cases written during corresponding design/Sprint |
| DevOps | CI/CD pipeline automating the V-Model's right arm |
| Design Thinking | Empathy research in pre-project "Discovery" stage |
| Kanban | WIP limits on Sprint Board, visual flow tracking |

**Architecture sketch:**

```
Discovery Stage          (Design Thinking empathy + PRINCE2 PID)
  └── Stage 1            (PRINCE2 stage gate)
      ├── Sprint 1       (Scrum + WIP limits)
      ├── Sprint 2       (Scrum + WIP limits)
      └── Sprint 3       (Scrum + WIP limits)
      └── Stage Gate     (Business Case review, V-Model system test, PRINCE2 End Stage Report)
  └── Stage 2
      ├── Sprint 4–6
      └── Stage Gate
  └── Release            (DevOps CD pipeline, PRINCE2 project closure)
```

**Why it's coherent:** The PRINCE2 stages provide the governance
envelope that regulators and contracts demand. Within that envelope,
Scrum provides adaptability. The V-Model's test structure is preserved
but automated through DevOps. Requirements are *baselined at the
stage level* (satisfying PRINCE2) but *emergent at the Sprint level*
(satisfying Scrum). The variation point bindings are compatible
because stage-level planning is coarser-grained than Sprint-level
adaptation.

**Real-world precedent:** This is essentially what IEC 62443
compliance in industrial environments requires — a governed lifecycle
with internal agility. The German V-Modell XT already moves in this
direction by allowing iterative execution within a V-Model frame.

## Hybrid B — "Discovery-Driven Flow"

**Target context:** Product companies, SaaS teams, startups. The
problem: pure Scrum's Sprint cadence can feel artificial for mature
teams; pure Kanban lacks discovery discipline; neither includes
systematic user research.

**Binding decisions:**

| VP | Binding |
|----|---------|
| VP1: Temporal Structure | **Continuous flow with periodic discovery cycles** — no Sprints for delivery, but 2-week Design Thinking cycles for discovery |
| VP2: Requirements | **Requirements are hypotheses** — validated through prototyping and A/B testing |
| VP3: Authority | **Product trio** — Product Manager (value), Tech Lead (feasibility), Designer (usability) co-decide; team self-organizes execution |
| VP4: QA Timing | **Continuous automated + user validation** — CI/CD pipeline for technical quality, regular user testing for product quality |

**Reused elements:**

| From | Element |
|------|---------|
| Design Thinking | Empathize → Define → Ideate → Prototype → Test cycles for discovery |
| Kanban | Visual board, WIP limits, flow metrics (lead time, throughput), pull system |
| DevOps | Full CI/CD pipeline, feature flags for safe experimentation, monitoring |
| Scrum | Retrospectives (every 2 weeks, decoupled from delivery), Definition of Done |
| SAFe | Architectural runway concept — dedicate ~20% of flow capacity to enablers |

**Architecture sketch:**

```
Continuous Discovery Track     (Design Thinking, 2-week cycles)
  ├── Empathize + Define       → Problem hypotheses
  ├── Ideate + Prototype       → Solution hypotheses
  └── Test with users          → Validated backlog items

Continuous Delivery Track      (Kanban + DevOps, no iterations)
  ├── Kanban board             → Pull validated items
  ├── WIP-limited execution    → Build + automated test
  ├── CI/CD pipeline           → Deploy to production
  └── Monitor + A/B test       → Validate in production

Periodic Rituals (decoupled from flow):
  ├── Retrospective            (every 2 weeks)
  ├── Architectural review     (monthly)
  └── Portfolio review         (quarterly)
```

**Why it's coherent:** Discovery (understanding *what* to build) runs
on Design Thinking's exploratory loop. Delivery (actually building
it) runs on Kanban's continuous flow with DevOps automation. The two
tracks are decoupled but connected through the backlog: discovery
*produces* validated items; delivery *consumes* them. This eliminates
the artificial synchronization of fitting discovery and delivery into
the same Sprint boundary.

**Real-world precedent:** Teresa Torres' "Continuous Discovery
Habits," Basecamp's "Shape Up" (which uses 6-week cycles for shaping
+ continuous build), Spotify's squad model (discovery + delivery
separation).

## Hybrid C — "Scaled Governed Flow"

**Target context:** Enterprises with a mix of project types: some
innovative, some regulatory, some maintenance. The problem: SAFe is
too prescriptive for small teams; PRINCE2 doesn't scale to continuous
work; pure Kanban lacks strategic alignment.

**Binding decisions:**

| VP | Binding |
|----|---------|
| VP1: Temporal Structure | **Mixed** — Portfolio on continuous Kanban flow; programs on quarterly PI cadence (SAFe-inspired); teams choose Scrum or Kanban |
| VP2: Requirements | **Tiered** — Portfolio-level: strategic themes and Lean business cases (stable); program-level: PI objectives (medium stability); team-level: emergent |
| VP3: Authority | **Portfolio Board → Value Stream Leads → Team-level autonomy** — governance at the top, self-organization at the bottom |
| VP4: QA Timing | **Continuous automated + PI-boundary integration testing + quarterly business review** |

**Reused elements:**

| From | Element |
|------|---------|
| SAFe | Agile Release Trains, PI Planning, portfolio Kanban, architectural runway |
| PRINCE2 | Business Case discipline, management by exception, stage-gate authorization (at PI boundary) |
| Kanban | Portfolio-level flow visualization, WIP limits at all levels, flow metrics |
| Scrum | Team-level Sprint execution (for teams that choose it) |
| DevOps | CI/CD across all teams, shared pipeline infrastructure |
| V-Model | For regulated products within the portfolio: V-Model test structure automated in the pipeline |
| Design Thinking | Discovery track for innovative initiatives, fed into PI planning |

**Architecture sketch:**

```
Portfolio Level (Kanban flow)
  ├── Strategic themes          → Lean business cases → Epic approval
  ├── Portfolio Kanban board    → WIP-limited epic flow
  └── Quarterly Business Review → PRINCE2-style business justification check

Program Level (PI cadence)
  ├── Agile Release Train       → Aligned teams on a value stream
  ├── PI Planning (quarterly)   → Teams commit to PI objectives
  ├── System Demo (per PI)      → Integrated demonstration
  └── Inspect & Adapt           → Program-level retrospective

Team Level (team chooses)
  ├── Option A: Scrum           → Sprints within PI
  ├── Option B: Kanban          → Continuous flow within PI
  └── Option C: V-Model Sprint  → For regulated deliverables (governed agile)

Technical Foundation (shared)
  ├── CI/CD pipeline            → All teams, automated quality gates
  ├── Architectural runway      → Cross-cutting enablers
  └── DevOps platform           → Shared infrastructure, monitoring
```

**Why it's coherent:** The key insight is that *different levels of
the organization face different variation-point contexts.* The
portfolio level needs strategic governance (PRINCE2-like), the
program level needs cross-team alignment (SAFe-like), and the team
level needs execution autonomy (Scrum/Kanban). Forcing a single
framework across all levels creates incoherence. The hybrid explicitly
binds each variation point *per level*, which is a legitimate product-
line technique (called "binding time differentiation" — different
parts of the system bind their variants at different times).

**Real-world precedent:** This is close to what large organizations
like Bosch, Siemens, and automotive Tier-1 suppliers actually practice
(often without naming it). The German automotive SPICE + Agile
harmonization efforts move in this direction.
