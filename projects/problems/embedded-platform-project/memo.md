# Decision Memo — New Embedded Platform Project Setup

**Prepared for:** Common manager (project and line organisation)
**Date:** April 2026
**Status:** For decision

---

## System under analysis

A new project organisation being established alongside the existing
line organisation to develop a renewed embedded platform for an
industrial automation system. The new platform introduces name-based
addressing in place of static addressing. The project team (~15
people) includes three experienced engineers from the current line,
approximately twelve engineers from the service area and new hires,
and is led by a technology lead with deep automation application
expertise. The line organisation continues running the current
platform under a DevOps process and carries an ongoing cybersecurity
obligation. A common manager sits above both organisations.

---

## Key findings

Five structural gaps were identified. Three require decisions before
the team is assembled. Two require decisions before the project ends.

### Finding 1 — No rule governs the split of the three shared engineers

The three experienced engineers who hold most of the system knowledge
are intended to spend 80% of their time on the project and 20% on
line bug fixes. This arrangement has no written rule defining what
qualifies as a line interruption or who has authority to call one.
Under pressure — and production crises in the line will occur — both
the technology lead and the line manager will assert priority. Without
a rule, the common manager will be called to arbitrate repeatedly and
unpredictably, and the 20% will expand.

### Finding 2 — The development process is undefined and has no owner

No development manager has been identified for the new project, and
the choice of development process has not been made. A team of fifteen
people, most of them new to embedded platform development, cannot
self-organise into a productive working method. Without a defined
process, there are no milestones, no quality gates, and no independent
signal telling the common manager whether the project is on track.
The technology lead — whose expertise is in automation applications,
not development process management — will be drawn into process
decisions they are not mandated to own, reducing the time available
for the technical leadership the project actually needs from them.

### Finding 3 — The common manager has no independent progress signal

Without defined milestones and quality gates, the only information
channel from the project to the common manager runs through the
technology lead. This means the manager's picture of project health is
populated by the same person whose work it is supposed to reflect.
Problems will become visible only when they are large enough to be
undeniable. An independent signal — in the form of stage-gate reviews
against defined exit criteria — is needed to give the common manager
early warning.

### Finding 4 — The handover to the line organisation is not designed

The project is a temporary structure. At some point the new platform
must be taken over by the line organisation and extended for further
use cases. This transition has not been designed. If handover planning
starts only when the project ends, the line team will face a new
architecture they do not understand, under operational pressure, with
the project team already disbanded. The handover needs to be treated
as a process running throughout the project, not as a final event.

### Finding 5 — The cybersecurity inheritance assumption needs verification

The current assumption is that the cybersecurity compliance work
being done for the existing platform covers the new platform as well.
A name-based addressing architecture is structurally different from
static addressing. Most industrial cybersecurity standards require a
fresh risk assessment when the addressing architecture changes, not a
transfer of the existing one. If this assumption is wrong, it will
surface late and require significant rework. A brief, targeted check
— one person, a few days — is sufficient to confirm or correct it.

---

## Structural causes

Each finding traces to a specific gap in the project's control
structure — the pattern of who has authority over what, and what
information reaches whom.

| Finding | Structural cause |
|---|---|
| 1 — Shared engineers | Two controllers (technology lead, line manager) with equal and competing authority over the same people, and no priority rule |
| 2 — Undefined process | The development process authority role does not exist; the technology lead cannot hold both content leadership and process leadership effectively |
| 3 — No progress signal | No stage gates means no independent information channel; the manager's only input is the team's self-report |
| 4 — Handover not designed | Transition planning left to the end concentrates knowledge in the project team and gives the line no preparation time |
| 5 — Cybersecurity assumption | An untested inheritance assumption that could become a late-breaking constraint |

---

## Recommended decisions

### Decision 1 — Write the priority rule for the shared engineers
*(Required before the project starts)*

The common manager should define in writing what qualifies as a line
interruption for the three shared engineers. A workable rule:
only P1 production incidents affecting customers in the field, capped
at two working days per incident, with the technology lead notified
before the engineer is pulled. Any request outside this definition
goes to the common manager for a one-time decision, not to the line
manager alone. This rule does not require renegotiating the 80/20
split — it simply makes "specific cases" specific.

