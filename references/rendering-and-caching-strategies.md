# Rendering and Caching Strategies

## 1. Purpose

Define practical rendering and caching strategies for modern frontend applications.

The goal is to select the right rendering approach based on:

- Application requirements.
- Data freshness.
- User-specific content.
- SEO requirements.
- Performance.
- Infrastructure.
- Framework capabilities.

Do not choose a rendering strategy simply because it is popular.

## 2. Understand the Rendering Strategies

### Client-Side Rendering (CSR)

The browser executes JavaScript to render the interface.

Suitable for:

- Interactive dashboards.
- Internal CRM applications.
- Highly interactive tools.
- Applications where SEO is not important.

Considerations:

- Initial JavaScript cost.
- Loading states.
- Browser performance.
- Data-fetching waterfalls.
- Search engine discoverability.

### Server-Side Rendering (SSR)

The server generates HTML for a request.

Suitable for:

- Personalized pages.
- Frequently changing content.
- Request-dependent information.
- Pages requiring server-rendered content.

Considerations:

- Server execution cost.
- Time to first byte.
- Data-fetching latency.
- Caching opportunities.

### Static Site Generation (SSG)

Pages are generated ahead of time.

Suitable for:

- Documentation.
- Blogs.
- Marketing pages.
- Public content that changes infrequently.

Considerations:

- Build time.
- Content freshness.
- Rebuild or revalidation requirements.

### Incremental Static Regeneration (ISR)

Previously generated content can be refreshed after deployment.

Suitable for:

- Product catalogs.
- Public listings.
- Content websites.
- Pages that do not require immediate updates.

Considerations:

- Revalidation strategy.
- Acceptable content staleness.
- Cache invalidation.

### Streaming

The server can progressively send rendered content.

Suitable for:

- Pages with independent data sections.
- Slow secondary requests.
- Large interfaces with progressive loading.

Use Suspense boundaries to control loading behavior.

## 3. Rendering Strategy Selection

Choose the simplest strategy that meets the requirements.

| Requirement | Possible strategy |
| ------------------------------------ | ---------------------------- |
| Public static content | SSG |
| Frequently changing public content | SSR or revalidation |
| Personalized content | Request-time rendering |
| Internal interactive dashboard | CSR or hybrid |
| SEO-sensitive public page | SSG or SSR |
| Large page with independent sections | Streaming |
| User-specific real-time data | Client fetching or streaming |

These are starting points, not mandatory rules.

Evaluate framework capabilities and installed versions before implementation.

## 4. Next.js Rendering

Next.js supports multiple rendering and caching approaches.

Understand the behavior of the installed version.

Consider:

- Static rendering.
- Dynamic rendering.
- Prerendering.
- Server Components.
- Client Components.
- Streaming.
- Partial rendering capabilities.
- Cache Components when supported and enabled.

Do not assume that every Next.js version uses identical rendering or caching defaults.

### Server Components

Use Server Components for:

- Server-side data access.
- Content rendering.
- Reducing browser JavaScript.
- Accessing trusted server resources.

### Client Components

Use Client Components for:

- Browser interactions.
- Local state.
- Event handlers.
- Browser APIs.
- Client-side subscriptions.

Do not make an entire application client-rendered without a reason.

## 5. Understand Different Cache Layers

Caching is not one single mechanism.

Identify the layer responsible for cached data.

### Browser cache

Stores resources in the browser.

Examples:

- Images.
- Fonts.
- Static assets.
- HTTP responses.

Consider:

- Cache-Control.
- ETag.
- Last-Modified.
- Immutable assets.

### CDN cache

Caches responses closer to users.

Suitable for:

- Static assets.
- Public pages.
- Public API responses where appropriate.

Avoid shared caching of private user-specific responses.

### Application data cache

Stores results of data fetching or application operations.

Consider:

- Cache keys.
- Expiration.
- Revalidation.
- Invalidation.
- Data freshness.

### Framework cache

Frameworks may provide their own data and rendered-output caching.

Understand the exact behavior of the installed framework version.

### Client-side server-state cache

Libraries such as TanStack Query maintain client-side server-state caches.

Consider:

- Query keys.
- Stale time.
- Garbage collection.
- Refetch behavior.
- Invalidation.
- Optimistic updates.

Do not confuse this with server-side framework caching.

## 6. Cache Design Principles

Before caching anything, answer:

1. What data is being cached?
1. Who is allowed to access it?
1. How frequently does it change?
1. How stale can the data become?
1. What event invalidates it?
1. Is the cache shared across users?
1. What happens when cached data expires?

### Public data

Public data may be suitable for shared caching.

Examples:

- Public product listings.
- Public documentation.
- Marketing content.

### Private data

User-specific data requires strict isolation.

Examples:

