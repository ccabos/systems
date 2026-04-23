# Problem: New Embedded Platform Project Setup

## Stakeholder

Common manager of a development organisation considering the setup
of a new project to build a renewed embedded platform for an
industrial automation system.

## Scope and boundary

Inside: the new project organisation (~15 people), its governance
structure, its relationship to the line organisation (DevOps,
current platform), and the planned handover of the new platform
back to the line.

Outside: the technical content of the new platform (name-based
addressing architecture specifics), the existing platform's
internals, and customer or market context.

## The presenting question

Is the planned project setup structurally sound, or will it produce
foreseeable delivery and integration problems?

## Observed symptoms

- Three of the most experienced engineers are to be shared 80/20
  between project and line with no written priority rule
- No development manager identified; development process not chosen
- No defined handover plan or handover gate criteria
- Cybersecurity compliance assumed to transfer from existing platform
  to new architecture without verification

## Goals in tension

- Deliver new embedded platform on time with a largely inexperienced
  team
- Maintain current platform in the line organisation (DevOps)
- Meet cybersecurity standard requirements
- Ensure the new platform can be handed back to the line and extended

## Constraints

- Three experienced engineers are the primary knowledge holders and
  cannot be fully dedicated to either the project or the line
- New team is mostly service staff and new hires unfamiliar with
  embedded platform development
- Common manager sits above both organisations but cannot arbitrate
  every conflict

## Analytical approach

Control-structure analysis using the four diagnostic questions and
three dangerous-pattern check. Product-line positioning against
the dev-frameworks catalogue (Hybrid A — Governed Agile identified
as best-fit process pattern). Handover designed as a stage-gate
process rather than a terminal event.

## Deliverables

Decision memo for the common manager: five findings, five decisions,
decision ownership table, evidence base.

See `memo.md`.

## Status

_delivered_
