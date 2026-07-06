# Sources and Further Reading

Very little in this book is original. The working definition of a
system, the control-structure diagnostics, the product-line
vocabulary, and even the justificatory-rung ladder are arrangements
of ideas that other people worked out first — often decades ago, and
often with far more empirical care than a synthesis like this one can
offer. This chapter names those sources, says what each contributes,
and points you to the ones worth reading in full.

The complete keyed bibliography lives in the project's knowledge
base:
[`knowledge/references/bibliography.md`](https://github.com/ccabos/systems/blob/main/knowledge/references/bibliography.md).
What follows is the guided tour.

## If you read only five books

1. **Donella Meadows, *Thinking in Systems* (2008).** The best short
   introduction to systems thinking ever written. Part I of this
   book is, in essence, Meadows' elements–interconnections–purpose
   triad plus an engineering toolkit; her ordering of intervention
   points (parameters < feedback loops < goals < paradigms) is the
   replaceability hierarchy of our "What Is a System?" chapter.
2. **Nancy Leveson, *Engineering a Safer World* (2012).** The source
   of STAMP and STPA, on which Parts I and IV depend entirely.
   Freely available from MIT. Note that Leveson's control
   hierarchies already include regulators, legislatures, and
   management — the move from engineering to social systems is
   shorter than it looks.
3. **Elinor Ostrom, *Governing the Commons* (1990).** The
   Nobel-recognised field programme that did empirically what Part
   II of this book does analytically: extract shared design
   principles from many real self-governing institutions. Where our
   conclusions and hers diverge, trust hers — they rest on decades
   of case data.
4. **James C. Scott, *Seeing Like a State* (1998).** The essential
   caution. Scott documents what happens when formal, legible,
   top-down models are imposed on social systems that run on local,
   tacit knowledge. Every remedy proposed in Part IV should be read
   with Scott open on the desk.
5. **Albert O. Hirschman, *Exit, Voice, and Loyalty* (1970).** All
   feedback channels in social systems come in two architectural
   families — leaving and speaking up. Our entire discussion of
   feedback richness is a control-theoretic elaboration of
   Hirschman's distinction.

## Foundations (Part I)

The definition of a system synthesises general system theory
(von Bertalanffy, *General System Theory*, 1968; Ackoff, "Towards a
System of Systems Concepts", 1971) with Meadows. The emergence
discussion follows Anderson's "More Is Different" (1972) and the
weak/strong distinction of Bedau (1997) and Chalmers (2006). The
insistence that the boundary is the analyst's first decision is
Churchman's (*The Systems Approach*, 1968), sharpened by Ulrich's
*boundary critique* (1983), which adds the question this book asks
of every social system: who decided who counts as inside? Simon's
"The Architecture of Complexity" (1962) explains why nested
hierarchies recur everywhere the book looks.

The five-level SE hierarchy is standard practice — see the INCOSE
*Systems Engineering Handbook* (5th ed., 2023), the *NASA Systems
Engineering Handbook*, and ISO/IEC/IEEE 15288. Deriving requirements
from goal models is worked out most rigorously in van Lamsweerde's
*Requirements Engineering* (2009). Product-line concepts (platform,
variation point, binding) follow Pohl, Böckle and van der Linden
(2005), with the founding idea in Parnas's "On the Design and
Development of Program Families" (1976).

The justificatory-rung ladder is a synthesis, not a discovery. Rungs
0–1 are Weber's authority types (*Economy and Society*, 1922) with
Arendt's power/violence distinction (*On Violence*, 1970); rung 3 is
Popper (*The Logic of Scientific Discovery*, 1959); rung 4 is
consilience (Whewell via E.O. Wilson, *Consilience*, 1998) and
Lakatos; rung 5 is post-normal science (Funtowicz & Ravetz, 1993)
and Knightian uncertainty; rung 6 is Habermas (*The Theory of
Communicative Action*, 1981) and the deliberative-democracy
literature (Fishkin, *When the People Speak*, 2009). Toulmin's *The
Uses of Argument* (1958) licenses the key move of treating the
standard of justification as a per-context variable.

## Social systems and their pathologies (Parts II and IV)

The distinction between what a system *claims* and what it *does*
runs through a century of social science: Merton's manifest vs
latent functions, Selznick's goal displacement (*TVA and the Grass
Roots*, 1949), Beer's "the purpose of a system is what it does",
Meyer and Rowan's decoupling of formal structure from operations
(1977), and — closest to this book's claimed-rung vs operating-rung
gap — the "isomorphic mimicry" documented in Andrews, Pritchett and
Woolcock's *Building State Capability* (2017, open access).

The dangerous patterns of Part IV each have their own literature.
The accountability void and its structural remedy is Federalist
No. 51. The self-sealing process model is Argyris and Schön's term
(*Organizational Learning*, 1978), with field evidence in Vaughan's
*The Challenger Launch Decision* (1996) and Wilensky's
*Organizational Intelligence* (1967). The proxy metric is Goodhart's
law (1975), Campbell's law (1979), Strathern's aphorism (1997), and
Muller's *The Tyranny of Metrics* (2018). The Great Leap Forward
case rests on Dikötter's *Mao's Great Famine* (2010) and Yang
Jisheng's *Tombstone* (2012). The corporate-governance evidence is
assessed in Coates (2007) on Sarbanes–Oxley and Jäger, Schoefer and
Heining's "Labor in the Boardroom" (2021) on co-determination — both
more cautious than the popular narratives. The reproducibility
material follows the Open Science Collaboration (2015) and Nosek et
al.'s "The Preregistration Revolution" (2018).

Safety science beyond Leveson: Rasmussen's "Risk Management in a
Dynamic Society" (1997) is the paper STAMP grew from and is
independently worth reading; Perrow's *Normal Accidents* (1984) and
Dekker's *Drift into Failure* (2011) give the sociological and
complexity-theoretic accounts of the same territory.

## Development frameworks (Part III)

Each framework's canonical text: Royce (1970) for Waterfall — who
actually warned *against* the single-pass reading; Boehm's spiral
model (1988); the Agile Manifesto (2001); the *Scrum Guide*
(Schwaber & Sutherland, 2020); Anderson's *Kanban* (2010), with its
lineage in Ohno's *Toyota Production System* (1988); Brown's
*Change by Design* (2009); *The DevOps Handbook* (Kim, Humble,
Debois & Willis, 2016) and its empirical companion *Accelerate*
(Forsgren, Humble & Kim, 2018); AXELOS's PRINCE2 manual (2017); and
*SAFe Distilled* (Knaster & Leffingwell, 2020). Treat each as a
self-description: independent outcome evidence is thin across the
whole field, strongest (with caveats) in *Accelerate*.

## A caution about this whole genre

Applying formal systems models to society is not new, and its track
record is mixed. General systems theory promised a unified science
of everything in the 1950s and delivered less; cybernetic management
reached its high-water mark with Stafford Beer's Project Cybersyn in
Allende's Chile (Medina, *Cybernetic Revolutionaries*, 2011); Scott
catalogues the grander failures. The survivors of each wave were the
*descriptive instruments* — feedback, variety, leverage points — not
the prescriptive programmes. That history is why this book tries to
stay on the diagnostic side of the line, and why the remedies it
does discuss are ones that were implemented and studied by others,
not designs of its own.
