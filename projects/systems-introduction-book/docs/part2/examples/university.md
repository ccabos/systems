# Example: University

The university is the organization family's most internally contested variant — it must simultaneously serve truth (research), education (teaching), and self-governance (academic freedom), goals that regularly conflict. Its SE decomposition exposes why corporatization threatens the system's core logic.

[**→ Interactive D3 Visualization**](../../interactive/university.html){ .md-button }

## SE Decomposition

The full five-level decomposition is shown in the interactive visualization linked above. Click any node to see its description, parent links, and child links. Use the Table view for the complete traceability matrix.

## Variation Point Bindings

VP1 = scholarly merit (unique among social systems), VP2 = competitive admission, VP3 = collegial deliberation (faculty senate), VP4 = mixed (elected rector + appointed deans). The tension between VP1 (merit) and external pressure to bind VP3 to hierarchical management is the central conflict in modern higher education.

## The Structural Pathology of VP1 = Scholarly Merit

"Scholarly merit" is the only variation-point binding in the social-systems catalogue that *requires the controller to be assessable on the same standard it controls under*. Faculty senates decide on faculty, peer review decides on peer-reviewed work, tenure committees decide on tenure-track scholarship. The system is structurally circular by design — and the circularity works *only when the merit signal is not corrupted*.

Two corruptions are now well documented. The first is the **proxy-metric substitution**: scholarly merit is hard to measure, but citation counts and journal impact factors are easy. The career structure has migrated to the easy metric, and so the system's most consequential decisions are now made on the proxy rather than the goal. The classic Goodhart pattern: "when a measure becomes a target, it ceases to be a good measure."

The second is **publication bias** — the literature itself is a biased sample, because journals select for positive, novel, surprising findings. The cumulative scholarship the system uses to validate further scholarship has therefore been selected by a mechanism that no longer tracks evidence strength. The 2015 Open Science Collaboration found that only 36% of psychology findings replicated. The collegial-merit decision the structure depends on is being made on data the structure has corrupted.

These are not failures of bad scholars. They are structural consequences of the VP1 binding combined with a measurement choice (impact factor) that the system was not architecturally protected against.

## STPA Highlights

**UCA-U1: Journals publish selectively (publication bias), so the literature accumulates a biased sample.**

*Causal factor:* the decision to publish is made *after* the result is known, by editors and reviewers who reward novelty and significance. A non-replication, a null result, or a careful but unsurprising study faces structural pressure against publication. The cumulative-evidence rung (rung 4) is supposed to correct rung-3 single-study errors; here the rung-4 corpus is itself a rung-3 sample biased at the source.

**UCA-U2: Tenure and promotion committees use bibliometrics as proxies for research quality.**

*Causal factor:* committees are overloaded, citation counts are countable, and quality is contested. The path of least administrative resistance is to use h-index, impact factor, and grant size as decision-makers for what is supposed to be a peer-review judgement. Once the proxy is the decision rule, scholars rationally optimise for the proxy.

**UCA-U3: Research budgets concentrate at institutions that already hold grant track records.**

*Causal factor:* grant applications are evaluated partly on prior funding success — a Matthew-effect feedback loop that makes the future distribution of resources a function of the past distribution, regardless of merit shifts. The intended rung-3 selection mechanism (peer review of the proposal) is overridden by a rung-1 institutional-reputation signal.

## Fixes That Worked

**Pre-registration and Registered Reports — addressing UCA-U1.**

Pre-registration commits researchers to hypotheses, methods, and analysis plans before data collection; Registered Reports take this further, with peer review of the *protocol* before any data exists, and an acceptance-in-principle that survives whatever the result turns out to be. *Evidence:* the Center for Open Science hosts over 100,000 pre-registrations; more than 300 journals offer Registered Reports. Pre-registered studies replicate at substantially higher rates than unconstrained ones. The structural change: the publication decision is decoupled from the result.

**DORA (Declaration on Research Assessment, 2012) and the UK REF panel review — addressing UCA-U2.**

DORA, signed by more than 25,000 individuals and 3,000 organisations, commits assessors to evaluate research on its *content* rather than the journal in which it appeared. The UK Research Excellence Framework moved to article-level panel assessment after the 2014 cycle, explicitly disconnecting reward from journal-level proxies. *Evidence:* the UK REF 2021 panels read submitted outputs directly; impact factor was excluded as an assessment input. The structural change: the proxy is severed from the decision.

**Open access mandates (Plan S, NIH 2008 onward) — partial fix for UCA-U1 and UCA-U3.**

Mandating open publication of publicly funded research removes the journal-publisher gatekeeping that selected the published sample. *Evidence:* Plan S coalition includes Wellcome Trust, ERC, UK Research Councils; compliance rates on funded grants exceed 70% by 2024. The structural change is partial — selection has migrated to preprint visibility — but the original gatekeeping is no longer load-bearing for funded research.

!!! example "The Design Principle"
    The fixes do not ask scholars to be more honest. They change the structure so that the proxy metric no longer determines the consequence. Pre-registration moves the publication decision before the result is known. Article-level assessment moves the reward decision off the journal-level proxy. Open access moves the visibility decision off the publisher. Each is a structural intervention against a specific causal pathway STPA identifies.

## Platform Mapping

This system fills all ten universal functional slots identified in the [Ten Social Systems Compared](../ten-systems.md):

| Functional Slot | How This System Fills It |
|-----------------|-------------------------|
| Authority & Decision-Making | Faculty senate (academic matters); rector/president (executive); board of trustees (strategic oversight) |
| Membership & Belonging | Matriculated students; academic and administrative staff; alumni (honorary standing) |
| Resource Allocation | Rector/president budget; competitive grant allocation; tuition and third-party research funding |
| Norm Setting & Enforcement | Academic regulations; research ethics boards; HR policy; accreditation standards |
| Dispute Resolution | Academic appeals committees; disciplinary panels; employment tribunals |
| Legitimation | Knowledge creation and transmission; accreditation; academic freedom as constitutive value |
| Succession & Continuity | Rector election or appointment; academic tenure; departmental and programme continuity |
| External Representation | Rector; research partnerships; international agreements; alumni relations |
| Socialisation | Academic induction; doctoral mentorship; collegiate culture; peer learning communities |
| Activity Delivery | Teaching; research; knowledge transfer; community engagement and public scholarship |

---

*Navigate to the [interactive visualization](../../interactive/university.html) for the full graph and table.*

## Sources

The rung-3/4 standard the university claims is classically stated as Merton's norms of science (1973); the governance triangle across jurisdictions is Clark (1983); the reproducibility evidence is the Open Science Collaboration (*Science*, 2015) and Nosek et al. (*PNAS*, 2018). Annotated sources: [`university/sources.md`](https://github.com/ccabos/systems/blob/main/knowledge/system-catalogues/social-systems/university/sources.md).
