# Reusable Frontend Modules

## 1. Purpose

Define standards for designing, implementing, modifying and maintaining reusable frontend modules.

Support:

- Shared UI components.
- Feature modules.
- Custom React hooks.
- Utility functions.
- API services.
- Validation schemas.
- Application-level providers.
- Shared configurations.
- Internal component libraries.
- Reusable business functionality.
- Module boundaries and public APIs.

The objective is to build reusable functionality without creating unnecessary dependencies, coupling or abstraction.

## 2. Inspect Before Creating

Before creating a reusable module:

1. Inspect the existing project structure.
1. Search for similar implementations.
1. Identify existing shared components.
1. Review custom hooks and utilities.
1. Check existing feature boundaries.
1. Identify dependencies between modules.
1. Understand how functionality is currently consumed.
1. Review naming and export conventions.

For existing projects, extend or improve existing modules when practical.

Do not create a second implementation of functionality that already exists.

## 3. Understand Reusability

Not every piece of code needs to become reusable.

Reuse is valuable when functionality:

- Appears in multiple places.
- Represents a consistent application pattern.
- Has a clear responsibility.
- Has a predictable interface.
- Can evolve independently.
- Reduces meaningful duplication.

Avoid abstraction when:

- The logic is used only once.
- The implementation is very small.
- Similar-looking features have different behavior.
- A generic solution introduces more complexity than duplication.

Prefer practical reuse over theoretical reuse.

## 4. Module Categories

Understand different module responsibilities.

| Module | Responsibility |
| ---------------- | ------------------------------ |
| UI component | Reusable visual element |
| Feature module | Complete feature functionality |
| Custom hook | Reusable React behavior |
| Utility | Framework-independent helper |
| API service | Backend communication |
| Schema | Data validation |
| Provider | Shared application context |
| Configuration | Centralized settings |
| Type definitions | Shared contracts |

Keep responsibilities clear.

Do not combine unrelated functionality into one shared module.

## 5. Feature-Based Architecture

Organize related functionality around application features.

Example:

```text
src/
├── app/
├── components/
│   ├── ui/
│   └── layout/
├── features/
│   ├── users/
│   │   ├── api/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── schemas/
│   │   ├── types/
│   │   └── index.ts
│   └── projects/
│       ├── api/
│       ├── components/
│       ├── hooks/
│       ├── schemas/
│       ├── types/
│       └── index.ts
├── hooks/
├── lib/
└── types/
```

This is an example, not a mandatory folder structure.

Adapt to the existing architecture and project size.

Avoid creating empty directories or excessive nesting.

## 6. Module Boundaries

A module should have a clear responsibility and boundary.

Consider:

- What does this module own?
- What functionality does it expose?
- Which modules may depend on it?
- Which dependencies should remain private?
- Can it be changed without breaking unrelated features?

Avoid circular dependencies.

Avoid importing internal implementation files from unrelated modules when a public interface exists.

Keep dependencies flowing in a predictable direction.

Example:

```text
Application
    |
    v
Feature Modules
    |
    v
Shared Modules
    |
    v
Core Utilities
```

Do not force every project into this exact dependency structure.

## 7. Public Module APIs

Expose only what consumers need.

Example:

```tsx
// features/users/index.ts

export { UserList } from "./components/user-list";
export { UserForm } from "./components/user-form";
export { useUsers } from "./hooks/use-users";
export type { User } from "./types/user.types";
```

Consumers can import through the public interface:

```tsx
import { UserList, useUsers } from "@/features/users";
```

Guidelines:

- Keep exports intentional.
- Export public types when useful.
- Avoid exposing internal implementation details.
- Avoid excessively large barrel files.
- Watch for circular dependencies.
- Consider tree shaking and module side effects.

Use barrel exports only when they improve module organization.

## 8. Reusable UI Components

Build shared UI components around stable visual and behavioral requirements.

Examples:

- Button.
- Input.
- Select.
- Checkbox.
- Dialog.
- Tooltip.
- Toast.
- Data table.
- Dropdown menu.
- Pagination.

Guidelines:

- Use semantic HTML.
- Support accessibility.
- Define predictable props.
- Keep variants understandable.
- Support composition.
- Avoid feature-specific business logic in generic components.

A generic button should not contain user-management or billing behavior.

See `reusable-ui-components.md`.

## 9. Custom Hooks

