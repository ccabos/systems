# What Will AI Do to Us? A Systems-Engineering Reading

_A chapter draft companion to the analysis in this folder. It
distils the structured artefacts (`analysis.md`, `remedy-proposals.md`,
`decision-memo.md`) into a form a non-specialist reader can follow
without the reference tables. If integrated into the
`systems-introduction-book` project, this chapter belongs in Part IV
as a worked counterpart to the religion case._

---

## 1. The questions, and why the usual answers do not satisfy

Three questions about artificial intelligence circulate in every
serious conversation about the next decade.

The first is about jobs. If software writes itself, what becomes of
the people who wrote it? If diagnoses, contracts, lesson plans,
research summaries, and software designs are produced in seconds by
machines that cost a fraction of a human salary to operate, how
many human roles survive? Will the result be a new wave of
unemployment, or a new kind of leisure?

The second is about power. The systems that now demonstrate near-
human reasoning at language tasks were built by perhaps a dozen
laboratories, financed by perhaps a hundred investors, and trained
on perhaps a few hundred specialised computers in a few jurisdictions.
If the technology becomes the central productive force of the next
era, what stops the firms that own the substrate from owning, by
extension, much of what the substrate produces?

The third is about geopolitics. The same technology is being built
in two large economic blocs that mistrust one another. The American
bloc's frontier laboratories sit at the top of the global capability
ranking; the Chinese bloc has matched them at lower rungs and is
catching up at the top. Export controls, sanctions, and chip-supply
dependencies have already produced the first skirmishes of an
infrastructure war. Where does this end?

Each question has been answered many times. The answers are
sophisticated, but they share a common shape and a common
limitation. The shape is the strategic essay: a narrative that
identifies the main forces, ranks them by importance, and concludes
with a list of probable scenarios or a cautious warning. The
limitation is that the essay's conclusions, however confidently
stated, are *free-floating*. They are not connected to specific
mechanisms in the world that one could intervene on. The essay
tells the reader what is likely to happen; it rarely tells the
reader where the system can be moved.

This chapter does something different. It treats the AI economy and
its political surroundings as a system in the engineer's sense: a
collection of parts connected by flows and feedback loops, each of
which can be examined and, if it is part of a failure pathway,
changed. The discipline that does this is called systems
engineering, and a particular variant of it called system-theoretic
process analysis (STPA) was originally developed for safety-critical
machines like aircraft and medical devices. We use it here for a
different class of artefact: not a machine, but the global
political economy of frontier AI.

The reader gains, by the end, a structural picture of the system,
five specific identified failure mechanisms inside it, nine
specific scenarios in which those mechanisms produce identifiable
harms, and twenty-two concrete interventions arranged into a
four-phase implementation plan. This is more than an essay can
deliver, and the reason it is more is the method. So we begin
with the method.

## 2. Two ways of thinking about the system

A strategic essay about AI says things that sound like this. *Power
will concentrate, but open-weight models from China will keep
prices honest. Workers will be displaced, but new categories of
work will emerge as they always have. The geopolitical risk is
significant but probably manageable. The most important uncertainty
is whether redistribution mechanisms catch up to the productivity
shock.* These sentences are useful for orientation. They are also,
on closer examination, the kind of observations that one could
make about almost any technology in almost any decade. They do not
tell you which lever to pull. They do not even tell you which
levers exist.

A systems-engineering analysis, by contrast, begins by asking who
is actually in the system, what each of them controls, and what
information each of them receives. It records this not as a
narrative but as a small set of explicit lists: the controllers,
the things they control, the *control actions* they issue, the
*feedback channels* they receive, and — crucially — the *internal
model* each controller carries of the thing it is controlling. It
then asks, for each control action, what it would mean for that
control action to be issued unsafely (provided when it should not
be, withheld when it should not be, given too late, given for too
long). Each unsafe possibility is recorded. Then it asks, for each
unsafe possibility, *why* the unsafe action could occur — the
controller's model could be wrong, the feedback could be missing
or filtered, the action could be misexecuted, the controlled
process could have changed underneath. Each cause suggests a
remedy: fix the model, fix the feedback, fix the actuator, fix
the structure.

This sounds like ordinary strategic thinking with extra paperwork,
and at first glance the difference is just that there are tables
where the essayist has paragraphs. The deeper difference shows up
at three points. First, the act of writing down every control
action and every feedback channel forces the analyst to confront
parts of the system that the essayist could quietly skip past;
the omissions become visible. Second, recording each unsafe
control action against the four standard categories produces a
checklist of things-that-could-go-wrong that is exhaustive in a
way that strategic intuition is not. The analyst is no longer
free to remember only the failure modes that fit the narrative.
Third, the loss-scenario step demands that the analyst not just
*assert* that a failure could occur but *trace* the causal chain
through the structure. This is what produces remedies. A
narrative observation that "regulators are slow" is not actionable;
a loss scenario showing that *labour ministries operate on a
years cycle while capability deployment happens on a months
cycle, so the corrective signal arrives after the cohort it was
meant to help is already displaced* points directly at automatic
stabilisers indexed to a fast-moving benchmark.

There is a further refinement, particular to systems engineering
applied to social and political systems: every flow in the
structure can be tagged with the *justificatory rung* on which
it operates. The rungs are a seven-step ladder of how a claim or
a control action gets its force. Rung 0 is naked coercion: do it
or else. Rung 1 is authority: do it because *I* say so, or because
the tradition says so, or because our group says so. Rung 2 is
formal consistency: this follows from rules we both accept. Rung
3 is empirical evidence: this works against rivals when tested.
Rung 4 is replicated cumulative evidence. Rung 5 is meta-rational
integration of multiple methods under uncertainty. Rung 6 is
deliberative legitimacy — the standard by which questions about
what should be done are settled in open discourse among those
affected.

Each of these rungs can be claimed. Each can be operated. The
two are not always the same, and where they differ, the system
typically produces specific kinds of damage. A laboratory that
claims to operate at rung 6 (its safety framework is "for the
benefit of humanity") but actually operates at rung 1 (the
framework binds only the laboratory itself, by its own choice,
amendable by its own governance) is in a *claim/operation* gap.
A funding flow that goes downward at rung 3 (financial-return
diligence) but receives capability evidence upward at rung 1
(the lab's own benchmarks, in the lab's own framing) is in an
*asymmetric loop* — the loop appears closed because there are
arrows in both directions, but the upward arrow is filtered by
the downward arrow's framing, and corrective information cannot
get through.

