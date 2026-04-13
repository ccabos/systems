# Product Line Thinking

!!! info "Canonical reference"
    The normative definitions of platform, variation points, binding decisions, the reuse gradient, the coherence rule, the workaround principle, and the product-line architect's toolkit are maintained as the project's knowledge base under `knowledge/se-techniques/product-line-engineering/`. This chapter is the narrative introduction; the knowledge base is the reference.

## Platform, Variation Points, and Reuse

A **product line** (or product family) is a set of systems that share a **common platform** but differ at defined **variation points**. The engineering discipline has three core ideas:

### The Platform

The platform is the set of architectural elements — goals, requirements, functions, subsystems, and physical components — that are shared across all (or most) members of the family. In automotive terms, this is the chassis. In social system terms, this is the governance function, the membership mechanism, the resource allocation subsystem.

### Variation Points

Variation points are the locations in the architecture where the platform deliberately leaves a decision open, because different family members will make different choices. A variation point has a defined *interface* (what connects to it) and a set of *variants* (what can be plugged in).

!!! example "Automotive Analogy"
    **Interface:** "Here, a powertrain connects to the drivetrain."
    
    **Variants:** 2.0L diesel · electric motor · plug-in hybrid
    
    Everything below the interface (suspension, brakes, steering) works with any variant.

!!! example "Political Analogy"
    **Interface:** "Here, executive authority is sourced and legitimated."
    
    **Variants:** hereditary succession · popular election · party appointment · clerical selection
    
    Everything below the interface (courts, civil service, tax authority) works with any variant.

### Binding Decisions

Binding decisions are the specific choices made at each variation point for a given product. Once a binding is made, it constrains which other bindings are compatible. Not all combinations are coherent.

### The Reuse Gradient

Our analysis reveals a general principle: **reuse feasibility decreases as you move upward in the SE hierarchy.**

| SE Level | Reuse Potential |
|----------|----------------|
| Physical Implementation | Highest — a tax authority works under any regime |
| Logical Architecture | High — subsystems transfer with adaptation |
| Functions | Medium — mechanisms may need interface adjustment |
| Requirements | Low — must be checked for goal compatibility |
| Goals | Lowest — goals define the system type; changing them means changing the system |

This gradient has a practical corollary: **start reform at the bottom.** Modernize physical implementations first (professional civil service, independent courts, transparent budgets), then work upward. Top-down reform — imposing new goals before building the implementing infrastructure — is the recipe for failed states and institutional collapse.

### The Coherence Rule

A system is coherent when its binding decisions at each variation point are mutually compatible, and when every element at every SE level traces consistently to the goals above it and the implementations below it. Incoherent systems — those with contradictory bindings — are unstable.

### The Workaround Principle

When a desirable module from another system type conflicts with a binding decision, the most successful reforms create a **workaround** — a modified version that preserves the function while respecting the constraint. The constitutional monarchy is the paradigm case.

These concepts are applied extensively in [Part II](../part2/index.md) (social systems) and [Part III](../part3/index.md) (development frameworks).
