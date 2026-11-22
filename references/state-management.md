# State Management

## 1. Purpose

Define standards for designing, implementing, modifying and maintaining state in frontend applications.

Support:

- Local component state.
- Shared application state.
- React Context.
- Zustand.
- Redux Toolkit.
- TanStack Query.
- Server state.
- URL state.
- Form state.
- Persistent state.
- Derived state.
- Asynchronous state.
- State synchronization.

The objective is to keep state predictable, maintainable and appropriately scoped.

Avoid unnecessary global state and duplicated data.

## 2. Inspect Before Implementation

Before introducing or modifying state management:

1. Inspect the existing state architecture.
1. Identify existing state libraries.
1. Review React Context providers.
1. Inspect custom hooks.
1. Identify API data-fetching patterns.
1. Review URL-based state.
1. Check persistence mechanisms.
1. Identify duplicated state.
1. Understand component ownership and data flow.

For existing projects, preserve the established architecture unless there is a clear reason to change it.

Do not introduce a new state library simply because a feature needs state.

## 3. Understand State Categories

Different types of state have different responsibilities.

| State category | Examples | Suitable approach |
| ---------------- | ------------------------------ | ----------------------------------------- |
| Local UI state | Open dialog, active tab | useState |
| Shared UI state | Sidebar visibility, theme | Context or Zustand |
| Server state | Users, products, API results | TanStack Query or framework data fetching |
| URL state | Search, filters, pagination | URL parameters |
| Form state | Input values, errors | Native state or form library |
| Persistent state | User preferences | Storage or backend |
| Derived state | Filtered list, computed totals | Calculate from existing state |

Identify the category before choosing a solution.

Do not store the same information in multiple state systems without a clear reason.

## 4. Local Component State

Use `useState` for state owned by a component.

Examples:

- Dialog visibility.
- Dropdown state.
- Selected local tab.
- Input values.
- Temporary interaction state.

Example:

```tsx
const [isOpen, setIsOpen] = useState(false);

<button onClick={() => setIsOpen(true)}>Open</button>;
```

Keep state close to the components that need it.

Do not move every component state into a global store.

## 5. State Lifting

When multiple components need the same state, consider lifting it to their nearest common parent.

Example:

```text
Parent
├── SearchInput
└── ResultsList
```

The parent owns the search value and passes the necessary data and callbacks to its children.

Use this approach when the shared state has a small and understandable ownership boundary.

Avoid excessively deep prop drilling.

## 6. React Context

Use Context to share values across a component subtree.

Common use cases:

- Theme.
- Authentication information.
- Locale.
- Application configuration.
- Shared UI preferences.

Example:

```tsx
interface ThemeContextValue {
  theme: "light" | "dark";
  setTheme: (theme: "light" | "dark") => void;
}
```

Guidelines:

- Keep providers focused.
- Avoid putting unrelated state into one large context.
- Provide safe default behavior.
- Avoid unnecessary provider nesting.
- Consider provider re-render behavior.
- Split contexts when update patterns differ.

Context is a dependency-injection and value-sharing mechanism, not automatically a complete global state management solution.

## 7. Custom Hooks

Use custom hooks to reuse stateful logic.

Examples:

- use-mobile-menu.
- use-theme.
- use-debounce.
- use-local-storage.
- use-network-status.

Guidelines:

- Keep hook responsibilities focused.
- Follow React hook rules.
- Avoid hiding complex side effects behind unclear names.
- Return predictable values and actions.
- Avoid unnecessary abstraction for one-time logic.

Custom hooks should improve reuse and readability.

## 8. Zustand

Zustand is a lightweight state management option.

Consider it for:

- Shared UI state.
- Cross-component interactions.
- Application preferences.
- Client-side workflows.
- State that does not belong in server-state caching.

Example:

```tsx
import { create } from "zustand";

interface UIStore {
  sidebarOpen: boolean;
  setSidebarOpen: (open: boolean) => void;
}

export const useUIStore = create<UIStore>((set) => ({
  sidebarOpen: true,
  setSidebarOpen: (sidebarOpen) => set({ sidebarOpen }),
}));
```

Guidelines:

- Create focused stores.
- Keep actions close to related state.
- Select only the state needed by a component.
- Avoid giant application stores.
- Avoid duplicating API data unnecessarily.
- Understand persistence and hydration behavior.

Use Zustand when its simplicity matches the application requirements.

## 9. Redux Toolkit

Redux Toolkit can be useful for applications requiring a structured, centralized state architecture.

Consider it when:

- The application already uses Redux.
- Many features share complex client state.
- Centralized update patterns are valuable.
- Existing tooling and team conventions depend on it.

Use modern Redux Toolkit patterns.

Avoid introducing Redux for simple local state or ordinary API caching.

Do not use legacy hand-written Redux boilerplate when Redux Toolkit is appropriate.

## 10. Server State

Server state represents data owned by a backend.

Examples:

- Users.
- Products.
- Orders.
- Projects.
- Notifications.
- Dashboard metrics.

Server state has different requirements from local UI state.