Once you start labelling every arrow with its rung, three patterns
keep appearing. The first is the asymmetric loop just described.
The second is the claim/operation gap. The third, which I will
explain when we encounter an instance, is *cross-loop rung
imposition* — when an institution tries to settle a question
that belongs at one rung using the authority of a different rung.
Each of these patterns has a generic remedy that the engineering
literature catalogues. The remedies are structural — they change
the architecture, not the personalities — and that is what makes
them robust.

We now have everything we need to look at the AI system itself.
We will list its parts, draw its loops, mark the mismatches that
the rung-tagging method surfaces, walk through the failures these
mismatches produce, and end with the remedies they imply. The
reader who finds the technical vocabulary unfamiliar can lean on
the prose: we will introduce each new term in plain English at
the moment it enters the chapter.

## 3. The system

To draw the AI system's control structure honestly we have to be
willing to write down a longer list of actors than a strategic
essay would normally bother with. The longer list matters because
the failures we are looking for happen in the connections between
actors, and a connection is invisible if either of its endpoints
is missing from the picture.

At the apex sits something we will call *the global polity*:
diffuse, slow, but the source of legitimacy on which most
controllers ultimately depend. Below it, three large state
groupings — the United States, the People's Republic of China,
and the European Union together with other states — each with
several distinct organs. The United States in this analysis is
not one actor but six: the Congress that passes legislation, the
Bureau of Industry and Security that issues export controls, the
Treasury that runs sanctions and tax, the Federal Trade Commission
that runs antitrust, the AI Safety Institute that runs technical
evaluation, and the national security apparatus that classifies
and designates. The People's Republic of China is three: the
party centre that sets strategic direction, the Ministry of
Industry and Information Technology that runs industrial policy,
and the Cyberspace Administration that regulates content and
approves models. The European Union is two: the Commission with
its AI Office, and the member states. Other states — the United
Kingdom, Japan, South Korea, India, the Netherlands, Taiwan, the
Gulf monarchies — appear as a coalition layer whose compliance or
defection determines whether the bigger states' levers actually
move anything.

Beneath the state layer sit the capital markets in their various
forms — public equities, private capital, sovereign wealth, debt.
These are the controllers that decide which laboratories can
sustain frontier training runs and which compute providers can
sustain capital-expenditure cycles. Beneath them sit the frontier
laboratories themselves, perhaps a dozen worldwide, each with its
internal mission narrative, its internal capability assessments,
and its internal safety framework. Beneath the laboratories sit
the compute infrastructure providers — the chip designers, the
foundries, the hyperscale cloud operators, the energy and grid
companies. To one side of this hierarchy, neither below nor above
the labs but functionally parallel to them, sits the open-weights
ecosystem: the laboratories, mostly Chinese but including some
Western publishers, that release model weights free for download.
On the other side sit the application-layer companies that turn
model capability into deployed software for paying customers.
Below those, the information platforms that distribute everything.
Below them the labour ministries and education systems that
interface with the people whom all of this affects, and the
information regulators that look after the integrity of the public
information environment. At the bottom — though "bottom" is wrong
because they are the controlled process this whole apparatus
ultimately produces effects on — are the workers, consumers, and
citizens of the cognitive-knowledge economy.

This is fourteen distinct kinds of controller, and a quarter of a
hundred when we count the sub-units. The point of writing them all
down is not exhaustiveness for its own sake. The point is that
each of them issues control actions — directives, allocations,
investments, releases, mandates, statutes, lawsuits, salaries —
and each of them receives feedback — financial returns,
benchmarks, statistics, news, lawsuits, elections, market prices.
The shape and the rung of those flows is what determines whether
the system as a whole works. A strategic essay that talks about
"the AI industry" or "the labour market" without pulling these
controllers apart cannot see, for example, that the antitrust
authority's process model treats concentration as something that
happens in mergers, while concentration in this market is
happening in long-duration compute-allocation contracts that no
merger review touches.

We can summarise the structure in a single picture. Money flows
downward — capital allocates to laboratories and compute providers;
laboratories pay compute providers for training; compute providers
pay foundries for chips; everyone hires people. Capability flows
outward — laboratories release models, application companies wrap
those models into products, products reach workers and consumers.
Information flows in two directions — capability claims and
incident reports flow upward from labs to capital, regulators, and
the public; benchmarks and prices flow horizontally between labs
and the open-weights ecosystem; employment and price statistics
flow upward from the labour and consumer base to ministries and
to the polity. State controllers issue rules and enforcement
actions downward; backlash flows upward when other channels fail.
The picture is dense, but it is not infinite. In the analysis
companion to this chapter, every arrow is enumerated; here we
only need the shape.

When we tag the arrows with their justificatory rungs, five
specific mismatches stand out. Each of them is a particular case
of one of the dangerous patterns we introduced in the previous
section. Each is a structural reason why specific failures occur.

### 3.1 The first mismatch: lab safety frameworks claim more legitimacy than they operate

Frontier laboratories publish documents — *responsible scaling
policies*, *deployment policies*, *constitutional AI charters* —
that claim deliberative legitimacy. Their tone is the tone of
public ethics: the lab is binding itself, on behalf of humanity,
to thresholds that cannot be crossed without specified cause. The
language sits at rung 6, the rung at which questions about what
*should* be done are settled.

The operating mechanism, however, is rung 1. The lab is bound
because the lab has chosen to be bound. The lab amends its
framework when its own governance decides to amend it. There is
no external party with standing to enforce, no court to which
violations can be brought, no parliament that can refuse a budget
on a non-compliant lab. This is the *claim/operation gap*. The
gap is not a sign of bad faith — many of these documents are
written in good faith by people who believe in them. The gap is
structural: a self-binding commitment, however sincere, is
operationally a rung-1 commitment, regardless of how it sounds.

The damage is that public trust calibrates to the higher claim
and gets eroded at the rate of the gap. Every release that rolls
back a previous threshold, every quiet amendment to an evaluation
protocol, every framework that survives commercial pressure only
in form, contributes to a slow loss of legitimacy that the labs
cannot themselves staunch — because the legitimacy was never
theirs to issue.