- User profiles.
- Account details.
- Private dashboards.
- Organization-specific records.

Never allow one user's cached response to be served to another user.

### Sensitive data

Apply stricter caching decisions to:

- Financial information.
- Authentication data.
- Private records.
- Permission-sensitive information.

Use appropriate private or no-store policies where necessary.

Do not assume every authenticated response must be uncached; evaluate the framework and isolation requirements carefully.

## 7. Cache Invalidation

Cache invalidation is as important as caching.

Common strategies:

### Time-based expiration

Refresh cached data after a configured period.

Suitable for content with predictable freshness requirements.

### Event-based invalidation

Invalidate after a successful mutation.

Examples:

- Creating a product.
- Updating a user.
- Deleting a record.
- Changing a permission.

### Tag-based invalidation

Group related cached data under meaningful tags.

Invalidate the appropriate group when the underlying data changes.

### Path-based invalidation

Refresh cached route output when a page's data changes.

### Invalidation principles

- Invalidate only affected data.
- Avoid invalidating everything unnecessarily.
- Prevent stale permission-sensitive information.
- Understand whether invalidation is immediate or eventual.
- Verify behavior after mutations.
- Keep invalidation logic close to the operation that changes the data when practical.

## 8. Next.js Cache APIs

Next.js has different caching models. Always identify the installed Next.js version and project configuration before using caching APIs.

### Cache Components model

In Next.js 16+, Cache Components can be enabled with:

```ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  cacheComponents: true,
};

export default nextConfig;
```

When enabled, understand these APIs:

- `use cache`: Marks a function or component for caching.
- `cacheLife`: Controls cache lifetime.
- `cacheTag`: Associates tags with cached data.
- `updateTag`: Immediately expires tagged data.
- `revalidateTag`: Revalidates tagged data.
- `revalidatePath`: Revalidates a route.

`use cache`, `cacheLife` and `cacheTag` must be used according to the Cache Components configuration and their documented restrictions.

### Cache invalidation

Choose the correct invalidation API:

| API | Use |
| ---------------- | --------------------------------------------------------------- |
| `updateTag` | Immediate expiration for read-your-own-writes in Server Actions |
| `revalidateTag` | Tag-based revalidation in Server Actions and Route Handlers |
| `revalidatePath` | Revalidation of a specific route |

For `revalidateTag`, prefer the `"max"` profile when stale-while-revalidate behavior is appropriate.

Do not assume these APIs have identical behavior.

### Previous caching model

Projects not using Cache Components follow the previous caching model.

Depending on the installed version and configuration, relevant APIs include:

- `fetch` cache options.
- `next.revalidate`.
- `next.tags`.
- `revalidateTag`.
- `revalidatePath`.
- `unstable_cache` for applicable non-fetch caching scenarios.

In this model, do not assume fetch requests are cached by default.

### Important rules

- Do not mix examples from different caching models.
- Check whether `cacheComponents` is enabled.
- Verify API availability against the installed Next.js version.
- Never assume a client-side query invalidation clears the server cache.
- Test cache behavior after mutations.
- Treat user-specific and permission-sensitive data carefully.

Official documentation:

- https://nextjs.org/docs/app/guides/caching
- https://nextjs.org/docs/app/getting-started/revalidating
- https://nextjs.org/docs/app/guides/caching-without-cache-components
- https://nextjs.org/docs/app/api-reference/functions/updateTag
- https://nextjs.org/docs/app/api-reference/functions/revalidateTag

## 9. TanStack Query Caching

Use TanStack Query for client-side server-state management when appropriate.

Understand:

- `queryKey`
- `queryFn`
- `staleTime`
- `gcTime`
- `refetchOnWindowFocus`
- `refetchOnReconnect`
- `invalidateQueries`
- `setQueryData`
- `prefetchQuery`
- `initialData`
- `placeholderData`

### Query key standards

Use predictable, structured query keys.

Example:

```ts
export const userKeys = {
  all: ["users"] as const,

  lists: () => [...userKeys.all, "list"] as const,

  list: (filters: object) => [...userKeys.lists(), filters] as const,

  details: () => [...userKeys.all, "detail"] as const,

  detail: (id: string) => [...userKeys.details(), id] as const,
};
```

Use appropriately typed filters rather than unrestricted objects in production implementations.

### staleTime

Controls how long data is considered fresh.

### gcTime

Controls how long inactive query data remains in memory before garbage collection.

### Invalidation

Invalidate related queries after successful mutations.

Avoid invalidating unrelated data.

Do not configure every query with identical cache settings automatically.

## 10. Avoid Data-Fetching Waterfalls

Identify independent requests.

Run independent operations in parallel where appropriate.

Avoid:

- Sequential requests that do not depend on one another.
- Fetching the same data repeatedly.
- Fetching from the browser when the server already has access.
- Calling internal API endpoints unnecessarily.
- Duplicating fetching between layouts and pages.

