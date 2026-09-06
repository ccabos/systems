# Corporation — Change-Loop Analysis

Applies `knowledge/se-techniques/change-loops/` to the for-profit
corporation. It is the first application of that technique to a
catalogued system, and it should be read alongside two files that
describe the *operating* loop: the control-structure profile in
`../cross-system/control-structure-profiles.md` and the unsafe control
actions and remedies in `../cross-system/remedies-case-studies.md` §2.
Sources for this folder are in `sources.md`; keys not expanded there
resolve in `knowledge/references/bibliography.md`.

The operating-loop analysis says how the corporation fails. This one
asks a different question: given that the failure is understood and a
remedy is known, who can actually install it, and will they still be
in office when it works.

## Two change loops, not one

Most catalogued systems have a single change loop. The corporation has
two, and they behave so differently that treating them as one is the
main source of confusion about corporate reform.

- **The operating-rule loop.** Processes, approval limits, reporting
  lines, objectives schemes, the systems that carry them. Owned inside
  the firm, changeable in weeks to months, and genuinely fast by the
  standards of any other system in the catalogue.
- **The governance-rule loop.** The rules that constitute the control
  structure itself: auditor independence, board composition, who sets
  executive pay, whether employees hold governance rights. Owned
  either outside the firm entirely, or by the actors the change would
  cost.

The corporation's reputation for adaptability comes from the first
loop. Its documented pathologies all sit in the second.

## Lever inventory

Latencies are brackets, not measurements — see
`knowledge/se-techniques/linear-algebra/false-precision-trap.md`. The
figures marked with a source are taken from the catalogue; the rest
are orders of magnitude for a large listed company and should be
re-derived for any specific firm.

| Lever | Who signs | Change latency | Effect latency | Who loses |
|-------|-----------|----------------|----------------|-----------|
| Work instruction, process step | Line management | Days–weeks | Weeks | Little |
| Approval and signature limits | CFO / executive board | Weeks | Immediate | Middle management, in autonomy |
| Reporting and metric set | CFO / controlling | Months | 1–2 quarters | Whoever looked good under the old report |
| ERP / CRM case-handling systems | CIO and contractor | Months | 2–4 years | Users of the displaced process |
| Workforce objectives scheme | Executive board, with works council where co-determination applies | Months–1 year | 1–2 quarters | Units holding an advantage under the old scheme |
| Executive remuneration structure | Board remuneration committee, with an AGM vote | ~1 year (AGM cycle) | 3–4 years (vesting) | The executives setting it |
| Board composition | AGM; supervisory terms run several years | ~1 year + terms | Years | Incumbent members |
| Articles, governance structure | AGM, qualified majority | 1–2 years | Years | Controlling shareholders |
| Auditor independence rules | **Legislature / securities regulator** | Years | Years | Audit firms' consulting revenue |
| Employee governance rights | **Legislature** | Years | Years | The capital side |

Controller tenure, for the loop's principal controller: executive
tenure averages about five years, against a 90-day external reporting
cycle and option vesting over three to four years (all three figures
from the UCA-C2 causal factor in
`../cross-system/remedies-case-studies.md` §2).

## Reading 1 — the actuator void is structural, not incidental

Apply diagnostic questions 2 and 4 (`who owns the actuator?` and `who
loses?`) to the table. For the operating-rule levers at the top they
have different answers, which is why those changes happen routinely.
For the governance levers at the bottom they converge: **the actor who
holds the lever is the actor the change would cost.**

The catalogue's own remedy record is the test, and it is unambiguous.
All three architectural remedies documented for the corporation were
installed from **outside** the firm:

| Remedy | Actuator | Inside the firm? |
|--------|----------|------------------|
| Sarbanes-Oxley 2002 — auditor independence, PCAOB | US legislature | No |
| Mitbestimmung 1976 — worker board representation | German legislature | No |
| UK Corporate Governance Code, post-Cadbury 1992 | Committee plus listing rules, comply-or-explain | No |

