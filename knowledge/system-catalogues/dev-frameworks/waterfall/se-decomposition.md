# Waterfall — SE Decomposition

Extracted from `projects/systems-introduction-book/docs/part3/frameworks.md`
§2.1. IDs use the `W*` prefix as in the source.

## Goals (WG)

- **WG1** — Deliver a defined product that meets specified requirements on time and on budget
- **WG2** — Minimize risk through comprehensive upfront planning
- **WG3** — Provide clear accountability and progress visibility to stakeholders

## Requirements (WR)

- **WR1** — Complete, stable requirements specification before design begins
- **WR2** — Sequential phase gates — each phase completed and signed off before the next starts
- **WR3** — Comprehensive documentation at each phase boundary
- **WR4** — Defined roles: analyst, designer, developer, tester, project manager
- **WR5** — Change control process — changes are formal, evaluated for impact, and approved

## Functions (WF)

- **WF1** — Requirements analysis — elicit, document, and baseline requirements
- **WF2** — System design — architecture, detailed design, interface specifications
- **WF3** — Implementation — code, build, integrate components
- **WF4** — Verification — test against requirements, identify defects
- **WF5** — Deployment and maintenance — release, operate, fix, enhance
- **WF6** — Project control — track schedule, budget, scope; report to stakeholders

## Logical Architecture (WL)

- **WL1** — Planning & Control Subsystem — project plan, Gantt chart, milestone tracking
- **WL2** — Requirements Subsystem — SRS, traceability matrix, change control board
- **WL3** — Design Subsystem — architecture documents, design reviews
- **WL4** — Build Subsystem — development environment, coding standards, integration
- **WL5** — Test Subsystem — test plans, test cases, defect tracking
- **WL6** — Release Subsystem — deployment procedures, operational handover

## Physical Implementation (WP)

- **WP1** — Project plan (MS Project), Gantt chart, WBS
- **WP2** — Software Requirements Specification (SRS), Requirements Traceability Matrix
- **WP3** — Architecture Document (SAD), Design Specification, UML diagrams
- **WP4** — IDE, version control (Git), build servers, coding standards document
- **WP5** — Test Plan, test suite, defect tracker (Jira, Bugzilla), test reports
- **WP6** — Release notes, deployment scripts, operations manual
