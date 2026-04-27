# Architectural Remedies — Case Studies

For each of five social systems, STPA identifies unsafe control
actions, traces their causal factors, and derives an architectural
remedy. Where the remedy has been implemented and its effects
measured, that evidence is included. The generic forms of the four
dangerous patterns these remedies address live in
`knowledge/se-techniques/control-structures/dangerous-patterns.md`,
with the rung-specific patterns in
`knowledge/se-techniques/justification-rungs/dangerous-mismatches.md`.

**Reading these remedies as rung-elevation moves.** Most of the
proven remedies below can be re-described as moves that *raise the
operating rung* of a feedback channel. The hierarchy of authority
at the controller end stays at rung 1 (legal, institutional, or
sacred); the corrective channel that previously fed back at rung 1
(internal reports filtered through the same hierarchy) is replaced
or paralleled by a rung-3 channel (independent audit, external
investigation, replicated study, statutory reporting). The
rung-elevation framing is summarised in §6 below; the original
control-structure framing remains the primary lens.

---

## 1. Democracy (Republic)

### Background

The democratic republic is structurally the richest of the ten
systems in this catalogue: more feedback paths, more redundant
control mechanisms, and more explicit separation of authority
than any other. Yet it can fail — and its failures follow
predictable structural patterns. The clearest historical
laboratory is the Weimar Republic (1919–1933), which was formally
democratic, constitutionally sophisticated, and destroyed from
within in under fifteen years.

### Key unsafe control actions

**UCA-D1:** Legislature enacts legislation that dismantles the
constitutional order, and no body can invalidate it.
*Causal factor:* Weimar's constitution contained no mechanism
for judicial review of constitutionality. The Enabling Act of
1933, which transferred legislative power to Hitler's cabinet,
passed through a parliament whose votes were formally valid.

**UCA-D2:** Head of government is removed without a functioning
alternative, enabling emergency rule.
*Causal factor:* Weimar's Article 48 gave the President powers
to rule by decree in emergencies; Article 25 allowed dissolution
of the Reichstag. Fragile coalitions combined with emergency
powers created a structural path from parliamentary deadlock to
authoritarian rule.

**UCA-D3:** A party uses democratic procedures to acquire power
with the declared intent of destroying democracy.
*Causal factor:* The constitution contained no mechanism to
exclude actors whose stated goal was the elimination of the
constitutional order.

**UCA-D4:** The information environment is captured, severing
corrective feedback between government behaviour and electoral
accountability.
*Causal factor:* When the press is controlled by the state or
by single-interest actors, citizens cannot vote against outcomes
they cannot see.

### Architectural remedies and real-world proof

The Federal Republic of Germany, established in 1949, is the
most thoroughly documented attempt to engineer a democracy that
cannot repeat the Weimar failure modes.

| UCA | Weimar failure | Basic Law remedy | Evidence |
|-----|---------------|-----------------|----------|
| UCA-D1 | No judicial review of constitutionality | Bundesverfassungsgericht with power to strike down unconstitutional laws | Court has struck down hundreds of laws; functioned continuously since 1951 |
| UCA-D2 | Easy government collapse + emergency powers | **Constructive vote of no confidence** — a Chancellor can only be removed if the Bundestag simultaneously elects a successor | Invoked only twice (1972, 1983), both appropriately; no government has fallen into a leadership vacuum |
| UCA-D3 | No defence against anti-constitutional parties | Article 21 GG: parties seeking to undermine the free democratic basic order can be banned by the Constitutional Court | SRP (neo-Nazi) banned 1952; KPD banned 1956 |
| UCA-D4 | Centralised or captured press | Public broadcasting (ARD, ZDF) governed by Rundfunkräte — councils of civil society representatives, not government officials | German press freedom index consistently among world's highest |

**Structural lesson.** The Basic Law's designers did not trust
good intentions. They trusted structure. Each remedy addresses
a specific causal factor derived from the Weimar failure
analysis. The result is a democracy that has operated without
interruption for 75 years through reunification, financial
crises, and significant polarisation — not because Germans are
different, but because the control structure is different.

---

## 2. Corporation (For-Profit)

### Background

The corporation's defining feature is its variation-point
binding: VP1 = capital ownership. Authority derives from shares,
not from contribution, expertise, or stake in outcomes. This
produces extraordinary efficiency in capital allocation and
significant structural pathologies wherever the interests of
shareholders, employees, customers, and society diverge.

### Key unsafe control actions