Extract reusable React behavior into custom hooks when useful.

Examples:

- `useDebounce`
- `useMediaQuery`
- `useLocalStorage`
- `useClickOutside`
- `useKeyboardShortcut`
- `useNetworkStatus`
- `usePagination`

Example:

```tsx
function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timeout = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => clearTimeout(timeout);
  }, [value, delay]);

  return debouncedValue;
}
```

This example requires the appropriate React imports.

Guidelines:

- Follow the Rules of Hooks.
- Keep hooks focused.
- Handle cleanup.
- Avoid unnecessary effects.
- Define clear return values.
- Document unusual behavior.
- Avoid abstractions that hide important side effects.

## 10. Utility Functions

Use utility modules for logic that does not require React.

Examples:

- Date formatting.
- Currency formatting.
- String normalization.
- URL construction.
- Data transformation.
- File-size formatting.
- Number formatting.

Prefer native platform capabilities where suitable.

Example:

```tsx
export function formatCurrency(
  amount: number,
  currency = "INR",
  locale = "en-IN",
): string {
  return new Intl.NumberFormat(locale, {
    style: "currency",
    currency,
  }).format(amount);
}
```

Guidelines:

- Keep utilities deterministic where possible.
- Avoid hidden global state.
- Handle invalid inputs deliberately.
- Use explicit parameters.
- Keep formatting consistent across the application.

Do not create a giant utility file containing unrelated functions.

## 11. Shared API Modules

Separate reusable HTTP behavior from feature-specific API operations.

Example:

```text
lib/
└── api/
    ├── client.ts
    ├── errors.ts
    └── types.ts

features/
└── users/
    └── api/
        └── users.api.ts
```

The shared API client handles common networking behavior.

Feature services handle their own endpoints and contracts.

Avoid putting every API endpoint in one global service file.

See `api-integration.md`.

## 12. Shared Validation Modules

Reusable validation should reflect actual domain rules.

Examples:

- Email validation.
- Phone number validation.
- Password policy.
- Common address schemas.
- Shared form field constraints.

Prefer shared schemas when the same rule genuinely applies in multiple places.

Do not force unrelated forms to share one schema.

Keep backend validation authoritative.

See `forms-and-validation.md`.

## 13. Configuration Modules

Centralize configuration that needs consistent access.

Examples:

- Navigation definitions.
- Application metadata.
- Feature flags.
- Supported locales.
- Public environment configuration.
- Route constants.

Avoid placing secrets in frontend configuration.

Separate public configuration from server-only configuration.

Environment-specific settings must be handled deliberately.

See `environment-configuration.md`.

## 14. Reusable Business Modules

Some functionality is reusable but not purely visual.

Examples:

- Permission checks.
- Pricing calculations.
- Search and filtering logic.
- Notification preferences.
- File metadata handling.
- Workflow status transitions.

Keep business rules separate from generic UI components.

Use clear interfaces and explicit inputs.

Do not duplicate backend authorization or business rules as if frontend logic were authoritative.

Frontend business logic improves interaction and consistency, but the backend remains the source of truth for protected operations.

## 15. Component Composition

Prefer composition when components need flexibility.

Example:

```tsx
<Card>
  <Card.Header>
    <Card.Title>Account</Card.Title>
  </Card.Header>

  <Card.Content>Account information</Card.Content>

  <Card.Footer>
    <Button>Save</Button>
  </Card.Footer>
</Card>
```

Use compound components when related components form a meaningful API.

Avoid deeply nested abstractions that make component behavior difficult to understand.

Prefer explicit props when composition does not add value.

## 16. Dependency Direction

Avoid tightly coupled modules.

A shared module should not depend on a feature-specific component.

Prefer:

- Feature modules depending on shared utilities.
- UI components receiving data through props.
- API services depending on shared API infrastructure.
- Business logic remaining independent of presentation when practical.

Avoid circular dependencies and hidden cross-feature coupling.

Do not create a generic shared module merely to move code into another folder.

## 17. TypeScript Contracts

Define clear module interfaces.

Use:

- Explicit parameter types.
- Explicit return types where helpful.
- Shared domain types.
- Discriminated unions.
- Generic types when justified.
- `unknown` for untrusted data.

Avoid:

- `any`.
- Excessively broad interfaces.
- Unnecessary type duplication.
- Unsafe type assertions.
- Exporting internal types without a consumer need.

