# TanStack Query Example

## 1. Purpose

Demonstrate how to manage server state in React applications using TanStack Query.

This example covers:

- QueryClient configuration.
- Query keys.
- Queries and mutations.
- Cache management.
- Query invalidation.
- Optimistic updates.
- Pagination.
- Filtering and search.
- Dependent queries.
- Error and loading states.
- Request cancellation.
- Authentication integration.
- Next.js integration considerations.

The goal is to manage remote application data reliably without confusing server state with local UI state.

## 2. Core Principles

1. Use TanStack Query for server state, not every kind of application state.
1. Design predictable query keys.
1. Reuse existing API services.
1. Keep query functions focused.
1. Invalidate only the cache entries affected by mutations.
1. Handle loading, error and empty states.
1. Prevent stale data from being displayed as current without clear intent.
1. Use optimistic updates only when justified.
1. Avoid duplicating server state in global client stores.
1. Verify cache behavior against the installed TanStack Query version.

## 3. What Is Server State?

Server state represents data owned and managed by an external system.

Examples:

- Customer records.
- User profiles.
- Product lists.
- Dashboard statistics.
- Notifications.
- Orders.

It differs from local UI state.

| State type | Examples | Typical approach |
| ---------------------- | ---------------- | ------------------------- |
| Server state | API data | TanStack Query |
| Local UI state | Modal visibility | React state |
| Form state | Input values | React or form library |
| URL state | Search filters | URL search parameters |
| Persistent preferences | Theme selection | Cookie or browser storage |

Do not use TanStack Query merely because an application uses React.

## 4. Suggested Structure

```text id="71q8x0"
src/
├── app/
│   └── providers.tsx
├── lib/
│   └── query/
│       ├── query-client.ts
│       └── query-keys.ts
└── features/
    └── customers/
        ├── hooks/
        │   ├── use-customers.ts
        │   └── use-update-customer.ts
        ├── services/
        │   └── customer-api.ts
        ├── components/
        │   └── customer-list.tsx
        └── types/
            └── customer.ts
```

This structure is illustrative.

Keep query hooks near the feature that owns the data when that improves maintainability.

## 5. Installation

Install the package using the existing package manager.

```bash
npm install @tanstack/react-query
```

For development tools, if useful:

```bash
npm install -D @tanstack/react-query-devtools
```

Do not install additional packages when the project already has suitable tooling.

## 6. QueryClient Configuration

Create a QueryClient configuration.

```ts id="b7ksqv"
// src/lib/query/query-client.ts

import { QueryClient } from "@tanstack/react-query";

export function makeQueryClient() {
  return new QueryClient({
    defaultOptions: {
      queries: {
        staleTime: 30_000,
        retry: 1,
        refetchOnWindowFocus: false,
      },
      mutations: {
        retry: 0,
      },
    },
  });
}
```

These values are illustrative.

Choose cache freshness, retries and refetch behavior based on the actual application.

Do not disable refetching globally without understanding the consequences.

## 7. Provider Setup

For a browser-side React application, provide a stable QueryClient instance.

Example:

```tsx id="8crk5c"
// src/app/providers.tsx

"use client";

import { useState } from "react";
import { QueryClientProvider } from "@tanstack/react-query";

import { makeQueryClient } from "@/lib/query/query-client";

type ProvidersProps = {
  children: React.ReactNode;
};

export function Providers({ children }: ProvidersProps) {
  const [queryClient] = useState(() => makeQueryClient());

  return (
    <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
  );
}
```

Use the provider in the appropriate application root.

For Next.js, avoid sharing a mutable QueryClient across server requests.

Server-side prefetching and hydration require a separate, carefully designed server/client lifecycle.

## 8. Query Keys

Query keys identify cached server data.

Use stable, descriptive keys.

```ts id="h7n5j4"
// src/lib/query/query-keys.ts

export const customerKeys = {
  all: ["customers"] as const,

  lists: () => [...customerKeys.all, "list"] as const,

  list: (filters: { page: number; search?: string }) =>
    [...customerKeys.lists(), filters] as const,

  details: () => [...customerKeys.all, "detail"] as const,

  detail: (id: string) => [...customerKeys.details(), id] as const,
};
```

Good query keys should:

- Be deterministic.
- Include all variables affecting the response.
- Separate lists from detail records.
- Support targeted invalidation.
- Avoid unrelated data sharing.

Do not use random values or unstable objects in query keys.

## 9. Fetching Data with useQuery

Example service:

```ts id="8a1n7p"
// src/features/customers/services/customer-api.ts

export type Customer = {
  id: string;
  name: string;
  email: string;
};

export async function getCustomers(signal?: AbortSignal): Promise<Customer[]> {
  const response = await fetch("/api/customers", {
    signal,
  });

  if (!response.ok) {
    throw new Error("Unable to load customers.");
  }

  return response.json() as Promise<Customer[]>;
}
```

Example hook:

```ts id="5byx0p"
// src/features/customers/hooks/use-customers.ts

import { useQuery } from "@tanstack/react-query";

import { customerKeys } from "@/lib/query/query-keys";
import { getCustomers } from "../services/customer-api";

export function useCustomers() {
  return useQuery({
    queryKey: customerKeys.lists(),
    queryFn: ({ signal }) => getCustomers(signal),
  });
}
```

Validate untrusted API responses at runtime when appropriate.

The TypeScript return type does not validate JSON data.

## 10. Displaying Query States

A component should handle the query's relevant states.

```tsx id="6xw1b4"
"use client";

import { useCustomers } from "../hooks/use-customers";

export function CustomerList() {
  const { data, isPending, isError, error, refetch } = useCustomers();

  if (isPending) {
    return <p>Loading customers...</p>;
  }

  if (isError) {
    return (
      <div role="alert">
        <p>{error.message}</p>

        <button type="button" onClick={() => refetch()}>
          Try again
        </button>
      </div>
    );
  }

  if (data.length === 0) {
    return <p>No customers found.</p>;
  }

  return (
    <ul>
      {data.map((customer) => (
        <li key={customer.id}>{customer.name}</li>
      ))}
    </ul>
  );
}
```

Adapt the UI to the actual error-handling conventions.

Do not expose internal server error messages directly to users.

## 11. Mutations

Use `useMutation` for operations that modify server data.

Examples:

- Create a record.
- Update a record.
- Delete a record.
- Submit a workflow action.

Example:

```ts id="0n8gqz"
import { useMutation, useQueryClient } from "@tanstack/react-query";

import { customerKeys } from "@/lib/query/query-keys";

type UpdateCustomerInput = {
  id: string;
  name: string;
};

async function updateCustomer(input: UpdateCustomerInput) {
  const response = await fetch(
    `/api/customers/${encodeURIComponent(input.id)}`,
    {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: input.name,
      }),
    },
  );

  if (!response.ok) {
    throw new Error("Unable to update customer.");
  }

  return response.json();
}

export function useUpdateCustomer() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: updateCustomer,

    onSuccess: async (_data, variables) => {
      await Promise.all([
        queryClient.invalidateQueries({
          queryKey: customerKeys.lists(),
        }),
        queryClient.invalidateQueries({
          queryKey: customerKeys.detail(variables.id),
        }),
      ]);
    },
  });
}
```

Use the actual API service rather than duplicating HTTP logic inside multiple mutation hooks.

## 12. Query Invalidation

Invalidate cached data after a successful mutation when the affected data may be stale.

Examples:

- Updating a customer can affect its detail record and customer lists.
- Creating a customer can affect list queries.
- Deleting a record can affect list and detail queries.

Prefer targeted invalidation.

Avoid invalidating the entire application cache after every mutation.

Understand the difference between invalidation, refetching and direct cache updates.

## 13. Optimistic Updates

Optimistic updates immediately update the UI before the server confirms success.

Use them when:

- The expected operation is likely to succeed.
- The UI can accurately predict the result.
- Rollback is possible.
- The improved responsiveness is valuable.

Example:

```ts id="x7v4s2"
const mutation = useMutation({
  mutationFn: updateCustomer,

  onMutate: async (input) => {
    await queryClient.cancelQueries({
      queryKey: customerKeys.detail(input.id),
    });

    const previousCustomer = queryClient.getQueryData(
      customerKeys.detail(input.id),
    );

    queryClient.setQueryData(
      customerKeys.detail(input.id),
      (old: Customer | undefined) => (old ? { ...old, name: input.name } : old),
    );

    return { previousCustomer };
  },

  onError: (_error, input, context) => {
    queryClient.setQueryData(
      customerKeys.detail(input.id),
      context?.previousCustomer,
    );
  },

  onSettled: async (_data, _error, input) => {
    await queryClient.invalidateQueries({
      queryKey: customerKeys.detail(input.id),
    });
  },
});
```

This is illustrative.

A production implementation must ensure the cached type, rollback behavior and concurrent mutation behavior are correct.

Avoid optimistic updates for complex workflows where the server's result cannot be predicted safely.

## 14. Pagination

Include pagination parameters in query keys.

Example:

```ts id="0f2wz3"
const query = useQuery({
  queryKey: customerKeys.list({
    page,
    search,
  }),
  queryFn: () => getCustomersByPage({ page, search }),
});
```

Consider:

- Current page.
- Page size.
- Total count.
- Empty pages.
- Search and filtering.
- URL synchronization.
- Previous and next controls.

Use placeholder data where appropriate to avoid unnecessary UI flicker between pages.

Verify the current TanStack Query API for the installed version.

## 15. Search and Filtering

Use debounced search when it meaningfully reduces unnecessary requests.

Keep query keys synchronized with all response-affecting filters.

Cancel obsolete requests when appropriate.

Do not hide legitimate query errors behind a loading indicator.

## 16. Dependent Queries

Use dependent queries when one request requires the result of another.

Example:

```ts id="i6tv2e"
const userQuery = useQuery({
  queryKey: ["user", userId],
  queryFn: () => getUser(userId),
});

const projectsQuery = useQuery({
  queryKey: ["projects", userId],
  queryFn: () => getProjects(userId),
  enabled: Boolean(userQuery.data?.id),
});
```

Avoid unnecessary sequential requests when the backend can return the required information in one request.

## 17. Request Cancellation

Pass the query function's `AbortSignal` to the underlying Fetch request.

This helps cancel obsolete requests when query behavior requires it.

Do not ignore the signal when the request supports cancellation.

## 18. Authentication and Cache Safety

When authentication changes:

- Clear or isolate user-specific cached data appropriately.
- Prevent one user's cached data from appearing in another user's session.
- Handle expired sessions.
- Avoid placing sensitive credentials in query keys.
- Ensure backend authorization remains authoritative.

Do not assume clearing a query cache replaces server-side access control.

## 19. Next.js Integration

TanStack Query can be used in Next.js applications, but the server and browser have different lifecycles.

Consider:

- QueryClient creation per server request.
- Browser QueryClient stability.
- Server-side prefetching.
- Dehydration and hydration.
- Initial stale time.
- Avoiding duplicate requests.
- Authentication and data isolation.
- Server Component data fetching versus client-side query fetching.

Do not move all server data fetching into TanStack Query automatically.

Use Next.js Server Components and native data fetching when they provide the simpler solution.

Use TanStack Query where client-side caching, mutations, refetching or interactive server-state management justify it.

## 20. Devtools

TanStack Query Devtools can help inspect:

- Query keys.
- Cache state.
- Stale and fresh queries.
- Mutation state.
- Query errors.
- Refetch behavior.

Use development-only configuration.

Do not expose development tools in production unless explicitly required and safely configured.

## 21. Testing

Test:

- Successful queries.
- Loading and error states.
- Empty data.
- Query key changes.
- Mutation success and failure.
- Cache invalidation.
- Optimistic rollback.
- Pagination.
- Search and filtering.
- Authentication changes.

Use a fresh QueryClient per test when isolation is needed.

Avoid sharing cache state between unrelated tests.

## 22. Existing TanStack Query Changes

When modifying an existing implementation:

1. Inspect QueryClient configuration.
1. Review query key conventions.
1. Trace related query hooks.
1. Inspect API services.
1. Review mutation and invalidation behavior.
1. Check optimistic updates.
1. Review authentication and cache isolation.
1. Inspect tests.
1. Make the smallest safe change.
1. Verify affected queries and mutations.

Do not rename or restructure query keys without checking existing cache consumers.

## 23. Common Anti-Patterns

Avoid:

- Using TanStack Query for all application state.
- Unstable query keys.
- Missing response-affecting query parameters.
- Duplicate API clients.
- Global cache invalidation after every mutation.
- Unsafe optimistic updates.
- Missing rollback behavior.
- Ignoring request cancellation.
- Duplicating server data in global state.
- Sharing a server QueryClient across requests.
- Unnecessary client-side fetching in Next.js.
- Exposing sensitive data through cached state.

## 24. Review Checklist

### Configuration

- [ ] QueryClient is created correctly.
- [ ] Server and browser lifecycles are separated.
- [ ] Defaults are appropriate.

### Queries

- [ ] Query keys are stable.
- [ ] Query functions handle errors.
- [ ] Loading and empty states exist.
- [ ] Cancellation is supported where useful.

### Mutations

- [ ] Mutation behavior is correct.
- [ ] Relevant queries are invalidated.
- [ ] Optimistic updates have rollback where needed.
- [ ] Concurrent operations are considered.

### Security

- [ ] User-specific cache data is isolated.
- [ ] Backend authorization is enforced.
- [ ] Sensitive values are not placed in query keys.

### Verification

- [ ] Query tests pass.
- [ ] Mutation tests pass.
- [ ] TypeScript checks pass.
- [ ] Lint checks pass.
- [ ] Production build succeeds.

## 25. Related References

- `../../references/state-management.md`
- `../../references/api-integration.md`
- `../../references/rendering-and-caching-strategies.md`
- `../../references/nextjs-engineering.md`
- `../../references/authentication-and-authorization.md`
- `../../references/testing-strategy.md`
- `../../references/typescript-and-code-quality.md`
- `../../references/anti-ai-slop-and-engineering-quality.md`

## 26. Official Resources

- TanStack Query: https://tanstack.com/query/latest/docs/framework/react/overview
- Query Keys: https://tanstack.com/query/latest/docs/framework/react/guides/query-keys
- Queries: https://tanstack.com/query/latest/docs/framework/react/guides/queries
- Mutations: https://tanstack.com/query/latest/docs/framework/react/guides/mutations
- Query Invalidation: https://tanstack.com/query/latest/docs/framework/react/guides/query-invalidation
- Optimistic Updates: https://tanstack.com/query/latest/docs/framework/react/guides/optimistic-updates
- Advanced Server Rendering: https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr
