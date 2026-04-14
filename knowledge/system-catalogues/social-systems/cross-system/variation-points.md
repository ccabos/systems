# Social System Variation Points

Extracted from `projects/systems-introduction-book/docs/part2/ten-systems.md`
§4. Six variation points identified across the ten decomposed social
systems, with their variants and binding constraints.

If the platform (see `platform.md`) is what social systems share, the
variation points are what makes them distinct. Six primary variation
points are identified, each with a defined interface and a set of
variants.

## VP1 — Source of Authority

*Interface:* The system requires a source from which governing
authority is derived.

| Variant | Used By |
|---------|---------|
| Divine mandate | Theocracy, traditional monarchy (divine right) |
| Hereditary right | Kingdom |
| Popular sovereignty (elections) | Republic, Verein |
| Ideological mandate (party) | One-party state |
| Capital ownership (shareholders) | Corporation |
| Scholarly merit (academic freedom) | University |
| Command hierarchy (commission) | Military |
| Biological/legal bond | Family |
| Charismatic/prophetic authority | Church (founding phase) |

VP1 is the *primary* variation point. It cascades most strongly into
all downstream levels.

## VP2 — Membership Boundary

*Interface:* The system needs criteria for who belongs and who does not.

| Variant | Used By |
|---------|---------|
| Birth (citizenship by blood/soil) | Kingdom, Republic, One-party state, Theocracy |
| Voluntary joining | Verein, Church, Corporation (employment) |
| Competitive selection (admission) | University, Military (enlistment/commission) |
| Biological/legal kinship | Family |
| Compulsory (subjects of a territory) | Kingdom, Theocracy |

## VP3 — Decision-Making Mechanism

*Interface:* The system needs a process for making binding collective
decisions.

| Variant | Used By |
|---------|---------|
| Autocratic decree | Kingdom, One-party state (politburo) |
| Democratic vote (one-person-one-vote) | Republic, Verein |
| Board/shareholder vote (weighted by capital) | Corporation |
| Collegial deliberation (faculty senate) | University |
| Command order (superior to subordinate) | Military |
| Consensual negotiation (parental agreement) | Family |
| Doctrinal interpretation (clerical authority) | Theocracy, Church |

## VP4 — Succession Mechanism

*Interface:* The system needs a way to replace its leaders when they
leave, die, or are removed.

| Variant | Used By |
|---------|---------|
| Hereditary (primogeniture, house law) | Kingdom, Family (inheritance) |
| Periodic election | Republic, Verein |
| Board appointment | Corporation, University (in some systems) |
| Internal promotion (seniority/merit) | Military, One-party state (cadre system) |
| Clerical selection (conclave, council) | Church |
| Self-selection (founding a new family) | Family |

## VP5 — Legitimation Narrative

*Interface:* The system needs a story that explains why its authority
is valid.

| Variant | Used By |
|---------|---------|
| Tradition and dynasty | Kingdom |
| Constitutional mandate and elections | Republic |
| Divine will / sacred text | Theocracy, Church |
| Historical necessity / ideological correctness | One-party state |
| Market success and shareholder return | Corporation |
| Academic freedom and truth-seeking | University |
| National defense and duty | Military |
| Love, kinship, and mutual obligation | Family |
| Shared interest and voluntary association | Verein |

## VP6 — Norm Enforcement Mechanism

*Interface:* The system needs a way to ensure members comply with its
rules.

| Variant | Used By |
|---------|---------|
| State coercion (police, courts, prison) | Republic, Kingdom, Theocracy, One-party state |
| Ecclesiastical discipline (excommunication, penance) | Church, Theocracy |
| Employment sanctions (warning, termination) | Corporation, University (for staff) |
| Military discipline (courts martial, confinement) | Military |
| Social pressure and expulsion | Verein, Family |
| Academic sanctions (grade penalties, expulsion) | University (for students) |

## Interactions and binding constraints

Not all combinations of variants are compatible. The binding at VP1
(source of authority) constrains the bindings at VP3 (decision-making)
and VP4 (succession). For example:

- If VP1 = "hereditary right," then VP4 *cannot* be "periodic election"
  for the head of state. It can, however, coexist with periodic
  election for the legislative branch — this is the constitutional
  monarchy pattern.
- If VP1 = "popular sovereignty," then VP4 *must* include periodic
  election at least for the legislature and usually for the executive.
- If VP1 = "divine mandate," then VP3 is constrained to "doctrinal
  interpretation" for ultimate questions of law.

These constraints define the **valid configurations** of the social
system product line. Not every possible combination of variants is
architecturally coherent. A system that claims popular sovereignty at
VP1 but uses hereditary succession for all leadership positions at
VP4 is incoherent — it will either evolve or collapse. A system that
claims divine mandate at VP1 but subjects doctrine to popular vote at
VP3 undermines its own foundational logic.

Understanding these constraints is precisely what product line
engineering contributes: it tells you which reforms are *structurally
compatible* with which system types, before you attempt them.
