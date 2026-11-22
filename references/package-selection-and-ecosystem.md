# Package Selection and Ecosystem

## 1. Purpose

Define standards for discovering, evaluating, selecting, installing, updating and maintaining frontend dependencies.

Support:

- Package discovery.
- Dependency evaluation.
- Framework compatibility.
- Package maintenance.
- Security assessment.
- Bundle-size analysis.
- Tree shaking.
- Dependency management.
- Version selection.
- Alternatives and trade-offs.
- Existing dependency reuse.
- Package replacement and removal.

The objective is to select reliable dependencies that solve real problems without unnecessarily increasing application complexity, bundle size or maintenance costs.

## 2. Inspect Before Installing

Before adding a package:

1. Inspect `package.json`.
1. Identify the package manager.
1. Review installed dependencies.
1. Check framework and runtime versions.
1. Inspect existing utilities and components.
1. Check whether the functionality already exists.
1. Review project conventions.
1. Identify bundle-size and compatibility constraints.

For existing projects, prefer using existing dependencies when they satisfy the requirement.

Do not install a new package before checking whether the project already has an appropriate solution.

## 3. Package Discovery

Discover packages through trustworthy sources.

Recommended sources:

- Official package documentation.
- npm registry.
- GitHub repositories.
- Official framework documentation.
- Package release notes.
- Security advisories.
- Bundle-size analysis tools.

Useful discovery platforms:

- npm: https://www.npmjs.com/
- GitHub: https://github.com/
- Bundlephobia: https://bundlephobia.com/
- Socket: https://socket.dev/
- Snyk: https://snyk.io/
- npm Trends: https://npmtrends.com/

Do not choose a package based only on download counts or popularity.

## 4. Package Evaluation Criteria

Evaluate a package using the following criteria.

### Functionality

- Does it solve the actual requirement?
- Does it support required use cases?
- Does it introduce unnecessary abstractions?
- Is a native browser or framework feature sufficient?

### Maintenance

- Is the project actively maintained?
- Are releases reasonably regular?
- Are issues and pull requests handled?
- Is there a clear maintenance history?
- Are breaking changes documented?

### Compatibility

- Does it support the project's framework version?
- Does it support the required React version?
- Is it compatible with TypeScript?
- Does it support the project's module system?
- Does it work with the required rendering environment?

### Security

- Are there known vulnerabilities?
- Does it execute installation scripts?
- Does it have suspicious dependency behavior?
- Does it require unnecessary permissions?
- Does it introduce unsafe runtime behavior?

### Performance

- What is the package's bundle impact?
- Does it support tree shaking?
- Does it load unnecessary dependencies?
- Does it increase runtime work?
- Can it be loaded lazily?

### Developer Experience

- Is the API understandable?
- Is documentation available?
- Are TypeScript types reliable?
- Are examples current?
- Is debugging practical?

## 5. Prefer Native Capabilities When Appropriate

Modern browsers and JavaScript provide many useful built-in APIs.

Examples:

| Requirement | Native option |
| ------------------------ | ------------------------------ |
| HTTP requests | Fetch API |
| Request cancellation | AbortController |
| URL query parameters | URLSearchParams |
| Form submission | HTML Forms and FormData |
| Local storage | Web Storage API |
| Date and time formatting | Intl |
| Clipboard | Clipboard API |
| Intersection detection | IntersectionObserver |
| Resize detection | ResizeObserver |
| Element visibility | CSS and browser APIs |
| Simple animations | CSS transitions and animations |

Use a package when it provides meaningful functionality beyond the native option.

Do not introduce a dependency for a small utility that can be implemented safely with built-in APIs.

However, avoid rebuilding complex functionality when a mature package is more reliable.

## 6. Framework Compatibility

Check compatibility before installation.

Verify:

- React version.
- Next.js version.
- Node.js version.
- TypeScript version.
- Browser support.
- Server-side rendering support.
- Client/server execution requirements.
- Peer dependencies.

Pay attention to:

- React Server Components.
- Server-side rendering.
- Hydration.
- ESM and CommonJS compatibility.
- Client-only browser APIs.
- React 19 compatibility where required.

Do not assume that a package supporting React also supports every Next.js rendering scenario.

Check the package's official compatibility documentation.

## 7. Dependency Categories

Understand the role of each dependency.

### Core framework

Examples:

- React.
- Next.js.
- Vite.

### UI and component libraries

Examples:

- Radix UI.
- React Aria.
- shadcn/ui.
- Material UI.

### Styling

Examples:

- Tailwind CSS.
- CSS Modules.
- Sass.

### State and data fetching

Examples:

- Zustand.
- Redux Toolkit.
- TanStack Query.
- SWR.

### Forms and validation

Examples:

- React Hook Form.
- TanStack Form.
- Zod.
- Valibot.