### 3.2 The second mismatch: capital cannot evaluate the laboratories it funds

Frontier laboratories are funded by capital allocators — venture
funds, growth equity, public markets, sovereign wealth. The funds
flow downward at rung 3: financial diligence, term-sheet
evaluation, comparable-round analysis. The capability evidence
flows back upward through the laboratories' own benchmark
selection, the laboratories' own model cards, the laboratories'
own mission narrative. This is rung 1 in disguise — capability
claims wrapped in the lab's chosen frame.

The result is what the engineering literature calls an *asymmetric
loop*. The arrows exist in both directions, but the upward arrow
is filtered by the framing of the downward arrow. Capital cannot
ask, with the rigour its own diligence claims, whether a lab's
mission claims are falsifiable: the very benchmarks against which
the question would be asked were chosen by the entity making the
claims. The fund can either underwrite the mission narrative as
given or refuse to fund — and at the scale of capital required
for frontier training runs, refusing means watching a competitor
fund the same lab on more pliable terms.

The consequence is that capital structure exerts a quiet but
relentless pressure on operating practice. Funding rounds occur
on a quarterly cadence; safety frameworks are amended on a
yearly cadence; capability releases happen between rounds. When
the cadences disagree, the cadence with the money wins.

### 3.3 The third mismatch: the labour-policy cycle cannot keep up with the capability-deployment cycle

Labour ministries and education systems track unemployment,
sectoral employment, vacancies, and wage statistics. These
indicators arrive at rung 3 or rung 4 — empirical aggregates,
sometimes cumulative — but they arrive on a quarterly or annual
cycle. Retraining programmes and curricular updates respond on a
multi-year cycle. Capability deployment, by contrast, moves on
a months cycle: a new model is released, application companies
integrate it, automation is in production within weeks.

The mismatch in cycle times means that the corrective signal — a
labour-market indicator showing that a class of workers is being
displaced — arrives after the cohort it would have informed is
already displaced. The signal cannot land in time to affect the
decisions that produced the displacement. When this happens
repeatedly, the rung-3/4 channel loses its informational value,
and the only channel left is rung 0: political backlash, which
arrives at the speed of news cycles and elections rather than
at the speed of statistics. The corrective intent of the
statistical channel is overrun by the rung-0 escape valve.

This is not a story about regulators being slow in some abstract
sense. It is a specific identification of two cycles whose periods
no longer line up — and the structural fix is not to be smarter,
but to install instruments whose triggers fire automatically on
a fast index, removing the requirement that a slow channel
confirm.

### 3.4 The fourth mismatch: incidents inside the labs do not reach outside observers