It may need:

- Fetching.
- Caching.
- Background refetching.
- Stale data handling.
- Mutations.
- Invalidation.
- Pagination.
- Synchronization.
- Error handling.

Prefer the project's existing server-state approach.

Do not manually recreate a full caching system with `useState` and `useEffect` when an established library already solves the problem.

## 11. TanStack Query

TanStack Query is useful for managing asynchronous server state.

Common features:

- Queries.
- Mutations.
- Query caching.
- Query invalidation.
- Background refetching.
- Pagination.
- Infinite queries.
- Optimistic updates.

Example:

```tsx
import { useQuery } from "@tanstack/react-query";

function useUsers() {
  return useQuery({
    queryKey: ["users"],
    queryFn: usersApi.getAll,
  });
}
```

Guidelines:

- Use stable query keys.
- Keep query functions separate where appropriate.
- Define appropriate stale times.
- Handle loading, error and empty states.
- Invalidate affected queries after mutations.
- Avoid duplicate fetching systems.
- Configure retries deliberately.
- Avoid storing secrets in query keys.

Example mutation:

```tsx
import { useMutation, useQueryClient } from "@tanstack/react-query";

function useCreateUser() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: usersApi.create,

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["users"],
      });
    },
  });
}
```

Adapt the example to the actual API service and project conventions.

See `api-integration.md`.

## 12. Query Key Design

Query keys identify cached server data.

Use predictable hierarchical keys.

Example:

```tsx
export const userKeys = {
  all: ["users"] as const,

  lists: () => [...userKeys.all, "list"] as const,

  list: (filters: UserFilters) => [...userKeys.lists(), filters] as const,

  details: () => [...userKeys.all, "detail"] as const,

  detail: (id: string) => [...userKeys.details(), id] as const,
};
```

Guidelines:

- Include parameters that change the result.
- Keep key structures consistent.
- Avoid unrelated values in keys.
- Reuse key factories where useful.
- Understand invalidation boundaries.

Never use unstable object values or random identifiers to generate unnecessary cache entries.

## 13. Mutations and Cache Updates

Use mutations for server-changing operations.

Examples:

- Create.
- Update.
- Delete.
- Assign.
- Approve.
- Submit.

After successful mutations:

- Invalidate affected queries.
- Update cached data when appropriate.
- Reconcile optimistic updates.
- Handle conflicts.
- Preserve consistency between related views.

Choose between invalidation and direct cache updates based on complexity.

Do not update unrelated cache entries.

## 14. Optimistic State

Optimistic updates temporarily assume an operation will succeed.

Typical flow:

1. Capture the previous state.
1. Apply the expected update.
1. Submit the mutation.
1. Confirm the server result.
1. Roll back or reconcile on failure.

Use only when the expected result is predictable.

Avoid optimistic updates for high-risk actions where immediate confirmation is more appropriate.

See `api-integration.md`.

## 15. URL State

Use URL parameters for state that should be shareable, bookmarkable or navigable.

Examples:

- Search.
- Filters.
- Sorting.
- Pagination.
- Selected resource.
- Active tab when it represents navigation.

Example:

```text
/products?search=laptop&category=electronics&page=2
```

Benefits:

- Shareable URLs.
- Browser history support.
- Reload persistence.
- Deep linking.
- Better navigation behavior.

Use the framework's routing and search-parameter APIs.

Do not duplicate URL state in local state without a synchronization strategy.

## 16. Form State

Form state has its own lifecycle.

Examples:

- Field values.
- Validation errors.
- Dirty state.
- Submission status.
- Dynamic field arrays.

Use native React state or an established form library according to complexity.

Do not put every form field into a global application store.

See `forms-and-validation.md`.

## 17. Persistent State

Some client-side state should survive reloads.

Possible storage:

- localStorage.
- sessionStorage.
- Cookies.
- Backend user preferences.
- IndexedDB.

Choose based on data sensitivity and lifecycle.

Examples:

| Data | Possible storage |
| --------------------------- | ---------------------- |
| Theme preference | localStorage or cookie |
| Temporary wizard progress | sessionStorage |
| Non-sensitive UI preference | localStorage |
| User profile preference | Backend |
| Large offline data | IndexedDB |

Security considerations:

- Do not store sensitive credentials in localStorage.
- Do not assume browser storage is trusted.
- Validate stored data before use.
- Handle missing or corrupted values.
- Consider cross-tab synchronization.
- Avoid accessing browser storage during server rendering.

Use HttpOnly cookies for suitable authentication session designs.

See `authentication-and-authorization.md`.

## 18. Derived State

Calculate values from existing state when possible.

Example:

```tsx
const completedTasks = tasks.filter((task) => task.completed).length;
```

Avoid maintaining duplicated values that can become inconsistent.

Do not store:

- Total count when it can be calculated.
- Filtered results when they can be derived cheaply.
- Multiple copies of the same selected entity.

Use memoization only when it provides a meaningful benefit.

## 19. React Effects and State Synchronization

Use `useEffect` for synchronizing React with external systems.

