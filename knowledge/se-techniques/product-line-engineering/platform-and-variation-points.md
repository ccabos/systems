# Platform and Variation Points

The two central concepts of product line engineering. For how these
concepts connect to reuse and binding decisions, see
`binding-and-reuse.md`.

## The platform

The platform is the set of architectural elements — goals,
requirements, functions, subsystems, and physical components — that
are shared across all (or most) members of the family.

- **In automotive terms**, the platform is the chassis.
- **In social-system terms**, the platform is the governance
  function, the membership mechanism, the resource allocation
  subsystem.
- **In development-framework terms**, the platform is the ten
  universal functional slots (work discovery, prioritisation,
  execution, QA, integration, delivery, feedback, governance,
  improvement).

A platform is not an abstract ideal. It is the specific structural
elements that empirically recur across the product family when all
members are decomposed using the same SE hierarchy. The
social-system platform and the development-framework platform were
both derived this way — see
`knowledge/system-catalogues/*/cross-*/platform.md`.

## Variation points

Variation points are the locations in the architecture where the
platform deliberately leaves a decision open, because different
family members will make different choices. A variation point has:

- A **defined interface** — what connects to it.
- A **set of variants** — what can be plugged in.

Everything below the interface works with any variant.

### Automotive analogy

- **Interface:** "Here, a powertrain connects to the drivetrain."
- **Variants:** 2.0L diesel · electric motor · plug-in hybrid.

Everything below the interface (suspension, brakes, steering) works
with any variant.

### Political analogy

- **Interface:** "Here, executive authority is sourced and
  legitimated."
- **Variants:** hereditary succession · popular election · party
  appointment · clerical selection.

Everything below the interface (courts, civil service, tax
authority) works with any variant.

## How platforms and variation points are discovered

In this project, platforms and variation points are discovered
*empirically* from the decompositions, not postulated in advance:

1. Decompose each candidate family member using the five-level SE
   hierarchy.
2. Align the decompositions level by level.
3. Identify elements that appear in every member (possibly with
   different bindings) — these constitute the platform.
4. Identify elements that vary across members — these become
   variation points.
5. For each variation point, list the variants observed and the
   family members that use each.

This empirical approach is how the social-system platform in
`knowledge/system-catalogues/social-systems/cross-system/platform.md`
and the six variation points in `variation-points.md` in the same
folder were derived. The development-framework equivalents in
`knowledge/system-catalogues/dev-frameworks/cross-framework/`
follow the same method.