When something goes wrong inside a frontier lab — a misuse case
caught in red-team testing, an unexpected capability surfaced
late in evaluation, a deployment incident in the wild — the
information first exists at rung 3, inside the lab, in the
internal logs. Outside observers — the AI Safety Institute, the
EU AI Office, the press, the public — depend on what the lab
chooses to disclose, which arrives wrapped in rung-1 framing
(the lab's authority on the meaning of its own incidents).

The loop appears closed. Labs do publish model cards and post-
mortems. But the closure is in form only. The rung-3 evidence
that exists inside is filtered through rung-1 disclosure before
reaching the controllers whose process models it would correct.
This is the same asymmetric pattern as the capital/lab loop, in
a different boundary. It is the structural reason why the press
keeps discovering things about labs that the labs already knew.

### 3.5 The fifth mismatch: antitrust looks at mergers; concentration happens in contracts

Antitrust authorities — the FTC and DoJ in the United States,
DG-COMP in the European Union, SAMR in China — evaluate market
concentration through merger review and conduct cases. Their
process models track mergers and acquisitions, dominant-firm
behaviour, and pricing patterns. The cycle on which they operate
is years. The threshold above which a transaction triggers
review is set in statute.

Concentration in this market, however, does not flow primarily
through mergers. It flows through long-duration exclusive
compute-allocation contracts between hyperscale providers and
frontier laboratories, through bundled tying arrangements between
chip designers and their largest buyers, through grandfathered
grid-interconnection rights at data-centre sites. None of these
trigger merger review, because none of them are mergers. They
happen at the contract level, on a quarters cycle, and they
foreclose entry by smaller actors before any antitrust authority
has cause to look.

This is *cross-loop rung imposition* in the third dangerous-
patterns sense. The rung-2 forum (statutory antitrust review) is
being asked to adjudicate a dispute generated below its threshold
and beneath its cadence, and it cannot. The forum is the wrong
shape for the adjudication. The structural fix is not to make
antitrust faster; it is to give the forum a different statutory
mandate that captures contract-level conduct.

### 3.6 What having five mismatches in hand changes

A strategic essay can speak generally about "the AI industry's
governance problem." Naming five specific mismatches changes the
conversation in three ways.

It changes what is observable. Once we know that the lab/capital
loop is asymmetric, we can look for the symptom: capability
claims that survive funding rounds but not independent evaluation.
We can know what *would* falsify the diagnosis, and what *would*
confirm it.

It changes what counts as a remedy. A general call for "better
AI governance" is not a remedy. A specific structural intervention
that turns an asymmetric loop into a symmetric one — say, by
inserting a statutory pre-deployment evaluation channel that does
not pass through the lab's own benchmark selection — is a remedy.
The intervention does not depend on anyone changing their mind;
it changes the architecture.

It changes what survives political turbulence. Personal commitments
and voluntary frameworks last as long as the people and the
incentives that sustain them. Structural changes — new statutes,
new institutions, new contractual rules — last as long as the
political settlement that created them, which is typically much
longer. The remedies the engineering literature catalogues are
the structural kind.

We turn now to what specifically goes wrong when these mismatches
are not addressed.

## 4. The nine ways the system can fail

A loss scenario, in the engineering vocabulary, is a description of
how a particular bad outcome arises from particular failures inside
the structure. It names the controllers whose process models go
wrong, the feedback channels that go missing or get filtered, the
controlled processes that drift into states from which exit is
costly, and the external disturbances that finish the job. A loss
scenario is, in effect, a small story about *how* the system
produces harm, told in the language of its own architecture.

The full analysis identifies nine such scenarios for the AI system.
They are not predictions. Each of them describes a pathway by which
a specific identified harm could be produced, traceable to specific
mechanisms one could intervene on. Some pathways are already partly
running; others are latent. None is inevitable. The analytic
purpose of writing them down is to attach each remedy to a specific
failure pathway, so that the policy debate has a structural rather
than a rhetorical anchor.

### 4.1 Concentration entrenches at the infrastructure layer

The first scenario is about how AI's economic gains end up
concentrated in the hands of a small number of firms — but not
through the obvious channel one would expect.

Antitrust authorities, as we saw in section 3.5, look at mergers.
They look in the wrong place. The actual mechanism of concentration
is contractual. A hyperscale cloud provider signs a multi-year
exclusive capacity agreement with a frontier laboratory. A chip
designer commits its leading-edge supply, a year ahead, to its
three largest buyers. A foundry pre-allocates capacity windows.
A data centre receives a grid-interconnection right while smaller
applicants sit in a queue. Each of these is a single transaction
that, on its own, looks like ordinary commerce. None of them
crosses a merger threshold. None of them appears in any one
controller's process model as concentration.

The cumulative effect is foreclosure. Smaller laboratories,
open-weights publishers, application companies that depend on
non-frontier compute, all find that the affordable supply has been
contracted away in advance. Entry becomes a financial impossibility.
The controlled process — the structure of the AI infrastructure
market — moves to a state from which exit is costly: the contracts
have already been signed; the grid interconnections have already
been allocated; the leading-edge fab capacity is forward-booked
for years.

The corrective channel exists, in principle. Concentration ratios,
prices, and entry rates are measured. But they are measured at the
slow rate at which antitrust evidence accumulates — over years —
while the foreclosing transactions happen quarterly. By the time
the evidence is strong enough to act on, the architecture is
already locked in. The remedy class is *cadence-matched controls*:
rules that fire on the transaction cycle, not on the evidence
cycle. The specific remedies in the catalogue are reservation
requirements on leading-edge supply (a defined fraction must be
sold to non-frontier customers), an expedited review window on
long-duration contracts during defined capability-jump moments,
and a merger-review reform that captures contract-level
foreclosure in the same statutory net as ordinary M&A.

### 4.2 Lab safety frameworks become ceremonial

The second scenario follows directly from the first and second
mismatches, working together. Capital pressures laboratories to
release on a fast cadence to defend market share. The laboratories'
safety frameworks claim deliberative legitimacy. The frameworks
are amended between releases, in response to commercial pressure,
to allow the next release. The amendment process is internal; the
legitimacy claim is external. The gap widens each cycle.

The damage here is not principally that any particular release is
unsafe. It is that the legitimacy claim erodes. Each visible
amendment to a safety threshold, each evaluation that produces a
result the lab finds inconvenient and reframes, each model that
ships with caveats no external party could have written, drains
the rung-6 reservoir the labs implicitly drew on when they
published their first safety frameworks. At some point the public
notices that the frameworks are advisory, the amendments are
unilateral, and the claims are aspirational. When that happens,
the labs can no longer issue legitimate safety assurances of any
kind.

The remedy class here works in two directions at once. It
*lowers the claim*: the lab admits, structurally, that its
frameworks are self-binding rung-1 commitments — useful, but
limited. It *raises the operation*: an external evaluator with
statutory authority enters the loop. The specific remedies in
the catalogue are mandatory pre-deployment evaluation by an
independent body (the AI Safety Institutes are early examples,
operating today as voluntary partners but candidates for
statutory upgrade), structural separation of safety governance
from commercial governance inside labs, and a capital-structure
mission-constraint mechanism that gives a public agent — a
state attorney general, a regulator — standing to enforce the
mission constraint, rather than relying on shareholder
litigation that will never come.

### 4.3 Workers cannot keep up with capability deployment

The third scenario is about the labour market and runs through the
third mismatch. Capability deploys on a months cycle — model
release, application integration, deployment in customer workflow.
Labour ministries' instruments — retraining programmes, curriculum
updates, unemployment-insurance schemes — operate on a years cycle.
Cohort-specific damage to early-career cognitive workers — the
hardest-hit group because their tasks are most substitutable —
is invisible in the headline employment statistics that
ministries track.

The corrective channel is structurally late. By the time the
employment data shows a problem, the cohort the data described
has already entered the labour force, found that the entry-level
roles they trained for are gone, and either dropped out, accepted
underemployment, or organised politically. The political channel
operates at rung 0 (electoral backlash) on a fast timescale that
the rung-3 statistical channel cannot match. The rung-0 channel
arrives, in other words, exactly when the rung-3 channel was
supposed to have prevented its arrival.

The remedy class is *automatic stabilisers* indexed to a fast
benchmark of task displacement, not to headline employment.
Indexed unemployment insurance, indexed earned-income tax credit,
indexed retraining credits: instruments whose triggers fire
without requiring legislative confirmation per cycle. To these
add cohort-specific transition programmes for the early-career
group — recognising that the affected cohort changes year by year
as substitution sweeps through different occupations — and
portable benefits that decouple healthcare and pension continuity
from continuous employment with a single employer. None of these
require new theory; they require the index, the statutory trigger,
and the political decision to commit ahead of the displacement
rather than after.

### 4.4 The productivity surplus accrues to capital and stays there

The fourth scenario is the distributional one. Suppose the
productivity gain from AI is real — every careful estimate
suggests it is, on the order of fractions of a percentage point
per year of GDP growth, possibly more. The question is who
receives it.

The mechanisms by which a productivity gain reaches workers, as
wages, depend on labour bargaining power. The mechanisms by
which it reaches consumers, as lower prices, depend on
competitive markets. The mechanisms by which it reaches the
public, as taxation, depend on a fiscal architecture calibrated
to the new factor shares. None of these is automatic. If
labour's bargaining power falls (because AI substitutes for
substitutable cognitive tasks), the wage channel narrows. If
markets concentrate (scenario 4.1), the price channel narrows.
If tax instruments calibrated to corporate income do not adjust
for the shift toward AI-as-capital that flows to less-taxed
bases, the public channel narrows.

