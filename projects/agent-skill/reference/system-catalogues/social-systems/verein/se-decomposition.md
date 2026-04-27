# Verein (Voluntary Association) — SE Decomposition

Extracted from `projects/systems-introduction-book/docs/part2/ten-systems.md`
§2.3.2. IDs use the `V*` prefix as in the source. The Verein is the
German legal form for a non-commercial voluntary association (eingetragener
Verein, e.V.) and is used here as the canonical example of the
voluntary-association pattern that also appears in clubs, co-ops, and
civic associations in other jurisdictions.

## Goals (VG)

- **VG1** — Enable citizens to pursue a shared non-commercial purpose collectively
- **VG2** — Provide a democratic, self-governing legal structure for civic participation
- **VG3** — Create social cohesion and community identity around shared interests
- **VG4** — Offer institutional continuity independent of individual members

## Requirements (VR)

- **VR1** — Written Satzung defining the purpose
- **VR2** — Legal personality through Vereinsregister (e.V. status)
- **VR3** — Democratic decision-making with equal voting rights
- **VR4** — Elected Vorstand accountable to the membership
- **VR5** — Regular activities that bring members together
- **VR6** — Financial sustainability through dues, donations, and grants

## Functions (VF)

- **VF1** — Constitutional governance — draft and enforce the Satzung
- **VF2** — Membership administration — admit, track, manage members
- **VF3** — Democratic assembly — Mitgliederversammlungen, elect Vorstand
- **VF4** — Executive management — represent the Verein, execute decisions
- **VF5** — Activity delivery — organize events, training, competitions
- **VF6** — Financial management — collect dues, bookkeeping, tax compliance

## Logical Architecture (VL)

- **VL1** — Governance Subsystem — Satzung, Mitgliederversammlung, Wahlordnung
- **VL2** — Administration Subsystem — member database, dues, correspondence
- **VL3** — Executive Subsystem — Vorstand, external representation, contracts
- **VL4** — Operations Subsystem — Abteilungen, coaches, event planning

## Physical Implementation (VP)

- **VP1** — Satzung document, Geschäftsordnung, Beitragsordnung
- **VP2** — Mitgliederversammlung, Protokolle, Kassenprüfung
- **VP3** — Membership software, Vereinsregister entry, Finanzamt registration
- **VP4** — Vorstand members, volunteer coordinators
- **VP5** — Vereinsheim, sports fields, rehearsal rooms