Not one of them is a board that reformed itself. That is what Pattern 1
of `knowledge/se-techniques/change-loops/dangerous-patterns.md`
predicts for a lever whose owner is its loser, and the corporation
supplies three independent instances of it.

## Reading 2 — UCA-C2 is a horizon mismatch, and the catalogue said so first

The causal factor recorded for UCA-C2 is that "the time horizon in the
incentive structure is shorter than the time horizon of the decisions
being made". That is Pattern 2 of the change-loop technique, written
down for one system before the pattern had a name.

Set out as nested horizons, the corporation runs four clocks at once:

- external reporting — 90 days
- option vesting — 3 to 4 years
- executive tenure — about 5 years
- consequences of a capital-allocation or platform decision — longer
  than all three

The technique adds two things to the catalogue's observation. First,
the general form: any controller whose feedback arrives after its
tenure is operating an open loop, whatever its motives. Second, the
prediction — a short-horizon controller changes the levers with short
effect latency and visible output, which in this table are the
operating-rule levers at the top. A programme of process changes and
reporting redesigns offered as governance reform is the expected
behaviour of this structure, not a failure of character.

## Reading 3 — which internal reforms are feasible

The inventory separates the two cases cleanly.

**Owner ≠ loser.** Process, approval limits, metric sets, the systems
underneath them. These change on management decision and show effect
within quarters. The binding constraint is usually the case-handling
system, whose two-to-four-year effect latency exceeds a typical
strategy cycle — the standard reason a reorganisation announced in one
year is still not visible in the workflow three years later.

**Owner = loser.** Remuneration structure, board composition,
governance rights. Internally these require the losing actor to sign,
so they need an external actuator, and an external actuator needs
energy from outside the firm. The record shows two distinct sources of
that energy, and it is worth keeping them apart:

- **Scandal.** Enron's collapse preceded Sarbanes-Oxley by months; the
  Maxwell affair preceded Cadbury. The scandal does not supply the
  analysis — the conflict of interest in the audit relationship was
  understood long before Enron — it supplies the political capacity to
  move a lever that was always there.
- **Organised interest.** Mitbestimmung came from a labour-political
  settlement rather than a precipitating failure. It is the useful
  counter-case: external energy need not be a crisis, and a standing
  organised interest can supply it on a slower schedule.

## What this adds to the control-structure profile

The profile records an **accountability void**: executive pay is set
by board members often appointed on executive recommendation, and the
audit committee reviews the accounts of the management that appointed
its members. The change-loop analysis finds the same concentration of
authority showing up in the second loop as an **actuator void**: the
rule that would repair the accountability void is held by the actor it
would cost.

The two are not the same finding, but they are the same fact seen in
two loops, and together they state something neither says alone:

> The corporation cannot correct this class of failure in operation,
> because the controller is the interested party — and cannot repair
> it by decision, because the lever belongs to the same party. Both
> paths out run through an actuator outside the firm.

This is a structural claim, not a moral one, and it has a
constructive reading. It says where reform effort is not wasted:
inside the firm, on levers whose owner and loser differ; outside it,
on the three or four governance rules that no board will change about
itself.

## What this does not establish

- **One system.** The pattern is drawn from a single catalogue entry.
  Whether owner-equals-loser is the general signature of
  capital-ownership governance, or an artefact of these three
  remedies, needs a second system worked to the same depth.
- **Selection in the evidence.** The catalogue records remedies that
  were installed and subsequently studied. Internal governance reforms
  that were attempted and failed leave no comparable record, so the
  "always external" reading is stronger than the evidence strictly
  supports. Read it as: no documented instance runs the other way.
- **Jurisdictional narrowness.** Two of the three remedies are
  Anglo-American and one German. Systems with concentrated family or
  state ownership have different actuator holders and would give a
  different table.
- **Effect claims stay tempered.** The evidence assessments in
  `../cross-system/remedies-case-studies.md` §2 apply unchanged here:
  attributing outcomes to SOX alone is not supportable [Coates2007],
  and the identified evidence for Mitbestimmung supports "a different
  stakeholder balance at no efficiency cost" rather than a performance
  gain [Jager2021].