**UCA-C1:** The external auditor certifies financial statements
that are materially false.
*Causal factor:* Arthur Andersen earned $25 million in audit
fees and $27 million in consulting fees from Enron in 2000. The
auditor's revenue depended on maintaining the client
relationship. An auditor who qualifies the accounts loses the
client; one who passes them retains it. The control structure
made accurate auditing financially irrational.

**UCA-C2:** The board approves compensation structures that
reward short-term stock price over long-term value.
*Causal factor:* Options vest over 3–4 years; quarterly earnings
reports create 90-day feedback cycles; executive tenure averages
5 years. The time horizon in the incentive structure is shorter
than the time horizon of the decisions being made.

**UCA-C3:** Employees have no formal authority over decisions
that directly affect them, despite being the system's primary
operators.
*Causal factor:* VP1 = capital ownership means only
shareholders hold formal governance rights. Employees who have
the most accurate process models have no structural channel
through which that knowledge reaches decision-makers.

### Architectural remedies and real-world proof

**Remedy for UCA-C1 — Sarbanes-Oxley Act 2002.**
Section 201 prohibits audit firms from providing most non-audit
services to their audit clients — severing the consulting
revenue incentive. Sections 302/906 require personal
certification of financial statement accuracy by CEO and CFO
under criminal penalty. The Public Company Accounting Oversight
Board (PCAOB) replaces self-regulation with independent
inspection.
*Evidence:* No Enron-scale accounting fraud has recurred in
US-listed companies at comparable magnitude in the 22 years
since SOX. The structural conflict of interest was directly
addressed.

**Remedy for UCA-C2 and UCA-C3 — German co-determination
(Mitbestimmung).**
Germany's Mitbestimmungsgesetz 1976 requires companies with
more than 2,000 employees to give workers equal representation
on the supervisory board (Aufsichtsrat). Worker representatives
bring a different time horizon and operational knowledge that
capital holders structurally lack.
*Evidence:* German DAX companies maintained significantly more
stable employment during the 2008–2009 financial crisis and the
2020 COVID recession than comparable US shareholder-governed
firms, using mechanisms like Kurzarbeit that require worker-
board buy-in. Volkswagen, Siemens, and BASF have maintained
global technological leadership across multi-decade cycles.

**Remedy for UCA-C2 — UK Corporate Governance Code
(post-Cadbury 1992).**
Separation of CEO and Chairman roles; majority independent
non-executive directors on audit, remuneration, and nomination
committees; annual shareholder vote on executive pay.
*Evidence:* UK listed companies report >90% compliance. The
concentration of CEO/Chairman in one person, which enabled
unchecked self-dealing in the Maxwell case, has been
architecturally eliminated as a governance norm.

**Structural lesson.** None of these remedies asks executives
to be more virtuous. They change the structure so the incentives
point in a different direction — severing the auditor's
financial dependence on the auditee, shortening or lengthening
the relevant time horizon, and adding voices with different
interests to the decision room.

---

## 3. Religion

### UCA-R1: Pastoral authority conceals abuse to protect institutional reputation

*Causal factor:* Bishops controlled both pastoral care and
external communication. The authority that received abuse
reports also decided whether to report externally, reassign
perpetrators, or settle quietly. Controller and interested party
were the same entity — the defining accountability void.

**Remedy — mandatory reporting laws superseding institutional
authority.**
Clergy are required by law to report suspected child abuse
directly to civil authorities, regardless of internal
procedures, institutional instruction, or confessional
confidentiality. The legal channel bypasses the institutional
hierarchy.
*Evidence:* Australia's Royal Commission into Institutional
Responses to Child Sexual Abuse (2013–2017) led to mandatory
reporting requirements applying to all clergy across all
Australian states (2017–2019). Ireland passed equivalent
legislation following the Murphy Report (2009). In jurisdictions
with mandatory reporting, institutional concealment becomes a
criminal act — the structural fix changes the cost calculus of
the accountability void from "this protects us" to "this
destroys us."

### UCA-R2: Doctrine becomes self-sealing — the process model at the top cannot be corrected by information from below

*Causal factor:* When doctrinal authority claims divine mandate
(VP1 = divine mandate), the process model is immune to external
correction by design. Errors propagate downward; feedback from
the community is filtered through the same doctrinal lens that
produced the error.

