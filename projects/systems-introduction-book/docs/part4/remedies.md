# Architectural Remedies

## The Analysis Generates the Fix

The introduction to this book used a secondary school to illustrate how structural analysis works: once you have traced *which feedback loop is misconfigured* and *why*, you know exactly which connection to change. Finland changed those connections and the outcomes changed with them.

This chapter applies the same logic across five social systems. For each, STPA identifies the unsafe control actions, traces their causal factors, and derives the architectural remedy. Where a remedy has been implemented and its effects measured, that evidence is included. The aim is to show that STPA is a design method — not merely a diagnostic — and that its prescriptions are testable.

!!! info "Canonical reference"
    The full case studies — unsafe control actions, causal factors, remedies, and the real-world evidence for each — are in `knowledge/system-catalogues/social-systems/cross-system/remedies-case-studies.md`. This chapter gives a narrative walk-through of the five worked cases; the knowledge file is the reference.

---

## The Five Worked Cases

### 1. Democracy (Republic) — the Weimar → Basic Law transition

The Weimar Republic (1919–1933) was formally democratic, constitutionally sophisticated, and destroyed from within in under fifteen years. Its failures — no judicial review of constitutionality, an emergency-powers path from parliamentary deadlock to authoritarian rule, no defence against anti-constitutional parties, and a capturable information environment — map onto four specific unsafe control actions.

The Federal Republic of Germany's Basic Law (1949) addressed each of them: the Bundesverfassungsgericht with power to strike down laws; the constructive vote of no confidence, which lets a Chancellor be removed only by simultaneously electing a successor; Article 21 GG allowing the Constitutional Court to ban parties seeking to undermine the free democratic basic order; and public broadcasting governed by civil-society councils rather than government officials. The result is a democracy that has operated without interruption for 75 years — not because Germans are different, but because the control structure is different.

### 2. Corporation — Sarbanes-Oxley, Mitbestimmung, and Cadbury

The corporation's defining structural feature is that authority derives from capital ownership. The three characteristic failures are: auditor dependence on the audited client, short-term compensation structures that outlive their consequences, and employee exclusion from governance despite holding the most accurate operational process models.

Three remedies, each tested in practice: Sarbanes-Oxley severed the auditor's consulting revenue from the audited client and made financial statement accuracy a personal criminal-liability matter for CEOs and CFOs. German co-determination (Mitbestimmung) placed worker representatives on supervisory boards of companies with more than 2,000 employees, bringing a different time horizon into the decision room. The UK Cadbury Code separated CEO and Chairman roles and required independent non-executive directors on key committees. None of the three asks executives to be more virtuous; each changes the structure so that the incentives point in a different direction.

### 3. Religion — mandatory reporting and Vatican II

Where bishops controlled both pastoral care and external communication, the authority that received abuse reports also decided whether to report externally. Mandatory reporting laws — enacted in Australia after the 2013–2017 Royal Commission, in Ireland after the 2009 Murphy Report, and elsewhere — bypass the institutional hierarchy by legal channel, changing the cost calculus of concealment from "this protects us" to "this destroys us."

The self-sealing property of doctrinal authority is harder to fix. The Second Vatican Council (1962–1965) was a structural opening to lay participation, ecumenical engagement, and modern scholarship. Its reforms were partially reversed in subsequent decades — itself a data point: the opening worked where it was maintained, showing the structural analysis was correct, and showing that reform requires sustained commitment at the goals level, not only the connections level.

### 4. University — pre-registration, Registered Reports, and DORA

Two failures dominate: selective reporting of positive results (the replication crisis: only 36% of psychology findings replicated in the 2015 Open Science Collaboration study), and impact-factor substitution for research quality (the classic proxy-metric failure).

The structural fixes: pre-registration and Registered Reports decouple the publication decision from the result, so that researchers commit to hypotheses, methods, and analysis plans before data collection. The Center for Open Science now hosts over 100,000 pre-registrations, and more than 300 journals offer Registered Reports. Pre-registered studies replicate at substantially higher rates. DORA and the UK REF's move toward article-level panel assessment disconnect the reward structure from the specific proxy metric. Both fixes change the connection between "result" and "consequence for the researcher" — and behaviour changes accordingly.