### Animation

Examples:

- Motion.
- GSAP.

### Testing

Examples:

- Vitest.
- Jest.
- React Testing Library.
- Playwright.

### Utilities

Examples:

- date-fns.
- clsx.
- nanoid.

These are examples, not mandatory dependencies.

Choose according to the project requirements.

## 8. Avoid Dependency Overlap

Avoid installing multiple libraries that solve the same problem without a clear reason.

Examples:

- Multiple HTTP clients.
- Multiple global state libraries.
- Multiple toast systems.
- Multiple form libraries.
- Multiple schema validation libraries.
- Multiple icon libraries.
- Multiple animation engines.

Before adding another package, determine whether the existing solution can be extended.

Prefer a consistent ecosystem.

## 9. Bundle Size and Performance

Evaluate the effect of dependencies on the delivered application.

Consider:

- Minified size.
- Gzipped and Brotli size.
- Runtime overhead.
- Transitive dependencies.
- Tree shaking.
- Code splitting.
- Lazy loading.
- Server-only dependencies.
- Client bundle impact.

Use appropriate analysis tools.

Examples:

- Bundlephobia.
- Webpack Bundle Analyzer.
- Next.js bundle analysis tools.
- Vite visualizer plugins.

Do not evaluate a package only by its published package size.

The actual browser impact depends on imported modules, build configuration and usage.

### Import only what is needed

Prefer targeted imports where supported.

Avoid importing an entire library when only a small part is required.

Verify that the package supports tree shaking rather than assuming it does.

### Lazy loading

Use dynamic imports for suitable heavy features.

Examples:

- Rich text editors.
- Large charts.
- Maps.
- Complex visualizations.
- Optional administration tools.

Do not lazy-load tiny components without a meaningful performance reason.

## 10. Dependency Security

Evaluate dependency security before and after installation.

Consider:

- Known vulnerabilities.
- Maintainer trust.
- Release history.
- Dependency tree.
- Installation scripts.
- Package provenance where available.
- Unusual network behavior.
- Dependency confusion risks.

Use available package-manager audit commands.

Examples:

```bash
npm audit
```

```bash
pnpm audit
```

```bash
yarn npm audit
```

Command availability and syntax can vary by package-manager version.

Do not automatically apply every suggested update.

Review breaking changes and the actual security impact first.

Avoid blindly running:

```bash
npm audit fix --force
```

This can introduce breaking dependency changes.

Never claim a dependency is secure merely because an audit reports no vulnerabilities.

## 11. Version Management

Follow the project's package-manager conventions.

Common version strategies:

- Exact versions.
- Compatible version ranges.
- Semantic versioning.
- Lockfile-based reproducibility.

Understand:

- Major versions may introduce breaking changes.
- Minor versions generally add backward-compatible features.
- Patch versions generally contain backward-compatible fixes.

Do not assume every package follows semantic versioning correctly.

Keep lockfiles committed when required by the package manager.

Do not manually edit lockfiles unless there is a specific reason.

## 12. Package Installation

Use the project's existing package manager.

Examples:

```bash
npm install package-name
```

```bash
pnpm add package-name
```

```bash
yarn add package-name
```

For development-only dependencies, use the appropriate development dependency command.

Do not mix package managers in one project without an explicit migration plan.

Do not delete or replace a lockfile casually.

After installation:

1. Inspect package changes.
1. Check peer dependency warnings.
1. Verify compatibility.
1. Run relevant checks.
1. Review bundle impact when appropriate.

## 13. Package Alternatives

Compare alternatives based on the actual requirement.

Example: global state management.

| Option | Suitable use |
| ------------- | ------------------------------------ |
| React state | Local component state |
| React Context | Shared subtree values |
| Zustand | Lightweight shared client state |
| Redux Toolkit | Structured complex application state |

Example: form management.

| Option | Suitable use |
| --------------- | --------------------------------------------------- |
| Native HTML | Simple forms |
| React Hook Form | Complex forms with broad ecosystem support |
| TanStack Form | Type-safe form state architecture |
| Formik | Existing Formik projects or suitable form workflows |

Example: styling.

| Option | Suitable use |
| ------------ | ----------------------- |
| CSS | Native styling |
| CSS Modules | Scoped component styles |
| Tailwind CSS | Utility-first styling |
| Sass | CSS preprocessing |

Do not choose a package based on personal preference alone.

Explain trade-offs when a decision materially affects the architecture.

## 14. Package Maintenance

Periodically review dependencies.

Consider:

- Outdated packages.
- Deprecated packages.
- Security advisories.
- Unsupported framework versions.
- Duplicate dependencies.
- Unused packages.
- Breaking changes.
- Migration requirements.

Useful commands include:

```bash
npm outdated
```

```bash
npm ls
```

```bash
npm uninstall package-name
```

Use the equivalent commands for the project's package manager when appropriate.

Do not remove dependencies merely because their names do not appear in source imports. Some packages are used by build tools, scripts, plugins or configuration files.

## 15. Dependency Replacement

Replacing a package requires understanding its usage.

Before replacement:

1. Identify all imports.
1. Search for indirect usage.
1. Inspect configuration files.
1. Check build and test scripts.
1. Identify behavior that depends on the package.
1. Compare replacement APIs.
1. Plan a safe migration.

After replacement:

- Update imports.
- Update configuration.
- Update tests.
- Remove obsolete dependencies.
- Check lockfile changes.
- Run lint, type checks and build.
- Verify affected functionality.

Do not replace dependencies across the entire project without understanding their impact.

## 16. Avoid Unnecessary Abstractions

Do not create wrappers around every dependency automatically.

A wrapper is useful when it:

- Encapsulates project-specific behavior.
- Provides a stable application interface.
- Centralizes configuration.
- Simplifies repeated usage.
- Makes future replacement practical.

A wrapper is unnecessary when it only renames an existing API without adding value.

Avoid building internal frameworks around simple packages.

## 17. AI-Assisted Package Discovery

When an AI agent recommends a package, it should:

1. Identify the actual requirement.
1. Search for existing project functionality.
1. Verify the package exists.
1. Check official documentation.
1. Review compatibility.
1. Inspect maintenance and release history.
1. Evaluate security and dependencies.
1. Compare reasonable alternatives.
1. Explain the reason for selection.
1. Install only when justified.

Never invent package names, APIs, installation commands or package features.

Do not rely on outdated model knowledge for version-sensitive package decisions.

Use official documentation and current package metadata.

## 18. Existing Project Dependency Changes

For existing projects:

- Preserve the package manager.
- Preserve the lockfile.
- Reuse installed packages.
- Avoid unnecessary major upgrades.
- Avoid unrelated dependency cleanup.
- Understand peer dependencies.
- Check build configuration.
- Review transitive changes.

When a requested feature can be implemented with existing dependencies, prefer that approach unless it creates unnecessary complexity.

## 19. Common Anti-Patterns

Avoid:

- Installing packages without checking existing functionality.
- Choosing packages only by popularity.
- Adding multiple overlapping libraries.
- Ignoring peer dependency warnings.
- Mixing package managers.
- Removing lockfiles unnecessarily.
- Blindly applying forced updates.
- Installing heavy libraries for trivial features.
- Ignoring browser and SSR compatibility.
- Trusting package size estimates without bundle analysis.
- Adding wrappers without value.
- Replacing dependencies without tracing their usage.

## 20. Decision Workflow

Before installing a dependency:

1. Define the requirement.
1. Inspect the existing project.
1. Check native platform capabilities.
1. Search for existing dependencies.
1. Identify suitable candidates.
1. Verify official documentation.
1. Evaluate maintenance and compatibility.
1. Assess security and bundle impact.
1. Compare alternatives.
1. Install only when justified.
1. Verify the project after installation.

Choose the smallest reliable dependency set that meets the requirements.

## 21. Review Checklist

### Discovery

- [ ] The actual requirement is understood.
- [ ] Existing functionality has been checked.
- [ ] Native alternatives have been considered.
- [ ] Package existence and documentation are verified.

### Compatibility

- [ ] Framework compatibility is confirmed.
- [ ] Runtime and browser requirements are understood.
- [ ] Peer dependencies are reviewed.
- [ ] Server/client requirements are understood.

### Quality

- [ ] Maintenance is evaluated.
- [ ] Security is reviewed.
- [ ] Bundle impact is considered.
- [ ] Alternatives are compared.

### Installation

- [ ] Existing package manager is used.
- [ ] Lockfile is preserved.
- [ ] Installation changes are reviewed.
- [ ] Relevant checks pass.

## 22. Related References

- architecture-and-project-structure.md
- reusable-ui-components.md
- reusable-frontend-modules.md
- react-engineering.md
- nextjs-engineering.md
- state-management.md
- api-integration.md
- testing-strategy.md
- frontend-security.md
- performance-and-core-web-vitals.md

## 23. Official Resources

- npm Documentation: https://docs.npmjs.com/
- pnpm Documentation: https://pnpm.io/
- Yarn Documentation: https://yarnpkg.com/
- npm Registry: https://www.npmjs.com/
- Node.js Documentation: https://nodejs.org/docs/latest/api/
- Bundlephobia: https://bundlephobia.com/
- Socket: https://socket.dev/
- OWASP Software Component Verification Standard: https://owasp.org/www-project-software-component-verification-standard/
- GitHub Dependabot: https://docs.github.com/en/code-security/dependabot
- React Documentation: https://react.dev/
- Next.js Documentation: https://nextjs.org/docs
