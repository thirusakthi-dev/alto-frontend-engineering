# Next.js Engineering

## 1. Purpose

Define engineering standards for building production-ready applications with Next.js.

The agent must understand Next.js architecture, rendering, routing, data fetching, caching, server-side execution and deployment.

Prioritize:

- Modern Next.js App Router.
- React Server and Client Components.
- Correct server/client boundaries.
- Secure data access.
- Efficient data fetching.
- Predictable caching.
- Scalable routing and layouts.
- SEO and metadata.
- Accessibility.
- Performance and production readiness.

Do not treat Next.js as simply React with file-based routing.

## 2. Version Awareness

Before implementing anything:

1. Inspect the installed Next.js version.
1. Inspect React and React DOM versions.
1. Inspect TypeScript and Node.js versions.
1. Identify App Router or Pages Router.
1. Inspect `next.config.*`.
1. Check installed dependencies.
1. Verify APIs against the documentation for the installed version.

Important:

- Next.js APIs and defaults change between major releases.
- Do not copy old Next.js examples without checking compatibility.
- Do not assume caching defaults from older versions.
- Do not mix App Router and Pages Router conventions.
- Do not introduce experimental APIs without justification.

Official documentation:

https://nextjs.org/docs

## 3. App Router and Pages Router

Understand both routing systems.

### App Router

Preferred for new Next.js applications.

Uses:

- `app/` directory.
- Server Components.
- Client Components.
- Nested layouts.
- Route Handlers.
- Server Functions and Actions.
- Loading and error boundaries.
- Metadata APIs.

### Pages Router

Supported for existing applications.

Uses:

- `pages/` directory.
- `pages/_app.tsx`.
- `pages/_document.tsx`.
- `getStaticProps`.
- `getServerSideProps`.
- API Routes.
- Router hooks.

Rules:

- Follow the router already used by the project.
- Do not migrate an existing application automatically.
- Do not mix APIs from the two routing systems.
- Recommend migration only when there is a clear benefit.

## 4. App Router Project Structure

Example:

src/
app/
layout.tsx
page.tsx
globals.css

```
loading.tsx
error.tsx
not-found.tsx

(auth)/
  login/
    page.tsx
  register/
    page.tsx

(dashboard)/
  layout.tsx
  dashboard/
    page.tsx
  users/
    page.tsx
    [id]/
      page.tsx

api/
  health/
    route.ts
```

components/
ui/
shared/

features/
auth/
dashboard/
users/

lib/
auth/
api/
utils/

hooks/
services/
types/

Adapt the structure to project complexity.

### App Router conventions

| File | Responsibility |
| ---------------------------- | --------------------------------------------------------- |
| `page.tsx` | Route UI |
| `layout.tsx` | Shared route layout |
| `template.tsx` | Recreated layout template |
| `loading.tsx` | Loading boundary |
| `error.tsx` | Route error boundary |
| `global-error.tsx` | Root-level error UI |
| `not-found.tsx` | Not-found UI |
| `route.ts` | HTTP request handler |
| `default.tsx` | Parallel route fallback |
| `middleware.ts` / `proxy.ts` | Request interception, depending on version and convention |

Do not create every special file automatically.

Use each only when the application requires it.

## 5. Server and Client Components

Understand this boundary before implementing components.

### Server Components

App Router pages and layouts are Server Components by default.

Use them for:

- Data fetching.
- Database access.
- Server-side business logic.
- Accessing private credentials.
- Rendering content without client interactivity.
- Reducing browser JavaScript.

Example:

```tsx
import { getProducts } from "@/features/products/services";

export default async function ProductsPage() {
  const products = await getProducts();

  return (
    <main>
      <h1>Products</h1>

      <ul>
        {products.map((product) => (
          <li key={product.id}>{product.name}</li>
        ))}
      </ul>
    </main>
  );
}
```

### Client Components

Use `"use client"` when a component requires:

- React state.
- Event handlers.
- Effects.
- Browser APIs.
- Client-side custom hooks.
- Interactive third-party libraries.

Example:

```tsx
"use client";

import { useState } from "react";

export function Counter() {
  const [count, setCount] = useState(0);

  return (
    <button onClick={() => setCount((value) => value + 1)}>
      Count: {count}
    </button>
  );
}
```

### Boundary rules

- Prefer Server Components by default.
- Keep Client Components as small as practical.
- Place `"use client"` at the appropriate component boundary.
- Do not mark the entire application as client-side unnecessarily.
- Do not import server-only modules into Client Components.
- Pass serializable props across the Server/Client boundary.
- Keep secrets and privileged operations on the server.

### Composition

A Server Component can render Client Components.

A Client Component can receive server-rendered UI through props such as `children`.

Prefer this composition instead of converting entire layouts into Client Components.

### Context providers

Place providers as deep as practical.

Do not wrap the whole application in multiple global providers without a reason.

Read:

https://nextjs.org/docs/app/getting-started/server-and-client-components

## 6. Routing and Navigation

Use framework-native routing.

### Static routes

Example:

`app/about/page.tsx`

### Dynamic routes

Example:

`app/products/[id]/page.tsx`

For modern App Router versions, check whether route parameters are asynchronous.

Example:

```tsx
type PageProps = {
  params: Promise<{ id: string }>;
};

export default async function ProductPage({ params }: PageProps) {
  const { id } = await params;

  return <main>Product: {id}</main>;
}
```

Adapt the signature to the installed Next.js version.

### Navigation

Use:

- `next/link` for navigation.
- `next/navigation` for App Router navigation hooks.
- Appropriate route groups for layout organization.
- Dynamic segments for parameterized routes.

Avoid using ordinary anchor elements for internal navigation when Next.js Link is appropriate.

Use anchors for external destinations and normal browser navigation when suitable.

### Route groups

Use route groups to organize application sections without changing URL paths.

Example:

- `(auth)`
- `(dashboard)`
- `(marketing)`

### Parallel and intercepting routes

Use only when the application needs advanced routing behavior.

Examples:

- Modal routes.
- Independent dashboard panels.
- Context-preserving navigation.

Avoid introducing advanced routing patterns for simple pages.

## 7. Layouts and Templates

Use layouts for shared UI.

Examples:

- Root layout.
- Dashboard layout.
- Authentication layout.
- Marketing layout.

Guidelines:

- Root layout must define the document structure.
- Keep shared navigation in appropriate layouts.
- Avoid unnecessary repeated data fetching.
- Keep layouts focused.
- Use templates when a route segment must receive a fresh component instance during navigation.

Understand that layouts can persist between navigations.

Do not assume that every layout rerenders for every navigation.

## 8. Data Fetching

Choose data access based on execution environment.

### Server-side fetching

Prefer fetching directly from the original data source in Server Components.

Possible sources:

- External APIs.
- Databases.
- ORM clients.
- Internal server services.

Example:

```tsx
async function getProducts() {
  const response = await fetch(`${process.env.API_BASE_URL}/products`);

  if (!response.ok) {
    throw new Error("Failed to fetch products");
  }

  return response.json();
}
```

Use appropriate error handling and runtime validation.

### Direct database access

Server Components can access server-side database services directly.

Do not expose database clients to browser code.

Always enforce authentication and authorization before returning private records.

### Client-side fetching

Use client-side fetching when the requirement involves:

- Frequently changing data.
- Polling.
- Client-driven filters.
- Interactive dashboards.
- Browser-dependent operations.
- Real-time updates.

Consider TanStack Query or SWR.

Do not add a client-side fetching library automatically when framework-native data loading is sufficient.

### Avoid unnecessary API round trips

Do not call your own Route Handler from a Server Component merely to fetch data.

Call the underlying service or data-access function directly.

This avoids unnecessary HTTP requests.

## 9. Caching and Revalidation

Caching must be intentional.

Never assume the default behavior of `fetch`, route caching or rendering from a previous Next.js version.

Inspect the installed version and configuration.

Understand:

- Request memoization.
- Data caching.
- Full route or prerender caching.
- Client Router Cache.
- Cache Components.
- `use cache`.
- `cacheLife`.
- `cacheTag`.
- `revalidatePath`.
- `revalidateTag`.

