# TypeScript and Code Quality

## 1. Purpose

Define consistent TypeScript and code-quality standards for production frontend applications.

The goal is to produce code that is:

- Type-safe.
- Readable.
- Maintainable.
- Predictable.
- Testable.
- Easy to extend.
- Resistant to runtime errors.

Use TypeScript to improve correctness, not to create unnecessary type complexity.

## 2. TypeScript Configuration

Use strict TypeScript settings for new projects.

Recommended starting configuration:

```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitReturns": true,
    "forceConsistentCasingInFileNames": true,
    "skipLibCheck": true
  }
}
```

Adapt the configuration to the framework and existing project.

Do not blindly replace an existing `tsconfig.json`.

Important considerations:

- Preserve framework-required settings.
- Use appropriate module resolution.
- Maintain path aliases consistently.
- Avoid weakening strictness to hide errors.
- Keep compiler settings compatible with installed dependencies.

## 3. Type vs Interface

Both `type` and `interface` are valid.

Use consistent conventions.

### Prefer interface for object contracts

```ts
interface User {
  id: string;
  name: string;
  email: string;
}
```

### Use type for unions and compositions

```ts
type Status = "pending" | "success" | "error";

type UserSummary = Pick<User, "id" | "name">;
```

Do not create unnecessary aliases for simple types.

Choose the approach that makes the code easiest to understand.

## 4. Avoid Any

Avoid `any` because it disables meaningful type checking.

Bad:

```ts
function getUser(user: any) {
  return user.name;
}
```

Better:

```ts
interface User {
  id: string;
  name: string;
}

function getUser(user: User): string {
  return user.name;
}
```

When the data shape is unknown, prefer `unknown`.

```ts
function handleError(error: unknown) {
  if (error instanceof Error) {
    console.error(error.message);
    return;
  }

  console.error("An unexpected error occurred.");
}
```

Do not use type assertions simply to silence compiler errors.

Use assertions only when the developer has verified the actual runtime shape.

## 5. Type Narrowing

Use TypeScript narrowing to handle uncertain values safely.

Common techniques:

- `typeof`
- `instanceof`
- `in`
- Equality checks.
- Discriminated unions.
- Custom type guards.

Example:

```ts
type ApiResult<T> =
  | { success: true; data: T }
  | { success: false; message: string };

function handleResult<T>(result: ApiResult<T>) {
  if (result.success) {
    return result.data;
  }

  throw new Error(result.message);
}
```

Prefer discriminated unions over loosely related optional properties.

## 6. Utility Types

Use built-in utility types where they improve clarity.

Common utilities:

| Utility | Purpose |
| ---------------- | ----------------------------- |
| `Partial<T>` | Makes properties optional |
| `Required<T>` | Makes properties required |
| `Pick<T, K>` | Selects properties |
| `Omit<T, K>` | Removes properties |
| `Record<K, V>` | Creates keyed object types |
| `Readonly<T>` | Makes properties readonly |
| `NonNullable<T>` | Removes null and undefined |
| `ReturnType<T>` | Extracts function return type |
| `Parameters<T>` | Extracts function parameters |
| `Awaited<T>` | Resolves promise return types |

Example:

```ts
interface User {
  id: string;
  name: string;
  email: string;
  password: string;
}

type PublicUser = Omit<User, "password">;
type UserUpdate = Partial<Pick<User, "name" | "email">>;
```

Avoid deeply nested utility types when a simple interface is easier to maintain.

## 7. Generics

Use generics when the same implementation genuinely works with multiple types.

Example:

```ts
function identity<T>(value: T): T {
  return value;
}
```

Typed API response:

```ts
interface ApiResponse<T> {
  data: T;
  message: string;
  success: boolean;
}
```

Usage:

```ts
interface Product {
  id: string;
  name: string;
}

type ProductResponse = ApiResponse<Product[]>;
```

Do not introduce generics when a concrete type is clearer.

## 8. API Type Safety

Define explicit types for API requests and responses.

Example:

```ts
interface CreateUserRequest {
  name: string;
  email: string;
}

interface UserResponse {
  id: string;
  name: string;
  email: string;
  createdAt: string;
}
```

Keep request and response types separate when their shapes differ.

Do not assume that frontend types validate actual server responses.

TypeScript types disappear at runtime.

