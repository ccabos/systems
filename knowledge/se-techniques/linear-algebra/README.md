# Linear Algebra

A complementary, quantitative technique for the cases where the
qualitative SE toolkit has already produced a structure that happens
to be a matrix or a graph. Linear algebra is *not* a general-purpose
analysis layer for the social-systems catalogue; it is narrowly
scoped to three artefacts that are already linear-algebraic in form.

- `overview.md` — what the technique is, scope, what it adds
- `how-it-works.md` — the three applications and their mechanics
- `false-precision-trap.md` — when not to use it; the safeguards
- `references.md` — sources

## Relationship to other techniques

| Sibling | What it does | What this technique adds |
|---------|-------------|-------------------------|
| `../control-structures/` | Diagnostic questions and dangerous patterns on a control graph | Spectral analysis of the same graph: dominant feedback modes, eigenvector centrality of controllers, algebraic connectivity |
| `../product-line-engineering/` | Identifies platform and variation points across a family | PCA/SVD on the variants × features matrix to find latent variation axes and redundant features |
| `../goals-requirements-hierarchy/` | Five-level decomposition with traceability | Design Structure Matrix (DSM) of the trace links; block-diagonalisation reveals modules and feedback cycles |

## Scope

Apply where the underlying object is already a matrix or graph and
the entries are defensible (presence/absence, count, well-defined
score). Do not apply where the matrix would have to be assembled by
coding qualitative judgements — the answers will reflect the coding
choices, not the system. See `false-precision-trap.md`.
