# Order Theory and FCA — How It Works

Five applications. Each one binds an order-theoretic construct to
an artefact that already exists in the project, then states what
the construct lets you check or compute.

## Application 1 — The rungs as a chain

Input: the seven rungs from `../justification-rungs/rungs.md`.

### Formalise

Let `R = {0, 1, 2, 3, 4, 5, 6}` with the usual order. `R` is a
chain (totally ordered set). Every controller, every control
action, and every feedback channel in a rung-tagged STPA model
carries an element of `R`.

### Operations and what they mean

| Operation | Meaning |
|---|---|
| `r₁ ≤ r₂` | Rung `r₁` is no stronger than rung `r₂` |
| `r₁ ∨ r₂` | The stronger of the two rungs (max) |
| `r₁ ∧ r₂` | The weaker of the two rungs (min) |
| Down-set `↓r` | All rungs at or below `r` — the standards a rung-`r` claim trivially satisfies |
| Up-set `↑r` | All rungs at or above `r` — the standards a rung-`r` claim cannot vouch for |

### Formal definition: rung mismatch

A control loop has a control action at rung `r_a` and a feedback
channel at rung `r_f`. The loop is **rung-asymmetric** iff
`r_a ≠ r_f`. It is **dangerously asymmetric** iff `|r_a − r_f| ≥ 2`,
or iff one of `r_a, r_f` is in `{0, 1}` and the other is in
`{3, 4, 5, 6}`. The dangerous-mismatch patterns in
`../justification-rungs/dangerous-mismatches.md` are then specific
cases of the second condition.

### What it adds

The rung-mismatch concept is informal in
`../justification-rungs/`. The chain reformulation makes it
checkable on a control graph: walk the loops, read `r_a` and `r_f`,
test the inequality. No interpretive judgement is required at the
test step (only at the upstream rung-tagging step).

## Application 2 — The SE hierarchy as a graded poset

Input: the five-level decomposition from
`../goals-requirements-hierarchy/`.

### Formalise

Let `H = G ⊔ R ⊔ F ⊔ L ⊔ P` be the disjoint union of items at the
five levels, with `level: H → {1, 2, 3, 4, 5}` the level function.
The trace links induce a covering relation `≺` such that `x ≺ y`
iff `x` is the parent of `y` in the trace and
`level(x) = level(y) − 1`. The reflexive-transitive closure `≤` is
a partial order, and `(H, ≤, level)` is a **graded poset** of rank
4.

### What the poset structure encodes

| Construct | Project meaning |
|---|---|
| Maximal elements (no parents) | Top-level Goals |
| Minimal elements (no children) | Leaf Physical Implementations |
| Up-set `↑x` | The chain of justification from `x` upward to a Goal |
| Down-set `↓x` | The chain of realisation from `x` downward to a Physical Implementation |
| Element with empty up-set at level > 1 | An **orphan with no upward trace** — the pathology in `../goals-requirements-hierarchy/how-it-works.md` |
| Element with empty down-set at level < 5 | An **orphan with no downward trace** — the second pathology |
| Antichains | Sets of items at incomparable positions; useful for partition-based subsystem grouping |

### What it adds

The traceability rules in
`../goals-requirements-hierarchy/how-it-works.md` are stated in
prose. The graded-poset reformulation gives a one-line algorithm
for orphan detection (compute the up-set and down-set of every
node) and a precise vocabulary for "what is a subsystem" (a
convex sub-poset closed under the relevant trace links).

## Application 3 — Authority and permission as a lattice

Input: the controller hierarchy in a control structure (see
`../control-structures/`).

### Formalise

Let `C` be the set of controllers. Define `c₁ ≤_auth c₂` iff `c₂`
can override `c₁`'s decisions. In well-behaved control structures
this relation is a partial order; in the four-level universal
control pattern (Supreme Authority > Intermediate > Local >
Individual) it is a chain. Where multiple controllers must concur,
or where permissions are unioned, the structure becomes a lattice.

For permissions, let `A` be the action set. A controller's
permission set is a subset `S ⊆ A`. The collection of permission
sets, ordered by inclusion, is a Boolean lattice with `∨ = ∪`,
`∧ = ∩`.

### Operations and what they mean

| Operation | Meaning |
|---|---|
| `c₁ ∨_auth c₂` | The smallest controller above both — the joint controller required for an action neither alone authorises |
| `c₁ ∧_auth c₂` | The largest controller below both — the *most senior* controller they both dominate |
| `S₁ ∨ S₂` | Combined permission set of `c₁` acting jointly with `c₂` |
| `S₁ ∧ S₂` | Permissions both must agree to (veto-style joint action) |

### What it adds

