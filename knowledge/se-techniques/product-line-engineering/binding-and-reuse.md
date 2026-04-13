# Binding Decisions and the Reuse Gradient

Given a platform with variation points (see
`platform-and-variation-points.md`), product line engineering asks
two further questions:

1. *Which variants are bound to which variation points in a given
   system?* — the **binding decisions**.
2. *Which elements can legitimately move between systems in the
   family?* — the **reuse analysis**.

## Binding decisions

A binding decision is the specific choice made at each variation
point for a given product. "This kingdom binds VP1 to hereditary
right"; "this republic binds VP1 to popular sovereignty"; "Scrum
binds VP1 to fixed-length iterations".

Once a binding is made, it constrains which other bindings are
compatible. Not all combinations are coherent. The cross-system
analyses in
`knowledge/system-catalogues/social-systems/cross-system/variation-points.md`
and `dev-frameworks/cross-framework/variation-points.md` list the
observed interaction constraints for each catalogue.

## The reuse gradient

Across both catalogues in this project, a general principle holds:

> **Reuse feasibility decreases as you move upward in the SE
> hierarchy.**

| SE Level | Reuse Potential |
|----------|----------------|
| Physical Implementation | Highest — a tax authority works under any regime |
| Logical Architecture | High — subsystems transfer with adaptation |
| Functions | Medium — mechanisms may need interface adjustment |
| Requirements | Low — must be checked for goal compatibility |
| Goals | Lowest — goals define the system type; changing them means changing the system |

### Practical corollary — start at the bottom

Modernise physical implementations first (professional civil service,
independent courts, transparent budgets, CI/CD pipelines), then work
upward. Top-down reform — imposing new goals before building the
implementing infrastructure — is the recipe for failed states and
failed methodology adoptions.

## The coherence rule

A system is coherent when its binding decisions at each variation
point are mutually compatible, and when every element at every SE
level traces consistently to the goals above it and the
implementations below it. Incoherent systems — those with
contradictory bindings — are unstable. They either resolve the
contradiction (through reform or revolution) or persist in
institutional dysfunction.

## The workaround principle

When a desirable module from another system type conflicts with a
binding decision, the most successful reforms do not force the
transplant. They create a **workaround** — a modified version that
preserves the function while respecting the constraint. The
constitutional monarchy is the paradigm case: it wants legislative
representation (a republican function) but cannot adopt popular
sovereignty for the executive, so the workaround is a parliament
that legislates *alongside* the crown.

See the worked examples of workarounds in
`knowledge/system-catalogues/social-systems/cross-system/principles.md`
(§ The Workaround Principle) and the hybrid architectures in
`knowledge/system-catalogues/dev-frameworks/cross-framework/hybrids.md`.

## The product-line architect's toolkit

Applying these concepts to a reform or hybrid-design problem gives
a standard sequence:

1. **Decompose both systems** (source and target) through the five
   SE levels.
2. **Identify the platform elements** shared between them — these
   are free to reuse.
3. **Map the variation points** — identify where the systems
   diverge.
4. **Check binding constraints** — determine which source-system
   elements conflict with the target's VP bindings.
5. **Classify reuse potential** — green (direct adoption), amber
   (adopt with workaround), red (incompatible without changing
   system identity).
6. **Start at the bottom** — implement physical-level changes
   first, then work upward.
7. **Design workarounds** for amber items — preserve the function
   while respecting the constraint.
8. **Accept red items as system-defining** — attempting to force
   them means changing the system type, not reforming it.
