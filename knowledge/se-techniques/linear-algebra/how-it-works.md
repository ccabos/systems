# Linear Algebra — How It Works

Three applications, each tied to one existing artefact. Each
application has the same shape: build the matrix from an existing
artefact, compute one or two spectral quantities, read the result
back into the qualitative diagnosis.

## Application 1 — Spectral analysis of a control structure

Input: the control graph from `../control-structures/`. Nodes are
controllers and controlled processes; directed edges are control
actions (downward) and feedback channels (upward).

### Build the matrices

- **Adjacency matrix** `A` of size `n × n`. `A[i,j] = 1` if there is
  a directed edge from node *i* to node *j*, otherwise 0. For
  weighted variants, use the rung tag from
  `../justification-rungs/` as the weight.
- **Degree matrix** `D` (diagonal, `D[i,i] =` out-degree of node
  *i*).
- **Graph Laplacian** `L = D − A` for the symmetrised graph, or the
  directed Laplacian for the original.

### Read the spectrum

| Spectral quantity | What it tells you |
|---|---|
| Eigenvector centrality (top eigenvector of `A`) | Which controllers actually steer the system, vs. which are nominal but disconnected from the dominant feedback loop |
| Algebraic connectivity (second-smallest eigenvalue of `L`) | How robust the structure is to edge or node removal — low values flag fragile single-point dependencies |
| Number of zero eigenvalues of `L` | Number of disconnected components — a positive count usually means a feedback channel is missing |
| Dominant eigenvalue of `A` | The growth rate of cascades in the structure — useful as a quick read of how fast a local failure propagates |

### What it adds to control-structures diagnosis

The five diagnostic questions in `../control-structures/` are
qualitative. Eigenvector centrality answers Q1 (feedback richness)
and Q3 (accountability voids) numerically: the controllers with high
centrality and no incoming feedback edges are the accountability
voids. Algebraic connectivity answers Q4 (circuit breakers): if
removing any single edge disconnects the graph, there is no circuit
breaker.

## Application 2 — Design Structure Matrix on the SE hierarchy

Input: the trace matrices from `../goals-requirements-hierarchy/`.
Each level produces a bipartite incidence matrix (Goals ×
Requirements, Requirements × Functions, Functions × Logical, Logical
× Physical).

### Build the DSM

The DSM is a square `m × m` matrix at one chosen level, typically
Functions × Functions. `DSM[i,j] = 1` if function *i* depends on
function *j* (data flow, control flow, or shared resource).
Construction:

1. Pick the level (Functions is the standard choice).
2. List the *m* items at that level.
3. For each ordered pair `(i, j)`, mark 1 if the project's existing
   trace links imply a dependency from *i* to *j*.

### Reorder the DSM

Apply a block-triangularisation algorithm (e.g. Tarjan's
strongly-connected-components decomposition). The result is a
permuted DSM where:

- **Diagonal blocks** are strongly connected components — sets of
  functions that depend on each other cyclically. Each block is a
  candidate logical subsystem.
- **Below-diagonal entries** are forward dependencies (no cycles).
- **Above-diagonal entries** are feedback edges across modules —
  these are the integration risk points.

### What it adds to the hierarchy

The traceability rules in
`../goals-requirements-hierarchy/how-it-works.md` catch *missing*
links (orphans). The DSM catches *cyclic* links: functions that have
become entangled across logical-subsystem boundaries. Block
reordering provides an objective grouping criterion when the
analyst's intuitive grouping is contested.

## Application 3 — PCA / SVD on a product-line feature matrix

Input: the variants × features matrix implicit in
`../product-line-engineering/`. For the dev-frameworks catalogue,
this is approximately 8 frameworks × ~30 features.

### Build the matrix

`F` is `n × p` where *n* = number of variants, *p* = number of
features. Entries are 0/1 (feature absent / present) or 0–N counts
where the feature has a natural integer scale (e.g. iteration
length in weeks).

Centre and, if scales differ, standardise the columns.

### Decompose

Compute the SVD: `F = U Σ Vᵀ`.

| Quantity | What it tells you |
|---|---|
| Singular values (diagonal of `Σ`) | The *effective dimensionality* of the family. If the first *k* singular values capture 90% of the variance, the *p* features really span a *k*-dimensional space |
| Right singular vectors (columns of `V`) | The latent axes — interpretable as "iteration cadence," "formality," "role specialisation," etc. |
| Left singular vectors (columns of `U`) | Where each variant sits along each latent axis |

### What it adds to PLE

`../product-line-engineering/` identifies a platform and a list of
variation points by inspection. PCA gives a second reading: how many
*independent* variation points there really are, and which features
are redundant (loaded heavily on the same axis as another feature).
A platform that is justified by inspection but collapses to one or
two axes under PCA is a signal that the platform is over-specified.

## Procedure for any of the three

1. **Confirm the qualitative reading exists.** Do not run linear
   algebra on a structure that has not first been read structurally
   by the relevant sibling technique.
2. **Confirm the entries are defensible.** Each non-zero entry must
   trace to an edge, a feature, or a dependency that can be cited
   from project documents.
3. **Compute the spectrum or factorisation.** Standard libraries
   (NumPy, SciPy, NetworkX) suffice. Record the matrix used.
4. **Read the result back into the qualitative diagnosis.** A
   spectral finding that contradicts the qualitative reading is a
   signal to recheck both — not to override one with the other.
5. **Stop at the second reading.** The technique is post-hoc; its
   role is to confirm, rank, or flag, not to drive design decisions
   on its own.
