# Reusable UI Components

## 1. Purpose

Define engineering standards for building, maintaining and improving reusable frontend components.

Support:

- New component development.
- Existing component modification.
- Component refactoring.
- Shared UI libraries.
- Design system implementation.
- Accessibility.
- Component composition.
- Consistent variants.
- Type-safe APIs.
- Testing and documentation.

The objective is to build reusable components that solve real application needs without unnecessary abstraction.

## 2. Inspect Before Building

Before creating a component:

1. Inspect the existing component structure.
1. Search for an existing component with similar functionality.
1. Identify the installed UI library.
1. Review existing styling conventions.
1. Inspect existing variants and design tokens.
1. Check whether the component is already used elsewhere.
1. Understand accessibility requirements.
1. Identify whether the component belongs to a shared UI layer or a feature.

Never create a duplicate component without a reason.

For existing projects, extend or improve the current implementation when practical.

## 3. Component Architecture

Organize components according to responsibility.

Common categories:

### Primitive components

Small reusable building blocks.

Examples:

- Button.
- Input.
- Label.
- Checkbox.
- Radio.
- Switch.
- Badge.
- Avatar.
- Separator.
- Skeleton.
- Spinner.

### Composite components

Components composed of multiple primitives.

Examples:

- Search input.
- Form field.
- Select with search.
- Date picker.
- Pagination.
- Dropdown menu.
- Confirmation dialog.

### Application components

Components that represent application-level patterns.

Examples:

- Sidebar.
- Navbar.
- Data table.
- Filter panel.
- Notification center.
- Dashboard statistics.
- Empty state.
- Error state.

### Feature components

Components tied to a specific business feature.

Examples:

- User profile form.
- Product editor.
- Customer details panel.
- Order status timeline.

Do not put feature-specific business logic into generic UI primitives.

## 4. Component Folder Structure

Use the existing project convention.

One possible structure:

```text
components/
├── ui/
│   ├── button.tsx
│   ├── input.tsx
│   ├── dialog.tsx
│   ├── badge.tsx
│   └── index.ts
├── layout/
│   ├── sidebar.tsx
│   ├── header.tsx
│   └── navbar.tsx
└── shared/
    ├── empty-state.tsx
    └── error-state.tsx
```

Feature-specific components should generally remain close to their feature.

Example:

```text
features/
└── users/
    ├── components/
    │   ├── user-form.tsx
    │   └── user-table.tsx
    ├── hooks/
    ├── services/
    └── types/
```

This structure is illustrative, not mandatory.

Avoid creating empty folders or unnecessary index files.

## 5. Component API Design

A good component API should be:

- Predictable.
- Type-safe.
- Easy to understand.
- Consistent with native HTML behavior.
- Flexible where necessary.
- Small enough to maintain.

Example:

```tsx
interface ButtonProps {
  children: React.ReactNode;
  variant?: "primary" | "secondary" | "outline" | "ghost";
  size?: "sm" | "md" | "lg";
  disabled?: boolean;
  loading?: boolean;
  onClick?: () => void;
}
```

Avoid:

- Excessive optional props.
- Unclear boolean combinations.
- Unnecessary configuration objects.
- Business-specific props on generic components.
- Props that duplicate native HTML functionality.
- APIs that require consumers to understand internal implementation.

Use discriminated unions when certain props depend on other props.

## 6. Component Composition

Prefer composition when it produces clearer APIs.

Example:

```tsx
<Card>
  <CardHeader>
    <CardTitle>Account</CardTitle>
    <CardDescription>Manage account settings.</CardDescription>
  </CardHeader>

  <CardContent>Account information</CardContent>

  <CardFooter>
    <Button>Save changes</Button>
  </CardFooter>
</Card>
```

Composition can help when:

- Components have distinct sections.
- Consumers need flexible layouts.
- Different parts have independent responsibilities.
- A component has too many configuration props.

Do not introduce compound component patterns for simple components that do not need them.

## 7. Component Variants

Use consistent variants for repeated visual styles.

Example:

```tsx
type ButtonVariant =
  | "primary"
  | "secondary"
  | "outline"
  | "ghost"
  | "destructive";

type ButtonSize = "sm" | "md" | "lg";
```

