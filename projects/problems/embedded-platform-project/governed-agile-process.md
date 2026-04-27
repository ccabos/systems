# Governed Agile — What to Add to Scrum

**Purpose:** A practical guide for the development manager of the new
embedded platform project. It starts from Scrum — the process the
line organisation already uses — and lists exactly what needs to be
added to make it Governed Agile: a process suited to an embedded
industrial platform, a mostly inexperienced team, and the governance
needs of a common manager who must authorise stages and have an
independent view of progress.

---

## What Governed Agile is, in plain language

Scrum is good at keeping a team moving and adapting. It is not good
at giving a manager above the team an independent, objective picture
of whether the project is on track. And it does not require
systematic traceability between what was promised and what was tested
— which matters for embedded systems and for cybersecurity standards.

Governed Agile keeps everything Scrum already does well and adds
three things Scrum lacks:

1. **Stage gates** — points at which the common manager looks at
   what has been built, checks it against defined criteria, and
   explicitly authorises the next stage. The team cannot proceed
   without this authorisation.
2. **Test traceability** — every requirement has a corresponding
   test, written at the same time as the requirement, not after
   the code is done. This is the V-Model's core insight, applied
   inside the Scrum cadence.
3. **A formal risk and change log** — a live document tracking open
   risks, their status, and any agreed changes to the baseline. This
   gives the common manager early warning of problems and a record
   of decisions.

---

## What Scrum already gives you — keep all of this

From the Scrum decomposition
(`knowledge/system-catalogues/dev-frameworks/scrum/se-decomposition.md`):

| Scrum element | Keep as-is |
|---|---|
| Sprints (fixed-length iterations, 2–4 weeks) | Yes |
| Product Backlog + Product Owner | Yes — Product Owner is the technology lead or their delegate |
| Cross-functional team, self-organising within the Sprint | Yes |
| No scope changes during a Sprint | Yes |
| Sprint Planning, Daily Scrum, Sprint Review, Retrospective | Yes |
| Definition of Done | Yes — and it needs to be extended (see below) |
| Working software as the primary measure of Sprint progress | Yes |

Nothing is removed from Scrum. Everything below is additive.

---

## What to add — four areas

### Area 1 — Stage governance (from PRINCE2)

This is the most important addition. It gives the common manager
authority over the project at defined intervals, and gives the
development manager a formal structure for reporting.

**What a stage is:** A stage is a group of Sprints — typically three
to five — that together deliver a meaningful chunk of the platform.
The common manager authorises each stage before it starts, based on
defined exit criteria from the previous stage. The project cannot
begin a new stage without that authorisation.

**What to create:**

*Project Initiation Document (PID) — once, at the start*

A short document (not more than four to six pages) that states:
- What the project is building and why
- The agreed stages and their expected duration
- The governance structure: who authorises what, and what happens
  when a tolerance is breached
- The baseline requirements for the new platform (high level)
- The risk log (started here, maintained throughout)

This is not a detailed specification. It is the document the common
manager signs off on to authorise the project to begin.

*Stage Plan — once per stage, before the stage starts*

A short document (one to two pages) that states:
- What the stage will deliver (in terms of working, tested capability)
- The exit criteria the common manager will check at the stage gate
- The Sprints planned within the stage and their goals
- Any known risks specific to this stage

*End Stage Report — once per stage, at the stage gate*

A short document showing:
- What was actually delivered (compared to the Stage Plan)
- Status of all exit criteria (met / not met / partially met)
- Risk log update
- Whether the business case for the project still holds
- Request for authorisation to begin the next stage

*Management by exception — ongoing*

Define tolerances in the PID. For example: the development manager
can handle a cost overrun of up to 10% within a stage without
escalating. If a tolerance is breached, the development manager
escalates to the common manager immediately — they do not wait for
the next stage gate. This prevents the common manager from being
surprised at a gate.

**Stage gate exit criteria — example set for this project:**

The following are suggested starting criteria. The development
manager and common manager should agree the actual criteria before
each stage starts.

- All Sprint goals for the stage were met (or agreed exceptions
  documented)