**Remedy — structural opening to external knowledge and lay
participation (Vatican II).**
The Second Vatican Council (1962–1965) introduced lay
participation in liturgy and governance, ecumenical engagement
with other traditions, acknowledgment of modern scholarship's
validity, and explicit recognition that the Church is the whole
people of God.
*Partial evidence:* Vatican II measurably increased doctrinal
updatability in certain domains. However, many of its
structural reforms were partially reversed in subsequent
decades — illustrating that connection-level changes are
unstable without corresponding goal-level commitment. A partial
fix that is subsequently undone is itself a data point: it
shows that the structural analysis was correct (the opening
worked where it was maintained) and that reform requires
sustained commitment at the goals level, not only the
connections level.

---

## 4. University

### Key unsafe control actions

**UCA-U1:** Researchers selectively report positive results,
producing a literature that systematically overestimates effect
sizes and replication rates.
*Causal factor:* Journal publication decisions favour novel,
positive results. Researcher careers depend on publication
count and citation impact. Null results are difficult to
publish and do not advance careers. The 2015 Open Science
Collaboration reproducibility study found only 36% of 100
psychology findings replicated when independently tested.

**UCA-U2:** Research quality is assessed by journal impact
factor rather than by the quality of the work itself.
*Causal factor:* Impact factor is measurable and comparable;
research quality requires domain expertise to assess.
Administrators use impact factor as a proxy — the classic
proxy-metric failure.

### Architectural remedies and real-world proof

**Remedy for UCA-U1 — pre-registration and Registered Reports.**
Researchers publicly commit to their hypotheses, methods, and
analysis plan *before* data collection begins. With Registered
Reports, a journal reviews and accepts the study design before
results are known — committing to publish regardless of outcome.
The publication decision is structurally decoupled from the
result.
*Evidence:* The Center for Open Science hosts over 100,000
pre-registrations. Registered Reports are offered by more than
300 journals across disciplines. Pre-registered studies
replicate at substantially higher rates than non-pre-registered
work.

**Remedy for UCA-U2 — DORA and article-level assessment.**
The San Francisco Declaration on Research Assessment (DORA,
2013) is a commitment by over 20,000 researchers and 2,000
organisations to evaluate research on its own merits, not by
journal impact factor. The UK Research Excellence Framework has
moved toward article-level panel assessment. The Netherlands
introduced a Recognition and Rewards framework in 2021
replacing publication metrics with broader criteria including
teaching, open science practice, and societal engagement.
*Evidence:* Early but directional. Wherever the proxy metric is
disconnected from the reward structure, behaviour changes.

---

## 5. Military (Civilian Control)

### Key unsafe control actions

**UCA-M1:** Military command undertakes operations without
civilian authorisation.
*Causal factor:* Civilian oversight structures frequently lack
accurate operational information. Intelligence and operational
reports pass through the military hierarchy — the same chain of
command that has institutional incentives to portray operations
favourably.

**UCA-M2:** Military justice is administered by the same
command whose conduct is under investigation.
*Causal factor:* When commanding officers control military
prosecution, the commanding officer is simultaneously the
authority who can suppress investigation and the party whose
institutional reputation is affected by its outcome. Controller
and interested party are the same entity.

### Architectural remedies and real-world proof

**Remedy for UCA-M1 — mandatory parliamentary authorisation and
independent inspection (German Bundeswehr model).**
All deployments of German armed forces outside German territory
require a Bundestag vote — including humanitarian missions. The
Wehrbeauftragter (Parliamentary Commissioner for the Armed
Forces) has independent access to any unit, any file, and any
individual soldier. No command authority can block an
inspection. The Commissioner reports to the Bundestag, not to
the Defence Ministry.
*Evidence:* Germany has maintained continuous, uninterrupted
civilian control of its military since 1955. The
Wehrbeauftragter has regularly surfaced structural problems
(equipment failures, morale crises, right-wing extremism in
units) that command had institutional incentive to conceal.

**Remedy for UCA-M2 — independent military prosecution
(US NDAA 2022).**
The National Defense Authorization Act 2022 transferred
jurisdiction over sexual assault, murder, and other serious
felonies from commanding officers to independent Special Trial
Counsel — removing the commanding officer from the prosecution
decision entirely.
*Evidence:* Sexual assault reporting rates in the US military
increased following the reform. Early data shows increased
prosecution rates for referred cases.

---

## Cross-system pattern

Across all five systems, the same structural failure recurs in
different forms:

| Failure type | Democracy | Corporation | Religion | University | Military |
|---|---|---|---|---|---|
| **Accountability void** | No review of constitutionality | Auditor depends on auditee | Bishop investigates own clergy | Peers review competitors | Command investigates own conduct |
| **Self-sealing process model** | State controls information | Management controls board agenda | Doctrine claims divine authority | Null results unpublishable | Intelligence filtered by hierarchy |
| **Proxy metric replaces goal** | Electoral wins replace democratic health | Quarterly EPS replaces long-term value | Institutional reputation replaces pastoral care | Impact factor replaces research quality | Compliance metrics replace readiness |
| **Proven remedy** | Basic Law: Constitutional Court + constructive confidence vote | SOX + Mitbestimmung + Cadbury | Mandatory reporting laws | Pre-registration + DORA | Parliamentary mandate + independent inspector |

The remedies are not generic. Each closes a specific causal
pathway identified by structural analysis — and each has been
tested in practice. That precision is what distinguishes
architectural reform from exhortation.

---

## Rung-elevation perspective

The same five families of remedy can be re-described as moves on
the **justificatory-rung ladder** (see
`knowledge/se-techniques/justification-rungs/`). Each remedy
preserves the controller's authority at rung 1 (legal,
institutional, or sacred) but installs a feedback channel that
operates at a higher rung — typically rung 3 (independent
empirical evidence) — and routes around the rung-1 filter that
previously distorted the upward signal.

| Remedy | Pre-remedy feedback rung | Post-remedy feedback rung | What the new channel adds |
|--------|-------------------------|---------------------------|---------------------------|
| Bundesverfassungsgericht (Basic Law) | 1 (parliamentary majority self-judges) | 2/6 (legal-rational + constitutional principle) | Legal consistency check independent of the legislative majority |
| Constructive vote of no confidence | 0/1 (raw arithmetic of confidence motions) | 2 (formal-procedural test) | Cannot remove without alternative — internal consistency requirement |
| Article 21 GG party ban | 1 (politics) | 2/6 (legal-rational + constitutional principle) | Constitutional limit on rung-1 majority politics |
| Public broadcasting under Rundfunkräte | 1 (state press) | 3 (civil-society pluralist channels) | Independent rung-3 information flow to electorate |
| Sarbanes-Oxley external audit | 1 (management self-reports) | 3 (audited financials with criminal liability) | External rung-3 channel that bypasses management filter |
| Mitbestimmung worker board representation | 1 (management self-reviews) | 6 (deliberative — multiple stakeholder perspectives at the board) | Stakeholder-deliberation channel inside governance |
| UK Cadbury / Corporate Governance Code | 1 (board self-defines independence) | 2/3 (formal independence test, comply-or-explain disclosure) | Externally readable rung-2/3 record of board composition |
| Mandatory abuse reporting (Religion) | 1 (clergy report internally) | 3 (statutory report to civil authority) | Civil authority's rung-3 investigation bypasses doctrinal filter |
| Vatican II lay councils | 1 (clerical hierarchy) | 1+2 (lay participation, doctrinal-procedural openness) | Partial rung elevation in doctrinal feedback; partially reversed in subsequent decades |
| Pre-registration and Registered Reports | 3 (publication-biased sample of trials) | 4 (cumulative evidence with no publication-bias filter) | Rung-3 channel hardened to rung 4 by removing the gatekeeping filter |
| DORA / article-level assessment | 1 (journal prestige proxy) | 3 (article-level merit) | Replaces rung-1 proxy with rung-3 evaluation of the work itself |
| Parliamentary mandate (German Bundeswehr) | 0/1 (executive decision) | 6 (parliamentary deliberation) | Civilian rung-6 deliberation precedes military rung-0/1 action |
| Wehrbeauftragter (independent military prosecutor) | 1 (commander investigates own troops) | 3 (independent investigation) | Rung-3 conduct feedback bypasses chain of command |

**Pattern.** All thirteen remedies share a common architecture:

1. The original loop transmits commands at rung 1 (the
   institution's natural authority rung) but its feedback channel
   is captured by the same rung-1 hierarchy.
2. The remedy *does not* try to convert the controller to a higher
   rung — that would dissolve the institution.
3. Instead, the remedy *parallels* the rung-1 channel with a new
   rung-3 (or rung-2/6) channel that routes feedback to a separate
   oversight body whose existence is independent of the
   controller.

This is the canonical fix for **Pattern A — Asymmetric Loop** in
`knowledge/se-techniques/justification-rungs/dangerous-mismatches.md`.
Where the remedy has been incomplete (Vatican II partially
reversed) it is because the rung-elevated channel was made
revocable by the same rung-1 hierarchy it was supposed to
correct — which is the precondition for remedies that the
control-structure technique already requires (see "Remedy
preconditions" in
`knowledge/se-techniques/control-structures/dangerous-patterns.md`).
