# Hospital — SE Decomposition

The canonical five-level SE decomposition of the acute-care hospital
as a social system. The hospital is the only system in this catalogue
with a triadic membership boundary (patient, professional, payer).

## Goals (G)

- **G1** — Restore, preserve, or extend patients' physical and mental health
- **G2** — Relieve suffering, including where cure is impossible
- **G3** — Maintain professional standards and the cumulative medical knowledge base
- **G4** — Operate financially sustainably under the constraints of the payer system
- **G5** — Train the next generation of clinical staff

## Requirements (R)

- **R1** — Qualified and licensed clinical workforce (doctors, nurses, allied health)
- **R2** — Diagnostic and therapeutic capability appropriate to the case mix
- **R3** — Triage and demand management for unscheduled care
- **R4** — Documentation, coding, and billing infrastructure for reimbursement
- **R5** — Safety, infection-control, and incident-reporting systems
- **R6** — Governance separating clinical from operational authority
- **R7** — Interfaces with primary care, social care, and post-acute services
- **R8** — Capital and operating budget sufficient for R1–R7

## Functions (F)

- **F1** — Triage and assessment — receive, prioritise, and route patients
- **F2** — Diagnosis — investigate, interpret, formulate clinical plan
- **F3** — Treatment delivery — medical, surgical, nursing, allied-health intervention
- **F4** — Monitoring and escalation — observe patient state, react to deterioration
- **F5** — Discharge and transition of care — coordinate next-stage providers
- **F6** — Documentation and billing — record care; submit claims
- **F7** — Clinical governance — guidelines, audit, M&M, safety reporting
- **F8** — Training and supervision — junior staff, residents, registrars
- **F9** — Operational management — staffing, beds, theatres, equipment, supplies

## Logical Architecture (L)

- **L1** — Clinical subsystem — wards, theatres, ICU, ED, outpatient clinics
- **L2** — Diagnostic subsystem — laboratory, radiology, pathology, imaging
- **L3** — Pharmacy subsystem — medicines management, dispensing, stewardship
- **L4** — Patient-flow subsystem — admissions, bed management, discharge planning
- **L5** — Governance subsystem — medical director, clinical governance committee, safety officer
- **L6** — Operational subsystem — chief executive, finance, HR, facilities, IT
- **L7** — External-interface subsystem — primary-care referrals, social care, payer relations, inspectorate

## Physical Implementation (P)

- **P1** — Doctors — consultants, registrars, residents, junior staff
- **P2** — Nurses — ward, ICU, theatre, community, advanced practice
- **P3** — Allied health professionals — physiotherapists, pharmacists, technicians
- **P4** — Hospital building — wards, ICU, theatres, ED, imaging suites, labs
- **P5** — Medical devices — imaging, monitors, ventilators, surgical equipment
- **P6** — Electronic health record (Epic, Cerner, Meditech, SAP IS-H, …)
- **P7** — Billing and coding systems (ICD-10, DRG, OPS, …)
- **P8** — Inspectorate / regulator (CQC, Joint Commission, IQTIG)
- **P9** — Payer institutions (insurer, Krankenkasse, single-payer body)
- **P10** — Patients themselves as the controlled process

## Key Structural Observations

**G1 (cure) and G2 (relief) trade off against G4 (sustainability)
through the same allocation decisions.**
The hospital's resource constraints are real; the question is which
of the three goals an allocation decision serves. The structural
risk is that whichever goal is most legible to the payer's
process model (typically G4) crowds out the others.

**Triadic VP2 means there is no single 'customer'.**
Patient, clinician, and payer each have legitimate but distinct
interests. The structural pathology appears when one corner of the
triangle monopolises the signalling channel: payer dominance →
billing-code distortion; clinician dominance → cost/access
divergence; manager dominance → proxy-metric substitution
(Mid-Staffordshire pattern).

**F4 (monitoring and escalation) is the highest-stakes loop.**
The early-warning literature and the rapid-response-team
literature both identify this as the single loop whose failure
most directly produces preventable in-hospital mortality, and the
fix in both cases is a parallel rung-3 channel (standardised
physiological score; team that bypasses normal hierarchy).

The full applied STPA analysis is in the book's chapter
`projects/systems-introduction-book/docs/part2/examples/hospital.md`.
