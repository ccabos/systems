# The Lever Inventory

The method behind the technique: given a proposed change, enumerate
the levers that could produce it, and record for each the four
properties from `overview.md`. The result is a table that shows,
before anything is attempted, whether the change can reach the
operating loop.

## Procedure

1. **State the intended outcome, not the intended action.** "Permits
   decided in months rather than years", not "reform the permitting
   law". The action is what the inventory is for.
2. **Trace the outcome back to the operating loop.** Which controller
   actually produces it? Almost never the one making the proposal.
   This is the step that reveals how far away the proposing controller
   is.
3. **Enumerate the levers.** Every rule whose change would alter that
   controller's behaviour: statutes, ordinances, competences,
   deadlines, budget lines, posts, case-handling systems, reporting
   duties, participation and appeal rights.
4. **Record the four properties per lever** — owner, change latency,
   effect latency, resistance — and the controller's tenure once, for
   the whole table.
5. **Read the table for the two patterns** in `dangerous-patterns.md`:
   levers the controller does not own, and levers whose effect arrives
   after the tenure ends.
6. **Name the binding constraint.** Usually one lever dominates, and
   it is usually not the one the proposal names.

## Table shape

| Lever | Who signs | Change latency | Effect latency | Who loses |
|-------|-----------|----------------|----------------|-----------|

Latencies are brackets, not measurements — see
`../linear-algebra/false-precision-trap.md`. A table with
single-figure latencies is asserting precision it does not have.

## Worked case — "we will speed up permitting"

A national governing party pledges that building and industrial-plant
permits will be decided in months rather than years. The pledge is
reasonable and the problem is real. The operating loop that produces
the outcome, however, sits three levels away: permits are decided by
a municipal or district authority, under state rather than federal
law, with statutory participation by nature-conservation, heritage and
fire-safety bodies, affected neighbours, and — on appeal — the
administrative courts.

The instance below is German; the shape recurs wherever permitting is
a shared competence.

| Lever | Who signs | Change latency | Effect latency | Who loses |
|-------|-----------|----------------|----------------|-----------|
| Amend the statute | Federal and state legislatures | 1–3 years | Immediate once in force | States, if competence moves |
| Ordinance or administrative circular | Ministry alone | 3–12 months | Months | Little; correspondingly limited reach |
| Move the competence | State and municipalities | 1–2 years | 1–2 years | Municipal authorities |
| Fund posts | Budget legislature | 1–2 years | 1–2 years | Competing budget lines |
| Train examiners | Universities, labour market | Weeks to decide | 3–6 years | Nobody — which is why it is skipped |
| Case-handling system | Authority and its contractor | Months | 2–4 years | Incumbent contractor, staff routines |
| Curtail participation and appeal rights | Legislature, then courts | 1–2 years | Years, contested | Objectors, environmental bodies |
| Measure processing time at all | Authority's own leadership | Months | Months | Nobody — no outcome changes either |

Controller tenure: one electoral term, four years.

**What the table shows.** Three things, none of which is visible in
the pledge.

First, the proposing controller signs almost nothing in the table. The
levers it owns outright are the ordinance and — indirectly, through
the budget — the posts. Everything else is a request to another
controller. That is Pattern 1.

Second, almost every effect latency exceeds the tenure. The lever with
the largest plausible effect, more trained examiners, has the longest
latency and produces nothing visible within the term at all. That is
Pattern 2, and it explains why this lever is consistently the one left
out.

Third, the only lever with no losers is the last one, and it changes
no outcome. It is worth doing anyway: without it, nobody will be able
to establish whether anything else worked. But a reform programme
consisting of it alone is measurement offered as change.

**The characteristic failure that follows.** What gets changed is what
can be changed quickly — the statute, because legislating is the
action a government knows how to take. The effect does not arrive,
because the binding constraint was staffing or the case-handling
system. The conclusion drawn is that the government failed or lied.
The more accurate conclusion is that a lever was turned that was not
the load-bearing one.

## What the inventory does not do

It does not say whether the change is desirable, and it does not
supply the outcome analysis. It answers one question — can this
controller reach this outcome, and will it still be here when the
outcome arrives — and it should be read alongside an operating-loop
analysis, never instead of one.
