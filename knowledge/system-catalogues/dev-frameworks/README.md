# Development Frameworks Catalogue

Case studies of software and product development process frameworks.
Each framework is treated as a specimen of "how to structure
development work" and decomposed with the same tools as any other
system.

## Current members

| Framework | Folder |
|---|---|
| Waterfall | `waterfall/` |
| V-Model | `v-model/` |
| PRINCE2 | `prince2/` |
| Scrum | `scrum/` |
| Kanban | `kanban/` |
| Design Thinking | `design-thinking/` |
| DevOps | `devops/` |
| SAFe (Scaled Agile Framework) | `safe/` |

## Primary sources

Each decomposition should be checked against the framework's own
canonical text. Citation keys resolve in
`knowledge/references/bibliography.md`:

| Framework | Primary source(s) |
|---|---|
| Waterfall | [Royce1970] — note that Royce presented the single-pass sequence as *risky* and recommended iteration; "Waterfall" as a prescribed method is largely a later reading. [Boehm1988] is the classic corrective. |
| V-Model | German federal V-Modell / V-Modell XT publications; [Boehm1988] for the verification-driven lineage |
| PRINCE2 | [Axelos2017] |
| Scrum | [SchwaberSutherland2020] |
| Kanban | [Anderson2010]; upstream lineage in the Toyota Production System [Ohno1988] |
| Design Thinking | [Brown2009] |
| DevOps | [Kim2016]; empirical evidence base in [Forsgren2018] |
| SAFe | [KnasterLeffingwell2020] |

All agile-family frameworks share [Beck2001] as their declared
value base. On evidence quality: [Forsgren2018] is survey-based
research with known methodological limits, and for SAFe in
particular there is little independent peer-reviewed outcome
evidence — its market success is documented; its delivery
superiority is not. Framework claims in this catalogue should be
read as *the framework's self-description* unless a source outside
the framework's own commercial ecosystem is cited.

## Cross-framework material

`cross-framework/` contains material that compares the frameworks: the
shared platform of universal functional slots, the variation points,
the reuse analysis, proposed hybrid architectures, and merging
principles.

## Adding a new framework

Copy `_template/` to a new folder and fill in each file. The template
omits the 6a (is-it-a-system) and 6c (historical-se-interventions)
files because development frameworks are themselves the *intervention*
— they exist to be applied to development projects, so the questions
become "what does the framework prescribe" rather than "how did
SE-like thinking show up historically."
