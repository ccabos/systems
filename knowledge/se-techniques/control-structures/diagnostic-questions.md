# The Four Diagnostic Questions

Once a system's control structure is drawn, four questions
expose most of its failure modes. Answering each question well
requires evidence — not just assertion. This page lists the
questions and what counts as a satisfactory answer.

## 1. Feedback richness

> *How many independent channels carry information upward, and
> how accurately do they represent the state of the controlled
> process?*

A **channel** is independent when its operation is not
controlled by the same actor whose behaviour it is supposed to
report on. A single channel is almost always insufficient:
whoever controls it controls the signal.

Rich feedback requires:

- **Multiple channels** — elections, press, courts, audits,
  complaints, inspections — not just one.
- **Independent operation** — the channel's staffing, budget,
  and publishing authority must not depend on the actor it
  reports on.
- **Low manipulation cost for reporters, high manipulation cost
  for controllers** — the signal must be cheap to emit
  truthfully and expensive to suppress.

A good answer names the channels, states who operates each, and
shows why each operator is not controlled by the actor being
reported on.

## 2. Self-sealing tendency

> *Can the process model at the top be corrected by information
> from below, or does it filter out contradictory signals?*

The **process model** is the controller's internal
representation of the state of the controlled process. A
process model is **self-sealing** when it contains mechanisms
that reject contradictory information as illegitimate:

- **By doctrine** — contradictory information is heretical,
  disloyal, or defeatist.
- **By incentive** — bearers of bad news are punished, so the
  controller only receives good news.
- **By structure** — contradictory information is classified,
  confidential, or excluded by the reporting format.

A good answer identifies the filtering mechanism by name. The
strongest warning sign is a doctrinal one: when the process
model at the top *cannot be wrong by definition*, the system
has no internal route back to reality.

## 3. Accountability voids

> *Where is the controller also the interested party, so that
> independent oversight is structurally prevented?*

An **accountability void** exists whenever the same actor both
decides and is judged. Canonical examples:

- Monarchs who judge Crown claims.
- Boards setting executive pay when executives chose the board.
- Bishops investigating their own clergy.
- Commanders prosecuting their own troops.
- Peers reviewing their own competitors' research.

A good answer locates each such overlap and names a remedy
that separates the deciding and judging roles — ideally by
giving the judging role to an actor whose continued existence
does not depend on the decider.

## 4. Circuit breakers

> *What mechanisms can interrupt an escalating harmful loop
> before it causes irreversible damage?*

A **circuit breaker** is a mechanism that can stop the system
from a state the system itself should not have entered. Its
defining property is *independence of the escalation*: the
breaker must not require the cooperation of the same actor
whose behaviour is being escalated against.

Good circuit breakers are:

- **Fast** — they activate before damage becomes irreversible.
- **Independent** — the actor being restrained cannot disable
  them.
- **Lawful** — they do not require extreme or revolutionary
  conditions to invoke.
- **Redundant** — multiple breakers with different activation
  conditions protect against single-point failure.

A good answer lists the breakers, states each breaker's
activation condition, and shows that the actor being restrained
cannot block activation.

## Using the four questions

The questions form a checklist, not a score. A single bad
answer in any of the four is a red flag warranting a full STPA
analysis and a search for the dangerous patterns catalogued in
`dangerous-patterns.md`.
