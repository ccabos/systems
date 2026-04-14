# Cross-Family Reuse — Case Studies

Extracted from `projects/systems-introduction-book/docs/part2/ten-systems.md`
§5. Five worked examples of reusing modules from one social system
type in another, classified by what can be reused directly, what
requires a workaround, and what is structurally incompatible.

## 5.1 Kingdom Adopting Republican Structures (Constitutional Monarchy)

- **Fully reusable (4 elements):** Independent judiciary, professional
  civil service, modern fiscal system, free press.
- **Partially reusable (4 elements):** Parliament, written constitution,
  elections for legislature, partial separation of powers.
- **Incompatible (3 elements):** Popular sovereignty as sole source,
  periodic executive election, electoral administration for head of state.

The constitutional monarchy is a textbook product-line variant: it
rebinds VP1 from "popular sovereignty" to "shared sovereignty"
(crown + parliament) while reusing approximately 80% of the republican
physical implementation.

## 5.2 Church Adopting Corporate Structures (Institutional Professionalization)

Many modern churches face the challenge of managing large-scale
operations (media, real estate, global workforce) while maintaining
spiritual authority.

**Reusable from corporation:**

- CL3 → Financial subsystem: professional accounting, external audit,
  transparent budgets. The Catholic Church's creation of the
  Secretariat for the Economy (2014) is exactly this transplant.
- CL4 → HR subsystem: formal employment contracts, safeguarding
  policies, professional development for clergy. Replaces informal
  patronage with structured HR.
- CL5 → Legal & compliance: centralized handling of abuse cases,
  regulatory compliance, insurance.
- CF6 → External relations: professional PR and communications teams.

**Partially reusable:**

- CL1 → Governance: some churches have adopted board-style governance
  (many Protestant denominations), but the Catholic model of papal
  authority cannot fully adopt shareholder-style accountability
  without changing VP1.

**Incompatible:**

- CG1 (profit maximization) contradicts HG1 (existential meaning).
  A church that optimizes for revenue over spiritual mission becomes
  a business by definition.
- CR2 (shareholder accountability) is incompatible with HR3 (clerical
  authority to interpret doctrine). Doctrinal questions cannot be
  settled by shareholder vote.

## 5.3 University Adopting Corporate Structures (New Public Management)

The corporatization of universities since the 1990s is one of the
most controversial cases of cross-family reuse.

**Reusable:**

- CL3 → Financial subsystem: professional controlling, cost accounting,
  performance budgeting. Widely adopted.
- CF4 → HR function: structured recruitment, performance reviews,
  competitive compensation for top researchers.
- CF6 → External relations: marketing, branding, alumni management,
  fundraising.

**Partially reusable (and contested):**

- CL1 → Governance: replacing collegial academic self-governance
  with an appointed board of directors (Hochschulrat). Works for
  operational efficiency but conflicts with UR3 (academic
  self-governance). Germany's Hochschulfreiheitsgesetz (NRW, 2007)
  is this exact experiment.
- CF1 → Strategic direction: corporate-style strategic planning.
  Partially compatible if faculty retain control over academic content.

**Incompatible:**

- CG1 (profit) contradicts UG1 (advance knowledge) and UG4 (academic
  freedom). When revenue targets override research priorities, the
  university ceases to function as a university.
- CR4 (hierarchical management) is fundamentally in tension with UR5
  (tenure protecting freedom of inquiry). A professor who can be
  directed by management like an employee loses the capacity for
  independent scholarship.

This case illustrates the danger of **over-reuse**: transplanting
corporate modules that conflict with the university's goal-level
bindings produces an incoherent system — one that looks efficient on
paper but hollows out its core purpose.

## 5.4 One-Party State Adopting Republican Fiscal Structures (China's Reform Model)

China's post-1978 reforms are an extraordinary case of selective reuse
from the republican product line while preserving one-party binding
at VP1.

**Fully adopted:**

- RL5 → Fiscal subsystem: modern central bank (PBOC modeled on the
  Fed), tax authority, bond markets, audit institutions. The fiscal
  infrastructure is essentially republican.
- RF5 → Public finance function: budget legislation (Budget Law of
  2014), transparent(ish) government accounting, local government
  bond regulation.

**Partially adopted:**

- RL3 → Judicial subsystem: professional courts, trained judges,
  commercial law. But judicial independence is bounded — the party
  retains final authority and can override courts on politically
  sensitive cases.
- RR5 → Professional civil service: competitive examinations
  (re-introduced from China's own historical tradition, congruent
  with republican practice).

**Incompatible (and deliberately rejected):**

- RG1 (popular sovereignty), RG5 (periodic executive transfer),
  RL4 (electoral and transparency subsystem). The party's VP1
  binding ("ideological mandate") makes these structurally impossible
  without regime change.

The Chinese model is often described as "authoritarian modernization."
In product-line terms, it is more precisely described as: *reuse the
entire fiscal and judicial physical implementation from the republican
product line, reuse the civil service function, but hard-bind VP1,
VP3, and VP4 to the one-party variants, and accept the resulting
constraint that VP6 must include party-controlled enforcement.*

## 5.5 Family Adopting Verein Structures (Democratic Parenting)

An intimate-scale but instructive case. Modern Western parenting has
increasingly borrowed from the Verein / democratic model:

**Reusable:**

- VF3 → Democratic assembly: "family meetings" where children have
  voice (and sometimes vote) on household decisions.
- VL1 → Governance subsystem: explicit "family rules" negotiated
  together, posted on the fridge — a domestic Satzung.
- VF6 → Financial management: children given allowances and budgeting
  responsibility — creating a micro fiscal subsystem.

**Partially reusable:**

- VR3 → Equal voting rights: partially adopted. Children may have
  voice but typically not equal vote on safety or financial decisions.
  The adaptation is age-graduated authority.

**Incompatible:**

- VR6 (open membership — voluntary joining and leaving) is incompatible
  with FR1 (biological/legal bond). You cannot resign from being
  someone's child. The membership boundary of a family is fundamentally
  different from a Verein.
- VG4 (institutional continuity independent of individual members)
  contradicts FG2 (emotional bonds between *specific* people). A family
  where the members are interchangeable has ceased to be a family.

This micro-case illustrates the variation-point constraint: you can
democratize a family's *decision-making mechanism* (VP3) without
changing its *membership boundary* (VP2) or *legitimation narrative*
(VP5: love and kinship). Pushing reuse too far — treating family
members as interchangeable Vereinsmitglieder — breaks the system's
core logic.
