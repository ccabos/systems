# The Five-Level SE Hierarchy

## A Universal Decomposition Instrument

Systems engineering decomposes any system — technical or social — into five levels of abstraction. Each level answers a different question, and each item at one level traces to items at the next level down, forming a directed acyclic graph with full traceability.

## The Five Levels

| Level | Prefix | Question Answered |
|-------|--------|------------------|
| **Goals** | G | *Why does this system exist?* What overarching objectives does it pursue? |
| **Requirements** | R | *What must be true?* What constraints, criteria, and conditions are derived from the goals? |
| **Functions** | F | *What does the system do?* What operations does it perform to meet requirements? |
| **Logical Architecture** | L | *How is it organized?* How are functions grouped into interacting subsystems? |
| **Physical Implementation** | P | *What is it made of?* What concrete people, buildings, documents, tools, and processes realize the architecture? |

## Why Five Levels?

The five levels are not arbitrary. They correspond to the fundamental decisions that any system designer — whether an engineer or a lawmaker — must make, in order:

1. **Purpose before structure.** You cannot design a system without knowing what it is for (Goals).
2. **Constraints before mechanisms.** You cannot choose mechanisms without knowing the constraints they must satisfy (Requirements).
3. **Functions before grouping.** You cannot group things into subsystems without knowing what functions need to exist (Functions).
4. **Logical before physical.** You should decide how subsystems interact before choosing which specific technologies, people, or buildings implement them (Logical → Physical).

Skipping a level — for example, jumping from goals directly to physical implementation — produces systems that "work" but are fragile, incoherent, and resistant to change. This is as true of a parliament as it is of a software architecture.

## Traceability Rules

Every item in the hierarchy must be connected:

- Every Goal links to at least one Requirement
- Every Requirement links to at least one Function
- Every Function links to at least one Logical Architecture element
- Every Logical Architecture element links to at least one Physical Implementation
- A child can have multiple parents (many-to-many is valid)
- No orphan nodes — every item must be traceable upward to a goal and downward to an implementation

These rules ensure **completeness** (every goal is implemented) and **necessity** (every implementation serves a goal). When applied to social systems, they reveal a common pathology: physical implementations that have lost their connection to any goal ("we do this because we've always done it") and goals that have no implementation ("we believe in this but have no mechanism to achieve it").

## Example: The German Verein

A brief example to make the abstraction concrete:

| Level | ID | Description |
|-------|----|-------------|
| Goal | G1 | Enable citizens to pursue a shared non-commercial purpose collectively |
| Req. | R1 | Written Satzung defining the purpose |
| Req. | R3 | Democratic decision-making with equal voting rights |
| Func. | F3 | Democratic assembly — Mitgliederversammlungen, elect Vorstand |
| Logical | L1 | Governance Subsystem — Satzung, Wahlordnung, Geschäftsordnung |
| Physical | P2 | Mitgliederversammlung (annual meeting), Protokolle, Kassenprüfung |

The traceability chain: G1 → R3 → F3 → L1 → P2. Every physical artifact (the annual meeting, the minutes, the financial audit) traces back to a goal. If you removed the annual meeting, you would break the trace to G1 — the system would lose its mechanism for collective purpose.

This is the instrument. In the following chapters, we apply it to systems that are not usually analyzed this way.
