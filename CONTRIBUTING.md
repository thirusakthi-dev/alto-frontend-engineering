# Contributing

Thank you for your interest in contributing to Modern Frontend Engineering.

Contributions are welcome to improve the skill, its reference documentation, examples, and validation tooling.

The goal is to maintain practical, accurate, consistent, and production-focused frontend engineering guidance that works across compatible AI coding agents.

## Getting Started

1. Fork the repository.
2. Clone your fork:

   ```bash
   git clone https://github.com/<your-username>/modern-frontend-engineering.git
   ```

3. Navigate to the project:

   ```bash
   cd modern-frontend-engineering
   ```

4. Create a branch:

   ```bash
   git checkout -b feat/your-change
   ```

## Project Structure

```text
modern-frontend-engineering/
├── SKILL.md
├── references/
├── examples/
├── scripts/
├── evals/
├── CHANGELOG.md
├── CONTRIBUTING.md
├── DEVELOPMENT_PLAN.md
├── PROJECT_STATUS.md
└── README.md
```

- `SKILL.md` — core instructions for the coding agent.
- `references/` — detailed engineering guidance.
- `examples/` — practical implementation patterns.
- `scripts/` — validation and maintenance tooling.
- `evals/` — skill evaluation cases.

## Contribution Guidelines

### 1. Core Skill Instructions

When modifying `SKILL.md`:

- Keep instructions clear, actionable, and concise.
- Focus on agent behavior rather than duplicating reference documentation.
- Preserve compatibility with supported Agent Skills implementations.
- Avoid unnecessary restrictions and repetitive instructions.
- Ensure the skill supports both new projects and existing codebases.

### 2. Reference Documentation

When adding or updating reference files:

- Keep content technically accurate and practical.
- Explain important decisions and trade-offs.
- Prefer established engineering practices over personal preferences.
- Include implementation guidance where it adds value.
- Avoid unnecessary complexity, repetition, and outdated recommendations.
- Update related documentation when changing shared guidance.

### 3. Examples

Examples should:

- Demonstrate realistic implementation patterns.
- Follow the principles described in the relevant references.
- Avoid placeholder-heavy or incomplete implementations.
- Include relevant security, accessibility, and error-handling considerations.
- Remain consistent with the technologies and conventions they describe.

### 4. Engineering Quality

Every contribution should prioritize:

- Correctness and reliability.
- Maintainability and readability.
- Security and accessibility.
- Performance and production readiness.
- Simplicity and justified technical decisions.
- Verification rather than unsupported claims.

Avoid generic AI-generated content, unnecessary abstractions, invented APIs, and unverified implementation details.

### 5. Compatibility

The skill is designed to be agent-independent.

Contributions must:

- Avoid unnecessary dependencies on a single coding agent.
- Preserve standard Agent Skills structure and metadata.
- Keep installation and usage documentation accurate.
- Avoid introducing agent-specific behavior into shared instructions unless clearly documented.

## Development Setup

This project uses Python and `uv` for validation tooling.

Install dependencies:

```bash
uv sync
```

Run the validation script:

```bash
uv run python scripts/validate_skill.py
```

Run individual checks when needed:

```bash
uv run ruff check scripts
uv run ruff format --check scripts
uv run pytest
```

## Commit Guidelines

Use clear, descriptive commit messages.

Suggested prefixes:

- `feat:` — new functionality or guidance.
- `fix:` — corrections and bug fixes.
- `docs:` — documentation changes.
- `refactor:` — structural improvements.
- `test:` — evaluation or validation changes.
- `chore:` — maintenance and tooling.

Examples:

```text
docs: improve accessibility guidance
feat: add frontend security reference
fix: correct Next.js caching recommendations
test: expand skill evaluation cases
```

## Pull Request Process

Before submitting a pull request:

1. Review your changes for correctness and consistency.
2. Run the validation script.
3. Check internal links and documentation references.
4. Update related documentation when necessary.
5. Update `CHANGELOG.md` when introducing notable changes.

In your pull request, explain:

- What changed.
- Why the change is necessary.
- Which files or areas are affected.
- How the changes were verified.

Keep pull requests focused and avoid combining unrelated changes.

## Reporting Issues

When reporting an issue, include:

- A clear description of the problem.
- The affected file or section.
- Steps to reproduce the issue, if applicable.
- Expected and actual behavior.
- Relevant technical references or examples.

## Code of Conduct

Be respectful, constructive, and professional.

Focus discussions on improving technical quality and helping maintain a welcoming open-source project.

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