### Decision 2 — Appoint a development manager before the team is assembled
*(Required before the project starts)*

A named person should be given explicit authority over the
development process — how the team works, what the milestones are,
what the quality gates are, and what is reported upward. This person
does not need to be senior; they need to be dedicated to the role.
The technology lead owns what is built. The development manager owns
how the team works. These are different jobs and should not be held
by the same person.

### Decision 3 — Choose a development process suited to this context
*(Required before the team is assembled)*

The context of this project — an embedded industrial platform,
a mostly inexperienced team, regulatory cybersecurity exposure, and
a DevOps line organisation alongside — points toward a
**stage-gated process with iterative execution inside each stage**.
In practical terms: the common manager authorises each stage based
on written exit criteria; the team works in short delivery cycles
within each stage; quality tests are automated and run continuously.
This pattern is documented in the project's knowledge base under
`knowledge/system-catalogues/dev-frameworks/cross-framework/hybrids.md`
as Hybrid A (Governed Agile) and is the model that industrial
cybersecurity standards such as IEC 62443 are designed to work with.

The stage gates give the common manager the independent progress
signal that is currently missing (Finding 3) and provide the
framework within which the handover gate (Finding 4) fits naturally
as the final stage.

### Decision 4 — Build the handover into the project from day one
*(Design decision, required before the project starts)*

Three mechanisms should be built into the project plan:

**Embedded line engineers.** One or two engineers from the line
organisation should participate in the project throughout — not full
time, but consistently enough to follow architecture decisions and
carry knowledge back to the line continuously. These are the people
who will bridge the handover.

**Handover gate criteria.** The common manager should define, before
the project starts, what the line organisation must be able to
demonstrate before the handover is complete. Suggested criteria:

- The line team can deploy, roll back, and diagnose the new platform
  without project team assistance
- The CI/CD pipeline covers the new platform in the line's own
  infrastructure
- A line engineer has successfully used a documented extension point
  to add a new capability
- A support runbook exists and has been tested by line operations staff
- No critical defects are open

**Progressive transfer.** The final stage of the project should be
a structured transfer phase — not a handover date — in which
operational responsibility moves from the project team to the line
in steps, with the project team available for support at each step
before fully withdrawing. The technology lead should have an
explicitly defined advisory role (recommended: twelve months after
full handover) after which the line is self-sufficient.

### Decision 5 — Commission the cybersecurity inheritance check
*(Low urgency, high consequence; assign within the first month)*

Assign one person to answer the following question in writing within
the first month of the project: does the applicable cybersecurity
standard require a new risk assessment for the new platform given
the change in addressing architecture? The answer determines whether
cybersecurity is a background constraint or an active workstream for
the project.

---

## Decisions summary

| Decision | Owner | Timing |
|---|---|---|
| Write priority rule for shared engineers | Common manager | Before project starts |
| Appoint development manager | Common manager | Before project starts |
| Choose development process | Common manager + development manager | Before team assembled |
| Define handover gate criteria | Common manager | Before project starts |
| Build embedded line engineers into project plan | Technology lead + development manager | At project plan stage |
| Commission cybersecurity inheritance check | Common manager | Within first month |

---

## What this analysis is based on

The structural analysis draws on:

- `knowledge/se-techniques/control-structures/diagnostic-questions.md` —
  four questions applied to the project's authority and feedback
  structure
- `knowledge/se-techniques/control-structures/dangerous-patterns.md` —
  accountability void and self-sealing process model patterns checked
  against the project setup
- `knowledge/system-catalogues/dev-frameworks/cross-framework/hybrids.md` —
  Hybrid A (Governed Agile) as the recommended process pattern
- `knowledge/system-catalogues/dev-frameworks/cross-framework/merging-principles.md` —
  variation-point compatibility rules applied to the line/project
  process boundary
- `knowledge/system-catalogues/dev-frameworks/cross-framework/variation-points.md` —
  VP1 (temporal structure), VP2 (requirements stability), VP3
  (authority), VP4 (QA timing) checked for coherence across the
  project and line setups

No finding in this memo is based on the individuals involved
behaving badly or making poor decisions. Every finding is structural:
it would occur under normal operating conditions regardless of who
fills the roles.
