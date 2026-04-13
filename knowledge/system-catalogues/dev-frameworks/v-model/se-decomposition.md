# V-Model — SE Decomposition

Extracted from `projects/systems-introduction-book/docs/part3/frameworks.md`
§2.2. IDs use the `V*` prefix as in the source. Note: the verein entry
in `social-systems/verein/` also uses `V*` — the prefixes collide
across catalogues but each file's IDs are local to that decomposition.

## Goals (VG)

- **VG1** — Deliver a verified and validated system with traceable quality evidence
- **VG2** — Ensure every design decision has a corresponding test
- **VG3** — Meet regulatory and contractual quality requirements (safety, compliance)

## Requirements (VR)

- **VR1** — Symmetric structure: each left-side (design) phase maps to a right-side (test) phase
- **VR2** — Test planning begins during the corresponding design phase, not after
- **VR3** — Complete traceability from requirements through design to test cases
- **VR4** — Independent verification and validation (IV&V) for critical systems
- **VR5** — Formal reviews and sign-offs at each phase transition

## Functions (VF)

- **VF1** — Requirements analysis — user requirements, system requirements
- **VF2** — System design — architecture, subsystem decomposition
- **VF3** — Detailed design — component-level specification
- **VF4** — Implementation — coding, unit construction
- **VF5** — Unit testing — verify individual components
- **VF6** — Integration testing — verify subsystem interactions
- **VF7** — System testing — validate against system requirements
- **VF8** — Acceptance testing — validate against user requirements

## Logical Architecture (VL)

- **VL1** — Left Arm — requirements → system design → detailed design → implementation
- **VL2** — Right Arm — unit test → integration test → system test → acceptance test
- **VL3** — Traceability Subsystem — requirements-to-test mapping, coverage analysis
- **VL4** — Review Subsystem — formal reviews, IV&V, sign-off gates

## Physical Implementation (VP)

- **VP1** — Requirements management tool (DOORS, Polarion), traceability matrix
- **VP2** — Design documents (SAD, SDD), review protocols
- **VP3** — Test management tool, test cases linked to requirements
- **VP4** — IV&V reports, certification evidence packages
