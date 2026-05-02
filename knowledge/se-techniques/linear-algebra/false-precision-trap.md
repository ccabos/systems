# The False-Precision Trap

The reason the rest of this catalogue is qualitative is that the
systems studied — religions, polities, families, organisations —
resist reliable numerical measurement. Linear algebra is the most
seductive technique to misapply in that setting because it produces
crisp numbers from any matrix, regardless of whether the matrix
should have existed in the first place.

This page lists the failure modes and the safeguards.

## Failure mode 1 — Inventing the matrix

The analyst codes narrative material into 0/1 or 1–5 entries to make
a matrix where none existed. The eigenstructure of that matrix then
reflects the analyst's coding choices, not the system. This is the
single most common misapplication of PCA in social science.

**Safeguard.** Every non-zero entry must trace to a structural
artefact already produced by another technique in this catalogue —
an edge in a control graph, a feature listed in a PLE catalogue, a
trace link in the SE hierarchy. If the entry's only source is the
analyst's reading of a narrative, do not include it.

## Failure mode 2 — Over-interpreting low-rank structure

PCA on small matrices (fewer than ~10 rows, ~30 columns — exactly
the size of this project's catalogues) produces dominant components
even on random data. A "first principal component captures 60% of
variance" finding can be a sampling artefact.

**Safeguard.** Compare the singular-value spectrum against the
spectrum of a random matrix of the same shape and sparsity. Report
only components whose singular values exceed the random baseline by
a clear margin. Treat single-component conclusions on small matrices
as suggestive, not decisive.

## Failure mode 3 — Confusing ranking with explanation

Eigenvector centrality and PageRank give a *ranking* of nodes. The
ranking is not an explanation of why a node is central; it is a
restatement of the graph's structure in scalar form. The
qualitative work in `../control-structures/` and `../stpa/` does the
explanatory work.

**Safeguard.** When reporting a spectral finding, always pair it
with the qualitative diagnosis it confirms or flags. A centrality
ranking that nobody can explain in control-structure terms is a
signal that the graph is wrong, not that the system is mysterious.

## Failure mode 4 — Asymmetric weighting silently injected

Symmetrising a directed control graph (replacing each directed edge
with an undirected edge) is convenient because the symmetric
Laplacian has a real spectrum and a clean theory. But it discards
exactly the asymmetry that the rung ladder in
`../justification-rungs/` exists to expose: a control action down
and a feedback channel up are *not* the same edge.

**Safeguard.** Use the directed Laplacian, or compute spectra on
the upward and downward subgraphs separately. Symmetrise only when
explicitly justified, and note it in the result.

## Failure mode 5 — Treating the spectrum as predictive

The eigenvalues of a static control graph describe the structure of
that graph. They do not predict how the system will behave under
disturbance unless the graph is also a *dynamical model* (with state
equations, time constants, gains). The catalogue's control graphs
are structural, not dynamical.

**Safeguard.** Restrict spectral claims to structural ones —
connectivity, centrality, modularity. Do not claim stability,
convergence rate, or oscillation behaviour from a structural graph
alone.

## When in doubt

The default answer is "do not apply linear algebra here." The
technique earns its place on the three artefacts named in
`how-it-works.md` because those artefacts already exist in
matrix or graph form. Anywhere else, the qualitative techniques in
the rest of this catalogue are the right tool.
