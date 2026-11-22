# Reusable React Components

## 1. Purpose

Demonstrate how to design, implement and maintain reusable React components using TypeScript.

The objective is to create components that are:

- Reusable.
- Composable.
- Accessible.
- Type-safe.
- Consistent.
- Maintainable.
- Easy to extend.
- Independent of unrelated business logic.

This example is a reference for frontend engineering agents.

Do not treat every component as something that must be extracted into a shared library.

## 2. Core Principles

Follow these principles:

1. Understand the component's responsibility.
1. Prefer composition over excessive configuration.
1. Use native HTML elements where appropriate.
1. Define clear TypeScript contracts.
1. Keep components focused.
1. Make interactive components accessible.
1. Reuse existing components when possible.
1. Avoid unnecessary abstractions.
1. Keep styling consistent.
1. Verify behavior and edge cases.

A reusable component should reduce duplication without introducing more complexity than it removes.

## 3. Component Categories

Organize components according to their actual responsibilities.

### Primitive Components

Small UI building blocks.

Examples:

- Button.
- Input.
- Label.
- Checkbox.
- Badge.
- Spinner.

### Composite Components

Components combining multiple primitives.

Examples:

- Search input.
- Form field.
- Pagination.
- Dropdown.
- Dialog.

### Application Components

Components used across application areas.

Examples:

- Header.
- Sidebar.
- Empty state.
- Page header.
- Data table.

### Feature Components

Components tied to a specific business feature.

Examples:

- Customer form.
- Product summary.
- Dashboard statistics.

Do not place every component inside a global shared UI directory.

## 4. Suggested Structure

```text
src/
├── components/
│   ├── ui/
│   │   ├── button.tsx
│   │   ├── input.tsx
│   │   ├── label.tsx
│   │   ├── checkbox.tsx
│   │   └── badge.tsx
│   ├── shared/
│   │   ├── empty-state.tsx
│   │   └── page-header.tsx
│   └── layout/
│       └── app-header.tsx
└── features/
    └── customers/
        └── components/
            └── customer-form.tsx
```

This is an example, not a mandatory architecture.

Choose a structure that matches the application's size and existing conventions.

## 5. Component API Design

A component's public API should be clear and predictable.

Example:

```tsx
type ButtonProps = {
  children: React.ReactNode;
  variant?: "primary" | "secondary" | "outline" | "ghost";
  size?: "sm" | "md" | "lg";
  disabled?: boolean;
  onClick?: React.MouseEventHandler<HTMLButtonElement>;
};
```

Consider:

- Required versus optional props.
- Sensible defaults.
- Native HTML attributes.
- Event handler types.
- Composition.
- Controlled and uncontrolled behavior.
- Accessibility requirements.

Avoid adding props that do not represent a real component responsibility.

## 6. Button Example

Prefer native button behavior.

```tsx
// src/components/ui/button.tsx

import type { ButtonHTMLAttributes } from "react";

type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: "primary" | "secondary" | "outline";
  size?: "sm" | "md" | "lg";
};

export function Button({
  children,
  variant = "primary",
  size = "md",
  type = "button",
  className,
  ...props
}: ButtonProps) {
  return (
    <button
      type={type}
      className={`button button--${variant} button--${size} ${className ?? ""}`}
      {...props}
    >
      {children}
    </button>
  );
}
```

Important:

- Use `type="button"` as the default to prevent accidental form submission.
- Allow callers to provide `type="submit"` when required.
- Preserve native button attributes.
- Ensure disabled states are visually and functionally clear.
- Use a consistent styling solution in the actual project.

Do not introduce a class-merging dependency unless the project needs one.

## 7. Composition

Prefer composing smaller components when it improves flexibility.

Example:

```tsx
type CardProps = {
  children: React.ReactNode;
  className?: string;
};

export function Card({ children, className }: CardProps) {
  return <section className={`card ${className ?? ""}`}>{children}</section>;
}
```

