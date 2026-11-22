# Alto Frontend Engineering

**Build with standards. Engineer with purpose.**

Alto Frontend Engineering is an AI coding-agent skill that brings a consistent, quality-first engineering approach to frontend development.

It helps coding agents understand, build, improve, debug, refactor, and review frontend applications — from initial project setup to production readiness.

Rather than focusing only on generating code, Alto emphasizes the complete engineering process: understanding the codebase, making sound technical decisions, implementing reliable solutions, and verifying the results.

---

## Installation

Alto uses the [Vercel Skills CLI](https://skills.sh/) to install the skill into compatible AI coding agents.

### Install Alto

```bash
npx skills add thirusakthi-dev/alto-frontend-engineering --skill alto-frontend-engineering
```

### Discover available skills

```bash
npx skills add thirusakthi-dev/alto-frontend-engineering --list
```

### Verify installation

```bash
npx skills list
```

The installed skill should appear in the project or global skills list, depending on your installation selection.

### Supported coding agents

Alto is designed for use with compatible agents supported by the Skills CLI, including:

- Kilo Code
- Cursor
- Claude Code
- Codex
- GitHub Copilot
- Gemini CLI
- Cline
- OpenCode
- Windsurf

Agent availability and installation options depend on the Skills CLI and the agent's support for Agent Skills.

---

## Why Alto?

AI coding agents can generate frontend code quickly, but code generation alone does not guarantee a reliable application.

Without sufficient engineering context, an agent may:

- Introduce unnecessary dependencies.
- Create generic or inconsistent interfaces.
- Ignore existing project conventions.
- Overcomplicate simple requirements.
- Miss accessibility and security concerns.
- Introduce performance problems.
- Leave incomplete or unverified implementations.

Alto addresses these problems by giving agents a structured engineering approach.

The goal is not to generate more code. It is to produce better engineering outcomes.

## What Alto Covers

Alto provides guidance across the frontend development lifecycle.

| Area                  | Coverage                                                                 |
| --------------------- | ------------------------------------------------------------------------ |
| Project Understanding | Repository inspection, stack discovery, conventions and requirements     |
| Architecture          | Component architecture, folder organization, separation of concerns      |
| UI/UX Engineering     | Responsive layouts, design consistency, interaction states and usability |
| React Development     | Components, hooks, composition, rendering and application patterns       |
| Next.js               | App Router, routing, layouts, rendering and application structure        |
| TypeScript            | Strict typing, reusable types and maintainable interfaces                |
| Styling               | Tailwind CSS, modern CSS, design tokens and responsive styling           |
| State Management      | Context, Zustand, Redux Toolkit and appropriate state ownership          |
| Data Fetching         | TanStack Query, API integration, caching and error handling              |
| Forms and Validation  | React Hook Form, Zod and form-state management                           |
| Animation             | Framer Motion, CSS transitions and motion accessibility                  |
| Tables and Data UI    | TanStack Table and structured data presentation                          |
| Accessibility         | Semantic HTML, keyboard navigation, focus management and WCAG principles |
| SEO                   | Metadata, indexing, structured data and technical SEO                    |
| Security              | Input handling, XSS prevention, safe rendering and frontend security     |
| Performance           | Rendering efficiency, bundle optimization and Core Web Vitals            |
| Testing               | Vitest, React Testing Library and Playwright                             |
| Debugging             | Error investigation, root-cause analysis and regression prevention       |
| Production Readiness  | Build verification, environment awareness and deployment considerations  |

These technologies are examples, not mandatory dependencies. Alto encourages agents to use the project's existing tools and introduce new packages only when they solve a genuine requirement.

## Built for New and Existing Projects

Alto supports two major development scenarios.

### 1. Building a New Application

When starting a new project, Alto helps agents:

- Understand the requirements and application scope.
- Choose an appropriate architecture and technology stack.
- Establish project conventions and folder organization.
- Set up reusable components and application foundations.
- Implement features with accessibility and performance in mind.
- Verify the application before considering the work complete.

### 2. Working with an Existing Application

Alto does not assume every task starts from an empty repository.

When modifying an existing project, agents should:

- Inspect the repository and relevant documentation.
- Identify the current framework, dependencies and conventions.
- Understand the existing architecture before making changes.
- Preserve established patterns where they remain appropriate.
- Fix bugs and implement changes without unnecessary rewrites.
- Refactor incrementally and safely.
- Run relevant checks and verify the final result.

The existing project's architecture should guide implementation decisions. Unnecessary migrations and structural changes should be avoided.

## Engineering Workflow

Alto encourages a structured workflow throughout development.

### 1. Understand

- Inspect the relevant project files.
- Understand the requirements and constraints.
- Identify existing conventions and dependencies.
- Clarify important ambiguities before implementation.

### 2. Plan

- Identify the affected components and files.
- Choose an appropriate implementation approach.
- Consider accessibility, security and performance.
- Avoid unnecessary complexity and unrelated changes.

### 3. Implement

- Write clean, maintainable and appropriately typed code.
- Reuse existing components and utilities where suitable.
- Handle loading, empty, error and success states.
- Follow established project conventions.
- Keep the implementation focused on the requested outcome.

### 4. Verify

- Review the implementation for correctness.
- Run relevant linting, type checks and tests.
- Run the production build when appropriate.
- Investigate and fix issues introduced by the changes.
- Clearly report what was verified and what remains unverified.

## Engineering Philosophy

Alto follows a quality-first engineering philosophy.

**Correctness over assumptions**

Understand the requirements and existing implementation before making changes.

**Simplicity over unnecessary abstraction**

Prefer straightforward solutions. Avoid overengineering and premature abstractions.

**Consistency over personal preference**

Respect the existing codebase and its conventions unless there is a clear reason to improve them.

**Accessibility by default**

Build interfaces that work for different users, devices and interaction methods.

**Performance as an engineering requirement**

Consider rendering, network requests, bundle size and user-perceived performance.

**Security throughout development**

Apply appropriate input handling, safe rendering and secure frontend practices.

**Verification over claims**

Do not claim that code works, builds or passes tests without actually checking it.

**Quality over AI-generated volume**

Avoid generic layouts, superficial implementations, unnecessary dependencies, placeholder-heavy output and invented functionality.

## Technology Coverage

Alto is designed around modern frontend engineering practices, with particular attention to:

- React and Next.js
- JavaScript and TypeScript
- Tailwind CSS and modern CSS
- Component-driven architecture
- Client-side and server-side state management
- API integration and data fetching
- Forms and schema validation
- Accessibility and technical SEO
- Frontend security and performance
- Unit, component and end-to-end testing
- Debugging, refactoring and production readiness

The guidance should adapt to the actual project. It does not require every application to use the same framework, library or architecture.

## Development Standards

Alto encourages agents to follow these standards:

- Inspect before modifying.
- Reuse before introducing new dependencies.
- Prefer strict typing and avoid unsafe shortcuts.
- Keep components focused and maintainable.
- Handle realistic application states and edge cases.
- Avoid duplicated logic and unnecessary abstractions.
- Respect environment-specific configuration.
- Keep secrets out of source code.
- Consider development, staging and production separately.
- Run appropriate checks after implementation.
- Report limitations and verification results honestly.

## Repository

**GitHub:** https://github.com/thirusakthi-dev/alto-frontend-engineering

The repository contains the Agent Skill entry point and its supporting project documentation and resources as maintained in the repository.

The `SKILL.md` file defines the skill's identity, purpose and core instructions.

## Contributing

Contributions and suggestions are welcome.

If you find an issue, have an improvement idea or want to contribute:

1. Explore the existing repository and its conventions.
2. Identify the specific improvement or issue.
3. Keep changes focused and consistent with Alto's engineering principles.
4. Verify documentation, examples and relevant checks.
5. Submit your contribution through GitHub.

Please avoid adding unnecessary complexity or duplicating existing guidance.

## Project Status

Alto Frontend Engineering is an evolving project.

Its goal is to provide practical, consistent frontend engineering guidance for AI coding agents as frontend technologies and development practices evolve.

## License

See the repository's `LICENSE` file for licensing information.

## Links

- **GitHub Repository:** https://github.com/thirusakthi-dev/alto-frontend-engineering
- **Skills CLI:** https://skills.sh/
- **Installation:** `npx skills add thirusakthi-dev/alto-frontend-engineering --skill alto-frontend-engineering`

---

**Alto Frontend Engineering**

_Build with standards. Engineer with purpose._
