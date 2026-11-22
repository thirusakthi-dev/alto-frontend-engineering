# React Engineering

## 1. Purpose

Define modern React engineering practices for building maintainable, reusable, accessible and performant applications.

The agent must understand React's rendering model and composition principles instead of treating React as a collection of hooks.

Prioritize:

- Correct React patterns.
- Component composition.
- Predictable state management.
- Reusable logic.
- Rendering performance.
- Accessibility.
- Type safety.
- Maintainability.
- Modern React APIs.

## 2. Version Awareness

Before implementing React features:

1. Inspect installed React and React DOM versions.
1. Check the project's TypeScript version.
1. Inspect framework and bundler compatibility.
1. Verify APIs against official React documentation.
1. Use APIs supported by the installed version.

### React version guidance

- React 19 introduced Actions, `useActionState`, `useOptimistic`, `use`, ref as a prop and improved form handling.
- React 19.2 introduced Activity, `useEffectEvent` and React Performance Tracks.
- React 19.3 introduced stable View Transitions, Fragment Refs, `browser()` and Trusted Types support.

Do not assume that every project supports the latest APIs.

Do not introduce experimental or Canary APIs into production projects without explicit justification.

Official documentation:
https://react.dev/reference/react

## 3. Component Fundamentals

Prefer functional components.

Use clear names and explicit props.

Example:

```tsx
type UserCardProps = {
  name: string;
  email: string;
  imageUrl?: string;
};

export function UserCard({ name, email, imageUrl }: UserCardProps) {
  return (
    <article>
      {imageUrl && <img src={imageUrl} alt="" />}

      <h2>{name}</h2>
      <p>{email}</p>
    </article>
  );
}
```

### Component standards

- Keep components focused.
- Use meaningful names.
- Define explicit prop types.
- Prefer composition over excessive configuration.
- Avoid unnecessary component nesting.
- Keep business logic understandable.
- Use semantic HTML.
- Handle empty and optional values.
- Avoid unnecessary wrapper elements.

Do not split every JSX element into a separate component.

Create components when they provide meaningful reuse, separation or readability.

## 4. Component Composition

Prefer composition over complicated prop APIs.

Example:

```tsx
type CardProps = {
  title: string;
  children: React.ReactNode;
  footer?: React.ReactNode;
};

export function Card({ title, children, footer }: CardProps) {
  return (
    <section className="card">
      <h2>{title}</h2>

      <div className="card-content">{children}</div>

      {footer && <footer>{footer}</footer>}
    </section>
  );
}
```

Use composition for:

- Dialogs.
- Cards.
- Layouts.
- Forms.
- Navigation.
- Tables.
- Complex reusable UI.

Avoid components with excessive boolean props such as:

```tsx
<Button primary rounded large outlined loading danger compact />
```

Prefer a small, intentional and documented component API.

## 5. Rules of React

Follow the Rules of React.

### Component purity

- Components must be pure during rendering.
- Do not perform side effects during render.
- Do not mutate props or state.
- Do not modify values after passing them to JSX.
- Keep rendering predictable.

### Rules of Hooks

- Call hooks only at the top level of React components or custom hooks.
- Do not call hooks inside conditions.
- Do not call hooks inside loops.
- Do not call hooks inside nested functions.
- Do not call hooks from ordinary JavaScript utility functions.

Correct:

```tsx
function Profile() {
  const [name, setName] = useState("");

  if (!name) {
    return <p>No name available</p>;
  }

  return <p>{name}</p>;
}
```

Incorrect:

```tsx
function Profile({ enabled }: { enabled: boolean }) {
  if (enabled) {
    const [name] = useState("");
  }

  return null;
}
```

Use React Strict Mode during development where supported.

Follow the React Hooks ESLint rules.

Reference:
https://react.dev/reference/rules

## 6. React Hooks

Use hooks according to their actual responsibilities.

### useState

Use for local component state.

Examples:

- Dialog visibility.
- Selected tabs.
- Input values.
- Local UI preferences.

Use functional updates when the next state depends on the previous state.

```tsx
setCount((previous) => previous + 1);
```

### useReducer

Use when state transitions involve multiple related values or complex update logic.

Do not use reducers for simple state that is easier to manage with useState.

### useEffect

Use Effects to synchronize React with external systems.

Examples:

- Browser event listeners.
- WebSocket connections.
- Third-party widgets.
- Browser APIs.
- Subscriptions.

Example:

```tsx
useEffect(() => {
  function handleResize() {
    console.log(window.innerWidth);
  }

  window.addEventListener("resize", handleResize);

  return () => {
    window.removeEventListener("resize", handleResize);
  };
}, []);
```

Important:

- Include correct dependencies.
- Clean up subscriptions and event listeners.
- Avoid unnecessary Effects.
- Avoid using Effects to derive values from props or state.
- Avoid using Effects as a replacement for event handlers.
- Avoid triggering unnecessary render cycles.

If there is no external system to synchronize with, consider whether an Effect is necessary.

### useRef

Use for mutable values that do not need to trigger rendering.

Examples:

- DOM references.
- Timer identifiers.
- Previous values when genuinely needed.
- Imperative integrations.

Do not use refs as a replacement for normal React state.

### useContext

Use for values shared across a component subtree.

Examples:

- Theme.
- Authentication context.
- Locale.
- Application configuration.

Avoid placing frequently changing, unrelated application state into one large context.

### useMemo and useCallback

Use only when there is a measurable or meaningful reason.

Possible use cases:

- Expensive calculations.
- Stable references for optimized children.
- Dependencies of other hooks.
- Referential stability required by an integration.

Do not wrap every calculation or function automatically.

### useTransition

Use to mark non-urgent state updates.

Suitable for:

- Expensive filtering.
- Large UI transitions.
- Non-blocking navigation or updates.

Do not use transitions for controlled input updates that must remain immediate.

### useDeferredValue

Use when a part of the UI can update later than the primary interaction.

Example use cases:

- Large search results.
- Expensive filtered lists.
- Non-critical visual updates.

### useId

Use to generate stable IDs for accessibility relationships.

Do not use useId as a list key.

### React 19 hooks and APIs

Understand these APIs:

| API | Purpose |
| -------------------- | ----------------------------------------------------- |
| use | Read supported resources such as Promises and Context |
| useActionState | Manage Action state and submission results |
| useOptimistic | Show optimistic UI updates |
| useFormStatus | Read the status of a parent form submission |
| useEffectEvent | Separate non-reactive event logic from Effects |
| useSyncExternalStore | Subscribe to external stores |

Use them only when their use cases match the requirement.

## 7. React 19 and Actions

Understand React 19 Actions and form improvements.

### useActionState

Use when managing an Action's result and pending state.

Example:

```tsx
import { useActionState } from "react";

type FormState = {
  error: string | null;
};

async function updateProfile(
  _previousState: FormState,
  formData: FormData,
): Promise<FormState> {
  const name = formData.get("name");

  if (typeof name !== "string" || !name.trim()) {
    return { error: "Name is required." };
  }

  // Perform the actual update through a trusted server/API.
  return { error: null };
}

function ProfileForm() {
  const [state, formAction, isPending] = useActionState(updateProfile, {
    error: null,
  });

  return (
    <form action={formAction}>
      <label htmlFor="name">Name</label>
      <input id="name" name="name" required />

      <button type="submit" disabled={isPending}>
        {isPending ? "Saving..." : "Save"}
      </button>

      {state.error && <p role="alert">{state.error}</p>}
    </form>
  );
}
```

This example demonstrates the React Action interface. The actual persistence, authentication and authorization must be implemented separately.

### useOptimistic

Use when immediate UI feedback improves an interaction.

Examples:

- Adding a comment.
- Updating a favorite.
- Sending a message.
- Changing a status.

Ensure the UI can recover when the underlying operation fails.

### useFormStatus

Use inside a child component of a form to access its submission status.

Do not call it in the same component that directly renders the form and expect it to describe that form.

### Ref as a prop

React 19 supports passing ref as a prop to function components.

Do not introduce forwardRef automatically in new React 19 components.

Check compatibility when maintaining older React versions.

## 8. React 19.2 and 19.3

Use newer capabilities when they solve a real problem.

### React 19.2

Understand:

- Activity.
- useEffectEvent.
- React Performance Tracks.

Do not introduce these APIs merely because they are available.

### React 19.3

Understand:

- ViewTransition.
- Fragment Refs.
- browser().
- Trusted Types integration.
- Direct Context rendering in supported Server Component environments.

Important considerations:

- ViewTransition is useful for coordinated UI transitions.
- Respect reduced-motion preferences.
- Fragment Refs can provide access to multiple DOM children without an extra wrapper.
- browser() is useful for intentionally browser-only rendering in supported environments.
- Trusted Types support does not replace safe handling and sanitization of untrusted content.

Check framework and library compatibility before adopting newer features.

## 9. Custom Hooks

Create custom hooks to reuse stateful behavior.

Examples:

- useDebounce.
- useMediaQuery.
- useLocalStorage.
- useClickOutside.
- useOnlineStatus.
- useClipboard.
- useIntersectionObserver.

Guidelines:

- Prefix custom hooks with use.
- Keep responsibilities focused.
- Define explicit return types when helpful.
- Handle cleanup correctly.
- Avoid hiding complex side effects.
- Avoid creating hooks that simply rename one built-in hook.
- Make browser-only assumptions explicit.
- Consider SSR and hydration behavior.

Example:

```tsx
function useOnlineStatus() {
  const [isOnline, setIsOnline] = useState(true);

  useEffect(() => {
    const updateStatus = () => {
      setIsOnline(navigator.onLine);
    };

    updateStatus();

    window.addEventListener("online", updateStatus);
    window.addEventListener("offline", updateStatus);

    return () => {
      window.removeEventListener("online", updateStatus);
      window.removeEventListener("offline", updateStatus);
    };
  }, []);

  return isOnline;
}
```

For applications that require robust external-store subscription semantics, evaluate useSyncExternalStore.

## 10. State Management

Identify the type of state before selecting a solution.

| State | Preferred approach |
| -------------------- | ----------------------------------------------- |
| Component UI state | useState |
| Complex local state | useReducer |
| Shared subtree state | Context |
| Server state | TanStack Query or framework-native data loading |
| Shared client state | Zustand or Context |
| Complex global state | Redux Toolkit |
| URL state | URL search parameters or nuqs |
| Form state | React Hook Form |

### State management rules

- Keep state close to where it is used.
- Avoid duplicating derived state.
- Avoid storing values that can be calculated.
- Avoid unnecessary global state.
- Separate server state from client state.
- Use stable and predictable update patterns.
- Avoid synchronizing multiple state systems without a reason.

Do not install a global state library for a simple component.

## 11. Rendering and Reconciliation

Understand how React renders and updates the UI.

Consider:

- Component rendering.
- Reconciliation.
- Element identity.
- Keys.
- State preservation.
- Component mounting and unmounting.
- Context updates.
- Suspense boundaries.
- Concurrent rendering.

### List keys

Use stable and unique keys.

Correct:

```tsx
users.map((user) => <UserCard key={user.id} user={user} />);
```

Avoid array indices when items can be reordered, inserted or removed.

Never generate random keys during rendering.

### Component identity

Avoid defining component types inside another component when doing so causes them to be recreated on every render.

Keep component definitions stable when their identity matters.

## 12. Performance Optimization

Optimize based on actual bottlenecks.

Consider:

- React DevTools Profiler.
- React Performance Tracks.
- Browser performance tools.
- Bundle analysis.
- Component rendering frequency.
- Large lists.
- Expensive calculations.
- Unnecessary state updates.

### memo

Use React.memo when avoiding repeated rendering provides a meaningful benefit.

### useMemo and useCallback

Use only when justified.

### Lazy loading

Use lazy loading for components that do not need to be included in the initial rendering path.

Use Suspense with appropriate fallback UI.

### Large lists

For large datasets, evaluate:

- Pagination.
- Virtualization.
- Server-side filtering.
- Incremental rendering.
- TanStack Virtual.

Do not render thousands of unnecessary DOM elements.

### React Compiler

React Compiler provides automatic memoization when correctly configured.

Before manually adding memoization everywhere:

1. Check whether React Compiler is enabled.
1. Check compiler compatibility.
1. Follow existing project configuration.
1. Use supported compiler diagnostics.
1. Keep code understandable.

Do not assume that React Compiler is installed or enabled.

Do not remove useful memoization without verifying the behavior and performance impact.

## 13. Suspense and Error Boundaries

Use Suspense for supported asynchronous rendering and lazy-loaded components.

Provide meaningful fallback UI.

Consider:

- Initial loading.
- Deferred content.
- Nested boundaries.
- Error recovery.
- Avoiding unnecessary fallback flashes.

