# Scope and Pitfalls

Order theory does not have linear algebra's false-precision
problem — a poset has no numerical entries to invent. But it has
its own characteristic misuses, listed below with the safeguards
the project adopts.

## Pitfall 1 — Asserting a total order where only a partial order exists

The seven justificatory rungs are presented as a chain. That is a
modelling claim: every pair of rungs is comparable, and the order
between any two is fixed. For some pairs (rung 0 vs. rung 6) this
is uncontroversial; for others (rung 4 cumulative-empirical
vs. rung 5 meta-rational) the comparison is defended in
`../justification-rungs/rungs.md` but is not beyond dispute.

**Safeguard.** When the project commits to a chain, the commitment
is documented at the technique level (in `../justification-rungs/`)
and the lattice operations here inherit it. If the chain claim is
weakened to a partial order, downgrade the rung-mismatch test from
`r_a ≠ r_f` to "either incomparable, or differ by ≥ 2" — which is
strictly the more defensive condition.

## Pitfall 2 — Treating missing trace links as "no relation"

The SE hierarchy's trace matrices are sparse. A blank entry in a
Goals × Functions matrix could mean (a) the function genuinely does
not serve that goal, or (b) the analyst has not yet recorded the
link. The graded-poset machinery treats both cases identically — as
"not in the relation" — and will then report orphans that are
artefacts of incomplete recording.

**Safeguard.** Run orphan detection only after the trace matrix is
declared *complete* by the analyst. Where completeness is
uncertain, mark the matrix as draft and treat orphan reports as
*candidate* orphans pending review.

## Pitfall 3 — Coercing non-binary features into a formal context

FCA requires a binary incidence relation. Real PLE feature lists
include non-binary attributes: iteration length (continuous),
team size (count), governance regime (categorical with several
values). Forcing these into 0/1 ("has iterations of length ≤ 4
weeks: yes/no") loses information, and the choice of threshold
silently determines the concept lattice.

**Safeguard.** For non-binary attributes, use **many-valued FCA**
(scaling): replace one many-valued attribute with several binary
ones encoding the relevant value ranges, with the scaling choice
documented. Where scaling would dominate the analysis, do not
apply FCA — write the variants × features comparison as a table
and stop there.

## Pitfall 4 — Concept-lattice explosion on dense contexts

The concept lattice of a formal context with `n` objects and `m`
attributes can have up to `2^min(n, m)` concepts. A dense context
produces a lattice too large to read. The dev-frameworks catalogue
(8 × 30) is small enough to be safe; richer catalogues are not
guaranteed.

**Safeguard.** Compute the lattice's size before drawing it. If it
exceeds ~30–50 concepts, summarise via the **Duquenne–Guigues
basis of implications** rather than by drawing the lattice. If the
basis is also unmanageable, the matrix is too dense for FCA;
sub-divide by attribute family.

## Pitfall 5 — Confusing the partial order with causation

`x ≤ y` in any of the technique's posets means a structural
relationship — derivation, authority, refinement. It does *not*
mean `x` causes `y`. A function below a goal in the SE hierarchy
serves the goal; it does not produce it. An action permitted under
a controller's authority does not happen because the authority
permits it.

**Safeguard.** Causal reasoning belongs to STPA Step 4 and the
loss-scenario analysis. Do not import causal language into
order-theoretic statements. When a causal claim is wanted, name
the technique (STPA) explicitly.

## Pitfall 6 — Algorithmic readings of socially-loaded relations

Lattice operations are mechanical. Once a controller poset is
written down, `c₁ ∨_auth c₂` produces a definite answer.
Mechanical answers can mislead readers into treating the upstream
modelling choice — *which* controllers count, *which* actions are
"the same action across two contexts" — as also mechanical, when
those choices are the substantive analytical work.

**Safeguard.** Always state the modelling choices alongside the
lattice. A figure of a permission lattice should carry the same
boundary statement as the SE decomposition that produced it (see
`knowledge/foundations/boundaries-and-environment.md`).

## When in doubt

The technique is a *formalisation* layer. Use it where the
qualitative work has produced a poset, a lattice, or a binary
incidence relation, and the question is about the structure of
that object. Do not use it to *replace* the qualitative work, and
do not let the mechanical operations carry weight the modelling
cannot bear.
