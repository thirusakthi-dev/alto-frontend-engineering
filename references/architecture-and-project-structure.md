# Architecture and Project Structure

## 1. Purpose

Define practical architecture standards for modern frontend applications.

The goal is to create applications that are:

- Easy to understand.
- Easy to maintain.
- Scalable when requirements grow.
- Consistent across features.
- Testable.
- Reusable without unnecessary abstraction.

Architecture must solve real project problems. Do not introduce complexity just to follow a pattern.

## 2. Inspect Before Designing

Before proposing or changing architecture:

1. Inspect the existing directory structure.
1. Identify the framework and installed version.
1. Inspect package.json and configuration files.
1. Understand routing and rendering.
1. Identify existing shared components.
1. Understand API and data-fetching patterns.
1. Identify state-management solutions.
1. Inspect authentication and authorization.
1. Review existing tests and development scripts.
1. Identify conventions already followed by the project.

Prefer extending existing conventions over introducing a competing architecture.

## 3. Architecture Selection

Choose architecture according to project complexity.

### Small applications

A simple structure is sufficient.

Example:

src/
components/
hooks/
lib/
pages/
services/
styles/
types/

Do not create unnecessary feature layers for a small application.

### Medium and large applications

Consider feature-oriented architecture.

Example:

src/
app/
features/
components/
hooks/
lib/
services/
types/

Each feature should own its related UI, logic and data operations when appropriate.

Do not force every project into this exact structure.

## 4. Feature-Oriented Architecture

Organize code around business capabilities rather than only technical file types.

Example:

src/
features/
users/
components/
hooks/
services/
schemas/
types/
utils/
index.ts

```
products/
  components/
  hooks/
  services/
  schemas/
  types/
  utils/
  index.ts
```

components/
ui/
shared/

lib/
hooks/
services/
types/

### Guidelines

- Keep feature-specific code inside its feature.
- Share components only when multiple areas genuinely need them.
- Avoid exposing internal implementation details unnecessarily.
- Keep business logic separate from presentation when useful.
- Avoid creating empty folders without a purpose.
- Do not create a barrel file for every directory automatically.

## 5. Next.js App Router Architecture

Understand the role of the App Router before organizing files.

Typical structure:

src/
app/
layout.tsx
page.tsx
loading.tsx
error.tsx
not-found.tsx
globals.css

```
(auth)/
  login/
    page.tsx

(dashboard)/
  dashboard/
    page.tsx
  users/
    page.tsx

api/
  health/
    route.ts
```

components/
ui/
shared/

features/
users/
dashboard/

lib/
hooks/
services/
types/

### App Router principles

- Use app/ for routing and route-level composition.
- Use route groups to organize layouts without changing URLs.
- Keep reusable business features outside route files.
- Keep route handlers focused on HTTP concerns.
- Use layouts for shared page structures.
- Use loading, error and not-found boundaries appropriately.
- Prefer Server Components by default.
- Introduce Client Components only when browser interactivity is required.

Do not turn the entire application into a Client Component unnecessarily.

## 6. React and Vite Architecture

For React applications using Vite:

src/
assets/
components/
ui/
shared/

features/
users/
dashboard/

hooks/
layouts/
lib/
pages/
routes/
services/
styles/
types/

### Guidelines

- Keep the entry point small.
- Separate route configuration from page implementation when useful.
- Organize complex features independently.
- Use shared layouts for common page structures.
- Avoid unnecessary framework-like abstractions.

## 7. Component Architecture

Build components with clear responsibilities.

Prefer:

- Single-purpose components.
- Explicit and typed props.
- Composition over excessive configuration.
- Accessible HTML elements.
- Consistent component APIs.
- Reusable primitives where justified.

Avoid:

- Components responsible for unrelated features.
- Large components containing all business logic.
- Excessive boolean props.
- Deeply nested conditional rendering.
- Unnecessary wrapper components.
- Premature generic components.

### Component placement

Use these guidelines:

- Feature-only component: keep inside its feature.
- Application-wide component: use shared components.
- Primitive UI component: use the UI component library directory.
- Page composition: keep near its route or page.

## 8. Separation of Responsibilities

Keep responsibilities clear.

### UI layer

Responsible for:

- Rendering.
- User interactions.
- Accessibility.
- Visual states.
- Component composition.

### Business logic

Responsible for:

