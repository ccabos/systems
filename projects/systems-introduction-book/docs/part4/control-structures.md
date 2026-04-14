# Control Structures in Social Systems

## The Universal Control Pattern

Every social system has a hierarchical control structure with the same basic shape. Authority flows downward; feedback — ideally — flows upward. STPA analyses this structure by asking four questions of every system:

1. **Feedback richness** — how many independent channels carry information from the base to the top, and how accurately do they represent reality?
2. **Self-sealing tendency** — can the process model at the top be corrected by information from below, or does it filter out contradictory signals?
3. **Accountability voids** — where is the controller also the interested party, structurally preventing independent oversight?
4. **Circuit breakers** — what mechanisms exist to interrupt a harmful escalating loop before it causes irreversible damage?

The four levels of the universal pattern are:

| Level | Role |
|-------|------|
| **Supreme Authority** | Issues doctrine, law, strategy, or policy |
| **Intermediate Controllers** | Interpret and transmit downward; aggregate and filter upward |
| **Local Community** | Enforces norms through social mechanisms; primary source of ground-truth feedback |
| **Individual** | Internalises norms; self-regulates; ultimate recipient of system outcomes |

What varies across systems is: who occupies each level, what mechanisms connect them, and how honest the upward flow is.

!!! info "Canonical reference"
    The technique definitions — the four diagnostic questions and the three dangerous patterns — live in `knowledge/se-techniques/control-structures/`. The per-system profiles for all ten social systems live in `knowledge/system-catalogues/social-systems/cross-system/control-structure-profiles.md`.

---

## The Ten Systems: Control Structure Profiles

For each of the ten social systems, the same four-level pattern is filled in with the specific controllers, intermediate actors, local communities, and individuals that occupy each role, and each system is rated on the four diagnostic questions.

The complete profiles — Kingdom, Republic, Theocracy, One-Party State, Corporation, University, Military, Religion (Church), Family, Verein — and the cross-system comparison table are in `knowledge/system-catalogues/social-systems/cross-system/control-structure-profiles.md`. A short summary of the pattern of feedback richness, self-sealing tendency, accountability voids, and circuit breakers across the ten systems appears there as a single table.

The key observation the profiles support is that the same control-structure weakness recurs in structurally identical forms across very different systems: the monarch judging the Crown's own claims, the bishop investigating his own clergy, the commanding officer prosecuting his own troops, the board setting the pay of executives who chose the board, the peer reviewing his own competitor's work. The *institutional vocabulary* differs; the *structural pattern* is the same.

---

## The Three Most Dangerous Structural Patterns

Across all systems, three patterns recur wherever the most serious harm occurs:

**Pattern 1: The Accountability Void.**
The controller and the interested party are the same entity. No external actor has authority to review the decision. The remedy in every case is the same: structurally separate the controller from the interested party, and give the separating body genuine authority.

**Pattern 2: The Self-Sealing Process Model.**
The top of the control structure populates its own process model — its internal representation of reality — from sources it controls. Contradictory information is excluded by design (doctrine), by incentive (career risk for bearers of bad news), or by structure (classification, privacy norms). The model diverges from reality while the authority acts with increasing confidence. The remedy: establish independent information channels with direct access to the apex, reporting to a body outside the hierarchy.

**Pattern 3: The Proxy Metric.**
The system measures something that is correlated with its actual goal, attaches resources and careers to that measure, and then watches as the system reorients toward producing the measure rather than the goal. Exam scores replace education. Quarterly earnings replace sustainable value creation. Publication counts replace scientific knowledge. Compliance reports replace operational readiness. The remedy: continuously examine what is being measured and whether the feedback loop connects to the goal or to a proxy, and restructure the measurement accordingly.

These three patterns are the recurring targets of the architectural remedies in the next chapter. The technique-level statement of all three — with the failure mode each corresponds to in a generic control loop, and the remedy preconditions — is in `knowledge/se-techniques/control-structures/dangerous-patterns.md`.