Use only APIs supported by the project's version and configuration.

### Cache decisions

For each data source, determine:

1. How frequently does the data change?
1. Is the data public or user-specific?
1. Can it be shared between users?
1. What freshness does the feature require?
1. What happens after a mutation?
1. How should stale data be invalidated?

### Public data

Potentially suitable for shared caching:

- Public product catalogs.
- Marketing content.
- Documentation.
- Public category data.

### User-specific data

Be careful with:

- Profiles.
- Account details.
- Orders.
- Private dashboards.
- Permission-sensitive records.

Never allow private user data to leak through shared caches.

### Revalidation

Use appropriate invalidation after mutations.

Examples:

- Invalidate a product tag after updating a product.
- Revalidate a route after publishing content.
- Refresh client queries after a mutation when using TanStack Query.

Do not use broad cache invalidation when targeted invalidation is possible.

Read the official caching documentation:

https://nextjs.org/docs/app/guides/caching

## 10. Streaming and Suspense

Use streaming when different parts of a page have different loading requirements.

Consider:

- `loading.tsx`.
- React Suspense.
- Nested loading boundaries.
- Independent data-fetching components.
- Meaningful skeletons.

Example:

```tsx
import { Suspense } from "react";

export default function DashboardPage() {
  return (
    <main>
      <h1>Dashboard</h1>

      <Suspense fallback={<p>Loading analytics...</p>}>
        <Analytics />
      </Suspense>
    </main>
  );
}
```

Guidelines:

- Avoid blocking the entire page on unrelated slow requests.
- Start independent requests in parallel where possible.
- Use meaningful loading states.
- Avoid excessive nested Suspense boundaries.
- Handle errors separately from loading states.

Do not use Suspense as a substitute for error handling.

## 11. Server Actions and Server Functions

Use Server Actions for appropriate server-side mutations.

Examples:

- Creating a record.
- Updating a profile.
- Submitting a form.
- Deleting a resource.

Example:

```tsx
"use server";

export async function createProduct(formData: FormData) {
  const name = formData.get("name");

  if (typeof name !== "string" || !name.trim()) {
    return {
      success: false,
      error: "Product name is required.",
    };
  }

  // Authenticate and authorize the request.
  // Validate the data.
  // Perform the database operation.

  return {
    success: true,
  };
}
```

### Security requirements

Server Actions are externally invokable server entry points.

Always:

- Authenticate the request.
- Authorize the requested operation.
- Validate all incoming data.
- Verify ownership and permissions.
- Avoid trusting client-supplied role information.
- Handle expected failures.
- Avoid exposing internal errors or secrets.

Never treat a hidden UI control as authorization.

Do not use Server Actions as a replacement for every API endpoint.

Do not use them for high-frequency data fetching.

## 12. Route Handlers

Use Route Handlers to expose HTTP endpoints.

Location:

`app/api/.../route.ts`

Supported methods include:

- GET.
- POST.
- PUT.
- PATCH.
- DELETE.
- HEAD.
- OPTIONS.

Example:

```tsx
import { NextResponse } from "next/server";

export async function GET() {
  return NextResponse.json({
    status: "ok",
  });
}
```

Use Route Handlers for:

- External API integrations.
- Webhooks.
- Client-facing backend endpoints.
- File processing.
- Custom HTTP responses.
- Authentication callbacks when appropriate.

### Route Handler standards

- Validate input.
- Authenticate and authorize requests.
- Return appropriate HTTP status codes.
- Handle errors consistently.
- Avoid exposing internal stack traces.
- Validate webhook signatures.
- Use correct content types.
- Configure caching intentionally.
- Protect sensitive operations.

Route Handlers are not cached by default in current App Router behavior, but verify version-specific configuration and exceptions.

Do not create an API route for every server-side function.

## 13. Authentication and RBAC

Choose an authentication solution appropriate to the project.

Possible options:

- Auth.js.
- Clerk.
- Managed identity providers.
- Custom authentication when justified.

Consider:

- Login and logout.
- Session management.
- Session expiration.
- Protected routes.
- Server-side authentication.
- Role-based access control.
- Permission-based authorization.
- Unauthorized and forbidden states.

