# What Is a System?

!!! info "Canonical reference"
    The normative statement of the foundational concepts in this chapter — the working definition, the replaceability hierarchy, emergence, boundaries, and the distinction between technical and non-technical systems — is maintained as the project's knowledge base under `knowledge/foundations/`. This chapter is the narrative discussion; the knowledge base is the reference.

## Before We Decompose, We Must Define

Every analytical framework rests on an ontology — a theory of what kinds of things exist. Before applying the SE hierarchy, product line thinking, or STPA, we need a precise answer to the question that precedes all of them: *what makes something a system in the first place?*

Two families of answers dominate the literature. They are not mutually exclusive; this chapter argues they are complementary and that understanding the tension between them clarifies what our analytical tools are actually doing.

---

## Theory I — Structure: Parts, Connections, and Goals

The first and most widely held view holds that a system is constituted by three elements:

1. **Parts** — the distinguishable components that can, in principle, be identified and listed
2. **Connections** — the relationships, flows, and dependencies between parts
3. **Goals** — the purpose or purposes the system pursues, whether declared or operative

### The Replaceability Hierarchy

A significant observation follows from this ontology: the three elements are not equally essential to system identity, and they differ in how easily they can be replaced without the system ceasing to be *the same system*.

| Element | Replaceability | Consequence of Change |
|---------|---------------|-----------------------|
| **Parts** | High — most easily swapped | System continues; this is routine maintenance |
| **Connections** | Moderate — harder to change | System is restructured; behaviour shifts significantly |
| **Goals** | Low — very difficult to change | System is transformed; what was there before is effectively a different system |

A human body replaces most of its cells over years and remains the same organism. A corporation can change its entire workforce and remain recognisably the same corporation. But a corporation whose goal shifts from profit to public service is, in any meaningful sense, a different institution wearing the same legal clothes. The Roman Catholic Church that abandoned the salvation of souls as its operative goal would not be a reformed Catholic Church — it would be something else entirely occupying the same physical infrastructure.

This hierarchy maps directly onto the SE decomposition used throughout this book. Physical implementations (P) correspond to parts. Logical architecture and functions (L, F) encode the connection patterns. Goals and requirements (G, R) encode purpose. Institutional reform that touches only P-level elements is maintenance. Reform that reaches G-level is transformation — and the historical record shows it is both rare and destabilising.

### Critical Assessment

The structural theory is productive and largely correct, but it has four significant gaps.

**1. Goals are often contested, latent, or split.** The framework assumes a system has goals. Real social systems typically have *declared* goals and *operative* goals that diverge substantially. A regulatory agency declared to protect the public may operate primarily to protect the regulated industry. A religion declared to save souls may operate primarily to perpetuate its own institutional authority. The structural theory needs to distinguish these two types of goal, or it will mistake the label for the contents. This book addresses the divergence directly in the STPA analysis (Part IV), where unsafe control actions typically arise from exactly this split.

**2. Connections may outrank goals as the determinant of system identity.** Donella Meadows argued that the *feedback structure* of a system — its loops, delays, and reinforcing dynamics — determines its long-term behaviour more than any stated goal. A system whose goals are replaced but whose feedback loops remain intact will tend to revert to its former behaviour over time. The Soviet Union changed its declared goals repeatedly; the feedback structure of centralised authority, information suppression, and reward for loyalty produced remarkably consistent outcomes across six decades and several ideological pivots. The replaceability ordering may need revision: connections as structure may be *more* fundamental to identity than goals as declaration.

**3. Every part is itself a system.** The framework is valid but incomplete: it defers the definition rather than grounding it. A part is a system with its own parts, connections, and goals. This recursion is not a defect — it reflects the genuine nested structure of complex systems — but it means the theory requires a boundary condition: a decision about where to stop decomposing. That decision is not given by the theory itself.

**4. The boundary question is missing.** The most important definitional act for any system is drawing its boundary: what is inside and what is outside. For social systems this is particularly fraught. Who is "in" a state? Citizens only? Residents? Who counts as a member of a religion — the registered faithful, the active practitioner, the nominal cultural adherent? The boundary choice determines what counts as a part, what counts as an internal connection, and what counts as an external relationship. A theory of systems that omits the boundary is like a theory of cells that omits the membrane.

---

## Theory II — Behaviour: Emergence

