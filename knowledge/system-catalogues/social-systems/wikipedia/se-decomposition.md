# Wikipedia / Open-Source Project — SE Decomposition

The canonical five-level SE decomposition of Wikipedia and the
canonical open-source project (Linux kernel, Debian, Python). They
are catalogued together because they share VP1 (authority by
demonstrated contribution evaluated against a rung-3 standard).

## Goals (G)

- **G1** — Produce and maintain a freely accessible body of work (encyclopaedia / software)
- **G2** — Ensure the work meets a contestable quality standard (verifiability / working code)
- **G3** — Sustain a community of contributors capable of carrying the work forward
- **G4** — Remain free in the constitutive sense (Wikipedia: free license; OSS: free/open license)

## Requirements (R)

- **R1** — Open submission mechanism for new contributions
- **R2** — Review process capable of accepting, rejecting, or amending submissions
- **R3** — Quality standard evaluable against rung-3 evidence (sources, tests, reproducibility)
- **R4** — Trust hierarchy that admits experienced contributors to expanded rights
- **R5** — Dispute-resolution mechanism for contested submissions
- **R6** — Infrastructure (servers, version control, communication channels)
- **R7** — Legal framework (license, foundation, governance documents)
- **R8** — Backstop authority for cases the consensus mechanism cannot resolve

## Functions (F)

- **F1** — Contribution intake — accept edits / patches / submissions
- **F2** — Review — evaluate against the rung-3 standard
- **F3** — Merge / publish — commit the contribution to the canonical work
- **F4** — Dispute resolution — handle contested submissions
- **F5** — Trust management — grant and revoke expanded rights
- **F6** — Community moderation — handle conduct, harassment, bad-faith contribution
- **F7** — Infrastructure operation — servers, build systems, communications
- **F8** — Governance — strategy, foundation relations, conflict escalation

## Logical Architecture (L)

- **L1** — Contribution subsystem — edit interface / pull-request mechanism / patch submission
- **L2** — Review subsystem — reviewer pool, review tooling, review norms
- **L3** — Trust subsystem — rights ladder (reader → editor → admin / contributor → committer → maintainer)
- **L4** — Dispute-resolution subsystem — talk pages / mailing-list debate, mediation, ArbCom / Steering Council
- **L5** — Community subsystem — code of conduct, moderation, onboarding
- **L6** — Infrastructure subsystem — servers, repositories, mailing lists, CI/CD
- **L7** — Governance subsystem — foundation, BDFL/Steering Council, legal counsel

## Physical Implementation (P)

- **P1** — Contributors — anonymous to maintainer, stratified by tenure and demonstrated competence
- **P2** — Foundation / non-profit (Wikimedia Foundation, Linux Foundation, Python Software Foundation)
- **P3** — BDFL / Steering Council / ArbCom — backstop authority
- **P4** — Servers, repositories, MediaWiki / Git / mailing lists
- **P5** — Verifiability / reliability sources; test suites; reproducibility tooling
- **P6** — Governance documents (project guidelines, code of conduct, PEPs, RFCs)
- **P7** — License (CC BY-SA, GPL, MIT, BSD, Apache)
- **P8** — External users (readers, downstream developers) as the system's beneficiaries

## Key Structural Observations

**VP1 = demonstrated contribution evaluated against rung-3 standards.**
This is the system's defining and unique feature in the catalogue.
The rung-3 standard (citable source, working code, passing tests)
exists before any institutional authority needs to enforce it; the
authority follows the demonstrated competence rather than the other
way around.

**The substitution is not absolute.**
Where the rung-3 standard is contested (contested political topics,
contested architectural decisions in software) or absent (matters of
style, governance, community conduct), the system falls back on
rough consensus — which has the failure modes documented for
deliberative systems generally, plus the tyranny-of-structurelessness
failure mode that the absence of formal authority creates.

**Backstop authority is structurally necessary.**
Every long-lived wiki / OSS project has at some point installed a
statutory backstop (ArbCom, Steering Council, BDFL succession). The
projects that have not — early small projects, some web standards
groups — either remained small, fragmented into forks, or got
captured. The structural finding is that pure VP1 = rung-3 is
sufficient for content but not for governance; the governance layer
needs at least a rung-2/6 mechanism for the cases rung-3 cannot
adjudicate.

The full applied STPA analysis is in the book's chapter
`projects/systems-introduction-book/docs/part2/examples/wikipedia.md`.
