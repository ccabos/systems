# STPA and STAMP

!!! info "Canonical reference"
    The normative statements of STAMP (the accident model) and STPA (the four-step hazard analysis procedure, the four UCA types, and the rules for translating an SE decomposition into STPA inputs) are maintained as the project's knowledge base under `knowledge/se-techniques/stamp/` and `knowledge/se-techniques/stpa/`. This chapter is the narrative introduction; the knowledge base is the reference.

## System-Theoretic Process Analysis

### The STAMP Accident Model

STAMP (Systems-Theoretic Accident Model and Processes), developed by Nancy Leveson at MIT, treats accidents not as the result of component failures but as **emergent properties of complex systems** — caused by inadequate control, including failures between components that may each be functioning exactly as designed.

This is precisely the right model for social systems, where the most devastating outcomes (inquisitions, abuse cover-ups, financial crises, failed reforms) typically occur not because the system has "broken" but because its control mechanisms are operating exactly as designed — just in a way that produces harm.

### The Four Steps of STPA

| Step | What It Produces |
|------|-----------------|
| **Step 1: Define Purpose** | Losses (unacceptable outcomes), Hazards (system states leading to losses), System-level Constraints |
| **Step 2: Model Control Structure** | Hierarchical diagram of controllers, control actions, feedback channels, and process models |
| **Step 3: Identify Unsafe Control Actions** | Systematic enumeration of UCAs across four types |
| **Step 4: Identify Loss Scenarios** | Causal analysis: why each UCA occurs, what contextual factors enable it |

### The Four UCA Types

For every control action in the system, STPA asks four questions:

1. **Not providing** — What happens if this control action is *not* issued when it should be?
2. **Providing** — What happens if this control action *is* issued when it shouldn't be, or is the wrong action?
3. **Too early / too late / wrong order** — What happens if the timing is wrong?
4. **Applied too long / stopped too soon** — What happens if the duration is wrong?

### From SE Decomposition to STPA

The SE hierarchy feeds directly into STPA:

- **Goals** define what the system must achieve → STPA **Losses** are the negation of goals
- **Requirements** define constraints → STPA **System-level Constraints** are safety requirements
- **Logical Architecture** defines subsystems → STPA **Control Structure** maps controllers and controlled processes
- **Physical Implementation** identifies actors → STPA identifies who issues which control actions

This integration is applied in detail in [Part IV](../part4/index.md).

### Rung tagging — the social-systems extension

For social systems, Step 2 acquires one more move: tag every
control action and every feedback channel with the **justificatory
rung** at which it operates (rung 0 coercion through rung 6
deliberative legitimacy), and tag each controller with both its
*claimed* and *operating* rung.

Rung information is not derivable from the SE decomposition — it is
its own elicitation activity, performed during Step 2 — and it is
required by Step 3 to identify rung-mismatch UCAs (over-rung
command, under-rung command, asymmetric loop). The previous chapter
[Justificatory Rungs](justification-rungs.md) introduces the ladder
and the three dangerous mismatch patterns; the canonical
integration with STPA Steps 1–4 is at
`knowledge/se-techniques/justification-rungs/application-to-stpa.md`.

For engineering systems where every loop operates at rung 3–4
throughout, rung tagging adds nothing and is omitted. Use this
extension where the system is social, institutional, or
policy-shaped — where the question being asked is *whether the
loop's rung fits its function*.

### References

- Leveson, N.G. (2012). *Engineering a Safer World: Systems Thinking Applied to Safety*. MIT Press.
- Leveson, N.G. & Thomas, J.P. (2018). *STPA Handbook*. MIT Partnership for Systems Approaches to Safety and Security.
- Leveson, N.G. (2004). "A New Accident Model for Engineering Safer Systems." *Safety Science*, 42(4), 237–270.
