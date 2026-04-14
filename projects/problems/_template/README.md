# Problem template

Copy this folder to a sibling folder named after the problem (short,
kebab-case, no stakeholder PII). Rename, fill in `problem.md` first,
then add other files only as the problem requires them.

## Files

- `problem.md` — **required.** Describes the problem at its root.
  Every problem folder must have one, at the top level, named
  exactly this.

## Optional files (create only if needed)

- `decomposition.md` — a fresh SE decomposition if the system under
  analysis is not already in `knowledge/system-catalogues/`.
- `stpa.md` — STPA hazard analysis output: losses, hazards, control
  structure, UCAs, loss scenarios.
- `remedy-proposals.md` — specific architectural remedies with their
  rationale, costs, and expected effects.
- `decision-memo.md` — the final deliverable for the stakeholder, if
  the engagement produces one.

## What does not belong here

- New canonical decompositions of systems (those go in
  `../../../knowledge/system-catalogues/`).
- New technique definitions (those go in
  `../../../knowledge/se-techniques/`).
- Bibliographies or evidence listings of general interest (those go
  in the relevant `knowledge/` folder).

If analysis of a problem produces genuinely new knowledge —
a new variation point, a new dangerous pattern, a new remedy
class — file it in `knowledge/` and cite it from the problem
folder, not the other way round.
