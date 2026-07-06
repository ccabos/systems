# Product Line Engineering — Overview

A **product line** (or product family) is a set of systems that
share a **common platform** but differ at defined **variation points**.
The engineering discipline has three core ideas, described in
`platform-and-variation-points.md` and `binding-and-reuse.md`.

In this project, product line engineering is the comparative
methodology that sits on top of the five-level SE hierarchy: each
system is first decomposed with the hierarchy (see
`../goals-requirements-hierarchy/`), and then product-line concepts
are applied across decompositions to identify what is shared and
where the systems legitimately diverge.

The worked results of applying this method to the two catalogues in
this project live in:

- `knowledge/system-catalogues/social-systems/cross-system/` —
  platform, variation points, reuse case studies, and principles for
  the ten social systems.
- `knowledge/system-catalogues/dev-frameworks/cross-framework/` —
  platform, variation points, reuse analysis, hybrid architectures,
  and merging principles for the eight development frameworks.

This page lists the technique's core concepts in one place. The
applications of those concepts are in the two catalogues above.

## Sources

Product-line engineering is an established discipline with standard
references; this project takes its vocabulary directly from them.
The founding idea — designing a *family* of systems rather than one
— is Parnas's [Parnas1976]. The practice canon is [ClementsNorthrop2002];
the platform / variation-point / binding-time vocabulary used
throughout this project follows [Pohl2005]. Citation keys resolve in
`knowledge/references/bibliography.md`.

What is *not* from the literature: applying the platform/variation-
point analysis across social systems (the `social-systems/cross-system/`
catalogue) is this project's transfer. The nearest published
relative is Ostrom's programme of extracting shared design
principles and a common institutional grammar from many field cases
of self-governed institutions [Ostrom1990; Ostrom2005] — reaching
platform-like conclusions from the empirical direction rather than
the engineering one. Where the two approaches disagree, Ostrom's
field evidence should win; her warning against transplanting
institutional blueprints between contexts [Ostrom2007] is the main
constraint on any reuse conclusion drawn from the cross-system
platform.