For dependent requests, preserve the required sequence.

Use prefetching when it provides measurable user-experience benefits.

## 11. Streaming and Suspense

Use streaming when different page sections can be rendered independently.

Consider:

- Route loading boundaries.
- Component-level Suspense.
- Independent data sections.
- Progressive content.
- Skeleton UI.

Example:

```tsx
import { Suspense } from "react";

export default function DashboardPage() {
  return (
    <main>
      <h1>Dashboard</h1>

      <Suspense fallback={<p>Loading statistics...</p>}>
        <DashboardStatistics />
      </Suspense>

      <Suspense fallback={<p>Loading activity...</p>}>
        <RecentActivity />
      </Suspense>
    </main>
  );
}
```

Keep loading boundaries meaningful.

Avoid excessive nested Suspense boundaries without a clear reason.

## 12. Real-Time Data

Not all changing data requires real-time infrastructure.

Choose based on update requirements.

| Requirement | Possible approach |
| -------------------------- | --------------------------------------- |
| Occasional refresh | Refetching |
| Background refresh | TanStack Query |
| Near real-time updates | Polling |
| Server-to-client events | Server-Sent Events |
| Two-way communication | WebSocket |
| Collaborative applications | WebSocket or suitable real-time service |

Consider:

- Connection management.
- Reconnection.
- Authentication.
- Cleanup.
- Error recovery.
- Data synchronization.
- Resource usage.

Do not introduce WebSockets when ordinary refetching is sufficient.

## 13. Performance Considerations

Evaluate:

- Time to First Byte.
- First Contentful Paint.
- Largest Contentful Paint.
- Interaction to Next Paint.
- Cumulative Layout Shift.
- JavaScript bundle size.
- Request waterfalls.
- Server response time.
- Cache hit ratio.
- Image and font loading.

Measure actual performance before optimizing.

Avoid caching strategies that make data incorrect merely to improve performance.

## 14. Common Anti-Patterns

Avoid:

- Caching private data in a shared cache.
- Treating every page as static.
- Treating every page as dynamic.
- Using no-store everywhere without analysis.
- Invalidating the entire cache after every mutation.
- Assuming client query invalidation clears framework caches.
- Fetching the same data in multiple layers unnecessarily.
- Using polling for every real-time requirement.
- Adding WebSockets without a need.
- Creating excessive Suspense boundaries.
- Ignoring stale-data behavior.
- Optimizing without measurements.

## 15. Decision Workflow

Before choosing a rendering or caching approach:

1. Identify whether content is public or private.
1. Determine freshness requirements.
1. Understand SEO requirements.
1. Identify whether user-specific rendering is necessary.
1. Inspect the installed framework version.
1. Identify available cache layers.
1. Define invalidation behavior.
1. Evaluate security and data isolation.
1. Measure performance where possible.
1. Document important decisions.

Prefer predictable behavior over unnecessary caching complexity.

## 16. Review Checklist

### Rendering

- [ ] Rendering strategy matches the requirement.
- [ ] Server and Client Components are used appropriately.
- [ ] SEO requirements are considered.
- [ ] Loading boundaries are meaningful.
- [ ] Streaming is used only when useful.

### Caching

- [ ] Cache ownership is understood.
- [ ] Public and private data are separated.
- [ ] Cache keys are predictable.
- [ ] Expiration is intentional.
- [ ] Invalidation is implemented.
- [ ] User data cannot leak across sessions.

### Data fetching

- [ ] Duplicate requests are avoided.
- [ ] Independent requests run in parallel.
- [ ] Request waterfalls are minimized.
- [ ] Real-time requirements are correctly identified.

### Performance

- [ ] Core Web Vitals are considered.
- [ ] Bundle size is monitored.
- [ ] Server response time is considered.
- [ ] Performance decisions are based on evidence.

## 17. Related References

- architecture-and-project-structure.md
- react-engineering.md
- nextjs-engineering.md
- api-integration.md
- application-state-and-utilities.md
- performance-and-core-web-vitals.md
- frontend-security-owasp.md
- production-readiness.md

## 18. Official Resources

- Next.js Caching: https://nextjs.org/docs/app/guides/caching
- Next.js Fetching Data: https://nextjs.org/docs/app/getting-started/fetching-data
- Next.js Updating Data: https://nextjs.org/docs/app/getting-started/mutating-data
- Next.js Cache Components: https://nextjs.org/docs/app/getting-started/cache-components
- React Suspense: https://react.dev/reference/react/Suspense
- TanStack Query: https://tanstack.com/query/latest/docs/framework/react/overview
- MDN HTTP Caching: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching
- Web.dev Performance: https://web.dev/articles/vitals