Usage:

```tsx
<Card>
  <h2>Account Overview</h2>
  <p>Manage your account settings.</p>
  <Button>View account</Button>
</Card>
```

Avoid creating large components with dozens of boolean props to control unrelated sections.

## 8. Native HTML and Accessibility

Prefer native HTML elements.

Examples:

- `<button>` for actions.
- `<a>` for navigation.
- `<input>` for user input.
- `<label>` for form labels.
- `<nav>` for navigation.
- `<main>` for primary content.
- `<dialog>` or an accessible dialog primitive for dialogs.

Do not replace native elements with clickable `<div>` elements without a valid reason.

Verify:

- Accessible names.
- Keyboard interaction.
- Focus behavior.
- Disabled behavior.
- Semantic structure.
- Screen reader announcements where necessary.

Use ARIA only when native HTML does not provide the required semantics.

## 9. Input Component Example

```tsx
// src/components/ui/input.tsx

import type { InputHTMLAttributes } from "react";

type InputProps = InputHTMLAttributes<HTMLInputElement>;

export function Input({ className, ...props }: InputProps) {
  return <input className={`input ${className ?? ""}`} {...props} />;
}
```

Usage:

```tsx
<label htmlFor="email">Email address</label>

<Input
  id="email"
  name="email"
  type="email"
  autoComplete="email"
  required
/>
```

Keep label and validation responsibilities clear.

A reusable input must not silently remove native attributes or accessibility behavior.

## 10. Controlled and Uncontrolled Components

Understand the difference.

### Controlled

The parent owns the value.

```tsx
<Input value={email} onChange={(event) => setEmail(event.target.value)} />
```

### Uncontrolled

The browser owns the value.

```tsx
<Input defaultValue="user@example.com" />
```

Use the approach appropriate to the form and application.

Do not mix `value` and `defaultValue` for the same input.

## 11. Variants and Styling

Choose a styling strategy consistent with the project.

Possible approaches:

- CSS Modules.
- Tailwind CSS.
- CSS variables.
- Existing design system utilities.
- A variant utility when the project needs it.

Keep variants explicit and predictable.

Avoid:

- Excessive conditional class strings.
- Arbitrary inline styles for shared design rules.
- Inconsistent spacing.
- Duplicated color values.
- Hidden styling dependencies.
- Uncontrolled combinations of boolean props.

Use semantic design tokens where appropriate.

## 12. Component State

Keep state close to the component that owns it.

Use local state for temporary UI behavior.

Use shared state only when multiple parts of the application need the same state.

Avoid:

- Duplicating derived state.
- Storing values that can be calculated.
- Global state for simple local interactions.
- Unnecessary effects.
- State updates during rendering.

See `../../references/state-management.md`.

## 13. Loading, Empty and Error States

Reusable data-oriented components should support meaningful states.

Examples:

- Loading indicator.
- Empty state.
- Error state.
- Retry action.
- Disabled state.

Do not display fake data as if it came from a real API.

Separate presentation components from data-fetching responsibilities when appropriate.

## 14. Ref and Native Attribute Support

When wrapping native elements, consider whether consumers need access to:

- Native HTML attributes.
- Event handlers.
- Focus management.
- Element references.

Preserve native attributes where appropriate.

Use React's current ref conventions for the installed version.

Do not introduce `forwardRef` automatically without checking the React version and component requirements.

## 15. UI Libraries and Primitives

Before building complex interactive components, inspect whether the project already uses a UI library or accessible primitive.

Possible options:

- Radix UI.
- React Aria.
- Headless UI.
- shadcn/ui.
- Mantine.
- Material UI.

Choose based on:

- Accessibility.
- Project compatibility.
- Styling requirements.
- Bundle impact.
- Maintenance.
- Existing dependencies.

Do not introduce multiple libraries that solve the same problem without justification.

## 16. Documentation

Document components when their public API or behavior is not obvious.

Useful documentation includes:

- Purpose.
- Props.
- Variants.
- Usage.
- Accessibility behavior.
- Controlled/uncontrolled behavior.
- Known limitations.

Avoid writing documentation that simply repeats the implementation.

## 17. Testing

Test behavior rather than internal implementation details.

For interactive components, consider:

- Rendering.
- Props.
- User interactions.
- Disabled behavior.
- Keyboard behavior.
- Accessible names.
- Form integration.
- Error states.

Example:

```tsx
import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import { Button } from "./button";

describe("Button", () => {
  it("renders its children", () => {
    render(<Button>Save</Button>);

    expect(screen.getByRole("button", { name: "Save" })).toBeInTheDocument();
  });
});
```

This example assumes the project has configured Vitest, React Testing Library and the appropriate DOM matchers.

Do not add testing dependencies solely to copy this snippet.

## 18. Existing Component System Changes

When modifying an existing component:

1. Inspect its implementation.
1. Find its usage across the project.
1. Review its public props.
1. Check styling conventions.
1. Identify dependent components.
1. Review existing tests.
1. Preserve backwards compatibility where practical.
1. Implement the requested change.
1. Verify affected usages.

Do not rename props or change defaults without considering existing consumers.

Avoid creating a second component that duplicates an existing one.

## 19. Performance

Keep components efficient without premature optimization.

Consider:

- Expensive rendering.
- Large lists.
- Unnecessary state.
- Expensive calculations.
- Large dependency imports.
- Unnecessary client-side JavaScript.

Use memoization only when profiling or component behavior justifies it.

Do not add `memo`, `useMemo` or `useCallback` everywhere by default.

## 20. Common Anti-Patterns

Avoid:

- One component handling unrelated responsibilities.
- Excessive boolean props.
- Overly generic components.
- Business logic inside basic UI primitives.
- Repeated UI implementations.
- Unnecessary wrapper components.
- Missing native HTML attributes.
- Inaccessible custom controls.
- Uncontrolled styling conventions.
- Unnecessary global state.
- Premature component extraction.
- Unnecessary dependencies.

## 21. Review Checklist

### Design

- [ ] Component responsibility is clear.
- [ ] Public API is understandable.
- [ ] Composition is supported where appropriate.
- [ ] Existing components are reused where practical.

### TypeScript

- [ ] Props are correctly typed.
- [ ] Native attributes are preserved where appropriate.
- [ ] Unnecessary `any` is avoided.
- [ ] Defaults are predictable.

### Accessibility

- [ ] Semantic HTML is used.
- [ ] Accessible names are present.
- [ ] Keyboard behavior is correct.
- [ ] Focus behavior is correct where applicable.

### Quality

- [ ] Loading, empty and error states are considered.
- [ ] Styling follows existing conventions.
- [ ] No unnecessary abstractions exist.
- [ ] Relevant tests pass.
- [ ] Existing consumers remain compatible.

## 22. Related References

- `../../references/react-engineering.md`
- `../../references/typescript-and-code-quality.md`
- `../../references/reusable-ui-components.md`
- `../../references/global-styles-and-design-tokens.md`
- `../../references/theming-and-dark-mode.md`
- `../../references/accessibility-and-wcag.md`
- `../../references/state-management.md`
- `../../references/testing-strategy.md`
- `../../references/package-selection-and-ecosystem.md`
- `../../references/anti-ai-slop-and-engineering-quality.md`

## 23. Official Resources

- React Components: https://react.dev/learn/your-first-component
- Passing Props: https://react.dev/learn/passing-props-to-a-component
- Sharing State: https://react.dev/learn/sharing-state-between-components
- React TypeScript: https://react.dev/learn/typescript
- TypeScript: https://www.typescriptlang.org/docs/
- WAI-ARIA Authoring Practices: https://www.w3.org/WAI/ARIA/apg/
- React Testing Library: https://testing-library.com/docs/react-testing-library/intro/
