# Linear Algebra — Overview

Linear algebra enters this project as a *complement* to the
qualitative SE techniques, not as a substitute. The other techniques
in this catalogue (`../stpa/`, `../control-structures/`,
`../goals-requirements-hierarchy/`, `../product-line-engineering/`,
`../justification-rungs/`) are deliberately structural: they produce
diagrams, tables, and traceability links that work in domains where
numerical measurement is unreliable. That choice is correct for most
of the social-systems catalogue.

But three of those structural artefacts are *already* matrices or
graphs in disguise. Where that is the case, eigenstructure and
factorisation give a second, quantitative reading of the same object
that the qualitative methods produced. The role of this technique is
to make that second reading available — and to mark clearly where it
is not.

## The three artefacts that admit linear-algebraic treatment

1. **Control structures** are directed graphs. Their adjacency and
   Laplacian matrices have eigenstructure that says something about
   feedback dominance, modal decomposition, and which controllers
   are central to the system rather than nominal.
2. **Product-line feature matrices** (variants × features) are
   sparse 0/1 matrices. PCA/SVD finds the latent axes along which
   the family actually varies, which is often a much smaller set
   than the raw feature count.
3. **Trace matrices from the SE hierarchy** (Goals × Requirements,
   Requirements × Functions, etc.) are bipartite incidence matrices.
   The Design Structure Matrix (DSM) — a square matrix obtained by
   composing them — can be reordered into block-triangular form to
   expose modules and feedback cycles.

## What this technique adds

The qualitative techniques tell you *that* a control structure is
unbalanced, *that* product variants share a platform, *that* a
hierarchy has cycles. Linear algebra adds a *measure*: how
unbalanced, how much shared, how cyclic. When the measure can be
trusted (see scope below), it ranks problems and solutions.

For control structures, eigenvector centrality identifies the
controllers that actually steer the system; algebraic connectivity
(the second-smallest Laplacian eigenvalue) measures how robustly the
graph stays connected under removal of edges or nodes. For product
lines, the singular values of the feature matrix tell you the
*effective dimensionality* of the family — eight dev frameworks
might span only three or four real axes. For the SE hierarchy, DSM
block-decomposition tells you which functions are tightly coupled
and which subsystems are separable.

## Scope

Apply only when:

- The matrix entries are defensible — presence/absence of an edge,
  a published count, a feature that either appears in a variant or
  does not.
- The structure exists *before* the analysis. Do not assemble the
  matrix by coding qualitative judgements about social-systems
  artefacts; the eigenstructure will then reflect the coding
  choices.
- A *qualitative* reading already exists. Linear algebra is the
  second pass, not the first; without the structural reading there
  is nothing to compare the spectrum to.

Do not apply to:

- Religions, families, polities described in narrative form. The
  matrices needed do not exist and inventing them launders
  judgements into eigenvalues. See `false-precision-trap.md`.
- Engineered safety analyses where STPA already operates at full
  precision and additional eigenstructure adds no information.
- Any artefact where the dominant uncertainty is in the entries
  rather than in the structure. Linear algebra propagates entry
  uncertainty by orders of magnitude — small coding errors become
  large eigenvector errors.

## Where it sits in the technique stack

| Step | Technique | Output |
|------|-----------|--------|
| 1 | `../goals-requirements-hierarchy/` | Five-level decomposition with traceability |
| 2 | `../control-structures/` | Control graph; five diagnostic questions |
| 3 | `../product-line-engineering/` | Platform + variation points across family |
| 4 | `../stpa/` | Unsafe control actions and loss scenarios |
| 5 | **Linear algebra** *(this technique)* | Quantitative second reading of artefacts from steps 1–3 |

The technique is post-hoc by design. It does not produce primary
findings; it ranks and confirms findings already produced by the
qualitative techniques.