### 5. Military — parliamentary authorisation and independent prosecution

German armed forces cannot be deployed outside German territory without a Bundestag vote. The Wehrbeauftragter — the Parliamentary Commissioner for the Armed Forces — has independent access to any unit, any file, and any individual soldier, and reports directly to the Bundestag rather than the Defence Ministry. Germany has maintained continuous civilian control of its military since 1955; the Commissioner has regularly surfaced structural problems that command had institutional incentive to conceal.

For military justice, the US National Defense Authorization Act 2022 transferred jurisdiction over sexual assault and other serious felonies from commanding officers to independent Special Trial Counsel, removing the commanding officer from the prosecution decision entirely. Reporting rates rose; prosecution rates for referred cases rose. The structural conflict of interest — commanding officer deciding whether to prosecute conduct that reflects on the command — was identified through sustained advocacy using exactly the structural argument this book makes, and directly addressed.

---

## Cross-System Pattern

Across all five systems, the same three structural failures recur: an accountability void, a self-sealing process model, and a proxy metric that has replaced the goal. The full cross-system table — failure type by system, with each proven remedy mapped to the corresponding control-loop fix — is in `knowledge/system-catalogues/social-systems/cross-system/remedies-case-studies.md`.

The remedies are not generic. Each closes a specific causal pathway identified by the structural analysis — and each has been tested in practice. That precision is what distinguishes architectural reform from exhortation.

## Reading the Remedies as Rung-Elevation Moves

The previous chapter introduced the seven [Justificatory Rungs](../part1/justification-rungs.md) and the dangerous **Pattern A — Asymmetric Loop**: rung-1 control downward with rung-3 evidence trying, and failing, to feed back upward. Re-read through that lens, **all thirteen catalogued architectural remedies share a common move**: the controller's authority remains at rung 1 (legal, institutional, or sacred); a *parallel* feedback channel is installed that operates at rung 3 (independent audit, statutory investigation, replicated study, criminal-liability disclosure); and the new channel routes around the rung-1 hierarchy that previously filtered upward signal.

| Remedy | Pre-remedy feedback rung | Post-remedy feedback rung |
|--------|-------------------------|---------------------------|
| Bundesverfassungsgericht (Basic Law) | 1 (parliamentary self-judgment) | 2/6 (legal-rational + constitutional principle) |
| Sarbanes-Oxley external audit | 1 (management self-reports) | 3 (audited financials with criminal liability) |
| Mitbestimmung worker board representation | 1 (management self-reviews) | 6 (deliberative — multiple stakeholder perspectives) |
| Mandatory abuse reporting (Religion) | 1 (clergy report internally) | 3 (statutory report to civil authority) |
| Vatican II lay councils | 1 (clerical hierarchy) | 1+2 (lay participation; partially reversed) |
| Pre-registration / Registered Reports | 3 (publication-biased trial sample) | 4 (cumulative evidence without publication-bias filter) |
| DORA / article-level assessment | 1 (journal prestige proxy) | 3 (article-level merit) |
| Parliamentary mandate (Bundeswehr) | 0/1 (executive decision) | 6 (parliamentary deliberation) |
| Wehrbeauftragter (independent military prosecutor) | 1 (commander investigates own troops) | 3 (independent investigation) |

The full thirteen-remedy table with detailed deltas is in `knowledge/system-catalogues/social-systems/cross-system/remedies-case-studies.md` §6.

**The remedies do not try to convert rung-1 controllers to higher rungs** — that would dissolve the institution they protect. They *parallel* the rung-1 channel with a rung-3 (or rung-2/6) channel routed to a separate oversight body whose existence does not depend on the controller. Where remedies have been incomplete (Vatican II's partial post-Council reversal) it is because the rung-elevated channel was made revocable by the same rung-1 hierarchy it was supposed to correct — which is the precondition this book's structural fixes already require.

This is the canonical architectural pattern for repairing **Pattern A — Asymmetric Loop** in the social-systems catalogue. It is the unifying idea behind the apparently disparate reforms above.