Constitutional questions like "can two ministers jointly authorise
what a single minister cannot" become lattice questions: does
`S₁ ∨ S₂` strictly contain `S₁` and `S₂`? **Veto coalitions** are
elements with the property that their meet `∧` is empty.
**Accountability voids** (Q3 in
`../control-structures/diagnostic-questions.md`) are nodes
high in the authority lattice with no upward feedback — a property
that is checkable from the lattice plus the feedback graph.

## Application 4 — Galois connections between trace levels

Input: any pair of adjacent levels in the SE hierarchy with their
trace matrix.

### Formalise

Take Goals `G` and Functions `F` with trace relation
`T ⊆ G × F` ("function `f` serves goal `g`"). Define two operators
between subsets:

- `↑: 2^F → 2^G` by `↑(F') = {g ∈ G : ∀f ∈ F', (g, f) ∈ T}`
  — "goals served by *every* function in `F'`."
- `↓: 2^G → 2^F` by `↓(G') = {f ∈ F : ∀g ∈ G', (g, f) ∈ T}`
  — "functions that serve *every* goal in `G'`."

`(↑, ↓)` is a Galois connection: `F' ⊆ ↓(G')` iff `G' ⊆ ↑(F')`.
The fixed points `(G', F')` with `↑(F') = G'` and `↓(G') = F'` are
exactly the FCA concepts of the formal context `(G, F, T)`.

### What it adds

The Galois connection makes precise the duality the SE hierarchy
already exploits informally:

- "What is the smallest function set that achieves these goals" is
  the closure of a set of goals.
- "What goals does this function set legitimately claim to serve"
  is the closure of a set of functions.

Operations the project already does by hand — checking whether a
proposed Function set covers the Goals, checking whether the Goal
list a Function justifies is plausible — become applications of
the closure operators.

## Application 5 — FCA on the PLE feature matrix

Input: the variants × features matrix from
`../product-line-engineering/`. For the dev-frameworks catalogue,
this is roughly 8 × 30; for the social-systems catalogue, roughly
10 × 40.

### Formalise

The matrix is a **formal context** `K = (G, M, I)` where `G` is
the set of variants (the *objects*), `M` the set of features (the
*attributes*), and `I ⊆ G × M` the incidence relation. The two
derivation operators

- `A' = {m ∈ M : ∀g ∈ A, (g, m) ∈ I}`
- `B' = {g ∈ G : ∀m ∈ B, (g, m) ∈ I}`

generate **formal concepts**: pairs `(A, B)` with `A' = B` and
`B' = A`. The set of all concepts, ordered by `(A₁, B₁) ≤
(A₂, B₂)` iff `A₁ ⊆ A₂` (equivalently `B₂ ⊆ B₁`), forms a
**concept lattice** `B(K)`.

### What the concept lattice encodes

| Lattice element | Project meaning |
|---|---|
| Top concept | All variants with no required common features |
| Bottom concept | The empty variant set with all features as common attributes |
| Concept `(A, B)` | The maximal variant family `A` characterised by exactly the feature set `B` |
| Concept hierarchy | A taxonomy of variant families, more general at the top, more specialised at the bottom |
| Implications between attributes | Rules of the form "every variant with features `X` also has feature `y`" — extractable directly from the lattice |

### What it adds

The PLE catalogue identifies a platform (features common to all)
and variation points (features that distinguish variants) by
inspection. FCA gives:

- **The platform** — exactly the attribute set of the top concept
  (or the concept just below it if the top concept is degenerate).
- **The intermediate families** — every concept above the bottom
  is a candidate "sub-platform" shared by a non-trivial subset of
  variants.
- **The implications** — a complete list of the if-then rules among
  features, computed by the algorithm of Ganter (the *Duquenne–
  Guigues basis*).
- **Variant clustering without numerical projection** — variants
  that sit at the same lattice node share exactly the same feature
  set; variants close in the lattice share most features.

Compared with PCA on the same matrix
(`../linear-algebra/how-it-works.md`, Application 3), FCA produces
*nameable* concepts rather than latent axes. The two are
complementary: PCA tells you the family has 3 effective dimensions;
FCA tells you what those families *are*.

## Procedure

1. **Identify the artefact.** Which of the five applications does
   the question fall under? If none, the technique does not apply.
2. **Recover the order or the formal context from the existing
   qualitative work.** Do not re-derive it from narrative.
3. **Compute the relevant construct.** For posets: orphan
   detection, antichain enumeration. For lattices: meet, join,
   sub-lattices. For FCA: concept lattice, Duquenne–Guigues basis.
   Standard tools: the `concepts` Python package, `FCAtools`, or
   any computer algebra system that supports lattice operations.
4. **Read the result back into the qualitative diagnosis.** A
   concept lattice that contradicts the project's stated platform
   is a signal to recheck both — possibly the platform was
   inspection-derived and missed an attribute.
5. **Stop at the structural reading.** The technique does not
   produce numerical scores or predictions. If the question
   genuinely needs numbers, hand off to `../linear-algebra/`.
