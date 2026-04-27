# Justificatory Rungs — Implementation Plan

**Working document.** Tracks the multi-session task of integrating
the seven-rung justificatory ladder into the systems project. Delete
this file when the task is finished.

---

## The concept (canonical statement)

Every control action and every feedback signal in a social system
relies on some standard for what counts as a *decisive reason* to act
on it. These standards form a ladder; later rungs add internal or
external checks that earlier rungs lack.

| Rung | Standard | Real-world example | What it adds over the previous rung |
|------|----------|--------------------|-------------------------------------|
| 0 | Power / coercion | Coups, monopolies, threats | No common standard at all |
| 1 | Authority / rhetoric / identity | Slogans, scripture, "as a parent…" | Persuasion without truth or consistency check |
| 2 | Formal consistency | Math proofs, court syllogisms | Internal check — contradictions lose |
| 3 | Empirical testability | Randomised trials, falsification | External check — data can sink a neat theory |
| 4 | Cumulative evidence / consilience | Meta-analyses, IPCC reports | Survives flukes and publication bias |
| 5 | Meta-rational integration | Risk engineering, AI-safety, complex-systems policy | Knows when each method breaks, combines under uncertainty |
| 6 | Normative legitimacy / deliberative ethics | Constitutional courts, citizens' assemblies, Habermasian discourse | Justifies *oughts* to all affected, not just facts |

## How it extends STPA

1. **Per-arrow rung tagging.** Step 2 of STPA tags each control
   action and each feedback channel with the rung it operates at.
2. **Dual-rung process models.** Each controller's process model
   acquires two beliefs: (a) what rung the controlled process accepts
   for *commands*; (b) what rung the controller accepts for
   *corrective feedback*. The two are often different — this is
   structurally important.
3. **Three new UCA modes** beyond Leveson's four types:
   - **UCA-R1 Over-rung command.** Controller issues a control action
     at a rung the receiver cannot decode (rung 4 → rung 1: data to a
     fundamentalist). Command fails silently.
   - **UCA-R2 Under-rung command.** Controller issues a control
     action at a rung the receiver rejects as illegitimate (rung 1 →
     rung 4: "trust me" to a scientist). Command fails noisily.
   - **UCA-R3 Asymmetric loop.** Control action and feedback on the
     same loop operate at different rungs, so the controller cannot
     hear what would correct it (or refuses to act on what it hears).
4. **New dangerous pattern: Rung Asymmetry.** Joins the existing
   three (Accountability Void, Self-Sealing Process Model, Proxy
   Metric) at the technique level. Symptom: stable downward control
   with structurally filtered upward feedback.
5. **New diagnostic question.** Joins the four existing questions in
   `control-structures/diagnostic-questions.md`: *"What rungs do
   control actions and feedback operate at, and is the loop
   symmetric?"*
6. **Claimed-rung vs operating-rung.** The catastrophic systems are
   those that *claim* a high rung but *operate* at a low one.
   Cataloguing the gap is its own diagnostic.
7. **Remedies are rung-elevation moves.** Mandatory external audit
   raises a rung-1 internal channel to rung 3. Citizens' assemblies
   insert a rung-6 loop where only rung-1 representation existed.
   Vatican II partially raised doctrinal feedback from rung 1 to
   rung 2/3.

## Tradeoff to keep visible

Leveson's STPA is deliberately neutral about controllers; the rung
ladder is openly normative (rung 6 > rung 0). Flag this everywhere
the integration happens. The ladder is a useful add-on *for social
systems where epistemic standards matter*; engineering systems mostly
operate at rung 3-4 throughout and do not need it.

---

## Phase plan

Each phase has explicit file edits. Tick boxes as you go.

### Phase 1 — Knowledge base: technique page (foundational) ✅ DONE (commit 6d15917)

Create new technique under `knowledge/se-techniques/justification-rungs/`:

- [x] `README.md` — index, link to siblings (stpa, stamp, control-structures)
- [x] `overview.md` — what the technique is, why it exists, when to use
- [x] `rungs.md` — the seven rungs in detail with definitions, examples, what each rung adds
- [x] `application-to-stpa.md` — the seven hooks above
- [x] `dangerous-mismatches.md` — the three rung-mismatch patterns + circuit breakers
- [x] `references.md` — Popper, Kuhn, Habermas, Leveson, "meta-rationality" sources

Update `knowledge/se-techniques/README.md` (if it exists) to list the new folder.

Acceptance: a reader of the new folder can fully understand the
technique and apply it without other prior context.

### Phase 2 — Knowledge base: extend STPA & control-structure pages ✅ DONE (commit f721fd3)

- [x] `knowledge/se-techniques/stpa/four-steps.md` — append a Step 2.5 paragraph: "Tag each arrow with a rung. See `../justification-rungs/application-to-stpa.md`."
- [x] `knowledge/se-techniques/stpa/unsafe-control-actions.md` — add a "Rung-mismatch UCA modes" section with UCA-R1/R2/R3.
- [x] `knowledge/se-techniques/stpa/from-se-to-stpa.md` — note rung as a per-arrow attribute that does not come from the SE decomposition; STPA must elicit it separately.
- [x] `knowledge/se-techniques/control-structures/diagnostic-questions.md` — add 5th question (rung).
- [x] `knowledge/se-techniques/control-structures/dangerous-patterns.md` — add "Rung Asymmetry" as the fourth pattern.
- [x] `knowledge/se-techniques/control-structures/overview.md` — bump "four diagnostic questions" / "three dangerous patterns" counts.