- Business rules.
- Domain calculations.
- Feature workflows.
- Validation rules where appropriate.

### Data layer

Responsible for:

- API requests.
- Data transformation.
- Query functions.
- Mutations.
- Cache interaction.

### Shared infrastructure

Responsible for:

- Configuration.
- Common utilities.
- Error handling.
- Shared types.
- Application-wide integrations.

Do not split every function into separate layers without a practical reason.

## 9. Import and Dependency Boundaries

Follow consistent import conventions.

- Prefer configured path aliases.
- Avoid deeply nested relative imports.
- Avoid circular dependencies.
- Keep dependencies flowing in a predictable direction.
- Avoid importing internal implementation details from unrelated features.
- Keep shared modules independent of feature-specific code when practical.

Example:

@/components/ui/button
@/features/users/components/user-list
@/lib/api-client

Use aliases that actually exist in the project configuration.

## 10. TypeScript Organization

Place types near the code that owns them.

Guidelines:

- Feature-specific types belong to the feature.
- Shared domain types belong in an appropriate shared location.
- API request and response types should be explicit.
- Avoid duplicating types unnecessarily.
- Avoid using any.
- Use unknown for values that require validation.
- Infer types from schemas when appropriate.
- Avoid oversized global type files.

Do not create a separate type file for every small component automatically.

## 11. Configuration and Environment Management

Separate application configuration from business logic.

Consider:

- Environment variable validation.
- Public and server-only configuration.
- API base URLs.
- Feature flags.
- Application metadata.
- Third-party service configuration.

Maintain separate behavior for:

- Development.
- Staging.
- Production.

Never expose private environment variables through browser-accessible code.

Do not commit secrets.

## 12. State Management Boundaries

Choose state management based on the type of state.

| State type | Possible solution |
| ------------------------- | ---------------------- |
| Local component state | React useState |
| Complex local state | useReducer |
| Server state | TanStack Query |
| Shared client state | Context or Zustand |
| Complex application state | Redux Toolkit |
| URL state | URL parameters or nuqs |
| Form state | React Hook Form |

Avoid duplicating server state in global client state without a clear reason.

Do not install a state-management package when built-in React capabilities are sufficient.

## 13. Routing and Layout Boundaries

Keep routing responsibilities separate from business logic.

Consider:

- Public routes.
- Protected routes.
- Authentication layouts.
- Dashboard layouts.
- Nested layouts.
- Permission-aware navigation.
- Not-found routes.
- Error boundaries.

For Next.js, use framework-native routing and layouts.

For React Router applications, follow the installed router's conventions.

Do not build a custom routing system unnecessarily.

## 14. Reusability Standards

A component or utility should become shared when:

- Multiple features need the same behavior.
- The abstraction has a stable interface.
- Shared maintenance provides real value.
- Reuse does not make implementation harder to understand.

Avoid speculative reusable abstractions.

A little duplication is preferable to a confusing abstraction when the requirements are still evolving.

## 15. Architecture Decision Workflow

When creating or modifying architecture:

1. Understand the requirement.
1. Inspect the current project.
1. Identify the simplest suitable architecture.
1. Check existing reusable modules.
1. Define ownership and boundaries.
1. Consider testing and maintainability.
1. Implement incrementally.
1. Verify imports and dependencies.
1. Run relevant checks.
1. Document important architectural decisions.

Explain significant trade-offs when they affect future maintenance.

## 16. Architecture Review Checklist

Before completing an architecture-related task, verify:

- [ ] Structure matches project complexity.
- [ ] Existing conventions are respected.
- [ ] Feature responsibilities are clear.
- [ ] Shared components are genuinely reusable.
- [ ] Business logic is not unnecessarily coupled to UI.
- [ ] Data access has clear ownership.
- [ ] Imports follow predictable boundaries.
- [ ] No unnecessary circular dependencies exist.
- [ ] TypeScript types are appropriately organized.
- [ ] Environment configuration is safe.
- [ ] Development, staging and production are considered.
- [ ] Testing remains practical.
- [ ] No unnecessary abstraction was introduced.

## 17. Related References

Load these documents when relevant:

- react-engineering.md
- nextjs-engineering.md
- rendering-and-caching-strategies.md
- typescript-and-code-quality.md
- component-and-design-systems.md
- application-state-and-utilities.md
- production-readiness.md