Examples:

- Browser event listeners.
- Subscriptions.
- Timers.
- External widgets.
- Browser APIs.

Do not use effects unnecessarily for values that can be calculated during rendering.

Avoid effects that repeatedly copy one piece of state into another.

Understand:

- Dependency arrays.
- Cleanup.
- Stale closures.
- Race conditions.
- Strict Mode development behavior.

Prefer event handlers for logic triggered directly by user actions.

## 20. Next.js State Considerations

In Next.js App Router applications, understand the difference between:

- Server Components.
- Client Components.
- Server-side data fetching.
- Client-side interactive state.
- URL state.
- Shared layouts.

Guidelines:

- Keep components server-rendered by default where appropriate.
- Add `"use client"` only where client interactivity is required.
- Avoid turning entire route trees into Client Components unnecessarily.
- Do not access browser APIs from Server Components.
- Understand hydration and persistence behavior.
- Avoid duplicating server-fetched data in client stores without a reason.

Choose between framework-native data fetching and TanStack Query based on the application requirements.

Do not automatically introduce TanStack Query into every Next.js project.

## 21. State Persistence and Hydration

Persistent state can create server/client differences.

Consider:

- Initial server-rendered values.
- Browser storage availability.
- Theme flash.
- Hydration mismatches.
- Delayed restoration.
- Default values.
- Cross-tab updates.

Use a deliberate hydration strategy.

Do not assume localStorage is available during server rendering.

Avoid rendering different initial markup on the server and client without an appropriate strategy.

## 22. State Performance

Keep state updates targeted.

Consider:

- Component ownership.
- Context update frequency.
- Store selectors.
- Memoization.
- Large collections.
- Derived computations.
- Expensive selectors.
- Unnecessary subscriptions.

Use React Profiler or appropriate development tools when diagnosing performance problems.

Avoid premature optimization.

Do not introduce memoization everywhere.

## 23. Existing State Architecture Modification

When changing an existing state system:

1. Identify the current state owner.
1. Trace consumers and update paths.
1. Check whether data is local, shared or server-owned.
1. Identify duplicated state.
1. Review persistence and hydration.
1. Check cache synchronization.
1. Understand side effects.
1. Make the smallest reliable change.
1. Update affected consumers.
1. Test existing workflows.

Avoid replacing Context, Zustand or Redux across the application for a feature that needs only a small adjustment.

Preserve existing behavior unless the task requires changing it.

## 24. Common Anti-Patterns

Avoid:

- Putting all state in a global store.
- Duplicating server data in Zustand or Redux without a reason.
- Using Context for frequently changing unrelated values.
- Excessive prop drilling.
- Unnecessary `useEffect` synchronization.
- Storing derived values unnecessarily.
- Unstable query keys.
- Incorrect cache invalidation.
- Persisting sensitive data in browser storage.
- Introducing Redux for simple UI state.
- Introducing multiple overlapping server-state libraries.
- Adding Zustand when local state is sufficient.
- Ignoring Next.js server/client boundaries.

## 25. Decision Workflow

Before implementing state:

1. Identify the state category.
1. Determine its owner and consumers.
1. Check whether it already exists.
1. Choose the smallest suitable solution.
1. Consider persistence and URL requirements.
1. Implement predictable updates.
1. Handle loading and error states.
1. Verify synchronization.
1. Check performance when relevant.
1. Test affected workflows.

Prefer the simplest solution that satisfies the actual requirements.

## 26. Review Checklist

### Architecture

- [ ] State ownership is clear.
- [ ] Existing conventions are respected.
- [ ] State is kept at the appropriate scope.
- [ ] Unnecessary global state is avoided.

### Server State

- [ ] Existing query system is reused.
- [ ] Query keys are stable.
- [ ] Cache invalidation is correct.
- [ ] Mutation failures are handled.

### Client State

- [ ] Derived values are not unnecessarily duplicated.
- [ ] Effects are used appropriately.
- [ ] Persistence is intentional.
- [ ] Hydration behavior is correct.

### Verification

- [ ] Existing workflows still work.
- [ ] Relevant tests pass.
- [ ] Type checking passes.
- [ ] Build passes.

## 27. Related References

- architecture-and-project-structure.md
- react-engineering.md
- nextjs-engineering.md
- api-integration.md
- forms-and-validation.md
- authentication-and-authorization.md
- theming-and-dark-mode.md
- rendering-and-caching-strategies.md
- typescript-and-code-quality.md
- testing-strategy.md

## 28. Official Resources

- React State: https://react.dev/learn/managing-state
- React Context: https://react.dev/learn/passing-data-deeply-with-context
- React Effects: https://react.dev/learn/synchronizing-with-effects
- Zustand: https://zustand.docs.pmnd.rs/
- Redux Toolkit: https://redux-toolkit.js.org/
- TanStack Query: https://tanstack.com/query/latest/docs/framework/react/overview
- TanStack Store: https://tanstack.com/store/latest
- Next.js App Router: https://nextjs.org/docs/app
- MDN URLSearchParams: https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams
