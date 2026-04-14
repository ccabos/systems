# Technical vs Non-Technical Systems

Extracted from `projects/systems-introduction-book/docs/part1/what-is-a-system.md`
(§ "Why This Matters for Social Systems"). Explains why the SE
hierarchy, which was developed in engineering, still applies to
social systems, and what is different when it does.

## Technical systems are legible by design

Technical systems — aircraft, software, power grids — are designed
with explicit goals, documented connections, and identifiable parts.
Their structure is legible because engineers made it so:

- **Goals** are written into requirements specifications, regulatory
  standards, and contracts.
- **Connections** are drawn in schematics, architecture diagrams,
  and interface control documents.
- **Parts** are listed in a bill of materials.
- **Boundaries** are set by the organisation that owns the system.

When something goes wrong, the documented structure is where the
investigation starts. The SE hierarchy is a natural fit because the
structure already exists in a form that maps onto G / R / F / L / P.

## Social systems are not designed the same way

Social systems — states, religions, corporations, families — were
not designed in the same deliberate sense. Their goals are often
implicit, their connections informal, and their boundaries contested.
Three consequences follow, and they shape how the SE techniques are
applied throughout this project:

**1. The decomposition is reconstructive, not documentary.** For a
technical system you can *read off* the decomposition from existing
documents. For a social system you have to *reconstruct* it from
observation, comparison, and historical evidence. The resulting
decomposition is a model — an explicit hypothesis about structure —
not a description of something already written down.

**2. Declared and operative goals diverge.** A regulatory agency
declared to protect the public may operate primarily to protect the
regulated industry. A religion declared to save souls may operate
primarily to perpetuate its own institutional authority. Technical
systems have this problem too (specifications that don't match
deployed behaviour), but in social systems the divergence is the
norm, not the exception. The STPA analysis (see
`knowledge/se-techniques/stpa/`) targets unsafe control actions that
arise from this split.

**3. The boundary is contested.** For a technical system the owning
organisation draws the boundary. For a social system the boundary
itself is a political and interpretive act. Who counts as a member
of a nation, a church, or a family is not a fact; it is a decision
(see `boundaries-and-environment.md`). This forces an explicit
boundary decision at the start of every analysis.

## What carries over, what doesn't

Carries over:

- The five-level SE hierarchy is applicable. Social systems have
  goals, requirements, functions, logical architectures, and
  physical implementations in exactly the same structural sense as
  technical ones.
- Product line concepts (platform, variation point, binding) apply,
  because social systems recurrently reuse the same functional slots
  (see the social-system cross-system platform in
  `knowledge/system-catalogues/social-systems/cross-system/platform.md`).
- Hazard analysis (STAMP / STPA) applies, because unsafe control
  actions, inadequate feedback, and unsafe controller behaviours are
  structural phenomena that do not require the system to be
  engineered on a drawing board.

Does *not* carry over:

- The assumption that requirements are written down. In social
  systems, requirements must be inferred from goals, behaviours, and
  historical decisions.
- The assumption that functions map cleanly to org-chart boxes. In
  social systems, a single physical element (a parish priest) may
  perform many functions; a single function (doctrinal governance)
  may be distributed across many physical elements.
- The assumption that the system is the unit of moral agency. In
  social systems, moral responsibility is always distributed across
  the structure, never fully located in any single part — this is
  the practical consequence of non-linear feedback in complex
  structures.

## Practical implication

The SE techniques in `knowledge/se-techniques/` are written so that
they apply to both technical and social systems. The worked examples
in `knowledge/se-techniques/*/technical-examples/` show the technique
on its original engineering domain; the case studies in
`knowledge/system-catalogues/` show the technique on social systems.
The technique itself is the same; the evidence base and the
interpretation of each level are different.
