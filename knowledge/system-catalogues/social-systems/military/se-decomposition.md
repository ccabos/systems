# Military — SE Decomposition

Extracted from `projects/systems-introduction-book/docs/part2/ten-systems.md`
§2.2.3. IDs use the `M*` prefix as in the source. Physical items in the
source table are labelled `ML1P..ML6P` (logical ID with a `P` suffix);
this file regularizes them to `MP1..MP6` to match the convention used
by the other nine systems in the catalogue.

## Goals (MG)

- **MG1** — Defend the state against external military threats
- **MG2** — Maintain internal order when directed by civilian authority
- **MG3** — Project power and deter aggression
- **MG4** — Provide disaster relief and humanitarian assistance

## Requirements (MR)

- **MR1** — Strict hierarchical command chain from supreme commander to individual soldier
- **MR2** — Trained, equipped, and deployable fighting force
- **MR3** — Subordination to civilian political authority (in democracies)
- **MR4** — Intelligence and situational awareness capability
- **MR5** — Logistics — supply, transport, medical, maintenance
- **MR6** — Legal framework — laws of armed conflict, military justice

## Functions (MF)

- **MF1** — Command — issue orders, coordinate units, make tactical/strategic decisions
- **MF2** — Combat operations — engage adversaries, defend positions
- **MF3** — Training and readiness — drill, exercises, qualification
- **MF4** — Intelligence — collect, analyze, disseminate information on threats
- **MF5** — Logistics — supply ammunition, fuel, food, medical care
- **MF6** — Military justice — enforce discipline, try offenses

## Logical Architecture (ML)

- **ML1** — Command Subsystem — general staff, operational headquarters, C4ISR
- **ML2** — Combat Subsystem — army brigades, naval vessels, air wings
- **ML3** — Training Subsystem — academies, schools, exercise ranges
- **ML4** — Intelligence Subsystem — signals, human, geospatial, cyber intelligence
- **ML5** — Logistics Subsystem — supply depots, transport, medical corps
- **ML6** — Military Justice Subsystem — courts martial, JAG, military police

## Physical Implementation (MP)

- **MP1** — General staff headquarters, situation rooms, communication networks
- **MP2** — Barracks, bases, warships, aircraft, armored vehicles
- **MP3** — Military academies (West Point, Sandhurst, Führungsakademie), training areas
- **MP4** — Intelligence agencies (BND, MI6, CIA military section), SIGINT stations
- **MP5** — Supply depots, field hospitals, transport aircraft, logistics battalions
- **MP6** — Military courts, provost marshal, detention facilities

## Justification rungs

For the technique see `../../../se-techniques/justification-rungs/`;
for the cross-system comparison see
`../cross-system/justification-rungs-by-system.md`.

| Attribute | Value |
|-----------|-------|
| Claimed rung (traditional) | **1** — oath, chain of command, professional honour |
| Claimed rung (modern democratic) | **1 + 2 + 6** — chain of command (1) constrained by laws of armed conflict (2) and parliamentary mandate (6) |
| Operating rung | **0/1** — coercion plus authority. Higher-rung claims hold during peacetime governance and in operations subject to civilian oversight; they degrade rapidly under operational stress |
| Loop symmetry (internal) | Symmetric at rung 0/1: orders down, compliance reports up. The same chain that issues orders is the channel for reports of their execution (MR1) |
| Loop symmetry (civil-military interface) | Asymmetric. Civilian oversight expects rung-3 information (audited, independent investigation); military self-reporting operates at rung 1 (chain of command) |
| Dominant rung pattern | **Pattern A — Asymmetric Loop** at the civil-military interface. The internal rung-0/1 operation is fit for combat; the failure mode is when rung-3 oversight needed by civilian authority is structurally captured by the rung-1 chain it is supposed to oversee |

**The civil-military rung mismatch is the distinguishing feature of
the modern professional military.** A soldier's loop with their
commander operates legitimately at rung 0/1 — combat does not admit
deliberation. But the *civilian* loop with the military operates at
rung 6 (parliamentary mandate, democratic legitimacy), and that
rung-6 loop needs rung-3 feedback (independent investigation, audit,
inspector-general reports) to function. When the rung-3 channel is
filtered through the rung-1 chain of command, the rung-6 loop opens.

The Bundeswehr model (mandatory Bundestag vote, independent
Wehrbeauftragter, civilian-led ministry of defence) is the most
structurally complete remedy for this rung mismatch (see
`../cross-system/remedies-case-studies.md` §5 and
`../cross-system/remedies-case-studies.md` §6 for its rung delta).
The remedy preserves the rung-0/1 internal operation while
inserting independent rung-3 channels that route around the chain
of command and reach the rung-6 civilian apex directly.