### Security rules

- Verify sessions on the server.
- Enforce permissions at the data-access or server-action boundary.
- Never trust roles sent from the browser.
- Validate resource ownership.
- Protect sensitive mutations.
- Do not rely only on route interception or middleware.
- Avoid exposing sensitive session information.

### Route protection

Use Proxy or Middleware according to the installed Next.js version and its supported conventions.

Use it for suitable request-level checks and redirects.

It must not replace authorization at the actual data-access boundary.

Read `authentication-and-rbac.md`.

## 14. Forms and Validation

Choose form handling according to complexity.

### Simple forms

Use native HTML forms and Server Actions where appropriate.

### Complex forms

Consider:

- React Hook Form.
- Zod.
- Server-side validation.
- Accessible field components.

Always validate data on the server.

Client-side validation improves user experience but is not a security boundary.

Handle:

- Pending state.
- Success state.
- Field errors.
- Server errors.
- Duplicate submissions.
- Failed network requests.

Read `forms-and-validation.md`.

## 15. Error Handling

Use framework-native error boundaries.

Consider:

- `error.tsx`.
- `global-error.tsx`.
- `not-found.tsx`.
- `notFound()`.
- `redirect()`.
- Expected error responses.

Guidelines:

- Keep error messages understandable.
- Provide recovery actions.
- Avoid exposing sensitive internal information.
- Log useful server-side diagnostic information.
- Distinguish expected business errors from unexpected exceptions.
- Handle API failures consistently.

Do not silently swallow important failures.

## 16. SEO and Metadata

Use Next.js Metadata APIs.

Consider:

- `metadata`.
- `generateMetadata`.
- Canonical URLs.
- Open Graph.
- Twitter metadata.
- Robots directives.
- Sitemap.
- Structured data.
- Dynamic metadata for content pages.

Example:

```tsx
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Products",
  description: "Explore our products.",
};
```

For dynamic pages, generate metadata from the relevant data source.

Avoid duplicate fetching when metadata and page content require the same data. Use appropriate request memoization or caching supported by the project.

Do not expose private application routes to search indexing.

Read `seo-and-discoverability.md`.

## 17. Styling and Design Systems

Use the styling approach already established by the project.

Supported approaches include:

- Tailwind CSS.
- CSS Modules.
- Global CSS.
- CSS variables.
- Component libraries.
- Design tokens.

For new projects, use a consistent styling system.

Consider:

- Global CSS architecture.
- Semantic design tokens.
- Light and dark themes.
- Responsive layouts.
- Accessible component states.
- Font optimization.
- Reusable components.

Avoid introducing multiple competing styling systems without a reason.

Read:

- `global-styles-and-design-tokens.md`
- `theming-and-dark-mode.md`
- `component-and-design-systems.md`
- `ui-design-quality-and-impeccable.md`

## 18. Images, Fonts and Assets

Use Next.js optimization features where appropriate.

Consider:

- `next/image`.
- `next/font`.
- Responsive image sizing.
- Correct image dimensions.
- Lazy loading.
- Priority loading for critical images.
- Appropriate formats.
- Local and remote image configuration.

Do not optimize every asset blindly.

Avoid unnecessary external font requests when local or framework-supported font loading is appropriate.

## 19. Environment Configuration

Maintain clear environment separation:

- Development.
- Staging.
- Production.

Use:

- `.env.local`.
- Deployment environment variables.
- Validated configuration modules.
- Server-only environment variables.
- Explicit public variables when required.

Rules:

- Never prefix secrets with `NEXT_PUBLIC_`.
- Never expose private API keys to client code.
- Validate required environment variables.
- Keep environment-specific API endpoints explicit.
- Avoid committing secrets.
- Do not assume local environment files exist in deployment.

## 20. Performance and Production

Review:

- Client JavaScript size.
- Server and client boundaries.
- Bundle composition.
- Image and font optimization.
- Streaming.
- Cache behavior.
- Navigation prefetching.
- Third-party scripts.
- Core Web Vitals.
- Server response time.

Use tools such as:

- Next.js build output.
- Bundle analyzers.
- Browser DevTools.
- Lighthouse.
- React DevTools.
- Sentry.

