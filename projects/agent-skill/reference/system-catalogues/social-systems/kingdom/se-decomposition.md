# Kingdom (Traditional Monarchy) — SE Decomposition

Extracted from `projects/systems-introduction-book/docs/part2/ten-systems.md`
§2.1.1. IDs use the `K*` prefix as in the source, for unambiguous
cross-system reference.

## Goals (KG)

- **KG1** — Maintain sovereign authority and dynastic continuity of the crown
- **KG2** — Ensure order, security, and territorial integrity
- **KG3** — Provide governance and welfare to subjects
- **KG4** — Preserve legitimacy through tradition, divine right, and hereditary succession

## Requirements (KR)

- **KR1** — Hereditary succession rules (primogeniture, house laws)
- **KR2** — Loyalty apparatus — oaths, titles, patronage binding subjects to crown
- **KR3** — Military force under direct royal command
- **KR4** — Revenue extraction — taxation, crown lands, trade monopolies
- **KR5** — Administrative apparatus executing royal will across the territory
- **KR6** — Legitimation narrative — religion, coronation rites, dynastic mythology

## Functions (KF)

- **KF1** — Royal decree — legislate by sovereign command
- **KF2** — Court administration — household, ceremony, patronage, honors
- **KF3** — Military command — defense, suppression of rebellion, war
- **KF4** — Tax collection and treasury management
- **KF5** — Royal justice — administer law in the king's name
- **KF6** — Diplomatic representation — treaties, dynastic marriages, alliances

## Logical Architecture (KL)

- **KL1** — Royal Court — household, privy council, chancellery
- **KL2** — Military Subsystem — army, navy, royal guard
- **KL3** — Fiscal Subsystem — treasury, tax collectors, crown estates
- **KL4** — Judicial Subsystem — royal courts, appointed judges
- **KL5** — Territorial Administration — governors, provincial lords

## Physical Implementation (KP)

- **KP1** — Crown, throne, palace, coronation cathedral
- **KP2** — Privy council, court officials
- **KP3** — Standing army, navy, fortresses
- **KP4** — Royal treasury, tax farmers, customs houses
- **KP5** — Royal courts of justice, appointed magistrates
- **KP6** — Provincial governors, feudal lords, bailiffs

## Justification rungs

For the technique see `../../../se-techniques/justification-rungs/`;
for the cross-system comparison see
`../cross-system/justification-rungs-by-system.md`.

| Attribute | Value |
|-----------|-------|
| Claimed rung | **1** — divine right, hereditary legitimacy, sacral tradition (KR6, KG4) |
| Operating rung | **0/1** — force backed by tradition. Coercion (KR3, KF3) is always available; deliberation is exceptional |
| Loop symmetry | Symmetric at the operating rung. Down: rung-1 royal decree (KF1) and rung-0 military command (KF3); up: rung-1 court reports filtered by KL1 and KL5 |
| Dominant rung pattern | None directly — claim and operation match closely. Failures here come from the *absence* of feedback at any rung (Patterns 1–2 — Accountability Void plus Self-Sealing Process Model) rather than rung asymmetry |

The kingdom is the cleanest case of *honest rung-1 operation*: the
system claims tradition and divine right, and it operates on
tradition and divine right. There is no claimed-vs-operating gap to
collapse. The structural failures are therefore the classical ones
catalogued in `../../../se-techniques/control-structures/dangerous-patterns.md`:
the monarch judges their own claims, and the court is the only
upward channel to the throne. Both operate inside rung 1.

This makes the kingdom the natural baseline for the rung dimension:
when later systems (theocracy, one-party state) take rung-1
operation but wrap it in rung-6 legitimacy claims, the result is
worse than the bare kingdom — because the gap itself becomes the
dominant hazard (HX in
`../religion/applied-se-analysis.md` §1.2 illustrates the
generalisation).