For untrusted data, validate the runtime shape using an appropriate schema-validation solution.

Examples include:

- Zod.
- Valibot.
- ArkType.

Choose one based on project requirements. Do not add multiple validation libraries without a clear reason.

## 9. Runtime Validation

Validate data received from:

- External APIs.
- URL query parameters.
- Forms.
- Local storage.
- Browser storage.
- Third-party integrations.
- User-controlled inputs.

Example using Zod:

```ts
import { z } from "zod";

const userSchema = z.object({
  id: z.string(),
  name: z.string().min(1),
  email: z.email(),
});

type User = z.infer<typeof userSchema>;

const user = userSchema.parse(responseData);
```

Use `safeParse` when validation failure should be handled without throwing.

Do not trust data simply because it has been assigned a TypeScript interface.

## 10. React Component Types

Use explicit prop types.

```tsx
interface ButtonProps {
  children: React.ReactNode;
  variant?: "primary" | "secondary" | "outline";
  disabled?: boolean;
  onClick?: () => void;
}

export function Button({
  children,
  variant = "primary",
  disabled = false,
  onClick,
}: ButtonProps) {
  return (
    <button
      type="button"
      disabled={disabled}
      data-variant={variant}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
```

Guidelines:

- Keep props focused.
- Use meaningful names.
- Prefer discriminated unions for mutually exclusive props.
- Avoid unnecessary prop forwarding.
- Avoid overly generic components.
- Use semantic HTML elements.
- Preserve native element behavior.
- Type event handlers correctly.

Do not use `React.FC` by default. Use ordinary function declarations with typed props unless a specific requirement justifies another approach.

## 11. Event Types

Use the appropriate React event types.

Examples:

```tsx
import type { ChangeEvent, FormEvent, MouseEvent } from "react";

function handleChange(event: ChangeEvent<HTMLInputElement>) {
  console.log(event.target.value);
}

function handleSubmit(event: FormEvent<HTMLFormElement>) {
  event.preventDefault();
}

function handleClick(event: MouseEvent<HTMLButtonElement>) {
  console.log(event.currentTarget);
}
```

Avoid manually recreating React event types.

## 12. Null and Undefined Handling

Handle nullable values intentionally.

Avoid non-null assertions when the value has not been verified.

Bad:

```ts
const userName = user!.name;
```

Better:

```ts
const userName = user?.name ?? "Unknown user";
```

Use optional chaining and nullish coalescing appropriately.

Distinguish between:

- Missing values.
- Explicit `null`.
- Empty strings.
- Empty arrays.
- Zero.
- `false`.

Do not use truthy checks when zero or false are valid values.

## 13. Error Handling

Use predictable error handling.

Avoid swallowing errors.

Bad:

```ts
try {
  await saveUser();
} catch {
  // Ignore
}
```

Better:

```ts
try {
  await saveUser();
} catch (error: unknown) {
  if (error instanceof Error) {
    console.error(error.message);
  } else {
    console.error("Unexpected error.");
  }

  throw error;
}
```

Application-specific error handling should:

- Provide meaningful user feedback.
- Preserve useful debugging information.
- Avoid exposing internal server details.
- Distinguish validation, network, authorization and server errors.
- Support retry only when safe.
- Avoid logging secrets or personal data.

Create shared error utilities when they remove meaningful duplication.

## 14. Code Organization

Keep code organized around responsibility.

Recommended principles:

- Group related functionality.
- Separate UI from business logic when useful.
- Keep API communication in a dedicated layer.
- Keep shared types in appropriate locations.
- Avoid circular dependencies.
- Avoid oversized components and utility files.
- Avoid creating files for every trivial expression.

Use feature-oriented organization when it improves maintainability.

Do not force a complex architecture on a small application.

## 15. Naming Conventions

Use consistent naming.

| Item | Convention |
| -------------------- | ----------------------------------------------- |
| Components | PascalCase |
| Interfaces and types | PascalCase |
| Functions | camelCase |
| Variables | camelCase |
| Constants | camelCase or UPPER_SNAKE_CASE where appropriate |
| Hooks | `use` prefix |
| Boolean variables | `is`, `has`, `can`, `should` prefixes |
| Event handlers | `handle` prefix |
| Event props | `on` prefix |
| Files | Follow existing project convention |

Choose descriptive names.

Avoid vague names such as:

- `data`
- `item`
- `value`
- `temp`
- `helper`
- `common`

These names are acceptable when the context makes their meaning obvious.

## 16. Code Quality Principles

Follow these principles:

### Readability

- Prefer straightforward code.
- Keep functions focused.
- Use meaningful names.
- Avoid deeply nested conditions.
- Use early returns where they improve clarity.

### Maintainability

- Avoid unnecessary duplication.
- Extract shared logic only when reuse is meaningful.
- Keep dependencies explicit.
- Limit side effects.
- Keep modules cohesive.

### Simplicity

- Follow KISS.
- Follow YAGNI.
- Avoid premature abstraction.
- Avoid unnecessary design patterns.
- Do not overengineer simple requirements.

### Reliability

- Handle expected failure cases.
- Validate external data.
- Keep types accurate.
- Avoid hidden state.
- Make side effects predictable.

## 17. ESLint, Oxlint and Formatting

Use the existing project's tooling where practical.

Possible tools:

- TypeScript compiler.
- ESLint.
- Oxlint.
- Prettier.
- Biome.

Do not install every tool.

Choose a minimal compatible toolchain.

### Linting

Use lint rules to catch:

- Unused variables.
- Unsafe patterns.
- Incorrect React Hooks usage.
- Accessibility issues where supported.
- Suspicious imports.
- Unnecessary complexity.

### Formatting

Use a consistent formatter.

Formatting should be automated rather than enforced through manual review.

### Import organization

Maintain consistent import grouping:

1. Framework and external packages.
1. Internal aliases.
1. Relative modules.
1. Styles and assets.

Adapt to the repository's established conventions.

Avoid unnecessary import-order tooling when the existing formatter or linter already handles it.

## 18. Testing Type Safety

Verify:

- TypeScript compilation.
- Component prop contracts.
- API request and response types.
- Runtime validation.
- Error handling.
- Nullable values.
- Edge cases.

Run the project's actual type-check command.

Do not assume a successful build always means there are no TypeScript errors.

Check the scripts in `package.json` before choosing commands.

## 19. Common Anti-Patterns

Avoid:

- Using `any` to bypass errors.
- Excessive type assertions.
- Duplicated type definitions.
- Overly complex generics.
- Unnecessary abstractions.
- Huge shared utility files.
- Ignoring nullable values.
- Assuming runtime API data matches TypeScript types.
- Swallowing exceptions.
- Disabling lint rules without justification.
- Using multiple formatters that conflict.
- Replacing project tooling without a clear benefit.

## 20. Decision Workflow

Before implementing TypeScript changes:

1. Inspect the existing TypeScript configuration.
1. Identify installed framework and library versions.
1. Understand existing naming and file conventions.
1. Reuse existing types where appropriate.
1. Define explicit API contracts.
1. Validate untrusted runtime data.
1. Handle errors and nullable values.
1. Keep abstractions proportional to complexity.
1. Run type checking and linting.
1. Verify affected functionality.

Prefer clear, maintainable types over clever type-level programming.

## 21. Review Checklist

### Type safety

- [ ] Strict TypeScript settings are enabled where practical.
- [ ] `any` is avoided.
- [ ] External data is validated.
- [ ] Nullable values are handled.
- [ ] API contracts are explicit.
- [ ] Type assertions are justified.

### Code quality

- [ ] Functions have clear responsibilities.
- [ ] Names are meaningful.
- [ ] Duplication is minimized.
- [ ] Abstractions are justified.
- [ ] Side effects are predictable.
- [ ] Errors are handled appropriately.

### Tooling

- [ ] Type checking passes.
- [ ] Linting passes.
- [ ] Formatting is consistent.
- [ ] Existing project tooling is respected.

## 22. Related References

- architecture-and-project-structure.md
- react-engineering.md
- nextjs-engineering.md
- rendering-and-caching-strategies.md
- api-integration.md
- forms-and-validation.md
- frontend-security-owasp.md
- testing-strategy.md

## 23. Official Resources

- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- TypeScript TSConfig: https://www.typescriptlang.org/tsconfig/
- React TypeScript Guide: https://react.dev/learn/typescript
- Zod: https://zod.dev/
- ESLint: https://eslint.org/docs/latest/
- Oxlint: https://oxc.rs/docs/guide/usage/linter.html
- Prettier: https://prettier.io/docs/