The structural diagnosis is that no controller in the existing
system is positioned to act on cross-sectoral productivity-gain
capture as such. Tax authorities track corporate income, capital
gains, and payroll — three categories that together miss the
factor-share shift. There is, in the engineering vocabulary, a
*controller absent* from the loop. The remedy class is to add
one: a transmission mechanism, of which the catalogue lists
four candidates — a productivity-indexed dividend (analogue:
Alaska Permanent Fund, but indexed to AI productivity rather
than oil), a value-added tax on AI inference with hypothecated
dividend, an expanded earned-income tax credit indexed to the
displacement benchmark, and sovereign-wealth participation in
AI infrastructure with public dividend.

These are not interchangeable. The productivity-indexed dividend
is conceptually clean but politically the hardest to land. The
inference VAT is operationally simpler because it taxes the
visible economic flow. The EITC expansion is the most familiar
because the instrument already exists. Sovereign-wealth
participation requires a fund and a governance mechanism; some
jurisdictions have one (Norway, Singapore, the Gulf), the United
States does not.

The point is not which one is correct; it is that without at
least one of them, the productivity surplus has no transmission
channel to labour, consumers, or the public. It will accrue to
capital not because capital is rapacious but because capital is
the only controller in the loop with a defined claim on it.

### 4.5 The open-weights price-setting mechanism collapses

The fifth scenario concerns a controller most strategic essays do
not name as a controller at all: the open-weights ecosystem.
Chinese laboratories and a handful of Western publishers release
model weights free for download. The releases serve many purposes,
but at the system level they perform one specific function: they
set a price ceiling on the model layer. Frontier laboratories
cannot price closed-weight inference far above what an
adequately-equipped competitor can do with a recent open-weight
release. The ceiling exists.

If the ceiling collapses, the model layer becomes a place where a
small number of closed-weight providers can extract whatever the
market will bear. The collapse can happen in three ways. Western
governments could regulate open-weights releases out of existence
— well-intentioned, on misuse-risk grounds, without recognising
that the regulation also removes the price-setting mechanism.
Capital could flee the few Western open-weights labs whose
business is harder than their closed-weights competitors',
leaving Chinese labs as the only credible open-weights suppliers
— at which point the political acceptability of using their
weights becomes a separate concern. Or Chinese labs could shift
strategy and stop releasing open weights, for reasons of their
own, and no one outside has the leverage to insist.

The diagnostic point is that the open-weights ecosystem performs
a function that no controller is assigned to protect. Regulators
treat open weights primarily as a misuse risk; market participants
treat them as a competitive threat or competitive crutch. No body
publishes a measure of the frontier-versus-open-weights gap as a
system-level state variable that regulators are obliged to
consider. The remedy class is what the dangerous-patterns
catalogue calls *domain-appropriate rung containment*: route
open-weights questions to a forum that holds both misuse risk
and price-setting in superposition, and require any rule
affecting open weights to document its impact on the gap.
Concretely: publish the gap, calibrate misuse-risk rules narrowly
enough to preserve the ecosystem below those thresholds, and
treat the ≤12-month gap as an explicit policy goal rather than
an emergent outcome.

### 4.6 Compute competition escalates to kinetic conflict

The sixth scenario is the most extreme. Compute is geographically
concentrated. Leading-edge logic chips come overwhelmingly from a
single foundry on a single island. Hyperscale capacity is
concentrated across a small number of operators in a small number
of regions. Energy and grid interconnections are concentrated
where electricity is cheap. The geography of AI infrastructure
is fragile in ways the geography of, say, the global oil supply
once was — a small number of physical chokepoints whose
disruption would stop the flow.

National security apparatuses on both sides of the US–PRC
relationship watch each other's compute build-out. Each side's
process model treats the other's build-out as preparation for
adversarial use. The defensive interpretation — each side is
building because each side fears being shut out — is filtered out
on both sides by the rung-1 strategic identity that does not
admit the other's defensive logic. There is no confidence-building
channel at the AI-infrastructure level. The only available
channels are coercive (export controls, sanctions, designations)
and rhetorical (state speeches).

A scenario in which a regional crisis, perhaps unrelated to AI
itself, transmits directly into the AI-infrastructure layer is
not implausible. A blockade or a strike that disrupts foundry
output. A sanctions package that pulls one side into commercial
escalation. A reciprocal designation that classifies a category
of research on both sides simultaneously. Each step is small; the
cumulative path is from rung-2 rule-making through rung-0 coercion
toward kinetic action.

The remedy class here is the hardest in the catalogue and the
most important. An independent inspection or observation regime
for AI-infrastructure deployments — analogous to the IAEA for
nuclear material, the OPCW for chemical weapons, or the now-
defunct Open Skies regime — would provide a rung-3 verification
channel that bypasses the rung-1 filter on both sides
simultaneously. It would not solve the conflict; it would create
a forum in which evidence about the system's actual state could
enter both sides' decision-making, reducing the chance that
either side acts on a process-model error. The argument for
such a regime, in the engineering vocabulary, is structural
rather than rhetorical: the conflict is being driven by mutual
process-model error, and only a r3 channel external to both
sides can correct mutual error symmetrically.

This will not be built quickly. It depends on a precondition —
shared technical vocabulary about what AI-infrastructure
verification could even mean — that current track-1.5 dialogues
are only beginning to produce. It depends, further, on
geographic diversification of fab capacity, so that verification
has somewhere to look that is not already monopolised. The
sequencing is therefore: track-1.5 dialogue first (months), fab
diversification in parallel (years), inspection regime later
(decade).

### 4.7 The Chinese mirror

The seventh scenario is a specific consequence of the second,
mirrored across the bloc boundary. Inside the Chinese state-lab
system, the same Pattern A asymmetric loop operates that we
identified in section 3.2 between US capital and US labs. The
party centre receives capability evidence from PRC labs filtered
through r1 mission-conformant disclosure; PRC labs cannot, in
their own internal process, fully separate r3 evidence from r1
authority because the r1 structure is constitutive rather than
contingent.

The damage is symmetric to what happens in the US case, with one
critical difference. The US side is open enough that external
r3 channels (independent benchmarks, AISI evaluations, academic
critique) can in principle reach the apex. Whether they do
depends on whether structural separation is enforceable. The
Chinese side has no equivalent external channel: the structure
that produces the asymmetry is the same structure that excludes
external correction.