- Definition of Done met for all items delivered in the stage
- All test cases for the stage's requirements have passed
- No critical or high-severity defects are open
- Risk log reviewed and all open risks have a named owner and a
  mitigation action
- Next Stage Plan drafted and reviewed by the development manager

---

### Area 2 — Test traceability (from V-Model)

From the V-Model decomposition
(`knowledge/system-catalogues/dev-frameworks/v-model/se-decomposition.md`),
the essential principle is: every design decision has a corresponding
test, and the test is designed at the same time as the decision, not
afterwards.

In practice, inside a Scrum Sprint, this means:

**Extended Definition of Done**

Add the following to the team's Definition of Done:

- A test case exists for every acceptance criterion of every backlog
  item delivered in this Sprint
- Test cases are linked to the requirement or backlog item they verify
  (in whatever tool the team uses — Jira, Azure DevOps, or a simple
  spreadsheet)
- Integration tests exist for every interface between the new platform
  and the systems it connects to
- All tests have been run and have passed before the Sprint Review

**Four test levels, each with a home in the process:**

| Test level | When it runs | Who checks it |
|---|---|---|
| Unit tests | Automated, on every commit (CI pipeline) | CI pipeline — fails the build |
| Integration tests | Automated, on every commit or nightly | CI pipeline |
| System tests | Manually or automated, at Sprint boundary | Development manager checks results before Sprint Review |
| Acceptance tests | At stage gate | Common manager sees results in End Stage Report |

The team does not need to do all four manually. The CI/CD pipeline
(see Area 4 below) handles unit and integration tests automatically.
System tests at Sprint boundary and acceptance tests at the stage gate
are the two levels that require deliberate attention.

**Requirements traceability — a lightweight version**

For each high-level requirement in the PID, maintain a simple table
showing which backlog items implement it and which test cases verify
it. This does not need a specialised tool. A spreadsheet or a
structured section in the project wiki is sufficient. The purpose is
to be able to answer, at any stage gate: "Is every requirement we
committed to covered by a test that has passed?"

This is the evidence the common manager sees at the stage gate. It is
also the evidence that a cybersecurity standard auditor would ask for.

---

### Area 3 — Risk and change management (from PRINCE2)

**Risk log**

A live document listing every identified risk with:
- A short description of what could go wrong
- The likelihood (high / medium / low is sufficient)
- The impact if it occurs
- A named owner who is responsible for managing it
- The current mitigation action and its status

The development manager reviews the risk log every Sprint. The common
manager sees it at every stage gate. Risks are not removed when they
are resolved — they are marked closed with the date and how they
were resolved.

Starting risks for this project (from the structural analysis):

| Risk | Owner | Mitigation |
|---|---|---|
| Three shared engineers pulled to line more than 20% | Development manager | Written priority rule (see memo) |
| Cybersecurity standard requires new assessment for new architecture | Common manager | Commission check within first month (see memo) |
| Line team not ready to take over at handover | Development manager | Embed line engineers during project; track readiness against gate criteria |
| 12 engineers unfamiliar with embedded platform domain | Technology lead | Pair new engineers with experienced ones; define onboarding plan in Sprint 1 |

**Change control**

When someone wants to change the baseline requirements agreed in the
PID, they cannot just update the backlog. They submit a brief change
request (one paragraph describing the change, its impact on scope,
time, and cost) to the development manager. The development manager
either approves it within the current tolerances or escalates it to
the common manager. All approved changes are logged.

This prevents scope drift — the gradual expansion of what the project
is building without any corresponding adjustment to timeline or
resources.

---

### Area 4 — CI/CD pipeline (from DevOps)

The line organisation already runs DevOps. The new platform needs
its own CI/CD pipeline from the start — not added later as a
clean-up task.

From the DevOps decomposition
(`knowledge/system-catalogues/dev-frameworks/devops/se-decomposition.md`),
the minimum pipeline for the new project:

| Pipeline stage | What it does | When it runs |
|---|---|---|
| Build | Compiles the embedded platform code | Every commit |
| Unit tests | Runs all unit tests; fails the build if any test fails | Every commit |
| Static analysis | Checks code quality and security patterns | Every commit |
| Integration tests | Runs tests against the platform's interfaces | Every commit or nightly |
| Artefact publishing | Produces a deployable build if all checks pass | Every commit to main branch |