Keep API contracts and domain types aligned.

See `typescript-and-code-quality.md`.

## 18. Reusable Modules Across Projects

When building a reusable module intended for multiple projects, consider:

- Framework compatibility.
- Runtime compatibility.
- Public API stability.
- Peer dependencies.
- Styling ownership.
- Accessibility.
- Configuration.
- Documentation.
- Versioning.
- Packaging.
- Testing.
- Distribution.

Avoid coupling reusable packages to one application's environment variables or backend.

Separate project-specific configuration from reusable behavior.

Do not turn an internal application module into a published package unless there is a real need.

## 19. Existing Module Modification

When modifying an existing reusable module:

1. Identify all consumers.
1. Inspect its public API.
1. Understand current behavior.
1. Search for internal and external imports.
1. Identify compatibility requirements.
1. Check tests and documentation.
1. Make the smallest reliable change.
1. Update affected consumers.
1. Test regression scenarios.
1. Verify exports and build output.

Preserve backward compatibility where practical.

If a breaking change is required, identify affected consumers and explain the migration.

Do not silently change shared component behavior in ways that break unrelated features.

## 20. Testing Reusable Modules

Test behavior at the module boundary.

### Utility tests

- Valid inputs.
- Invalid inputs.
- Edge cases.
- Expected output.

### Hook tests

- Initial state.
- Updates.
- Cleanup.
- Async behavior.
- Error conditions.

### Component tests

- Rendering.
- Props.
- User interactions.
- Accessibility.
- Loading and error states.

### Feature integration tests

- Module interactions.
- API integration.
- State synchronization.
- Permission behavior.

Use the project's existing testing framework.

Avoid testing private implementation details unless necessary.

## 21. Documentation

Document reusable modules when consumers need additional guidance.

Useful information:

- Purpose.
- Public API.
- Required props.
- Return values.
- Configuration.
- Usage examples.
- Dependencies.
- Limitations.
- Accessibility behavior.

Keep documentation close to the module or in the project's established documentation location.

Avoid documenting obvious implementation details that will become outdated.

## 22. Common Anti-Patterns

Avoid:

- Abstracting code too early.
- Creating giant shared utility files.
- Duplicating existing modules.
- Excessive barrel exports.
- Circular dependencies.
- Shared UI components containing business logic.
- Feature modules depending on unrelated features.
- Exposing internal implementation details.
- Overly generic components.
- Unnecessary configuration layers.
- Replacing stable modules without a clear benefit.
- Breaking consumers without migration guidance.

## 23. Decision Workflow

Before creating a reusable module:

1. Identify the repeated functionality.
1. Search existing implementations.
1. Define its responsibility.
1. Identify consumers.
1. Determine module boundaries.
1. Design a small public API.
1. Choose an appropriate location.
1. Implement with existing conventions.
1. Test expected behavior.
1. Document non-obvious usage.

Build reusable functionality around real requirements.

## 24. Review Checklist

### Architecture

- [ ] Module responsibility is clear.
- [ ] Existing modules have been checked.
- [ ] Dependencies flow in a predictable direction.
- [ ] Circular dependencies are avoided.

### API Design

- [ ] Public exports are intentional.
- [ ] Types are clear.
- [ ] Internal implementation stays private.
- [ ] Consumers are not unnecessarily coupled.

### Quality

- [ ] Accessibility is considered.
- [ ] Business logic is separated from generic UI.
- [ ] Tests cover important behavior.
- [ ] Documentation explains non-obvious usage.

### Existing Projects

- [ ] Existing consumers were inspected.
- [ ] Backward compatibility was considered.
- [ ] Unrelated features remain unchanged.
- [ ] Relevant checks pass.

## 25. Related References

- architecture-and-project-structure.md
- reusable-ui-components.md
- react-engineering.md
- nextjs-engineering.md
- typescript-and-code-quality.md
- api-integration.md
- forms-and-validation.md
- state-management.md
- package-selection-and-ecosystem.md
- testing-strategy.md

## 26. Official Resources

- React Documentation: https://react.dev/
- React Rules of Hooks: https://react.dev/reference/rules
- TypeScript Documentation: https://www.typescriptlang.org/docs/
- Next.js Documentation: https://nextjs.org/docs
- Node.js Modules: https://nodejs.org/api/modules.html
- npm Packages: https://docs.npmjs.com/creating-and-publishing-scoped-public-packages
