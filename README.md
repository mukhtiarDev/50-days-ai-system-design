# 50 Days of AI System Design & Architecture

A structured, implementation-oriented portfolio course covering fundamentals, advanced distributed-system design and end-to-end AI product architectures.

## Tracks

| Track | Days | Focus |
|---|---:|---|
| `lessons/basics/` | 1–15 | Requirements, APIs, data, scaling foundations and distributed-system fundamentals |
| `lessons/advanced/` | 16–30 | Reliability, security, operations, performance and architectural decisions |
| `lessons/use-cases/` | 31–50 | AI platforms and complete product case studies |

## Learning approach

Read one lesson, sketch the architecture yourself, challenge the assumptions, then complete the practical exercise. The diagrams are logical reference architectures; they are not prescriptions to deploy every box as a separate service.

## Repository structure

```text
.
├── lessons/
│   ├── basics/       # Days 01–15
│   ├── advanced/     # Days 16–30
│   └── use-cases/    # Days 31–50
├── scripts/
│   └── validate.py
├── tests/
├── .github/workflows/
├── README.md
├── ROADMAP.md
├── PROGRESS.md
└── CONTRIBUTING.md
```

## Suggested pace

- Days 1–15: establish requirements, API and data fundamentals.
- Days 16–30: reason about scale, security, reliability and operations.
- Days 31–50: apply the ideas to realistic AI and non-AI product architectures.

## Prerequisites

Basic programming, HTTP, SQL and familiarity with a backend application are helpful. You do not need a cloud account. Most exercises can be completed with diagrams, local Python/SQLite/PostgreSQL and lightweight test services.

## Validate locally

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
```

## Daily publishing

This archive contains all lesson source files up front. A separate central scheduler can publish one lesson every three days across multiple repositories. Do not enable independent daily publishing workflows in each target repository, or they may publish on the same day. See `docs/GITHUB_AUTOMATION_SETUP.md` for the intended central-scheduler design.

## Disclaimer

This is educational material, not a substitute for security review, production capacity testing or domain-specific compliance advice. Validate current product/vendor limits before deployment.
