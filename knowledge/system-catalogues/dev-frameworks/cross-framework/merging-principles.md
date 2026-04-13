# Principles for Framework Merging

Extracted from `projects/systems-introduction-book/docs/part3/frameworks.md`
§7. Principles for combining elements from different development
frameworks coherently, derived from the reuse analysis
(`reuse-analysis.md`) and the hybrid architectures (`hybrids.md`).

## The Compatibility Rule

Before merging two framework elements, check whether their VP bindings
are compatible. A merger is coherent only if the combined bindings
don't contradict each other:

1. **You cannot bind VP1 to both "sequential phases" and "continuous
   flow" in the same work stream.** You can have different work
   streams with different bindings (Hybrid C), but a single stream
   must choose.
2. **VP2 and VP1 must align.** If you assume requirements are stable
   (VP2), sequential phases (VP1) are natural. If requirements are
   volatile, you need iterations or flow. Misalignment here is the
   single most common source of methodology failure.
3. **VP3 must be consistent across a given organizational level.**
   You cannot have a PM assigning tasks *and* a self-organizing team.
   Choose one or create explicit boundaries (e.g., PM governs scope,
   team governs execution).
4. **VP4 should be as automated and continuous as possible regardless
   of other bindings.** This is the one variation point where "more"
   is almost always better. Even a Waterfall project benefits from CI.

## The Granularity Principle

Different variation points can be bound at different granularities:

- **VP1 (temporal structure)** can differ *between organizational
  levels* (portfolio = flow, team = iterations) but should be
  consistent *within* a level.
- **VP2 (requirements stability)** can differ *between work types*
  within the same team (bug fixes: stable requirements; new features:
  emergent) but the team needs explicit policies for which work type
  gets which treatment.
- **VP3 (authority)** should follow a clear hierarchy: strategic
  authority at the top, execution authority at the bottom, with
  explicit delegation boundaries.
- **VP4 (QA timing)** should be *cumulative*: automated tests on
  every commit AND periodic manual testing AND user validation. These
  don't conflict; they complement.

## The "Start from the Platform" Principle

When designing a hybrid, don't start from a specific framework and
"add bits of another." Start from the ten universal functional slots
(the platform) and for each slot, consciously choose which framework's
mechanism best serves your context. This prevents the common failure
of "Scrum-but" — which happens when people start from Scrum and then
subtract elements without understanding what they're losing.

The platform-first approach:

1. List the ten functional slots.
2. For each slot, identify your context constraints (regulated?
   fast-changing? large-scale? small team?).
3. For each slot, select the mechanism from whichever framework best
   fits those constraints.
4. Check VP compatibility across your selections.
5. Resolve any incoherences by adjusting bindings.

## The "Automate the Right Arm" Principle

The V-Model's core insight — every design decision deserves a
corresponding test — is universally valuable but historically
expensive because it was manual. DevOps makes it cheap. The principle:
whatever your temporal structure (VP1), automate the V-Model's right
arm as a CI/CD pipeline. This gives you V-Model quality assurance at
DevOps speed, regardless of whether your left arm is sequential,
iterative, or continuous.

This single reuse — V-Model testing structure + DevOps automation —
is arguably the highest-value cross-framework transplant available
today.

## The "Separate Discovery from Delivery" Principle

Most frameworks conflate two fundamentally different activities:
*figuring out what to build* (discovery) and *building it* (delivery).
Scrum crams both into a Sprint. Waterfall separates them into phases
but forbids looping back. Design Thinking excels at discovery but
says nothing about delivery. DevOps excels at delivery but says
nothing about discovery.

The cleanest hybrid separates these into parallel tracks with a
defined interface (the validated backlog). Discovery runs on Design
Thinking's exploratory loop. Delivery runs on Scrum iterations or
Kanban flow. The two tracks operate at different cadences and can be
staffed differently. The interface between them — "validated, sized,
prioritized items ready for delivery" — is the product-line equivalent
of a platform interface specification.