The second view defines systems not by what they are made of but by what they *do* that their parts cannot. A system is characterised by **emergent properties** — properties that are present in the organised whole but absent from any of the individual parts considered in isolation.

No individual neuron is conscious. No individual water molecule is wet. No individual trader sets market prices. Consciousness, wetness, and market prices are real; they exist; but they exist only at the level of the organised system, not at the level of its parts. If emergence is present, something is a system. If it is absent — if the whole is simply the sum of its parts — what we have is an aggregate, not a system.

This provides an observational test: can the behaviour of the whole be predicted by summing the behaviours of the parts? If yes: aggregate. If no: system.

### Critical Assessment

The emergence criterion captures something real and important. But it has three significant weaknesses that limit its usefulness as a *definition* of system.

**1. Emergence is descriptive, not constitutive.** The emergence criterion tells you what to observe once you have already decided you are looking at a system; it does not tell you how to identify or engineer one. You cannot look for emergence before you have decided what to treat as the parts — and that decision already presupposes a structural theory. Emergence is the *output* of a system's structure, not the criterion that defines it. For an SE-based approach, this is a practical limitation: you design structure and observe emergence as a consequence; you cannot design emergence directly.

**2. The criterion is trivially satisfied by aggregates.** A pile of sand has a height and an angle of repose that no individual grain possesses. A crowd has a density that no individual person has. These are properties present in the aggregate but absent from the parts — but no one seriously claims a pile of sand is a system in the relevant sense. The emergence criterion must be qualified: we need to specify *which* emergent properties matter. The relevant ones are goal-directed or self-maintaining behaviours — and as soon as we say this, we have smuggled goal back in through the back door, returning to Theory I.

**3. The strong/weak emergence distinction matters.** Philosophers distinguish *weak emergence* (in principle reducible to lower-level description, but practically too complex to compute) from *strong emergence* (genuinely irreducible, a new causal power not explainable even in principle from the parts). Almost all emergence in social systems is weak: complex, non-linear, and surprising, but not metaphysically mysterious. Treating social emergence as strong emergence — as if "the system" were a force beyond analysis — is an error that forecloses the very analysis this book attempts.

---

## Synthesis: The Working Definition

The two theories are not rivals. They are the **inside view** and the **outside view** of the same reality.

- **From the inside** (Theory I): a system is a *structure* — organised parts, patterned connections, directing goals, within a defined boundary.
- **From the outside** (Theory II): a system is an *actor* — something whose boundary-level behaviour cannot be read off from its parts in isolation.

Neither is sufficient alone. A structure with no emergent behaviour is a machine, not a system in the interesting sense. An emergent phenomenon with no describable structure is magic, not analysis.

Adding the boundary gives the working definition this book operates with throughout:

!!! abstract "Working Definition"
    A system is a **bounded structure of parts and connections organised by goals**, whose behaviour at the boundary **cannot be predicted from its parts in isolation**.

Four corollaries follow from this definition and recur throughout the analysis:

1. **Changing parts is maintenance.** It preserves the system.
2. **Changing connections restructures the system.** It changes what the system does, often dramatically.
3. **Changing goals transforms the system.** The result is a different system with inherited infrastructure.
4. **Changing the boundary redefines the system.** What counts as internal, external, and relational changes entirely.

The SE hierarchy in the next chapter is a formal instrument for making this structure explicit and tractable. Goals become the G-level. Connections between functional components become the L-level. Parts become the P-level. The boundary is the decision to start the decomposition at all.

---

## Why This Matters for Social Systems

Technical systems — aircraft, software, power grids — are designed with explicit goals, documented connections, and identifiable parts. Their structure is legible because engineers made it so.

Social systems — states, religions, corporations, families — were not designed in the same deliberate sense. Their goals are often implicit, their connections informal, and their boundaries contested. The structural theory predicts that this makes them harder to reform: if the connection patterns are not documented, you cannot know what you are changing. If operative goals are not distinguished from declared goals, reform efforts target the label and leave the engine untouched.

The emergent-behaviour theory adds a further warning: social systems produce outcomes that no participant intended and no individual can fully understand. This is not mysticism — it is the practical consequence of non-linear feedback in complex structures. It means that moral responsibility is always distributed across the structure, never fully located in any single part.

Both warnings are taken seriously in what follows.
