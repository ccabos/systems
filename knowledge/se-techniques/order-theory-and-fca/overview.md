# Order Theory and FCA — Overview

A **partial order** is a binary relation `≤` on a set that is
reflexive, antisymmetric, and transitive. A **lattice** is a partial
order in which every pair of elements has a least upper bound (join,
`∨`) and a greatest lower bound (meet, `∧`). **Formal Concept
Analysis (FCA)** is a specialisation: given a binary incidence
relation between objects and attributes, FCA constructs a complete
lattice of *concepts*, each concept being a maximal pair (object
set, attribute set) consistent with the relation.

Together, these tools form the qualitative mathematical complement
to `../linear-algebra/`. Where linear algebra gives a *numerical*
second reading of matrix-shaped artefacts, order theory gives a
*structural* first reading: it formalises the ordering relations
that the project's qualitative techniques already produce, and
makes their properties precise without inventing entries.

## The five artefacts that admit order-theoretic treatment

1. **The justificatory rungs** are a chain (totally ordered set)
   from rung 0 (raw coercion) to rung 6 (deliberative legitimacy).
   See `../justification-rungs/`.
2. **The SE hierarchy** (Goals → Requirements → Functions → Logical
   → Physical) is a graded poset. See
   `../goals-requirements-hierarchy/`.
3. **Authority structures** within control structures are partial
   orders, often with lattice structure when multiple controllers
   can act jointly. See `../control-structures/`.
4. **Trace matrices between levels** (Goals × Requirements,
   Functions × Logical, etc.) induce Galois connections — a pair
   of monotone maps that capture the duality between "what serves
   what."
5. **PLE feature matrices** (variants × features) are formal
   contexts in the FCA sense. See `../product-line-engineering/`.

## What this technique adds

The qualitative techniques tell you *that* the rungs form a ladder,
*that* the hierarchy decomposes top-down, *that* certain controllers
hold authority over others. Order theory adds three things:

1. **Formal definitions** for properties that the qualitative
   techniques use informally: "rung mismatch," "orphan," "joint
   authority," "platform feature."
2. **Decision procedures** for those properties — algorithms that
   check whether a given control loop is rung-asymmetric, whether
   a hierarchy has orphans, whether a permission set is closed
   under composition.
3. **Concept lattices** (via FCA) that give an interpretable
   taxonomy of a variant family without coercing 0/1 features into
   numerical axes.

## What it does *not* add

It does not give numerical scores, predictive dynamics, or
stability analyses. Those require additional structure (metrics,
state equations, probabilities) that the project's qualitative
artefacts do not provide. The technique is structural; if a
question is genuinely quantitative, see `../linear-algebra/` or
acknowledge the limit.

## Where it sits in the technique stack

| Step | Technique | Output |
|------|-----------|--------|
| 1 | `../goals-requirements-hierarchy/` | Five-level decomposition |
| 2 | `../control-structures/` | Control graph |
| 3 | `../justification-rungs/` | Rung-tagged controllers and arrows |
| 4 | `../product-line-engineering/` | Platform + variation points |
| 5a | **Order theory and FCA** | Structural formalisation of 1–4: posets, lattices, concept lattices |
| 5b | `../linear-algebra/` | Numerical second reading of 1–4 (where defensible) |

Steps 5a and 5b are alternative second-pass readings: one
qualitative-structural, one quantitative. They can both be
applied; they answer different questions.
