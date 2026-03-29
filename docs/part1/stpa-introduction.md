# STPA and STAMP

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

### References

- Leveson, N.G. (2012). *Engineering a Safer World: Systems Thinking Applied to Safety*. MIT Press.
- Leveson, N.G. & Thomas, J.P. (2018). *STPA Handbook*. MIT Partnership for Systems Approaches to Safety and Security.
- Leveson, N.G. (2004). "A New Accident Model for Engineering Safer Systems." *Safety Science*, 42(4), 237–270.