Acceptance: the existing STPA pages reference rungs explicitly;
no broken cross-references.

### Phase 3 — Knowledge base: cross-system catalogue ✅ DONE (commit 24dc05f)

- [x] `knowledge/system-catalogues/social-systems/cross-system/control-structure-profiles.md` — add two rows to each system's profile: **Claimed rung** and **Operating rung**, with a one-sentence note on the gap.
- [x] `knowledge/system-catalogues/social-systems/cross-system/remedies-case-studies.md` — re-read each remedy as a rung-elevation move; add a "Rung delta" line to each.
- [x] New file: `knowledge/system-catalogues/social-systems/cross-system/justification-rungs-by-system.md` — comparison table across the ten systems with claimed/operating/gap.

Acceptance: each catalogue file shows the rung dimension; the new
comparison file enumerates all ten.

### Phase 4 — Religion deep dive (also clears earlier debt) ✅ DONE (commits 70d878c, 78a0976, 6d79be9, 427450c, 22ba7fd)

- [x] Create `knowledge/system-catalogues/social-systems/religion/applied-se-analysis.md` (the file `se-decomposition.md:59` already forward-references). Build the rung dimension into it from the start: Step 1–4 STPA artefacts, with each control action and feedback channel rung-tagged, and a final section "Rung mismatch as the structural driver."
- [x] Update `knowledge/system-catalogues/social-systems/religion/se-decomposition.md` — keep the forward reference, now satisfied; add a top-of-file pointer to `applied-se-analysis.md`.

Acceptance: the religion folder is complete to the social-systems
template (sans `is-it-a-system.md`, `historical-se-interventions.md`,
`sources.md` which remain optional per project pattern).

### Phase 5 — Per-system rung notes (touch only what is structural) ✅ DONE (commits 0cb30c8 + 5b)

For each system below, add a "Justification rungs" subsection to its `se-decomposition.md`:

- [x] `kingdom/se-decomposition.md` — operates rung 0/1; honest baseline
- [x] `military/se-decomposition.md` — operates rung 0/1, claims higher in modern professional armies; civil-military rung mismatch is the distinguishing feature
- [x] (`theocracy/`, `one-party-state/`, `democracy/`, `corporation/`, `university/`, `family/`, `verein/` currently have no per-system files; their rung notes live only in cross-system files for now. Skip until/unless a per-system file is created.)

Acceptance: the two existing per-system files acknowledge the rung dimension; no new files are created here.

### Phase 6 — Book Part I: foundational chapter ✅ DONE

- [x] Create `projects/systems-introduction-book/docs/part1/justification-rungs.md` — narrative chapter introducing the ladder with examples, ending with a forward reference to STPA chapter and Part IV.
- [x] Update `projects/systems-introduction-book/docs/part1/index.md` — list the new chapter.
- [x] Update `projects/systems-introduction-book/mkdocs.yml` — add nav entry under Part I.
- [x] Update `projects/systems-introduction-book/generate_pdf.py` — add NAV tuple for the new chapter.

### Phase 7 — Book: integrate rungs into STPA & Part IV ✅ DONE

- [x] Edit `docs/part1/stpa-introduction.md` — add a "Rung tagging" subsection in the Step 2 / control structure discussion. (commit 2f84d0e)
- [x] Edit `docs/part4/religion-stpa.md` — new §6.4 reading §§6.1–6.3 as manifestations of the same rung-1 vs rung-3 asymmetry. (commit d55f692)
- [x] Edit `docs/part4/control-structures.md` — five questions, four dangerous patterns. (commit 9764f2a)
- [x] Edit `docs/part4/remedies.md` — re-read each architectural remedy as a rung-elevation move with the thirteen-remedy table.

### Phase 8 — Skill integration ✅ DONE

- [x] Edit `projects/agent-skill/README.md` — insert rung tagging as new step 5 (between control-structure sketch and STPA pass), renumber subsequent steps. Update step 4's question/pattern counts to five/four. Add the rung-elevation framing to step 7.
- [x] Edit `projects/agent-skill/SKILL.md` — record that the procedure is now eight steps and that the future implementation must cite `knowledge/se-techniques/justification-rungs/`. Note that step 5 is N/A for engineered systems where all loops operate at rung 3–4.

### Phase 9 — Build & verify

- [ ] `cd projects/systems-introduction-book && mkdocs build --strict` — catch broken links.
- [ ] `python generate_pdf.py` — regenerate the book PDF.
- [ ] Manual check: cross-system profiles, remedies, religion KB & book all link to `justification-rungs/`.
- [ ] `git status` clean except for tracked changes; commit per phase.

---

## Sequencing notes

- Phase 1 must finish before Phase 2 (Phase 2 references files Phase 1 creates).
- Phases 2–5 can be done in any order after Phase 1.
- Phase 6 can begin in parallel with Phase 4 (book + religion KB are independent).
- Phase 7 depends on Phase 6 only for the new chapter URL.
- Phase 9 runs last.

## Outstanding from earlier work

- The religion KB STPA file was promised in a previous turn but not
  written. Phase 4 here delivers it. Do not duplicate.

## Commit style

One commit per phase, scoped to that phase's files. Final commit
re-builds the PDF.
