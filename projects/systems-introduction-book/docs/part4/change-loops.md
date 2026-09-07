# Installing the Remedy

## The question the last chapter leaves open

Every remedy in the previous chapter exists because somebody installed it. The Bundesverfassungsgericht did not follow from the analysis of Weimar's failure; it followed from a constituent assembly writing it into a constitution. Sarbanes-Oxley did not follow from understanding the auditor's conflict of interest — that had been understood for decades — it followed from a session of the United States Congress.

Structural analysis says which connection to change. It does not say who can change it, how long the change takes to bite, or whether the person who ordered it will still be in office when it does. Between "this is the correct fix" and "this fix is in force" lies a second control loop, and this book has said nothing about it until now.

That gap has a practical cost. An analysis that ends at the remedy produces a recommendation whose installability is untested — which is precisely the shape of a reform proposal that is agreed by everyone and never happens.

!!! info "Canonical reference"
    The technique — the lever inventory, five diagnostic questions, and two failure patterns — is in [`knowledge/se-techniques/change-loops/`](https://github.com/ccabos/systems/tree/main/knowledge/se-techniques/change-loops). The cross-system actuator analysis this chapter draws on is in [`knowledge/system-catalogues/social-systems/cross-system/change-loops-by-system.md`](https://github.com/ccabos/systems/blob/main/knowledge/system-catalogues/social-systems/cross-system/change-loops-by-system.md), and the full lever inventory for the corporation is in [`knowledge/system-catalogues/social-systems/corporation/change-loop-analysis.md`](https://github.com/ccabos/systems/blob/main/knowledge/system-catalogues/social-systems/corporation/change-loop-analysis.md).

---

## Two loops, not one

Everything in this book so far has described the **operating loop**: a controller issues instructions, a process responds, feedback returns. The loop that *changes* that loop is a different object, because it acts on something else.

| Loop | Controller | What it acts on | When feedback arrives |
|------|-----------|-----------------|----------------------|
| **Operating** | The institution's controllers | The world — cases decided, patients treated, students taught | Continuously |
| **Change** | Whoever wants the institution to behave differently | The institution's own rules | Much later |

The change loop acts on rules, and as [Part I](../part1/what-is-a-system.md) sets out, an organisation's rules are not descriptions of its connections — they *are* its connections, written down. A statute, a tenure regime, a signature limit is physical in form and a connection in function. That is what makes the change loop a distinct object rather than a figure of speech: the operating loop acts *through* the connections, the change loop acts *on* them.

## The assumption that breaks

STPA assumes that a controller holds the control actions it issues. For an autopilot this is true: it commands the elevator directly. For institutions it is false for exactly the reform-relevant actions. A head of government does not hold building law or a municipal authority's case handling. A chief executive does not hold the remuneration structure alone. A bishop does not hold the criminal code.

So a change loop is characteristically one in which the controller must first pass through *other* controllers who hold the lever. Analysing it means naming them — the step that ordinary reform talk skips, and the step at which most reform proposals turn out to be requests rather than decisions.

## What you write down

For each lever that could produce the intended outcome: **who signs** (not who is responsible — who signs), **how long until the rule is in force**, **how long after that until anything is observable**, and **who loses** a competence, a budget, or a certainty. Then one figure for the controller: **how long it will be in post.**

Separating the two latencies is not pedantry. Funding training places is decided in weeks and shows in years. Amending a statutory deadline is the reverse. They are different blockages, they take different remedies, and a single figure cannot tell them apart. Latencies here are orders of magnitude, not measurements; the guard against dressing them up as data is the [false-precision trap](https://github.com/ccabos/systems/blob/main/knowledge/se-techniques/linear-algebra/false-precision-trap.md).

## When the feedback outlives the controller

Add the change latency to the effect latency and set the total against the controller's time in post. Where the effect horizon is longer, the controller never receives feedback on its own instruction. The loop is open — not because a channel is missing, but because nobody who issued the action is still there when the signal returns.

This yields a prediction rather than a complaint. Every controller optimises for signals that return inside its own horizon. Short latency and visible output belong to an institution's *parts* — a new agency, new staff, a new portal. Long latency and invisible output belong to its *rules*. A structure of short-tenure controllers will therefore reliably produce part-changes offered as rule-changes: institutions that acquire the form of a reform without its function. Development economists call this **isomorphic mimicry**, and it is normally reported as an empirical regularity. The change loop derives it from loop structure. It is what this arrangement produces, not a failure of character in the people occupying it.

The corporation supplies the sharpest instance, and this book recorded it before the pattern had a name: the causal factor behind its compensation failure is that "the time horizon in the incentive structure is shorter than the time horizon of the decisions being made". Four clocks run at once — a ninety-day reporting cycle, three-to-four-year option vesting, five-year average executive tenure, and capital decisions whose consequences outlast all three.

---

## Who installed the thirteen remedies

Ask the actuator question of the previous chapter's own material, and a cross-system result appears that none of the individual case studies states.

Of the thirteen architectural remedies catalogued in this book, **twelve were installed by an actuator outside the control structure they repair.** Legislatures installed Sarbanes-Oxley, co-determination, mandatory abuse reporting, the parliamentary deployment mandate and the Wehrbeauftragter. A committee working through exchange listing rules installed the Cadbury reforms. Journals, funders and learned societies installed pre-registration and article-level assessment. A constituent assembly installed the Basic Law's three constitutional remedies, and Länder legislatures the broadcasting councils.

The thirteenth is Vatican II — a council convoked by the Church's own hierarchy, the one remedy in the catalogue installed from inside the structure it was meant to correct. It is also the one the catalogue records as **partially reversed in subsequent decades.**

That is not an observation about the Catholic Church. It is what the technique predicts. A captured loop is by definition one where the controller is also the interested party; the rule that would repair it is therefore held by that same controller; and an actuator that can install can also revoke. The previous chapter required, as a precondition, that a remedy survive a change of leadership. The actuator column explains why so many do not: where the installing actuator sits inside the repaired loop, the remedy's survival depends on the goodwill of the actor it constrains.

The constructive form of the same finding is this. An institution cannot repair a captured loop from inside it. Where no outside position exists, one has to be **supplied** — a legislature, a court, a regulator, a funder, an exchange — or **manufactured**, which is what a constituent assembly is: a body placed deliberately outside the ordinary legislative loop so that it can rewrite the rules that loop runs on. The Basic Law is the clearest case in the catalogue, and it required the prior collapse of the system it repaired.

## The corporation, worked through

The corporation is the one system with a full lever inventory, and it shows why the two loops must be kept apart. Its operating rules move quickly; its governance rules do not, and the difference is not effort but ownership.

| Lever | Who signs | Until it takes effect | Who loses |
|-------|-----------|----------------------|-----------|
| Process, approval limits, metric sets | Management | Weeks to two quarters | Little |
| Case-handling systems | CIO and contractor | Two to four years | Users of the old process |
| Executive remuneration structure | Remuneration committee, AGM vote | Three to four years (vesting) | The executives setting it |
| Board composition | AGM; terms run several years | Years | Incumbent members |
| Auditor independence rules | Legislature or securities regulator | Years | Audit firms' consulting revenue |
| Employee governance rights | Legislature | Years | The capital side |

Read the last four rows against the first two. For the operating levers, the owner and the loser are different actors, which is why those changes happen routinely. For the governance levers they converge: **the actor holding the lever is the actor the change would cost.** That is why all three corporate remedies in the previous chapter arrived from outside, and why the corporation's reputation for adaptability — earned honestly in the first two rows — does not extend to the rest of the table.

---

## What this changes about the rest of the book

Parts II and III decompose systems. Part IV finds what is unsafe in them and what would repair it. This chapter adds the step that makes a remedy a proposal rather than an observation: name the actuator, add the two latencies, check them against the tenure of whoever is meant to act.

An analysis that stops at the remedy is not finished. If the actuator sits inside the loop being repaired, it has found a fix that the system cannot install — which is useful to know, and is a different finding from the one it appears to be.

## Sources

The lever inventory and the two failure patterns are this project's framing of results from the implementation literature in public administration, a tradition this book had not previously drawn on: Pressman and Wildavsky's *Implementation* (1973), whose subject is a federal programme that dissolved between the decision in Washington and delivery in Oakland; Lipsky's *Street-Level Bureaucracy* (1980) on why the last step in the chain so often dominates; Mazmanian and Sabatier (1983) on the conditions under which an implementation chain holds; and James Q. Wilson's *Bureaucracy* (1989) on why formal authority over an agency is not control of it. The change loop's status as a leverage point in its own right is Meadows (1999), who ranks the power to change system structure above the rules themselves. Isomorphic mimicry is Andrews, Pritchett and Woolcock (2017), with the decoupling of institutional form from function in Meyer and Rowan (1977). Requisite variety, applied here to the reformer rather than the operating controller, is Ashby (1956). Full entries are in the [Sources and Further Reading](../further-reading.md) chapter and the project [bibliography](https://github.com/ccabos/systems/blob/main/knowledge/references/bibliography.md).