Do not add performance packages without a measurable need.

## 21. Testing

Consider:

- Unit tests.
- Component tests.
- Integration tests.
- End-to-end tests.
- API tests.
- Accessibility tests.

Possible tools:

- Vitest.
- React Testing Library.
- Playwright.

Test:

- Route behavior.
- Authentication.
- Permission boundaries.
- Form submission.
- API responses.
- Error handling.
- Loading states.
- Important user workflows.

Do not assume a production build proves that application behavior is correct.

## 22. Deployment

Understand the deployment target before implementing runtime-dependent features.

Consider:

- Vercel.
- Node.js hosting.
- Docker.
- Self-hosted environments.
- Static export where suitable.

Check compatibility for:

- Server Actions.
- Route Handlers.
- Image optimization.
- Middleware or Proxy.
- WebSockets.
- File storage.
- Runtime APIs.
- Scheduled tasks.

Do not assume every hosting provider supports every Next.js feature.

Maintain development, staging and production configuration separately.

## 23. Next.js Anti-Patterns

Avoid:

- Making the whole application a Client Component.
- Using Route Handlers unnecessarily for Server Component data fetching.
- Treating Server Actions as public trusted functions.
- Trusting client-side roles.
- Sharing user-specific data through unsafe caches.
- Assuming older caching defaults.
- Duplicating API and database logic.
- Using client-side Effects for data that can be fetched on the server.
- Creating excessive layouts and providers.
- Exposing private environment variables.
- Ignoring loading and error boundaries.
- Mixing App Router and Pages Router patterns without a reason.
- Introducing experimental APIs without checking compatibility.

## 24. Next.js Review Checklist

### Project and architecture

- [ ] Correct router identified.
- [ ] Installed version inspected.
- [ ] Folder structure matches project complexity.
- [ ] Existing conventions respected.

### Server and client

- [ ] Server Components used where appropriate.
- [ ] Client Components limited to interactive boundaries.
- [ ] Secrets remain server-side.
- [ ] Props across boundaries are supported and serializable.

### Data and caching

- [ ] Data fetching happens in the appropriate environment.
- [ ] Unnecessary HTTP round trips are avoided.
- [ ] Cache behavior is intentional.
- [ ] Private data cannot leak through shared caches.
- [ ] Mutations invalidate the appropriate data.

### Security

- [ ] Server Actions authenticate and authorize.
- [ ] Route Handlers validate requests.
- [ ] RBAC is enforced server-side.
- [ ] Environment variables are protected.
- [ ] Webhooks are verified where applicable.

### User experience

- [ ] Loading states exist where needed.
- [ ] Errors have recovery paths.
- [ ] Navigation works correctly.
- [ ] Metadata is appropriate.
- [ ] Responsive behavior is checked.

### Production

- [ ] Build succeeds.
- [ ] Type checking succeeds.
- [ ] Relevant tests pass.
- [ ] Environment separation is correct.
- [ ] Deployment compatibility is verified.

## 25. Related References

Load these documents when relevant:

- architecture-and-project-structure.md
- react-engineering.md
- rendering-and-caching-strategies.md
- typescript-and-code-quality.md
- component-and-design-systems.md
- global-styles-and-design-tokens.md
- theming-and-dark-mode.md
- authentication-and-rbac.md
- api-integration.md
- forms-and-validation.md
- seo-and-discoverability.md
- frontend-security-owasp.md
- performance-and-core-web-vitals.md
- testing-strategy.md
- production-readiness.md

## 26. Official Resources

- Next.js Documentation: https://nextjs.org/docs
- App Router: https://nextjs.org/docs/app
- Server and Client Components: https://nextjs.org/docs/app/getting-started/server-and-client-components
- Data Fetching: https://nextjs.org/docs/app/getting-started/fetching-data
- Route Handlers: https://nextjs.org/docs/app/getting-started/route-handlers
- Caching: https://nextjs.org/docs/app/guides/caching
- Production Checklist: https://nextjs.org/docs/app/guides/production-checklist
- Pages Router: https://nextjs.org/docs/pages
