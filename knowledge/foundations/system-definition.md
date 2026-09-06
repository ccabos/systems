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
changing it *costs*. They are different orderings, and the table
below keeps them in separate columns.

| Element | Identity-constitutive | Effort to change | Consequence of change |
|---------|----------------------|------------------|-----------------------|
| **Parts** | Low | Low | System continues; this is routine maintenance |
| **Connections** — in an organisation, its written rules | Moderate | High | System is restructured; behaviour shifts significantly |
| **Goals** | High | Very high | System is transformed; what was there before is effectively a different system |

**Where the rules belong.** In an organisation the connections are
not abstract. They are written down: a constitution, a career and
tenure regime, a budget ordinance, signature-authority limits, an
objectives-and-targets scheme, reporting duties. Because these are
concrete objects with a file name, it is tempting to count them
among the parts. That is the mistake this hierarchy most often
invites, and it inverts the table: it files the expensive,
high-consequence elements under "most easily swapped".

A written rule is **physical in form and a connection in function**.
What it does is decide which part is coupled to which, in which
direction, under which conditions. Classify it by what it does. The
practical difference is large: a part can be replaced over a weekend
and little follows, while a rule takes years to change, is owned by
someone other than whoever wants it changed, and moves the system's
behaviour when it moves.

A human body replaces most of its cells over years and remains the
same organism. A corporation can change its entire workforce and
remain recognisably the same corporation. But a corporation whose
goal shifts from profit to public service is, in any meaningful sense,
a different institution wearing the same legal clothes.

Both orderings track the literature, and reading them against
Meadows shows why the classification above matters. Meadows ranks
intervention points by *leverage* — how much system behaviour
changes per unit of intervention [Meadows1999; Meadows2008]. Read
against the three constitutive elements, her ranking is close to
monotone: parameters, buffers and stock-and-flow structures, at the
weak end, are parts; delays, feedback loops, information flows and
the *rules* of the system, in the middle, are connections; goals and
the paradigm behind them, at the strong end, are purpose.

The ordering only appears to break when the elements are read off
the five SE levels instead, because the physical level holds both
parts and the documents that carry the connections. That is a defect
of the mapping, not of either ordering — which is the practical
reason to classify a physical-level item by what it does. The
underlying identity claim — that a system *is* its organisation, not
its components — is the autopoiesis position [MaturanaVarela1980].

The replaceability hierarchy maps directly onto the five-level SE
decomposition used throughout the project (see
`knowledge/se-techniques/goals-requirements-hierarchy/`):

- **Physical implementations (P)** hold two different kinds of thing:
  the parts themselves, and the written rules that carry the
  connections. Classify each P-level item by what it does, not by the
  fact that it is written down.
- **Logical architecture and functions (L, F)** describe the pattern
  of connections in the abstract; the P-level rule documents are how
  that pattern is actually enforced.
- **Goals and requirements (G, R)** encode purpose.

Institutional reform that touches only parts is *maintenance*.
Reform that changes the rules is not: it leaves the system
recognisably itself while changing what it does, and it is where
most successful institutional reform happens. The worked
decompositions show the mix directly — in the democracy
decomposition `RP1` is "Parliament building, rules of procedure" and
`RP2` is "Constitution, bill of rights"
(`knowledge/system-catalogues/social-systems/democracy/se-decomposition.md`);
the first is largely parts, the second is entirely connection.
Reading the whole physical level as maintenance would make a
constitutional amendment a routine swap of the state's most easily
replaced element. Reform that reaches G-level is *transformation* —
and the historical record shows it is both rare and destabilising.

## The four corollaries

Four corollaries follow from the working definition and recur
throughout the project:

1. **Changing parts is maintenance.** It preserves the system.
2. **Changing connections restructures the system.** It changes what
   the system does, often dramatically. In an organisation this means
   changing the written rules — the most consequential move available
   below the goal level, and the one most often mistaken for
   maintenance.
3. **Changing goals transforms the system.** The result is a
   different system with inherited infrastructure.
4. **Changing the boundary redefines the system.** What counts as
   internal, external, and relational changes entirely.

The SE hierarchy is a formal instrument for making this structure
explicit and tractable. Goals become the G-level. Connections between
functional components become the L-level. Parts become the P-level,
alongside the documents that carry the connections.
The boundary is the decision to start the decomposition at all — see
`boundaries-and-environment.md`.

## Dependability and changeability pull against each other

A system is dependable to the degree that its connections do not
yield on request. Equal treatment, predictability and reviewability
are not side effects of an organisation's rules; they are what the
rules *are*. The same property makes the system slow to change: a
set of rules that could be rewritten on demand would also be a set
anybody could bend.

Resistance to change is therefore not a defect to engineer out. It
is the price of the property that makes the system worth having, and
every proposed reform buys one at the cost of the other. Two failure
modes follow, and both are common:

- **Announcing a change without touching the rules.** Nothing moves
  except trust, which falls. The form this takes in the reform
  literature is *isomorphic mimicry* — institutions that look
  reformed and do not function [Andrews2017; MeyerRowan1977].
- **Removing rules without knowing what they held.** Something moves
  immediately, and it is usually dependability.

This is the foundational reason the reform corollary in
`knowledge/system-catalogues/social-systems/cross-system/principles.md`
says to start at the bottom *with the rules* rather than with
whatever is easiest to change.

## Declared vs operative goals

A system often has *declared* goals that diverge substantially from
*operative* goals. A regulatory agency declared to protect the public
may operate primarily to protect the regulated industry. A religion
declared to save souls may operate primarily to perpetuate its own
institutional authority. When applying the SE hierarchy, the operative
goals are what the STPA analysis (see
`knowledge/se-techniques/stpa/`) must catch, because unsafe control
actions typically arise from exactly this split.

The distinction is only useful if the operative goals can actually
be found, and they can — though not by asking. **The operative goals
are what the rules encode.** Read what the system measures, what it
checks, what it sanctions and what it rewards, and the answer is
there: a body that declares quality and counts units has units as
its operative goal, whatever its statute says. This is the practical
reason the rules are the place to look. They are the connections,
and a system's behaviour follows its connections rather than its
declarations.

This distinction has a long pedigree under other names: Merton's
*manifest* vs *latent* functions [Merton1968], Selznick's *goal
displacement* — operative goals drifting from declared ones under
environmental pressure, documented in the TVA field study
[Selznick1949] — and Beer's dictum that "the purpose of a system is
what it does" (POSIWID) [Beer2002]. The convergence of three
independent traditions on the same distinction is part of why this
project treats it as load-bearing.
