# System Definition — Working Definition

Extracted from `projects/systems-introduction-book/docs/part1/what-is-a-system.md`.
The narrative version with full critical assessment lives in the
book; this file contains only the claim, the working definition, and
the direct corollaries used throughout the rest of the project.

## The working definition

> A system is a **bounded structure of parts and connections organised
> by goals**, whose behaviour at the boundary **cannot be predicted
> from its parts in isolation**.

This definition is not original to this project. It restates a
consensus position in the systems literature: Meadows defines a
system as "elements, interconnections, and a function or purpose"
[Meadows2008] — exactly the parts / connections / goals triad used
here — and the pairing of structure with irreducible boundary-level
behaviour goes back to general system theory [Bertalanffy1968] and
Ackoff's system-of-concepts paper [Ackoff1971]. (Citation keys
resolve in `../references/bibliography.md`.)

The definition combines two perspectives that are complementary
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

Two questions are easy to merge here and must be kept apart: whether
changing an element makes the system *a different system*, and what
changing it *costs*. They are not the same ordering, and for one
class of element they point in opposite directions.

| Element | Identity-constitutive | Effort to change | Consequence of change |
|---------|----------------------|------------------|-----------------------|
| **Instances** | Low | Low | System continues; this is routine maintenance |
| **Rule sets** | Low | **High** | System keeps its identity but behaves differently |
| **Connections** | Moderate | High | System is restructured; behaviour shifts significantly |
| **Goals** | High | Very high | System is transformed; what was there before is effectively a different system |

**Parts split into two classes**, and collapsing them is the most
common error made with this hierarchy. *Instances* are the concrete
occupants of a role: this building, this office, this official, this
form. *Rule sets* are the codified regularities that govern how the
parts are coupled: a constitution, a career and tenure regime, a
budget ordinance, signature-authority limits, a bonus scheme,
reporting duties. Both are physical-level elements — concrete,
nameable, writable — and neither is identity-constitutive. They
differ in everything else. An instance can be swapped over a weekend
and little follows. A rule set takes years to change, is owned by
someone other than whoever wants it changed, and changes system
behaviour when it moves.

A human body replaces most of its cells over years and remains the
same organism. A corporation can change its entire workforce and
remain recognisably the same corporation. But a corporation whose
goal shifts from profit to public service is, in any meaningful sense,
a different institution wearing the same legal clothes.

The identity ordering tracks the literature. The leverage ordering
tracks it only at the ends. Meadows ranks intervention points by
*leverage* — how much system behaviour changes per unit of
intervention — and at the extremes she agrees: changing numbers and
parameters does least, changing the system's purpose or the paradigm
behind it does most [Meadows1999; Meadows2008]. In the middle she
does not. Two of her strongest non-goal leverage points are the
structure of *information flows* (who can see what) and the *rules*
of the system (incentives, sanctions, constraints) — and both are
physical-level elements under the mapping below. Leverage is
therefore **not monotone** in the G/L/P decomposition, and the two
orderings have to be read separately rather than as one gradient.
The underlying identity claim — that a system *is* its organisation,
not its components — is the autopoiesis position
[MaturanaVarela1980].

The replaceability hierarchy maps directly onto the five-level SE
decomposition used throughout the project (see
`knowledge/se-techniques/goals-requirements-hierarchy/`):

- **Physical implementations (P)** correspond to parts — to *both*
  classes of part, instances and rule sets alike.
- **Logical architecture and functions (L, F)** encode the connection
  patterns.
- **Goals and requirements (G, R)** encode purpose.

Institutional reform that touches only P-level *instances* is
*maintenance*. Reform that changes P-level *rule sets* is not: rule
sets decide how the parts are coupled, so changing one changes what
the system does while leaving its identity intact. This is where most
successful institutional reform actually happens. The P level of the
worked decompositions contains both — `RP1` of the democracy
decomposition is "Parliament building, rules of procedure" and `RP2`
is "Constitution, bill of rights"
(`knowledge/system-catalogues/social-systems/democracy/se-decomposition.md`).
Reading the undivided P level as maintenance would make a
constitutional amendment a routine swap of the most easily replaced
element in the state. Reform that reaches G-level is
*transformation* — and the historical record shows it is both rare
and destabilising.

## The four corollaries

Four corollaries follow from the working definition and recur
throughout the project:

1. **Changing instances is maintenance.** It preserves the system.
   Changing *rule sets* is not: it preserves the system's identity
   while changing its behaviour, and it is the most consequential
   move available below the goal level.
2. **Changing connections restructures the system.** It changes what
   the system does, often dramatically.
3. **Changing goals transforms the system.** The result is a
   different system with inherited infrastructure.
4. **Changing the boundary redefines the system.** What counts as
   internal, external, and relational changes entirely.

The SE hierarchy is a formal instrument for making this structure
explicit and tractable. Goals become the G-level. Connections between
functional components become the L-level. Parts — instances and rule
sets both — become the P-level.
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

This distinction has a long pedigree under other names: Merton's
*manifest* vs *latent* functions [Merton1968], Selznick's *goal
displacement* — operative goals drifting from declared ones under
environmental pressure, documented in the TVA field study
[Selznick1949] — and Beer's dictum that "the purpose of a system is
what it does" (POSIWID) [Beer2002]. The convergence of three
independent traditions on the same distinction is part of why this
project treats it as load-bearing.
