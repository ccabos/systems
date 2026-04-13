# System Definition — Working Definition

Extracted from `projects/systems-introduction-book/docs/part1/what-is-a-system.md`.
The narrative version with full critical assessment lives in the
book; this file contains only the claim, the working definition, and
the direct corollaries used throughout the rest of the project.

## The working definition

> A system is a **bounded structure of parts and connections organised
> by goals**, whose behaviour at the boundary **cannot be predicted
> from its parts in isolation**.

This definition combines two perspectives that are complementary
rather than rival:

- **Inside view** — a system is a *structure*: organised parts,
  patterned connections, directing goals, within a defined boundary.
- **Outside view** — a system is an *actor*: something whose
  boundary-level behaviour cannot be read off from its parts in
  isolation.

Neither is sufficient alone. A structure with no emergent behaviour
is a machine, not a system in the interesting sense. An emergent
phenomenon with no describable structure is magic, not analysis.

## The three constitutive elements (inside view)

From the structural view, a system is constituted by three elements:

1. **Parts** — the distinguishable components that can, in principle,
   be identified and listed.
2. **Connections** — the relationships, flows, and dependencies
   between parts.
3. **Goals** — the purpose or purposes the system pursues, whether
   declared or operative.

These are not equally essential to system identity. They differ in
how easily they can be replaced without the system ceasing to be
*the same system*.

## The replaceability hierarchy

| Element | Replaceability | Consequence of Change |
|---------|----------------|-----------------------|
| **Parts** | High — most easily swapped | System continues; this is routine maintenance |
| **Connections** | Moderate — harder to change | System is restructured; behaviour shifts significantly |
| **Goals** | Low — very difficult to change | System is transformed; what was there before is effectively a different system |

A human body replaces most of its cells over years and remains the
same organism. A corporation can change its entire workforce and
remain recognisably the same corporation. But a corporation whose
goal shifts from profit to public service is, in any meaningful sense,
a different institution wearing the same legal clothes.

The replaceability hierarchy maps directly onto the five-level SE
decomposition used throughout the project (see
`knowledge/se-techniques/goals-requirements-hierarchy/`):

- **Physical implementations (P)** correspond to parts.
- **Logical architecture and functions (L, F)** encode the connection
  patterns.
- **Goals and requirements (G, R)** encode purpose.

Institutional reform that touches only P-level elements is
*maintenance*. Reform that reaches G-level is *transformation* — and
the historical record shows it is both rare and destabilising.

## The four corollaries

Four corollaries follow from the working definition and recur
throughout the project:

1. **Changing parts is maintenance.** It preserves the system.
2. **Changing connections restructures the system.** It changes what
   the system does, often dramatically.
3. **Changing goals transforms the system.** The result is a
   different system with inherited infrastructure.
4. **Changing the boundary redefines the system.** What counts as
   internal, external, and relational changes entirely.

The SE hierarchy is a formal instrument for making this structure
explicit and tractable. Goals become the G-level. Connections between
functional components become the L-level. Parts become the P-level.
The boundary is the decision to start the decomposition at all — see
`boundaries-and-environment.md`.

## Declared vs operative goals

A system often has *declared* goals that diverge substantially from
*operative* goals. A regulatory agency declared to protect the public
may operate primarily to protect the regulated industry. A religion
declared to save souls may operate primarily to perpetuate its own
institutional authority. When applying the SE hierarchy, the operative
goals are what the STPA analysis (see
`knowledge/se-techniques/stpa/`) must catch, because unsafe control
actions typically arise from exactly this split.