Guidelines:

- Use meaningful variant names.
- Keep variant combinations manageable.
- Follow the existing styling system.
- Reuse design tokens.
- Avoid arbitrary one-off variants.
- Keep default behavior predictable.

Use existing variant utilities when available.

Examples include CVA or the project's existing class composition solution.

Do not install a new dependency solely to handle a few class combinations.

## 8. Native HTML and Accessibility

Use semantic HTML elements whenever possible.

Examples:

- `<button>` for actions.
- `<a>` for navigation.
- `<label>` for form labels.
- `<input>` for data entry.
- `<nav>` for navigation.
- `<main>` for primary content.
- `<dialog>` where appropriate.

Do not replace native elements with clickable `<div>` elements unnecessarily.

Ensure:

- Keyboard interaction.
- Accessible names.
- Focus visibility.
- Correct disabled behavior.
- Appropriate ARIA attributes.
- Logical focus order.
- Screen reader compatibility.

Use ARIA only when native HTML semantics are insufficient.

Do not add redundant ARIA attributes.

## 9. Ref and Native Props

Preserve native element capabilities when appropriate.

For example, a Button may support:

- `type`.
- `disabled`.
- `name`.
- `value`.
- `form`.
- `aria-*`.
- `data-*`.

Use appropriate HTML attribute types.

Do not expose every native property automatically if doing so creates an unsafe or confusing API.

Follow the React version's supported ref patterns.

React 19 supports passing `ref` as a prop in applicable components. Do not force `forwardRef` into every new component. Existing projects may still use it where appropriate.

## 10. Styling Standards

Components should use the project's established styling system.

Common approaches:

- Tailwind CSS.
- CSS Modules.
- Vanilla CSS.
- Styled components.
- Existing component-library styling.

Guidelines:

- Use semantic design tokens.
- Keep styles consistent.
- Avoid hardcoded colors.
- Support light and dark themes.
- Support responsive layouts.
- Avoid excessive specificity.
- Avoid duplicated style definitions.
- Avoid unnecessary runtime styling dependencies.

Do not mix multiple styling systems without a clear reason.

## 11. Component State

Keep state as close as practical to where it is used.

Distinguish:

- Local UI state.
- Shared UI state.
- Server state.
- Form state.
- URL state.
- Persisted user preferences.

Examples:

| State | Suitable location |
| ---------------- | --------------------- |
| Dropdown open | Local component |
| Dialog open | Local or parent |
| Current filters | URL or feature state |
| API data | Server-state solution |
| Form values | Form state |
| Theme preference | Theme system |

Avoid making every component globally stateful.

Do not duplicate state that can be derived from existing data.

## 12. Loading, Empty and Error States

Reusable components should communicate important states.

Consider:

- Loading.
- Empty.
- Error.
- Disabled.
- Success.
- Validation failure.
- Unauthorized.
- Offline.

Example:

```tsx
interface AsyncStateProps {
  loading: boolean;
  error?: string | null;
  isEmpty?: boolean;
}
```

Do not force unrelated components into one oversized state abstraction.

Create focused reusable components when a pattern genuinely repeats.

## 13. Component Library Integration

Evaluate existing libraries before implementing complex components.

Possible libraries include:

- Radix UI.
- shadcn/ui.
- React Aria.
- Headless UI.
- Mantine.
- Material UI.

Choose based on:

- Accessibility.
- Customization.
- Framework compatibility.
- Bundle impact.
- Maintenance.
- Existing project dependencies.
- Design requirements.

Important:

- shadcn/ui is a collection of component source code built on existing primitives, not simply a traditional runtime component package.
- Radix UI provides accessible component primitives.
- React Aria provides accessibility-focused interaction patterns.

Do not replace an existing component library without a clear technical or product reason.

Do not combine multiple component libraries unnecessarily.

## 14. Component Documentation

Document shared components when their behavior is not obvious.

Useful documentation:

- Purpose.
- Props.
- Variants.
- Usage examples.
- Accessibility behavior.
- Edge cases.
- Known limitations.