Use Error Boundaries to isolate rendering failures.

An Error Boundary does not automatically catch every asynchronous error or event-handler exception.

Handle API errors and user interactions explicitly.

Provide recovery options when appropriate.

## 14. Forms and Validation

Choose form management based on complexity.

### Simple forms

Use native HTML forms and React state when sufficient.

### Complex forms

Evaluate:

- React Hook Form.
- Zod.
- Native browser validation.

Standards:

- Use semantic form elements.
- Associate labels with controls.
- Provide field-level validation.
- Display understandable errors.
- Preserve user input when appropriate.
- Handle submission states.
- Prevent duplicate submissions.
- Support keyboard interaction.
- Announce errors accessibly.

Never trust frontend validation as the only security boundary.

Read forms-and-validation.md.

## 15. Accessibility

React components must support accessible interaction.

Check:

- Semantic elements.
- Keyboard navigation.
- Accessible names.
- Labels and descriptions.
- Focus management.
- Dialog focus behavior.
- Error announcements.
- Loading announcements.
- Screen reader compatibility.

Avoid unnecessary ARIA attributes.

Prefer native HTML controls whenever appropriate.

Read accessibility-wcag.md.

## 16. TypeScript Standards

Use strict TypeScript.

Prefer:

- Explicit prop interfaces or types.
- Discriminated unions.
- Narrowing.
- Unknown for untrusted values.
- Correct event types.
- Typed callbacks.
- Generic components only when useful.

Avoid:

- any.
- Excessive type assertions.
- Unnecessary non-null assertions.
- Duplicated types.
- Overly complex conditional types without a reason.

Use React types from the installed React TypeScript definitions.

Do not manually recreate types already provided by React.

Read typescript-and-code-quality.md.

## 17. React Anti-Patterns

Avoid:

- Direct DOM manipulation for normal React state updates.
- Mutating props or state.
- Calling hooks conditionally.
- Using Effects for derived state.
- Using array indexes as unstable list keys.
- Defining unstable component types inside render.
- Excessive Context usage.
- Unnecessary global state.
- Unnecessary memoization.
- Giant components.
- Prop drilling without evaluating composition or context.
- Overly generic component APIs.
- Ignoring loading and error states.
- Treating frontend validation as security.
- Using browser APIs without considering SSR.

## 18. React Code Review Checklist

### Components

- [ ] Components have clear responsibilities.
- [ ] Props are correctly typed.
- [ ] Composition is used appropriately.
- [ ] Semantic HTML is used.
- [ ] Component APIs are understandable.

### Hooks

- [ ] Rules of Hooks are followed.
- [ ] Effects synchronize with external systems.
- [ ] Dependencies are correct.
- [ ] Cleanup is implemented.
- [ ] Custom hooks have focused responsibilities.

### State

- [ ] State is placed appropriately.
- [ ] Derived values are not unnecessarily duplicated.
- [ ] Server state and client state are separated.
- [ ] No unnecessary global state exists.

### Performance

- [ ] No obvious unnecessary rendering exists.
- [ ] Large lists are handled appropriately.
- [ ] Memoization is justified.
- [ ] Lazy loading is used where useful.
- [ ] React Compiler compatibility is considered.

### Quality

- [ ] TypeScript types are safe.
- [ ] Forms have validation and feedback.
- [ ] Accessibility is considered.
- [ ] Error states are handled.
- [ ] Tests cover important behavior.

## 19. Related References

Load these documents when relevant:

- architecture-and-project-structure.md
- nextjs-engineering.md
- rendering-and-caching-strategies.md
- typescript-and-code-quality.md
- component-and-design-systems.md
- reusable-ui-components.md
- application-state-and-utilities.md
- forms-and-validation.md
- accessibility-wcag.md
- performance-and-core-web-vitals.md
- testing-strategy.md

## 20. Official Resources

- React Documentation: https://react.dev/
- React Reference: https://react.dev/reference/react
- React Hooks: https://react.dev/reference/react/hooks
- Rules of React: https://react.dev/reference/rules
- React 19: https://react.dev/blog/2024/12/05/react-19
- React 19.2: https://react.dev/blog/2025/10/01/react-19-2
- React 19.3: https://react.dev/blog/2026/09/09/react-19-3
- React Compiler: https://react.dev/learn/react-compiler
