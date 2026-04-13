# Architectural Remedies

## The Analysis Generates the Fix

The introduction to this book used a secondary school to illustrate how structural analysis works: once you have traced *which feedback loop is misconfigured* and *why*, you know exactly which connection to change. Finland changed those connections and the outcomes changed with them.

This chapter applies the same logic across five social systems. For each, STPA identifies the unsafe control actions, traces their causal factors, and derives the architectural remedy. Where a remedy has been implemented and its effects measured, that evidence is included. The aim is to show that STPA is a design method — not merely a diagnostic — and that its prescriptions are testable.

---

## 1. Democracy (Republic)

### Background

The democratic republic is structurally the richest of the ten systems analysed in this book: it has more feedback paths, more redundant control mechanisms, and more explicit separation of authority than any other. Yet it can fail — and its failures follow predictable structural patterns. The clearest historical laboratory is the Weimar Republic (1919–1933), which was formally democratic, constitutionally sophisticated, and destroyed from within in under fifteen years.

### Key Unsafe Control Actions

**UCA-D1: Legislature enacts legislation that dismantles the constitutional order, and no body can invalidate it.**

*Causal factor:* Weimar's constitution contained no mechanism for judicial review of constitutionality. The Reichstag could legally pass laws that undermined the constitution itself. The Enabling Act of 1933, which transferred legislative power to Hitler's cabinet, passed through a parliament whose votes were formally valid. There was no circuit breaker.

**UCA-D2: Head of government is removed without a functioning alternative, enabling emergency rule.**

*Causal factor:* Weimar's Article 48 gave the President powers to rule by decree in emergencies; Article 25 allowed the President to dissolve the Reichstag. Fragile coalitions that fell easily, combined with executive emergency powers, created a structural path from parliamentary deadlock to authoritarian rule. Fourteen chancellors in fourteen years exhausted the system.

**UCA-D3: A political party uses democratic procedures to acquire power with the declared intent of destroying democracy.**

*Causal factor:* The constitution contained no mechanism to exclude actors whose stated goal was the elimination of the constitutional order. The system's openness provided no defence against participants who intended to close it permanently.

**UCA-D4: The information environment is captured, severing corrective feedback between government behaviour and electoral accountability.**

*Causal factor:* When the press is controlled by the state or by actors with a single political interest, citizens cannot vote against outcomes they cannot see.

### Architectural Remedies and Real-World Proof

The Federal Republic of Germany, established in 1949, is the most thoroughly documented attempt to engineer a democracy that cannot repeat the Weimar failure modes. Its designers — working explicitly from the structural analysis of what went wrong — made the following changes:

| UCA | Weimar failure | Basic Law remedy | Evidence |
|-----|---------------|-----------------|----------|
| UCA-D1 | No judicial review of constitutionality | Bundesverfassungsgericht with power to strike down unconstitutional laws | Court has struck down hundreds of laws; functioned continuously since 1951 |
| UCA-D2 | Easy government collapse + emergency powers | **Constructive vote of no confidence** — a Chancellor can only be removed if the Bundestag simultaneously elects a successor | Invoked only twice (1972, 1983), both appropriately; no government has fallen into a leadership vacuum |
| UCA-D3 | No defence against anti-constitutional parties | Article 21 GG: parties seeking to undermine the free democratic basic order can be banned by the Constitutional Court | SRP (neo-Nazi) banned 1952; KPD banned 1956; mechanism functions as credible structural deterrent |
| UCA-D4 | Centralised or captured press | Public broadcasting (ARD, ZDF) governed by Rundfunkräte — councils of civil society representatives, not government officials | German press freedom index consistently among world's highest; public broadcasting financially independent of government |

!!! abstract "The Structural Lesson"
    The Basic Law's designers did not trust good intentions. They trusted structure. Each remedy addresses a specific causal factor derived from the Weimar failure analysis. The result is a democracy that has operated without interruption for 75 years through reunification, financial crises, and significant polarisation — not because Germans are different, but because the control structure is different.

---

## 2. Corporation (For-Profit)

### Background

The corporation's defining structural feature is its variation-point binding: VP1 = capital ownership. Authority derives from shares, not from contribution, expertise, or stake in outcomes. This produces extraordinary efficiency in capital allocation and significant structural pathologies wherever the interests of shareholders, employees, customers, and society diverge.

### Key Unsafe Control Actions

**UCA-C1: The external auditor certifies financial statements that are materially false.**

*Causal factor:* Arthur Andersen earned $25 million in audit fees and $27 million in consulting fees from Enron in 2000. The auditor's revenue depended on maintaining the client relationship. An auditor who qualifies the accounts loses the client; one who passes them retains it. The control structure made accurate auditing financially irrational. Enron's collapse destroyed $74 billion in shareholder value and 20,000 jobs.

**UCA-C2: The board approves compensation structures that reward short-term stock price over long-term value.**

*Causal factor:* Options vest over 3–4 years; quarterly earnings reports create 90-day feedback cycles; executive tenure averages 5 years. The time horizon encoded in the incentive structure is shorter than the time horizon of the decisions being made. Executives are rationally rewarded for actions — leveraged acquisitions, aggressive accounting, capacity-depleting cost cuts — whose full consequences materialise after they have left.

**UCA-C3: Employees have no formal authority over decisions that directly affect them, despite being the system's primary operators.**

*Causal factor:* VP1 = capital ownership means only shareholders hold formal governance rights. Employees who have the most accurate process models — who know which cuts will destroy quality, which acquisitions will fail to integrate — have no structural channel through which that knowledge reaches decision-makers.

### Architectural Remedies and Real-World Proof

**Remedy for UCA-C1: Sarbanes-Oxley Act 2002**

The US Sarbanes-Oxley Act, passed after Enron and WorldCom, made these structural changes:

- Section 201: Prohibits audit firms from providing most non-audit services to their audit clients — severing the consulting revenue incentive that corrupted the auditor's independence.
- Sections 302/906: CEO and CFO must personally certify financial statement accuracy under criminal penalty.
- Established the Public Company Accounting Oversight Board (PCAOB) — an independent inspectorate replacing self-regulation.

*Evidence:* No Enron-scale accounting fraud has recurred in US-listed companies at comparable magnitude in the 22 years since SOX. The structural conflict of interest that made Enron possible was directly addressed. The fix is structural, not absolute — smaller cases persist — but the most dangerous accountability void was closed.

**Remedy for UCA-C2 and UCA-C3: German co-determination (Mitbestimmung)**

Germany's Mitbestimmungsgesetz 1976 requires companies with more than 2,000 employees to give workers equal representation on the supervisory board (Aufsichtsrat). Worker representatives bring a different time horizon — employment stability, long-term skill investment — and carry operational knowledge that capital holders structurally lack.

*Evidence:* German DAX companies maintained significantly more stable employment during the 2008–2009 financial crisis and the 2020 COVID recession than comparable US shareholder-governed firms, using mechanisms like Kurzarbeit (short-time work) that require worker-board buy-in. German industrial companies have sustained R&D investment cycles measured in decades. Volkswagen, Siemens, and BASF — all with co-determined boards — have maintained global technological leadership across multi-decade cycles despite cyclical downturns that felled less structurally grounded competitors.

**Remedy for UCA-C2: UK Corporate Governance Code (post-Cadbury 1992)**

Following corporate scandals (Maxwell, BCCI, Polly Peck), the UK Cadbury Report made mandatory:
- Separation of CEO and Chairman roles
- Majority independent non-executive directors on audit, remuneration, and nomination committees
- Annual shareholder vote on executive pay (say-on-pay)

*Evidence:* UK listed companies report >90% compliance. The concentration of CEO/Chairman in one person — which enabled unchecked self-dealing in the Maxwell case — has been architecturally eliminated as a governance norm.

!!! abstract "The Structural Lesson"
    None of these remedies asks executives to be more virtuous. They change the structure so that the incentives point in a different direction — severing the auditor's financial dependence on the auditee, shortening or lengthening the relevant time horizon, and adding voices with different interests to the decision room.

---

## 3. Religion

The full STPA analysis of religion is in the [dedicated chapter](religion-stpa.md). Two remedies with real-world implementation records merit attention here.

### UCA-R1: Pastoral authority conceals abuse to protect institutional reputation

*Causal factor:* Bishops controlled both pastoral care and external communication. The authority that received abuse reports also decided whether to report externally, reassign perpetrators, or settle quietly. Controller and interested party were the same entity — the defining accountability void.

**Remedy: Mandatory reporting laws superseding institutional authority**

Clergy are required by law to report suspected child abuse directly to civil authorities, regardless of internal procedures, institutional instruction, or confessional confidentiality. The legal channel bypasses the institutional hierarchy.

*Evidence:* Australia's Royal Commission into Institutional Responses to Child Sexual Abuse (2013–2017) led to mandatory reporting requirements applying to all clergy across all Australian states (2017–2019). Ireland passed equivalent legislation following the Murphy Report (2009). In jurisdictions with mandatory reporting, institutional concealment becomes a criminal act — the structural fix changes the cost calculus of the accountability void from "this protects us" to "this destroys us."

### UCA-R2: Doctrine becomes self-sealing — the process model at the top cannot be corrected by information from below

*Causal factor:* When doctrinal authority claims divine mandate (VP1 = divine mandate), the process model is immune to external correction by design. Errors propagate downward; feedback from the community is filtered through the same doctrinal lens that produced the error.

**Remedy: Structural opening to external knowledge and lay participation (Vatican II)**

The Second Vatican Council (1962–1965) introduced: lay participation in liturgy and governance, ecumenical engagement with other traditions, acknowledgment of modern scholarship's validity, and explicit recognition that the Church is the whole people of God, not only its hierarchy.

*Partial evidence:* Vatican II measurably increased doctrinal updatability in certain domains. However, many of its structural reforms were partially reversed in subsequent decades — illustrating the book's core point about connection-level changes being unstable without corresponding goal-level commitment. The remedy is real; its implementation was incomplete. A partial fix that is subsequently undone is itself a data point: it shows that the structural analysis was correct (the opening worked where it was maintained) and that reform requires sustained commitment at the goals level, not only the connections level.

---

## 4. University

### Key Unsafe Control Actions

**UCA-U1: Researchers selectively report positive results, producing a literature that systematically overestimates effect sizes and replication rates.**

*Causal factor:* Journal publication decisions favour novel, positive results. Researcher careers depend on publication count and citation impact. Null results are difficult to publish and do not advance careers. Selective reporting is individually rational and collectively destructive. The 2015 Open Science Collaboration reproducibility study found only 36% of 100 psychology findings replicated when independently tested — a direct measurement of the structural damage.

**UCA-U2: Research quality is assessed by journal impact factor rather than by the quality of the work itself.**

*Causal factor:* Impact factor is measurable and comparable; research quality requires domain expertise to assess. Administrators use impact factor as a proxy — the same proxy-metric failure as the school grading example. This rewards publication in prestigious journals over doing important work, and incentivises gaming the metric through citation cartels, safe incremental topics, and result-sculpting.

### Architectural Remedies and Real-World Proof

**Remedy for UCA-U1: Pre-registration and Registered Reports**

Researchers publicly commit to their hypotheses, methods, and analysis plan *before* data collection begins. With Registered Reports, a journal reviews and accepts the study design before results are known — committing to publish regardless of outcome. The publication decision is structurally decoupled from the result.

*Evidence:* The Center for Open Science hosts over 100,000 pre-registrations. Registered Reports are offered by more than 300 journals across disciplines. Pre-registered studies replicate at substantially higher rates than non-pre-registered work. This is a structural fix with a directly measurable effect: changing the connection between "result" and "publication decision" changes researcher behaviour and the quality of published knowledge.

**Remedy for UCA-U2: DORA and article-level assessment**

The San Francisco Declaration on Research Assessment (DORA, 2013) is a commitment by over 20,000 researchers and 2,000 organisations to evaluate research on its own merits, not by journal impact factor. The UK Research Excellence Framework has moved toward article-level panel assessment. The Netherlands introduced a Recognition and Rewards framework in 2021 explicitly replacing publication metrics with broader criteria including teaching, open science practice, and societal engagement.

*Evidence:* Still early, but directional. Wherever the proxy metric is disconnected from the reward structure, the behaviour changes. The DORA movement represents the academic community's own diagnosis of its control structure failure and its attempt to fix it through structural commitment rather than exhortation.

---

## 5. Military (Civilian Control)

### Key Unsafe Control Actions

**UCA-M1: Military command undertakes operations without civilian authorisation.**

*Causal factor:* Civilian oversight structures frequently lack accurate operational information. Intelligence and operational reports pass through the military hierarchy — the same chain of command that has institutional incentives to portray operations favourably. The process model at the civilian level is populated by the actors being overseen, making accurate oversight structurally difficult even when civilian authority is formally intact.

**UCA-M2: Military justice is administered by the same command whose conduct is under investigation.**

*Causal factor:* When commanding officers control military prosecution, the commanding officer is simultaneously the authority who can suppress investigation and the party whose institutional reputation is affected by its outcome. Controller and interested party are the same entity.

### Architectural Remedies and Real-World Proof

**Remedy for UCA-M1: Mandatory parliamentary authorisation and independent inspection (German Bundeswehr model)**

All deployments of German armed forces outside German territory require a Bundestag vote — including humanitarian missions. The Wehrbeauftragter (Parliamentary Commissioner for the Armed Forces) has independent access to any unit, any file, and any individual soldier. No command authority can block an inspection. The Commissioner reports to the Bundestag, not to the Defence Ministry.

*Evidence:* Germany has maintained continuous, uninterrupted civilian control of its military since 1955 — across reunification, Cold War deployments, and international operations. The Wehrbeauftragter has regularly surfaced structural problems (equipment failures, morale crises, right-wing extremism in units) that command had institutional incentive to conceal, triggering reforms that would not have occurred through the hierarchy alone. This is the feedback mechanism functioning as designed.

**Remedy for UCA-M2: Independent military prosecution (US NDAA 2022)**

The National Defense Authorization Act 2022 transferred jurisdiction over sexual assault, murder, and other serious felonies from commanding officers to independent Special Trial Counsel — removing the commanding officer from the prosecution decision entirely.

*Evidence:* Sexual assault reporting rates in the US military increased following the reform. The structural conflict of interest — a commanding officer deciding whether to prosecute a subordinate for an offence reflecting on the command's culture — was identified through sustained advocacy using exactly the structural argument this book makes, and directly addressed. Early data shows increased prosecution rates for referred cases.

---

## Cross-System Pattern

Across all five systems, the same structural failure recurs in different forms:

| Failure type | Democracy | Corporation | Religion | University | Military |
|---|---|---|---|---|---|
| **Accountability void** | No review of constitutionality | Auditor depends on auditee | Bishop investigates own clergy | Peers review competitors | Command investigates own conduct |
| **Self-sealing process model** | State controls information | Management controls board agenda | Doctrine claims divine authority | Null results unpublishable | Intelligence filtered by hierarchy |
| **Proxy metric replaces goal** | Electoral wins replace democratic health | Quarterly EPS replaces long-term value | Institutional reputation replaces pastoral care | Impact factor replaces research quality | Compliance metrics replace readiness |
| **Proven remedy** | Basic Law: Constitutional Court + constructive confidence vote | SOX + Mitbestimmung + Cadbury | Mandatory reporting laws | Pre-registration + DORA | Parliamentary mandate + independent inspector |

The remedies are not generic. Each closes a specific causal pathway identified by the structural analysis — and each has been tested in practice. That precision is what distinguishes architectural reform from exhortation.
