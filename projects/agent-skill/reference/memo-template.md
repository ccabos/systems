# Decision Memo Template

> **How to use.** Replace every italic placeholder with content for
> the user's case. Aim for 1–2 pages of plain language. **No
> technical notation that has not first been defined in plain
> language.** Every claim drawn from the SE / STPA / rung techniques
> or from a catalogue must cite the `reference/...` file it came
> from. If a section does not apply, write *Not applicable: <reason
> in one sentence>* — do not silently drop it.

---

# Decision Memo — *<short, concrete title naming the system or problem>*

**Prepared for:** *<role of the decision-maker, in plain words>*
**Prepared by:** *<your name or role>*
**Date:** *<month and year>*
**Status:** *<For decision | For discussion | For information>*

---

## System under analysis

*One paragraph in plain language. What institution, organisation,
or setup is the memo about? Who is inside it, who is outside it,
and what is the user trying to understand or fix? Avoid technical
notation here — this paragraph must be readable by someone with
no SE background.*

---

## Key findings

*One short paragraph framing the findings: how many there are,
which require decisions before the next concrete milestone, which
can wait, and which are uncertainties rather than gaps.*

### Finding 1 — *<one-line headline in plain language>*

*Two to four sentences. State the gap or risk in plain words. Name
the structural feature that produces it (which controller does
what, which feedback channel is missing, which rung the loop runs
on). Do not yet propose a remedy.*

### Finding 2 — *<headline>*

*…*

### Finding 3 — *<headline>*

*…*

*(Add or remove findings as needed. Three to five is typical for a
memo; more belongs in the full report.)*

---

## Structural causes

*One short paragraph mapping the findings onto one or more of the
four dangerous patterns from `reference/se-techniques/control-structures/dangerous-patterns.md`:*

- *Accountability void — controller and interested party are the same*
- *Self-sealing process model — apex of the hierarchy populates its own evidence base*
- *Proxy metric replacing goal — the system is measuring the wrong thing*
- *Rung asymmetry (social systems) — control at one rung, feedback expected at another*

*State which patterns apply, in plain language, with one example
from the user's own system per pattern. Cite the technique file
the pattern comes from.*

---

## Recommended decisions

*One sentence framing the recommendations: how many decisions are
needed, in what order, and what they collectively achieve.*

### Decision 1 — *<imperative-mood headline: "Write the priority rule," "Appoint X before Y," etc.>*

**What.** *One paragraph in plain language describing the action.*

**Why.** *Which finding or findings this closes; which structural
cause it removes; cite the remedy in
`reference/system-catalogues/<branch>/cross-*/remedies-case-studies.md`
that this is an instance of.*

**Who decides.** *Role, not name.*

**By when.** *Concrete trigger or date.*

### Decision 2 — *<headline>*

*…*

*(One decision per finding is the default. Combine where two
findings have a single fix, but do not silently merge.)*

---

## Decisions summary

| # | Decision | Closes finding | Decided by | By when |
|---|----------|----------------|-----------|---------|
| 1 | *…* | F1 | *role* | *date* |
| 2 | *…* | F2 | *role* | *date* |

---

## What this analysis is based on

*Bullet list of cited files, one per claim made above. Group by
type:*

**Techniques used.**

- `reference/se-techniques/goals-requirements-hierarchy/five-level-hierarchy.md` *(decomposition)*
- `reference/se-techniques/control-structures/diagnostic-questions.md` *(five questions)*
- `reference/se-techniques/control-structures/dangerous-patterns.md` *(four patterns)*
- *Add others actually cited above.*

**Catalogue entries used.**

- `reference/system-catalogues/<branch>/<best-match>/se-decomposition.md` *(known family member used as a scaffold)*
- `reference/system-catalogues/<branch>/cross-*/remedies-case-studies.md` *(remedy precedents)*
- *Add others actually cited above.*

**Open questions / known gaps.**

- *List explicit gaps, especially anywhere the system was novel
  and remedies could not be derived from pattern-matching.*

---

> **Note for non-technical readers.** This memo is the short form.
> The full analysis report (with the eight-step procedure, the
> control-structure map, the UCA table, and the traceability
> matrix) is available in
> `report.md` in the same folder if you want to inspect the
> reasoning step by step.
