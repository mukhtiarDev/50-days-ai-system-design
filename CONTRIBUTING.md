# Contributing

Thanks for improving this learning repository.

## Content standards
- Keep lessons practical, technically accurate and understandable to an early-career engineer.
- State assumptions and distinguish a logical diagram from a deployable topology.
- Prefer technology-neutral concepts; when naming a vendor or framework, explain why it fits.
- Include failure handling, security, scaling and trade-offs—not only the happy path.
- Use Mermaid for architecture diagrams and fenced code blocks for contracts/queries.
- Do not add credentials, personal data, proprietary documents or unlicensed content.

## File naming
`lessons/<track>/<day>-<short-kebab-case-title>.md`

Days are globally numbered from `01` through `50`. Do not reuse a day number.

## Local checks
```bash
python scripts/validate.py
python -m unittest discover -s tests -v
```

## Pull requests
Describe the problem, affected lesson numbers, technical sources checked and how you validated the change. For architecture changes, include alternatives and consequences.