Security scanning should be included from the start, given the
cybersecurity context. The DevOps decomposition calls this DevSecOps:
automated scanning for known vulnerabilities in dependencies and
in the code itself, running as part of the pipeline, not as a
separate manual activity.

The pipeline does not need to be sophisticated on day one. A working
build-and-unit-test pipeline on the first day of the project is more
valuable than a complete pipeline delivered in Sprint 3.

---

## How the process looks in practice — one full stage

```
Stage start
  │
  ├── Common manager authorises the stage (reviews Stage Plan)
  │
  ├── Sprint 1
  │   ├── Sprint Planning (select backlog items, define Sprint Goal)
  │   ├── Daily Scrums
  │   ├── Development with test cases written alongside
  │   ├── CI/CD pipeline running on every commit
  │   ├── Sprint Review (demonstrate working capability to stakeholders)
  │   └── Retrospective (improve the process)
  │
  ├── Sprint 2  (same structure)
  │
  ├── Sprint 3  (same structure)
  │
  └── Stage gate
      ├── Development manager prepares End Stage Report
      ├── System test results reviewed
      ├── Requirements traceability table reviewed
      ├── Risk log reviewed
      ├── Exit criteria checked
      └── Common manager authorises next stage (or pauses to resolve issues)
```

---

## What NOT to take from PRINCE2 or V-Model

Governed Agile is a deliberate selection, not full PRINCE2 plus full
V-Model. The following elements from those frameworks are explicitly
not included, because they add overhead without value at this project
scale:

| Element | Why it is excluded |
|---|---|
| Full PRINCE2 management product set (15+ documents) | Too heavy for a 15-person project; the four documents above are sufficient |
| Sequential V-Model phases (all design before any build) | Prevents the iterative delivery that Scrum enables; the V-Model's value is its test structure, not its phase sequence |
| Formal IV&V (independent verification and validation) | Appropriate for safety-critical systems; not required here unless the cybersecurity assessment identifies it as necessary |
| PRINCE2 Project Board with Customer, Senior Supplier, Senior User | The common manager fills this role alone for this project; a full board adds meeting overhead without adding governance capability |

---

## The additions in one table

| What | From | In the process | Frequency |
|---|---|---|---|
| Project Initiation Document | PRINCE2 | Once, at start | — |
| Stage Plan | PRINCE2 | Once per stage, before it starts | Every 3–5 Sprints |
| Stage gate (common manager authorisation) | PRINCE2 | End of each stage | Every 3–5 Sprints |
| End Stage Report | PRINCE2 | End of each stage | Every 3–5 Sprints |
| Management by exception (tolerances) | PRINCE2 | Ongoing | Immediate on breach |
| Risk log | PRINCE2 | Ongoing | Reviewed every Sprint |
| Change log | PRINCE2 | Ongoing | On every change request |
| Test cases written alongside requirements | V-Model | Inside every Sprint | Every Sprint |
| Requirements traceability table | V-Model | Ongoing | Updated every Sprint |
| System test at Sprint boundary | V-Model | End of every Sprint | Every Sprint |
| Acceptance test at stage gate | V-Model | End of every stage | Every stage |
| CI/CD pipeline (build, unit, integration, security) | DevOps | From day one | Every commit |

---

## Sources

- `knowledge/system-catalogues/dev-frameworks/scrum/se-decomposition.md`
- `knowledge/system-catalogues/dev-frameworks/prince2/se-decomposition.md`
- `knowledge/system-catalogues/dev-frameworks/v-model/se-decomposition.md`
- `knowledge/system-catalogues/dev-frameworks/devops/se-decomposition.md`
- `knowledge/system-catalogues/dev-frameworks/cross-framework/hybrids.md`
  (Hybrid A — Governed Agile)
- `knowledge/system-catalogues/dev-frameworks/cross-framework/merging-principles.md`
- `knowledge/system-catalogues/dev-frameworks/cross-framework/variation-points.md`
