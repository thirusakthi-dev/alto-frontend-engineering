# Modern Frontend Engineering

A production-focused Agent Skill for building, architecting, improving, debugging, reviewing, and maintaining modern frontend applications.

Designed to help AI coding agents deliver reliable, accessible, secure, maintainable, and production-ready frontend solutions.

Works with both new projects and existing codebases, following the project's actual stack, architecture, requirements, and conventions.

## Installation

Install using the [Skills CLI](https://github.com/vercel-labs/skills).

### Prerequisites

- Node.js and npm.
- A coding agent that supports the Agent Skills format.
- Internet access to retrieve the skill repository.

### Install for All Detected Agents

Run the following command and select the coding agents you want to install the skill in:

```bash
npx skills add thirusakthi-dev/modern-frontend-engineering
```

### Install for a Specific Agent

Use the `--agent` option to target a particular coding agent.

**OpenCode**

```bash
npx skills add thirusakthi-dev/modern-frontend-engineering -a opencode
```

**Claude Code**

```bash
npx skills add thirusakthi-dev/modern-frontend-engineering -a claude-code
```

**Cursor**

```bash
npx skills add thirusakthi-dev/modern-frontend-engineering -a cursor
```

**OpenAI Codex**

```bash
npx skills add thirusakthi-dev/modern-frontend-engineering -a codex
```

Agent identifiers and availability depend on the Skills CLI version. Refer to its documentation for the current supported list.

### Global Installation

Install the skill globally so it can be discovered across projects by the selected agent:

```bash
npx skills add thirusakthi-dev/modern-frontend-engineering -g
```

### Global Installation for a Specific Agent

```bash
npx skills add thirusakthi-dev/modern-frontend-engineering -g -a opencode
```

Replace `opencode` with the identifier of your preferred supported agent.

### Project-Level Installation

To install the skill within the current project:

```bash
npx skills add thirusakthi-dev/modern-frontend-engineering
```

When prompted, choose the project-level installation option and the target agent.

### Verify Installation

After installation:

1. Open your coding agent.
2. Open a frontend project.
3. Ask the agent to use the `modern-frontend-engineering` skill.
4. Verify that it follows the skill instructions and uses the relevant reference documentation.

If the agent does not discover the skill, check its supported skill directory and restart or reload the agent.

### Updating the Skill

To update installed skills:

```bash
npx skills update
```

The CLI updates installed skills where supported. Check the CLI documentation for update behavior and options.

### Uninstalling

Use the Skills CLI to remove an installed skill:

```bash
npx skills remove modern-frontend-engineering
```

Check the CLI prompts and options to select the appropriate agent and installation scope.

### Installation Resources

- [Skills CLI](https://github.com/vercel-labs/skills)
- [Agent Skills Specification](https://agentskills.io/)
- [GitHub Repository](https://github.com/thirusakthi-dev/modern-frontend-engineering)

---

## Overview

Modern Frontend Engineering provides practical engineering instructions and detailed references across the frontend development lifecycle.

It is built around one core principle:

**Build software with engineering judgment, not just generated code.**

The skill guides coding agents to understand the project before making changes, choose justified solutions, implement complete functionality, and verify their work.

It does not assume every task starts from a blank project or force a particular framework, architecture, or technology into existing codebases.

## Key Capabilities

### 1. Project Understanding

- Inspect existing repositories, project structures, and dependencies.
- Understand framework versions and established conventions.
- Identify relevant files before modifying code.
- Follow existing architecture where appropriate.
- Recognize project-specific constraints and requirements.
- Avoid unnecessary rewrites and migrations.

### 2. Frontend Development

- React engineering.
- Next.js App Router.
- TypeScript and code quality.
- Application architecture and project structure.
- Reusable UI components and frontend modules.
- State management and data fetching.
- Package selection and ecosystem evaluation.

### 3. UI/UX Engineering

- UI design quality and visual consistency.
- Responsive layouts and navigation.
- Accessibility and WCAG.
- Theming, dark mode, and design systems.
- Internationalization and RTL.
- Dialogs, modals, and overlays.
- Notifications and push support.

### 4. Application Development

- API integration and error handling.
- Forms and validation.
- Authentication and authorization.
- Role-based access control (RBAC).
- SEO and discoverability.
- Progressive Web Apps and offline support.
- Rendering and caching strategies.

### 5. Production Engineering

- Frontend security.
- Environment configuration.
- Development, staging, and production separation.
- Performance and Core Web Vitals.
- Testing strategies.
- Debugging and root-cause analysis.
- Observability and monitoring.
- CI/CD and deployment.
- Production readiness.

### 6. Engineering Quality

- Correctness over superficial implementation.
- Maintainability and readability.
- Simplicity over unnecessary abstraction.
- Security and accessibility throughout development.
- Evidence-based package and architecture decisions.
- Verification instead of unsupported claims.
- Protection against generic AI-generated output and AI slop.

## How It Works

The skill guides coding agents through a context-aware engineering workflow.

### Understand

- Inspect the repository and relevant files.
- Identify the existing stack and conventions.
- Understand the requested outcome and constraints.
- Review relevant documentation and dependencies.

### Plan

- Identify the appropriate implementation approach.
- Consider existing architecture and potential side effects.
- Select justified tools and dependencies.
- Avoid unnecessary changes.

### Implement

- Make focused, complete, maintainable changes.
- Follow existing project conventions.
- Handle errors, edge cases, and accessibility.
- Preserve unrelated functionality.

### Verify

- Run relevant tests and checks.
- Review the implementation for correctness.
- Check security, accessibility, and performance implications.
- Report what was actually verified.

This workflow applies to both new development and existing project maintenance.

## Engineering Philosophy

The skill emphasizes the following standards:

| Principle       | Expectation                                           |
| --------------- | ----------------------------------------------------- |
| Context first   | Understand the project before changing it             |
| Correctness     | Implement functional and reliable solutions           |
| Simplicity      | Avoid unnecessary complexity                          |
| Maintainability | Keep code understandable and extensible               |
| Security        | Apply security practices throughout development       |
| Accessibility   | Include accessible behavior in implementations        |
| Performance     | Avoid unnecessary dependencies and overhead           |
| Consistency     | Respect established project conventions               |
| Verification    | Run relevant checks and validate changes              |
| Practicality    | Prefer real engineering solutions over generic advice |

Recommendations should be based on actual requirements and project context rather than personal preferences or fixed technology assumptions.

## Technology Coverage

The skill provides guidance across modern frontend technologies and engineering practices.

| Area             | Coverage                            |
| ---------------- | ----------------------------------- |
| Frameworks       | React, Next.js                      |
| Languages        | TypeScript, JavaScript              |
| Styling          | CSS, Tailwind CSS, theming          |
| Data fetching    | API integration, TanStack Query     |
| State management | Client and server state             |
| Forms            | Validation and form handling        |
| Security         | Authentication, authorization, RBAC |
| Accessibility    | WCAG and inclusive interfaces       |
| SEO              | Metadata and discoverability        |
| Performance      | Core Web Vitals, rendering, caching |
| Testing          | Testing strategy and verification   |
| Deployment       | CI/CD and production environments   |

The skill does not require every project to use every technology listed. Recommendations depend on the existing stack and project requirements.

## Repository Structure

```text
modern-frontend-engineering/
├── SKILL.md
│
├── references/
│   ├── accessibility-and-wcag.md
│   ├── anti-ai-slop-and-engineering-quality.md
│   ├── api-integration.md
│   ├── architecture-and-project-structure.md
│   ├── authentication-and-authorization.md
│   ├── ci-cd-and-deployment.md
│   ├── debugging-and-self-correction.md
│   ├── dialogs-modals-and-overlays.md
│   ├── environment-configuration.md
│   ├── forms-and-validation.md
│   ├── frontend-security.md
│   ├── internationalization-and-rtl.md
│   ├── layouts-and-navigation.md
│   ├── nextjs-engineering.md
│   ├── notifications-and-push.md
│   ├── observability-and-monitoring.md
│   ├── package-selection-and-ecosystem.md
│   ├── performance-and-core-web-vitals.md
│   ├── production-readiness.md
│   ├── pwa-and-offline-support.md
│   ├── react-engineering.md
│   ├── rendering-and-caching-strategies.md
│   ├── reusable-frontend-modules.md
│   ├── reusable-ui-components.md
│   ├── seo-and-discoverability.md
│   ├── state-management.md
│   ├── testing-strategy.md
│   ├── theming-and-dark-mode.md
│   ├── typescript-and-code-quality.md
│   └── ui-design-quality-and-impeccable.md
│
├── examples/
│   ├── README.md
│   ├── api-integration/
│   ├── authentication-and-rbac/
│   ├── forms-and-validation/
│   ├── modal-and-notifications/
│   ├── nextjs-app-router/
│   ├── reusable-components/
│   └── tanstack-query/
│
├── scripts/
│   └── validate_skill.py
│
├── evals/
│   └── evals.json
│
├── CHANGELOG.md
├── CONTRIBUTING.md
├── DEVELOPMENT_PLAN.md
├── PROJECT_STATUS.md
├── LICENSE
├── README.md
├── pyproject.toml
└── uv.lock
```

### Important Files

| File or Directory     | Purpose                                        |
| --------------------- | ---------------------------------------------- |
| `SKILL.md`            | Core instructions followed by the coding agent |
| `references/`         | Detailed frontend engineering guidance         |
| `examples/`           | Practical implementation patterns and examples |
| `scripts/`            | Validation and maintenance tooling             |
| `evals/`              | Evaluation cases for assessing skill behavior  |
| `CHANGELOG.md`        | Release history                                |
| `CONTRIBUTING.md`     | Contribution guidelines                        |
| `DEVELOPMENT_PLAN.md` | Development direction and planned improvements |
| `PROJECT_STATUS.md`   | Current project status                         |
| `LICENSE`             | MIT License                                    |

## Development and Validation

The repository uses Python and `uv` for its validation tooling.

### Prerequisites

- Python.
- [uv](https://docs.astral.sh/uv/).
- Git.

### Setup

Clone the repository:

```bash
git clone https://github.com/thirusakthi-dev/modern-frontend-engineering.git
cd modern-frontend-engineering
```

Install development dependencies:

```bash
uv sync
```

### Run Full Validation

```bash
uv run python scripts/validate_skill.py
```

### Run Individual Checks

Python linting:

```bash
uv run ruff check scripts
```

Python formatting:

```bash
uv run ruff format --check scripts
```

Tests:

```bash
uv run pytest
```

Markdown formatting is checked by the validation script.

The validation tooling checks skill structure, Markdown formatting, Python code quality, available tests, and Markdown links.

Passing automated validation does not guarantee that every instruction or implementation example has been tested in every coding agent or application.

## Compatibility

Modern Frontend Engineering follows the Agent Skills format and is designed to work across compatible AI coding agents.

The skill is intended to remain agent-independent.

Installation, discovery, and supported features may vary depending on the coding agent and its implementation of the Agent Skills format.

Agent-specific installation instructions and limitations should be verified against the respective agent's documentation.

## Contributing

Contributions are welcome.

You can help improve the project by:

- Improving engineering guidance.
- Correcting outdated technical recommendations.
- Adding practical implementation examples.
- Improving core skill instructions.
- Expanding evaluation coverage.
- Testing compatibility with coding agents.
- Reporting issues and suggesting improvements.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes.

## Development Roadmap

Planned development priorities include:

- Continuously improving core skill instructions.
- Maintaining accurate framework and ecosystem guidance.
- Expanding practical implementation examples.
- Improving evaluation coverage.
- Testing compatibility across coding agents.
- Refining validation tooling.
- Improving documentation based on practical usage and community feedback.

See [DEVELOPMENT_PLAN.md](DEVELOPMENT_PLAN.md) for the development direction.

## Project Status

**Current version:** `0.1.0`

**Release status:** Initial release.

The project includes core skill instructions, detailed reference documentation, implementation pattern examples, evaluation cases, and validation tooling.

See [PROJECT_STATUS.md](PROJECT_STATUS.md) for current capabilities, validation results, and known limitations.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for release history and notable changes.

## License

This project is licensed under the [MIT License](LICENSE).

You are free to use, modify, and distribute this project under the terms of the license.

## Links

- **Repository:** https://github.com/thirusakthi-dev/modern-frontend-engineering
- **Issues:** https://github.com/thirusakthi-dev/modern-frontend-engineering/issues
- **Contributing:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Development Plan:** [DEVELOPMENT_PLAN.md](DEVELOPMENT_PLAN.md)
- **Project Status:** [PROJECT_STATUS.md](PROJECT_STATUS.md)
- **Changelog:** [CHANGELOG.md](CHANGELOG.md)
- **License:** [LICENSE](LICENSE)
- **Skills CLI:** https://github.com/vercel-labs/skills
- **Agent Skills Specification:** https://agentskills.io/
