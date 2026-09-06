# Cross-System Principles

Extracted from `projects/systems-introduction-book/docs/part2/ten-systems.md`
§6. General principles derived from the cross-family reuse case
studies (see `reuse-case-studies.md`).

## The Reuse Gradient

Reuse feasibility **decreases as you move upward in the SE hierarchy**.

- **Physical implementations** are the most portable — a tax authority
  works the same way under a king or a parliament.
- **Logical architectures** require more adaptation — a parliament
  must share space with a crown in a constitutional monarchy.
- **Functions** can often be transplanted but need interface
  adjustments.
- **Requirements** must be checked for compatibility with the target
  system's goals.
- **Goals** themselves are almost never reusable across system types —
  they are what *define* the type.

This gradient has a practical corollary: **start reform at the
bottom.** Modernize physical implementations first (professional civil
service, independent courts, transparent budgets), then work upward.

The corollary is routinely misread as *start with the easy changes*,
and the three examples just given show why that reading is wrong:
a career and tenure regime, a judicial-independence rule, and an
information-disclosure rule. All three are physical-level, and none
of them is a *part*: each is a written rule, and a written rule is a
connection in physical form (see
`knowledge/foundations/system-definition.md`). They are the
expensive half of the P level and the half that carries the
leverage. Reform that stays among the parts — a new agency, new
staff, a new portal — is cheap, fast, and is precisely the
isomorphic mimicry the next paragraph warns about. Start at the
bottom means start with the rules, not with the easy part.

The corollary is well supported outside this project — and the
support also bounds it. Scott's case record of high-modernist
schemes shows goal-first, top-down redesign failing precisely
because it overwrites the local operational knowledge the formal
model cannot see [Scott1998]; Lindblom argued on decision-theoretic
grounds that incremental, bottom-up change is how institutional
reform actually succeeds [Lindblom1959]; and the state-capability
literature documents that transplanting upper-level institutional
*forms* without working implementations produces "isomorphic
mimicry", not capability [Andrews2017]. Two cautions from the same
literature: institutions that merely *look* reformed at the P-level
can persist for decades without functioning [MeyerRowan1977], and
physical-level transplants also fail where the surrounding power
distribution rejects them [AcemogluRobinson2012] — so "start at the
bottom" is a default, not a guarantee. (Citation keys resolve in
`knowledge/references/bibliography.md`.)

## The Coherence Rule

A system is coherent when its binding decisions at each variation
point are mutually compatible, and when every element at every SE
level traces consistently to the goals above it and the implementations
below it. Incoherent systems — those with contradictory bindings —
are unstable. They will either resolve the contradiction (through
reform or revolution) or persist in a state of institutional
dysfunction.

Examples of incoherent configurations:

- A theocracy with a free press (VP6 contradicts VP1): the press will
  inevitably challenge clerical authority, forcing either repression
  or secularization.
- A corporation governed by equal-vote democracy (VP3 = one-person-
  one-vote for all employees) combined with VP1 = capital ownership:
  decision-making and authority source contradict each other.
  Yugoslav self-management enterprises demonstrated this instability.
- A university with VP1 = profit maximization and VP3 = management
  command: produces degree mills, not universities.

## The Workaround Principle

When a desirable module from another system type conflicts with a
binding decision, the most successful reforms do not force the
transplant. Instead, they create a **workaround** — a modified version
that preserves the function while respecting the constraint.

The constitutional monarchy is the paradigm case: it wants legislative
representation (a republican function) but cannot adopt popular
sovereignty for the executive. The workaround is a parliament that
legislates *alongside* the crown, with the crown retaining defined
prerogatives. The function (legislative debate and representation) is
preserved; the binding (hereditary executive) is respected.

Other examples of workarounds:

- **China's "socialist market economy"**: reuses the market allocation
  function from capitalist systems while binding VP1 to party
  authority. The workaround: markets for goods, but not for political
  power.
- **Papal infallibility within collegial structures**: reuses
  collegial deliberation (synods, episcopal conferences) for most
  decisions, but reserves a doctrinal override for the pope. The
  workaround: democracy for administration, autocracy for doctrine.
- **Military ombudsman**: the military needs strict command hierarchy
  (VP3) but modern democracies require accountability (republican
  VP6). The workaround: an external ombudsman (Wehrbeauftragter in
  Germany) who can receive complaints without undermining the chain
  of command.

## The Product Line Architect's Toolkit for Social Reform

The product line framework offers institutional reformers a structured
methodology. Before using it, read Ostrom's warning against
institutional panaceas: designs that work are diagnosed into their
context, not copied between contexts [Ostrom2007]. Steps 3–5 below
(variation points, binding constraints, red items) are this
project's way of operationalising that warning — a red item *is* a
context the design cannot be copied into.

1. **Decompose both systems** (source and target) through the five SE
   levels.
2. **Identify the platform elements** shared between them — these are
   free to reuse.
3. **Map the variation points** — identify where the systems diverge.
4. **Check binding constraints** — determine which source-system
   elements conflict with the target system's VP bindings.
5. **Classify reuse potential** — green (direct adoption),
   amber (adopt with workaround), red (incompatible without changing
   system identity).
6. **Start at the bottom** — implement physical-level changes first,
   then work upward.
7. **Design workarounds** for amber items — preserve the function
   while respecting the constraint.
8. **Accept red items as system-defining** — attempting to force them
   means changing the system type, not reforming it.