Use Storybook or another component documentation tool when the project benefits from a dedicated component development environment.

Do not introduce documentation infrastructure for a small application without a clear need.

## 15. Component Testing

Test meaningful behavior rather than implementation details.

Verify:

- Rendering.
- User interactions.
- Keyboard behavior.
- Accessible names.
- Disabled states.
- Loading states.
- Error states.
- Variant behavior.
- Responsive behavior where relevant.

Use the existing testing stack.

Avoid brittle tests that depend on internal class names or component implementation details.

## 16. Existing Component System Improvement

When modifying an existing component library:

1. Identify the affected component.
1. Find all relevant usages.
1. Understand its existing API.
1. Check dependent components.
1. Identify compatibility risks.
1. Plan the smallest safe change.
1. Update the component.
1. Update affected consumers.
1. Run relevant tests and checks.
1. Review for regressions.

Preserve existing public APIs where possible.

If a breaking API change is necessary, identify affected usages and migrate them deliberately.

Do not replace the entire UI library to fix one component.

## 17. Performance Considerations

Consider:

- Component rendering cost.
- Unnecessary state updates.
- Expensive calculations.
- Large dependency imports.
- Excessive context updates.
- Unnecessary component abstraction.
- Bundle size.
- Dynamic imports for genuinely heavy features.

Do not add `memo`, `useMemo` or `useCallback` everywhere.

Measure performance and use optimization where it provides a real benefit.

## 18. Common Anti-Patterns

Avoid:

- Duplicating existing components.
- Creating components for trivial one-use markup.
- Oversized generic components.
- Business logic inside primitive UI components.
- Excessive prop combinations.
- Unnecessary global state.
- Inaccessible clickable elements.
- Hardcoded colors.
- Excessive abstraction.
- Multiple competing UI libraries.
- Rewriting component systems unnecessarily.
- Breaking existing APIs without migration.

## 19. Decision Workflow

Before building or changing a reusable component:

1. Inspect the existing project.
1. Search for similar components.
1. Identify component responsibility.
1. Design a clear API.
1. Select the appropriate semantic HTML.
1. Reuse design tokens.
1. Add only necessary variants.
1. Handle accessibility and interaction states.
1. Verify affected consumers.
1. Test and document meaningful behavior.

Prefer composition and simplicity over excessive configurability.

## 20. Review Checklist

### Architecture

- [ ] Component responsibility is clear.
- [ ] Existing functionality is reused.
- [ ] Business logic is separated appropriately.
- [ ] Component placement follows project conventions.

### API

- [ ] Props are type-safe.
- [ ] Variants are consistent.
- [ ] Native behavior is preserved.
- [ ] No unnecessary configuration exists.

### Accessibility

- [ ] Semantic HTML is used.
- [ ] Keyboard interaction works.
- [ ] Accessible names are present.
- [ ] Focus behavior is correct.

### Styling

- [ ] Design tokens are reused.
- [ ] Light and dark themes work.
- [ ] Responsive behavior is considered.
- [ ] Existing styling conventions are followed.

### Verification

- [ ] Relevant usages are checked.
- [ ] Tests pass.
- [ ] Type checking passes.
- [ ] No unrelated functionality is broken.

## 21. Related References

- architecture-and-project-structure.md
- global-styles-and-design-tokens.md
- theming-and-dark-mode.md
- layouts-and-navigation.md
- dialogs-modals-and-overlays.md
- notifications-and-push.md
- accessibility-and-wcag.md
- testing-strategy.md

## 22. Official Resources

- React Components: https://react.dev/learn/your-first-component
- React Props: https://react.dev/learn/passing-props-to-a-component
- React Composition: https://react.dev/learn/passing-props-to-a-component
- React TypeScript: https://react.dev/learn/typescript
- Radix UI: https://www.radix-ui.com/primitives/docs/overview/introduction
- React Aria: https://react-spectrum.adobe.com/react-aria/
- shadcn/ui: https://ui.shadcn.com/docs
- Storybook: https://storybook.js.org/docs
- Testing Library: https://testing-library.com/docs/react-testing-library/intro/
