# Order Theory and Formal Concept Analysis

A qualitative-friendly mathematical technique built on partial
orders, lattices, and the concept-lattice construction of Formal
Concept Analysis (FCA). Operates directly on the project's existing
qualitative artefacts — chains, hierarchies, incidence matrices,
permission structures — without requiring numerical entries.

- `overview.md` — what the technique is, scope, what it adds
- `how-it-works.md` — five applications and their mechanics
- `scope-and-pitfalls.md` — when not to use it; the safeguards
- `references.md` — sources

## Relationship to other techniques

| Sibling | What it does | What this technique adds |
|---------|-------------|-------------------------|
| `../justification-rungs/` | Defines a 7-rung ladder of justificatory standards | Recasts the ladder as a chain (totally ordered set); makes "rung mismatch" a formal structural property of a control loop |
| `../goals-requirements-hierarchy/` | Five-level decomposition with traceability rules | Recasts the hierarchy as a graded poset; orphan-detection becomes a poset condition; cross-level trace becomes a Galois connection |
| `../control-structures/` | Diagnostic questions on a control graph | Treats authority and permission as lattices; meet and join give "joint authority needed" and "weakest sufficient authority" |
| `../product-line-engineering/` | Identifies platform and variation points | FCA on the variants × features matrix yields a concept lattice — a qualitative, interpretable taxonomy of variant families |
| `../linear-algebra/` | Quantitative second reading of matrix-shaped artefacts | Qualitative *first* reading of the same artefacts: where LA gives latent axes, FCA gives concept hierarchies; complementary, not competing |

## Why this technique was added

The qualitative SE techniques in this catalogue produce structured
objects that are already lattice- or poset-shaped: the rungs are a
chain, the SE hierarchy is a graded poset, authority is a partial
order, the PLE feature matrix is a binary incidence relation. Order
theory is the native mathematics of those objects. Unlike linear
algebra, it requires no numerical entries — its operations are
defined by the structure itself.

## Scope

Apply where the underlying object is a partial order, a chain, a
permission structure, or a binary incidence relation that already
exists in the project. Do not use to *manufacture* an order from
narrative material. See `scope-and-pitfalls.md`.