The implication is uncomfortable but operationally important.
Unilateral remedies on the US side can produce evidence that
PRC analysts read; capability claims that survive Western r3
evaluation also survive their own internal r1 wrapping. An
externalised r3 channel becomes a correction channel for both
sides at once. But the only remedy that works *directly* on the
PRC side is a bilateral one — an inspection regime of the kind
described in scenario 4.6, which exists outside both national
hierarchies. This is one of several reasons that the bilateral
remedies are higher-leverage than they appear.

### 4.8 The information environment degrades faster than authentication scales

The eighth scenario is about epistemics. The volume of AI-
generated content already exceeds the capacity of human readers
to authenticate it manually and is approaching the capacity of
automated detection systems to track it. Provenance signals
exist — cryptographic content credentials, watermarking — but
their adoption is voluntary, and adversarial actors strip them
at low cost. Information platforms whose business model is
engagement-driven amplification have no incentive to favour
verified content over high-engagement AI content; moderation, if
it happens, imposes a unilateral cost on a single platform in a
multi-platform competition for attention.

The structural diagnosis is that the controlled process — the
information environment — is moving to a state in which trust
in *any* signal degrades trust in *all* signals, and from that
state recovery is difficult. The corrective feedback channel
(measurement of provenance failure rates) does not exist at the
aggregate level; only individual incidents are tracked. The
controller responsible (information regulators) tracks takedowns,
not aggregate state.

The remedy class is to move provenance from the platform layer
(where it can be stripped) to the capture layer (camera, OS) and
the transmission layer (model output API, where it can be
cryptographically attested). To this add a statutory regime for
aggregate measurement of provenance-failure rate, so that the
question "is the information environment getting worse, by how
much" can be answered. Watermarking alone is insufficient; the
analogy is with seatbelt laws — voluntary mechanisms have a
ceiling; mandatory mechanisms with measurement do not.

### 4.9 Rules calibrated to capability tiers already obsolete

The ninth scenario is the regulatory cadence one, mirrored.
Legislatures pass AI rules calibrated to a defined capability
threshold — typically a specific compute or capability level
named in the statute. Algorithmic-efficiency improvements move
the threshold under the rule by a factor of three or four every
year. The regulator's process model treats the threshold as a
fixed boundary; in reality it is a moving target. Five years
after the rule passes, the rule applies to capabilities the
intended scope did not anticipate, while capabilities that match
the intended scope have moved into a less-regulated regime.

The corrective mechanism — recalibration — depends on
re-passage of primary legislation, which requires legislative
attention that is itself rationed. By the time the rule is
re-passed, the threshold has moved again. The remedy class is
to write rules whose thresholds move with a published benchmark,
and to grant a standing body the authority to recalibrate without
primary legislation, subject to a notice-and-comment process.
This is not novel — securities regulators in many jurisdictions
recalibrate margin and capital requirements without primary
legislation — but it requires a deliberate political decision to
delegate, and the political appetite for delegation varies by
jurisdiction.

### 4.10 What having nine scenarios gives us

Nine scenarios is more than a strategic essay would provide and
fewer than the underlying analysis admits. The number is roughly
right because each scenario corresponds to one identifiable
failure mechanism. Together they cover all the unsafe control
actions catalogued in the analysis; each remedy class points at
specific UCAs whose failure pathway it interrupts.

The nine scenarios are not independent. Scenario 4.1
(concentration) makes scenario 4.4 (surplus capture) worse.
Scenario 4.2 (ceremonial safety) makes scenario 4.8
(epistemic degradation) worse. Scenarios 4.6 and 4.7 (the
geopolitical pair) interact symmetrically with each other. The
remedies, in turn, are not independent: as we will see in the
next section, several of them share preconditions, several form
sequencing chains, and the structurally hardest remedies are
exactly those whose absence would cost the most to live with.

## 5. What can be done

Twenty-two specific remedies follow from the analysis. They
divide into five families, each addressed at one or more of the
nine loss scenarios. The family-level summary first; then the
sequencing.

The first family is *measurement and feedback channels*. Several
of the most damaging mismatches occur because the system lacks an
honest measurement of its own state. Regulators do not know the
frontier-versus-open-weights gap; nobody publishes the aggregate
provenance-failure rate; labour ministries track headline
employment but not task-by-task displacement. Four remedies fill
these channels: a quarterly assessment of the open-weights gap, a
quarterly aggregate provenance-failure measurement, a task-
displacement benchmark indexed by occupation cohort, and a
track-1.5 dialogue process that builds shared technical
vocabulary between the US and PRC technical communities about
what AI-infrastructure verification could mean. Each of these is
operationally close to existing instruments and politically
modest. Each of them, however, is a precondition for remedies in
later families.

The second family is *rules built on the new measurements*. Once
the open-weights gap is published, a targeted misuse-risk regime
can be calibrated narrowly enough to preserve the ecosystem
below those thresholds. Once the provenance-failure rate is
measured, mandatory provenance becomes specific rather than
gestural. Once the task-displacement benchmark exists, automatic
stabilisers — unemployment insurance, retraining credits, EITC
top-ups — can be indexed to it, so that triggers fire on the
fast cycle that the disturbance arrives on. Reservation
requirements on leading-edge supply, capability-tier rules
indexed to a moving benchmark with sunset clauses, and a
standing recalibration authority for AI rules each address a
specific identified pathway. A mandatory pre-deployment
evaluation regime — turning the AI Safety Institutes from
voluntary partners into statutory ones — closes the asymmetric
loop between labs and capital.

The third family is *structural remedies*. These are the
interventions that change the architecture rather than the
operating parameters. Merger-review reform that captures
contract-level foreclosure. Structural separation of safety
governance from commercial governance inside frontier
laboratories. A statutory public-benefit-corporation class with
mission constraints enforceable by a public agent, not by
shareholder litigation. Cohort-specific transition programmes
for early-career cognitive workers. Portable benefits that
decouple healthcare and pension continuity from continuous
employment. A value-added tax on inference, hypothecated to a
public dividend. Sovereign-wealth participation in AI
infrastructure, where the jurisdiction has a fund. These are
harder to land politically and slower to take effect, but each
of them addresses a structural failure that no operating-
parameter adjustment can fix.

