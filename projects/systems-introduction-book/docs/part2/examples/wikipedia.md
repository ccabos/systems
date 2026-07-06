# Example: Wikipedia / Open-Source Project

Wikipedia and the canonical open-source project (Linux kernel, Debian, Python) are the test case for whether the book's framework generalises to systems with **no formal authority**. Their SE decomposition reveals that the framework does generalise — but only because their apparent absence of authority is actually a substitution: rung-3 evidence (cited sources, working code, test results) replaces rung-1 institutional authority at the centre of the control loop. When that substitution holds, the system is stable; when it slips, the same failure modes appear that the book documents for institutionally authorised systems.

[**→ Interactive D3 Visualization**](../../interactive/wikipedia.html){ .md-button }

## SE Decomposition

The full five-level decomposition is shown in the interactive visualization linked above. The canonical reference is at [`knowledge/system-catalogues/social-systems/wikipedia/se-decomposition.md`](https://github.com/ccabos/systems/blob/main/knowledge/system-catalogues/social-systems/wikipedia/se-decomposition.md).

## Variation Point Bindings

| Variation Point | Binding |
|----------------|---------|
| VP1: Source of Authority | *Tenure + demonstrable contribution* — established editors / committers carry weight in proportion to their visible track record |
| VP2: Membership Boundary | Self-selecting and effectively open; participation gradient from anonymous reader to administrator/maintainer |
| VP3: Decision-Making | "Rough consensus", supplemented by a "Benevolent Dictator For Life" (BDFL) or arbitration committee for unbreakable deadlocks |
| VP4: Succession | Emergent: contributors who sustain quality over time accumulate trust and rights; formal roles ratify what has already happened informally |

**The key structural feature:** authority is *granted by demonstrated contribution measurable against rung-3 standards* (a Wikipedia edit cites sources; a Linux patch must compile and pass tests). The system's distinctiveness in the catalogue is that the rung-3 standard exists *before* any institutional authority is needed to enforce it — the source citation, the unit test, the compilation result, the reproducibility check.

## The Structural Pathology of Rough Consensus

The system's strength is that VP1 cannot be captured by patronage, inheritance, or capital — because the only currency that buys influence is contribution that survives external evaluation. The matching weaknesses are three.

**The tyranny of structurelessness** (Jo Freeman's classic critique of the early women's-liberation movement, applied here): when no formal authority exists, *informal* authority concentrates around individuals whose social-network position, time commitment, and emotional stamina exceeds others'. The early Wikipedia editor with 60,000 edits has accumulated, by tenure alone, an effective veto on consensus calls. The system's claim to operate at rung 6 (open deliberative consensus) is structurally compromised by a rung-1 informal-tenure stratification that consensus calls cannot disentangle from substantive argument.

**Edit wars and the dominance of stamina.** Where rough consensus fails to converge — typically on contested political, religious, or biographical articles — the editor who can outlast the others controls the outcome. Stamina is the rung at which the contest is decided; it has no truth-tracking property. The arbitration committee was created to resolve exactly these cases, but the cases that reach it are the ones where the underlying disagreement is not actually about facts.

**Hostile entry by coordinated minorities.** Open membership combined with consensus-without-counting decision-making is exploitable by coordinated factions whose individual contributions look organic. The pattern is documented across Wikipedia (state-sponsored editing campaigns, paid PR editing), open-source projects (governance takeover attempts), and the early Bitcoin community (governance fork dynamics). The defence — community moderation by experienced editors — collides with the informal-authority pathology above.

These are not failures of community spirit. They are structural consequences of the VP1 binding when the rung-3 standard (verifiable evidence) is contested or absent.

## STPA Highlights

**UCA-W1: Long-tenured editors dominate consensus calls regardless of the substantive merit of contested edits.**

*Causal factor:* the system has no formal mechanism to weight contributions by current relevance vs accumulated tenure. The rung-1 deference to "established editor" interacts with the rough-consensus mechanism such that the consensus call effectively counts the established editor's opinion above newcomers' regardless of the rung-3 evidence either presents.

**UCA-W2: A contested article is controlled by the editor with the most stamina, not the editor with the strongest sources.**

*Causal factor:* the rough-consensus mechanism resolves contested edits by edit-war attrition; the attrition is governed by editor time and stamina, which have no truth-tracking property. The matching failure mode in open-source: maintainer burnout, where the project is captured by whoever is willing to sustain the unpaid review workload.

**UCA-W3: A coordinated minority of editors with hidden coordination wins a consensus call against an uncoordinated majority.**

*Causal factor:* the system's mechanisms cannot reliably distinguish independent editors with similar views from coordinated editors presenting similar views. Where coordination is real and hidden, the consensus call is corrupted; where it is suspected but not proven, the suspicion itself corrupts the call.

**UCA-W4: The "Benevolent Dictator" resigns or burns out, and no succession mechanism is structurally ready to substitute.**

*Causal factor:* VP4 (succession) is emergent rather than statutory. When the BDFL exits suddenly (Python's Guido van Rossum, 2018), the system enters a structurally ambiguous interregnum until a new authority is recognised. The interregnum is a failure window in which contested decisions cannot be settled.

## Fixes That Worked

**Wikipedia's Arbitration Committee — partial fix for UCA-W2 and UCA-W3.**

The Wikipedia ArbCom is an elected body of senior editors empowered to decide cases the consensus mechanism cannot. *Evidence:* the committee has consistently handled the highest-conflict cases (BLP disputes, coordinated-editing investigations, sustained editor conduct) at a rate of dozens per year over two decades. The structural change: a rung-2/6 formal-rule mechanism is installed as a backstop where the rung-6 consensus mechanism fails.

**Mandatory disclosure of paid editing — addressing UCA-W3.**

Wikipedia's 2014 Terms of Use amendment requires disclosure of paid editing affiliation. *Evidence:* the disclosure regime is imperfectly enforced but has shifted significant volumes of paid editing from undisclosed to disclosed, where the community can evaluate it explicitly; high-visibility undisclosed-paid-editing cases now reliably trigger blocks.

**Python PEP 8016 governance transition (2018) — addressing UCA-W4.**

After Guido van Rossum's resignation as BDFL, the Python community executed a structured succession: PEP 8016 established an elected Steering Council, codifying the previously informal authority structure into a statutory one with a fixed term and rotation. *Evidence:* the transition was completed without forking the language; subsequent governance has surfaced and resolved several controversial decisions (typing syntax, packaging, performance) through the new mechanism. The structural change: VP4 was moved from emergent to statutory before the next succession crisis hit.

**Linux kernel maintainer hierarchy — emergent structural defence against UCA-W1 and UCA-W2.**

The kernel project distributes authority across hundreds of subsystem maintainers, each with rung-3 demonstrable competence in a specific component. Linus Torvalds's authority is real but exercised only at the top of a deep delegation tree; no single contested area falls entirely under any one person's exclusive control. *Evidence:* the kernel has scaled to 30+ years and millions of lines without governance crisis, despite many individual flashpoints. The structural feature: VP1 (authority by demonstrated contribution) is *finely distributed* by domain, so the failure modes that appear when authority concentrates in one place cannot accumulate.

!!! example "The Design Principle"
    The wiki / open-source pattern shows that rung-3 evidence (cited sources, working code, reproducible tests) can substitute for rung-1 institutional authority *as long as the substitution holds*. Where the rung-3 standard is contested, absent, or relegated to stamina contests, the same failure modes that the book documents for institutionally authorised systems reappear — and the same fix applies: install a parallel channel (ArbCom, statutory governance, disclosure regime) that catches the cases the rung-3 mechanism cannot. The conclusion is not that "Wikipedia is different"; it is that *every* social system in the catalogue is held together by the rung at which its claims are actually evaluated, and Wikipedia just made the rung explicit.

## Platform Mapping

| Functional Slot | How This System Fills It |
|-----------------|-------------------------|
| Authority & Decision-Making | Rough consensus + BDFL / Steering Council / ArbCom backstop; subsystem maintainers; experienced contributors as informal authorities |
| Membership & Belonging | Self-selecting and effectively open; participation gradient from reader/lurker to admin/maintainer; identity by stable handle |
| Resource Allocation | Volunteer time (primary); foundation budget (Wikimedia, Linux Foundation, PSF) for infrastructure and a thin paid-staff layer |
| Norm Setting & Enforcement | Verifiability/notability rules; code review and commit policy; code of conduct; community moderation; ArbCom |
| Dispute Resolution | Talk-page discussion; informal mediation; ArbCom / Steering Council; in extremis, project fork |
| Legitimation | Demonstrable contribution surviving rung-3 evaluation; cumulative reputation; project usefulness to external users |
| Succession & Continuity | Emergent rights accretion (Wikipedia "rollback", "admin"); statutory transitions (Python PEP 8016); maintainer delegation chains |
| External Representation | Foundation (Wikimedia, Linux Foundation, PSF) as legal entity; project spokespersons; press contacts |
| Socialisation | Onboarding via documentation; mentorship of new contributors; project-specific norms (e.g. "be bold", "rough consensus") |
| Activity Delivery | Article writing and curation; code authoring and review; bug triage; release management; community support |

---

*For the full SE decomposition: [interactive visualization](../../interactive/wikipedia.html). For the comparative analysis across all systems: [Ten Social Systems Compared](../ten-systems.md). For the cross-system control-structure analysis: [Control Structures](../../part4/control-structures.md).*

## Sources

The production mode is Benkler's commons-based peer production (*The Wealth of Networks*, 2006); the structurelessness failure mode is Freeman (1972); Wikipedia's installation of its governance layer is documented in Forte, Larco & Bruckman (2009); and Shaw & Hill's study of 683 wikis (2014) shows Michels' iron law of oligarchy operating even under contribution-based authority. Annotated sources: [`wikipedia/sources.md`](https://github.com/ccabos/systems/blob/main/knowledge/system-catalogues/social-systems/wikipedia/sources.md).
