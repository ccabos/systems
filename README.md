# Systems Thinking — From SE to STPA

Applying Systems Engineering Decomposition, Product Line Thinking, and STPA to Social and Technical Systems.

## Website

The book is published at [https://ccabos.github.io/systems/](https://ccabos.github.io/systems/)

## About

This book explores a single idea: the tools we use to engineer safe aircraft and reliable software apply with surprising precision to human institutions — political regimes, religions, corporations, families, and development methodologies.

Three frameworks, layered:

1. **Five-Level SE Hierarchy** — Goals → Requirements → Functions → Logical Architecture → Physical Implementation
2. **Product Line Thinking** — Platform, variation points, and reuse across system types
3. **STPA** — System-Theoretic Process Analysis for identifying unsafe control actions

## Structure

```
├── docs/
│   ├── index.md                    # Home page
│   ├── part1/                      # Foundations
│   │   ├── se-hierarchy.md         # The five-level decomposition
│   │   ├── product-lines.md        # Platform & variation points
│   │   └── stpa-introduction.md    # STAMP and STPA
│   ├── part2/                      # Social Systems
│   │   ├── religion.md             # The founding decomposition
│   │   ├── kingdom-republic.md     # Reuse analysis
│   │   ├── ten-systems.md          # Full comparative analysis
│   │   ├── platform.md             # The social system platform
│   │   └── variation-points.md     # Six variation points
│   ├── part3/                      # Development Frameworks
│   │   ├── frameworks.md           # Eight frameworks decomposed
│   │   ├── framework-platform.md   # Ten functional slots
│   │   └── hybrids.md              # Three hybrid architectures
│   ├── part4/                      # STPA Applied
│   │   ├── religion-stpa.md        # Full STPA on religion
│   │   ├── control-structures.md   # Control architectures compared
│   │   └── remedies.md             # Design principles
│   └── about.md
├── mkdocs.yml                      # MkDocs configuration
└── .github/workflows/deploy.yml    # GitHub Pages deployment
```

## Local Development

### Prerequisites

- Python 3.x

### Installation

```bash
pip install mkdocs mkdocs-material pymdown-extensions
```

### Local Server

```bash
mkdocs serve
```

The site is available at `http://127.0.0.1:8000`

### Build

```bash
mkdocs build
```

## License

Personal research and documentation project.