The fourth family is *the slow geopolitical remedies*. Three of
the most consequential remedies operate on a decade horizon
because their preconditions are physical or diplomatic.
Geographic diversification of fab capacity — bringing leading-
edge logic-chip production to a strategically meaningful share
outside the present chokepoint — is funded but slow; the
constraint is sustained political commitment across electoral
cycles. The independent inspection or observation regime for
AI infrastructure depends on shared technical vocabulary, which
the track-1.5 process slowly produces, and on geographic
diversification, so that verification has somewhere to look that
is not already monopolised. A productivity-indexed dividend, of
the Alaska-Permanent-Fund kind but indexed to AI productivity,
operates on a decade horizon because it requires both a fiscal
instrument (which the inference VAT could provide) and a
governance mechanism (which sovereign wealth could provide).
Each of these is the long-cycle remedy whose absence the others
cannot make up for.

The fifth family is *the politically novel ones*. Two remedies
do not fit cleanly into any of the four prior categories. An
expedited capability-jump merger-review window, granting
antitrust authorities a temporary hold on long-duration compute
contracts during defined capability-jump moments, is a small
intervention with a precise function but no real precedent. An
employer-independent benefits regime is operationally familiar
but politically contested in jurisdictions where employer-tied
benefits define the post-war social contract. These are listed
separately not because they are less important, but because they
require political adoption on terms the system does not yet
provide.

### 5.1 The four-phase sequence

The 22 remedies do not all enter the world at once. They enter
in a specific order constrained by the dependency graph among
them, and the analysis derives a four-phase implementation plan.

The first phase, months one through eighteen, is measurement.
The four feedback-channel remedies — the open-weights gap, the
provenance-failure rate, the task-displacement benchmark, the
track-1.5 dialogue — can begin without statutory change. An AI
Safety Institute could initiate the open-weights gap publication
tomorrow, as a non-binding research output. A national statistics
office could establish a provenance-measurement programme on
existing authority. A labour-statistics office could publish a
task-displacement index using existing labour data and AI task
mapping. The track-1.5 dialogue is already running in several
forums; sustaining and broadening it requires nothing more than
philanthropic funding and continued attention. By month twelve,
each of these channels will have produced a first batch of
evidence; by month eighteen, the question of whether to formalise
each one statutorily will have a real answer.

The second phase, months twelve through forty-eight, builds rules
on the new feedback channels. This is where most of the
operationally familiar remedies sit: indexed automatic
stabilisers, indexed EITC, mandatory provenance, reservation
requirements on leading-edge supply, capability-tier rules with
sunset clauses, a recalibration authority, mandatory pre-
deployment evaluation, a targeted misuse-risk regime for open
weights. Each of these is a piece of legislation or a regulation
written against a measurement that the first phase produced. Each
is operationally close to existing instruments. Each requires
political work but not novel theory.

The third phase, months thirty-six through eighty-four, is the
structural remedy phase. Merger-review reform, structural
separation of lab safety and commercial governance, the statutory
PBC class with public-agent enforcement, cohort-specific
transitions, portable benefits, the inference VAT with
hypothecated dividend, sovereign-wealth participation. These
require political capital that the first two phases will have
generated, and an empirical record that shows whether the
operating-parameter remedies were sufficient on their own (the
analysis suggests they will not be, but the evidence by month
thirty-six will be specific). Each of these is structurally novel
and politically harder than the second-phase remedies; each
addresses a pathway the second-phase remedies cannot close.

The fourth phase, months sixty through one hundred and forty-four,
is the long-cycle remedy phase. Fab diversification will already
be running in parallel; what completes in this phase is the
inspection regime, the productivity-indexed dividend, and the
expedited capability-jump review window if it has not already
been adopted. These are the remedies whose absence imposes the
largest tail cost — concentration unbroken, geopolitical
escalation unverified, surplus capture untransmitted — and whose
adoption is hardest because their political horizon exceeds
electoral cycles.

The decision-memo companion to this chapter sets out the
dependency graph in full and identifies, at each phase boundary,
the question that the prior phase must have answered before the
next phase becomes feasible. By month twelve: did anyone publish
the open-weights gap? By month eighteen: is the displacement
benchmark stable? By month thirty-six: have at least three of
the eight phase-two rules been adopted? At each decision point,
the analysis describes both what success looks like and what
failure implies for downstream sequencing. This is what
distinguishes a planning artefact from a wish list.

### 5.2 The non-state actor's leverage

The remedies are not, as a class, things that one private actor
can do alone. They are political and statutory. But several of
them have entry points where a non-state actor — a foundation, a
research institute, a coalition of application companies, a
group of labour organisations — can move first and, by moving
first, make the statutory work tractable.

Phase-one measurement is the cleanest example. Each of the four
channels can be initiated as a non-binding publication; once the
data exists, the statutory mandate becomes specific rather than
gestural. Drafting model-bill language for phase-two rules is
work that legal-policy institutes do well, and adoption rates of
model-bill language are unusually high in jurisdictions where
the legislature is overstretched. Coalition-building among
open-weights-dependent companies is work that market participants
can do without waiting for political alignment. Track-1.5
dialogue is the canonical philanthropic-funded geopolitical
intervention; it is not a substitute for state action, but it
produces the vocabulary state action requires.

The leverage point for any non-state actor, then, is to ask
which of the 22 remedies in which phase has an entry point that
matches the actor's position, and to commit to the entry-point
work for at least one full decision cycle. The dependency graph
makes the leverage points explicit; it also makes clear which
work, however well-meaning, is not on the critical path.

### 5.3 Reversibility

A final consideration constrains the remedy set. Most of the
proposals are reversible at moderate cost within their first
cycle. Statistical publications can be discontinued. Indexed
triggers can be recalibrated. Pre-deployment evaluation
requirements can be relaxed. Reservation requirements can be
adjusted. This is structurally important because it means a
risk-averse stakeholder can support phase-one and most of
phase-two with limited downside. The risk of getting the rule
wrong is not the risk of locking in an error.

The exceptions are the structural and slow-cycle remedies. Once
established, an inspection regime is hard to withdraw because
withdrawal would itself signal an escalation posture. Sovereign-
wealth participation in AI infrastructure cannot be unwound
without selling at unfavourable timing. Fab diversification is
sunk capital. A productivity-indexed dividend, once it becomes a
household income source, is politically irreversible in practice.
A loss-averse stakeholder considering tail risks — the kinetic-
escalation risk in scenario 4.6, the cohort-displacement risk in
scenario 4.3 — would weight these irreversible remedies more
heavily despite their cost. A risk-averse stakeholder weights
phase-one and phase-two preferentially.

