# Five-Level SE Hierarchy — Level Definitions

Level-by-level definitions of the Goals → Requirements → Functions →
Logical Architecture → Physical Implementation hierarchy, with the
question each level answers and the kind of statement that appears
at that level.

## Goals (G)

**Question:** *Why does this system exist?*

A goal is a stated purpose the system pursues. Goals are phrased as
outcomes, not activities: "ensure territorial integrity," "educate
the next generation of scholars," "generate sustainable profit."

A system normally has between three and six goals. Two of them tend
to be universal in social systems: (1) achieve a declared collective
purpose, and (2) ensure the system's own continuity. The rest are
system-specific.

Goals are the **least replaceable** element in a system. Changing a
goal transforms the system into something structurally different —
see the replaceability hierarchy in
`knowledge/foundations/system-definition.md`.

## Requirements (R)

**Question:** *What must be true for the goals to be achievable?*

A requirement is a constraint, criterion, or condition derived from
one or more goals. Requirements are phrased as "must" statements:
"must have a codified constitution with enforceable fundamental
rights," "must have a sustainable revenue source," "must enforce
separation of powers."

A requirement names *what* must hold, not *how* it is achieved.
Multiple different functions can satisfy the same requirement; the
choice between them is made at the next level down.

## Functions (F)

**Question:** *What does the system do?*

A function is an operation the system performs in order to satisfy
one or more requirements. Functions are phrased as active verbs:
"legislate," "adjudicate disputes," "collect revenue," "socialize
children."

Functions are still implementation-independent: "legislate" says
nothing about whether laws come from a king, a parliament, or a
party politburo. The mechanism is chosen at the logical or physical
level.

## Logical Architecture (L)

**Question:** *How is the system organised into interacting
subsystems?*

The logical architecture groups functions into cohesive subsystems
and specifies how they interact. Logical elements are phrased as
subsystem names plus their responsibilities: "Legislative Subsystem
— parliament, committees," "Fiscal Subsystem — treasury, tax
authority, audit court."

The logical architecture is still free of specific buildings, tools,
and people. A "Judicial Subsystem" is the same logical element
whether implemented as a constitutional court or a council of
clerics — but at the physical level it becomes one or the other.

## Physical Implementation (P)

**Question:** *What concrete people, buildings, documents, tools,
and processes realise the architecture?*

The physical level names the specific instantiations: "Parliament
building, rules of procedure," "Constitution, bill of rights,"
"Tax authority, central bank, audit institution."

Physical implementations are the **most replaceable** element in a
system. Replacing the parts is routine maintenance; the system
continues to exist.

## Level summary

| Level | Prefix | Answers | Kind of statement |
|-------|--------|---------|-------------------|
| Goals | G | Why does it exist? | Outcome |
| Requirements | R | What must be true? | Must-statement |
| Functions | F | What does it do? | Verb phrase |
| Logical Architecture | L | How is it organised? | Subsystem name + responsibility |
| Physical Implementation | P | What is it made of? | Concrete artefact / person / document |

## Example trace

A single chain through all five levels for a Verein:

| Level | ID | Description |
|-------|----|-------------|
| Goal | G1 | Enable citizens to pursue a shared non-commercial purpose collectively |
| Requirement | R3 | Democratic decision-making with equal voting rights |
| Function | F3 | Democratic assembly — Mitgliederversammlungen, elect Vorstand |
| Logical | L1 | Governance Subsystem — Satzung, Wahlordnung, Geschäftsordnung |
| Physical | P2 | Mitgliederversammlung (annual meeting), Protokolle, Kassenprüfung |

Chain: G1 → R3 → F3 → L1 → P2. Every physical artefact (the annual
meeting, the minutes, the financial audit) traces back to a goal.
If you removed the annual meeting, you would break the trace to G1 —
the system would lose its mechanism for collective purpose.