The point of putting reversibility in the analysis explicitly is
that different stakeholders, with different risk tolerances,
will rank the same remedies differently. The analysis does not
adjudicate the ranking. It surfaces the trade-off so that the
adjudication can happen on terms a deliberative process can
accept.

## 6. What the analysis does not do

A method that produces twenty-two specific remedies is also a
method that risks being read as a forecast or a manifesto. It is
neither, and it is worth being explicit about what the limits are
before closing.

It does not predict which of the nine loss scenarios will occur,
or in what combination, or on what timescale. The scenarios are
*possibility statements*: each one describes a pathway from the
current structure to a specific bad outcome, and the structure
does in fact have those pathways. Whether the outcomes occur
depends on which control actions are issued, by which controllers,
in which sequence, and with what feedback. The analysis maps the
terrain; it does not tell the reader how the journey ends.

It does not settle value disputes. The remedies are derived from
the loss scenarios, and the loss scenarios are derived from
stakeholder-named losses. Different stakeholders would name
different losses. A reader who does not consider concentrated
ownership of the AI substrate to be a loss — perhaps because they
believe the firms in question are well-governed and well-
intentioned — will not find scenario 4.1 a problem and will not
weight remedies R-1 through R-3 highly. The analysis cannot
adjudicate that disagreement; it can only show that *if* the
loss is taken to be a loss, *then* certain remedies follow with
specific properties. The reader's own values determine which
"ifs" are live.

It does not tell any particular government or firm what to do.
Decisions belong to controllers; the analysis describes what
each controller could in principle do and what consequences each
choice would have for the controlled processes. A decision-memo
addressed to a specific stakeholder — say, a foundation
allocating its grant budget over five years, or a labour union
prioritising its lobbying agenda, or a cabinet office choosing
between policy packages — would be a different document, derived
from this analysis but committing to that stakeholder's goals
and constraints.

It does not, finally, exhaust the possible failure modes of the
AI system. The analysis is a first cycle in the engineering
sense: every loss scenario is one that the controller / control-
action / feedback / process-model decomposition can surface.
There may well be failure modes that this decomposition cannot
see — failures that emerge from interactions across multiple
loops simultaneously, failures that depend on non-controllers
the analysis treats as environment, failures whose causes lie
below the threshold of the current decomposition. A second cycle,
with refined boundaries and a tighter decomposition, would find
some of these. The analysis we have is bounded in the way every
engineering analysis is bounded: by the granularity at which
the system was modelled.

## 7. Coda: the question reformulated

We started with three questions: about jobs, about power, about
geopolitics. The structured analysis allows us to reformulate
each of them in a way that points at action.

The jobs question — *will AI cause mass joblessness or freer
prosperity?* — is, structurally, the question of whether the
labour-policy cycle (years) will be brought into alignment with
the capability-deployment cycle (months) before the cohort
displacement that the mismatch produces becomes irreversible.
The technology produces the surplus; the institutions decide
whether the surplus reaches workers, consumers, the public, or
only capital. The analysis identifies the specific instruments
that would close the cycle gap (indexed automatic stabilisers, a
displacement benchmark, cohort-specific transitions, portable
benefits) and the specific instruments that would transmit the
surplus (the inference VAT, the productivity-indexed dividend,
the EITC top-up, sovereign-wealth participation). Whether any
of these is adopted is a political choice made under known
trade-offs — not, as the strategic essay would have it, an open
question with a wide range of plausible answers.

The power question — *will a few firms own everything?* —
becomes, structurally, the question of whether the contract-level
foreclosure mechanism currently moving compute infrastructure
into a small number of hands is captured by an antitrust regime
calibrated to the right cadence and the right threshold. The
analysis identifies merger-review reform, reservation
requirements on leading-edge supply, and an expedited capability-
jump review window as the specific instruments. It also
identifies the open-weights ecosystem as a price-setting
mechanism whose suppression would be the worst single thing that
could happen at the model layer, and identifies the specific
regulatory pathway (well-meaning misuse-risk regulation that
fails to recognise the price-setting function) by which the
suppression could occur.

The geopolitics question — *will the US–PRC AI competition
escalate?* — becomes, structurally, the question of whether a
rung-3 verification channel can be installed between the two
blocs before mutual process-model error converts a series of
rung-2 coercive moves into a kinetic exchange. The analysis
identifies track-1.5 dialogue as the precondition, fab
diversification as the parallel constraint, and an
infrastructure-inspection regime as the long-cycle remedy. It
also identifies the symmetric Pattern-A failure on both sides
that makes mutual error structurally likely, and explains why
unilateral US-side remedies (especially mandatory pre-deployment
evaluation) produce evidence that bypasses the rung-1 filter on
the PRC side as well, making them more valuable than they appear
when each is considered in isolation.

None of these reformulations resolves the questions. Each of them
turns a forecasting question into a structural question, and a
structural question is one a deliberative process can act on. A
political community that refuses to take action on a forecasting
question — because the future is uncertain, because experts
disagree, because the right thing to do is unclear — can take
action on a structural question, because the structural question
is not "what will happen" but "what feedback channels are missing
and what institutions are needed to install them." The first
question admits indefinite postponement; the second does not.

That, finally, is what an engineering reading offers that an
essay does not. The engineering reading produces a list of
specific things that could be done, in a specific order, by
specific actors, with specific costs and specific reversibility
profiles. It does not promise that any of them will be done. It
does promise that, if one of them is done, the system will
respond in the way the analysis predicts — because the
prediction is not a guess about behaviour but a derivation from
structure.

Whether the structures change is, in the end, the same question
as whether the political communities affected by AI choose to
change them. The technology will not make the choice. Capital
will not make the choice. The labs will not make the choice. The
choice has to be made by the controllers whose process models
the structural analysis maps and whose feedback channels the
remedies repair. And the choice can only be made if the
controllers see the structure clearly enough to know which
levers exist.

This chapter has tried to make the structure visible. The rest
is up to whoever is reading.
