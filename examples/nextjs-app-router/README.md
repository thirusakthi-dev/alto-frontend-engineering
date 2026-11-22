# Next.js App Router Example

## 1. Purpose

Demonstrate a maintainable Next.js application structure using the App Router, React Server Components, Client Components, TypeScript and modern application conventions.

This example is a reference implementation for frontend engineering agents.

It demonstrates how to:

- Structure a Next.js application.
- Organize routes and layouts.
- Separate Server and Client Components.
- Fetch and display data.
- Handle loading and error states.
- Manage application-level styles.
- Implement reusable components.
- Configure metadata and SEO.
- Manage environment variables.
- Organize application logic.
- Verify application quality.

This is a reference example, not a mandatory folder structure for every Next.js project.

## 2. Technology Stack

| Technology | Purpose |
| ------------------ | ------------------------------- |
| Next.js App Router | Application framework |
| React | UI development |
| TypeScript | Type safety |
| Tailwind CSS | Styling |
| Lucide React | Icons |
| Zod | Runtime validation where needed |

Use current stable, mutually compatible versions when creating a runnable project.

Do not install a dependency simply because it appears in this reference. Evaluate whether the actual application needs it.

## 3. Example Architecture

A recommended starting structure:

```text
nextjs-app-router/
├── README.md
└── src/
    ├── app/
    │   ├── (public)/
    │   │   ├── page.tsx
    │   │   └── about/
    │   │       └── page.tsx
    │   ├── dashboard/
    │   │   ├── layout.tsx
    │   │   ├── loading.tsx
    │   │   ├── error.tsx
    │   │   └── page.tsx
    │   ├── api/
    │   │   └── health/
    │   │       └── route.ts
    │   ├── layout.tsx
    │   ├── globals.css
    │   ├── not-found.tsx
    │   └── page.tsx
    ├── components/
    │   ├── ui/
    │   ├── layout/
    │   └── shared/
    ├── features/
    │   └── dashboard/
    │       ├── components/
    │       ├── services/
    │       ├── hooks/
    │       └── types/
    ├── lib/
    │   ├── api/
    │   ├── utils/
    │   └── validations/
    ├── config/
    └── types/
```

This structure is illustrative.

Do not create every folder automatically.

Add directories when the application has actual responsibilities that justify them.

## 4. App Router Fundamentals

The `src/app/` directory defines the application's routes and layouts.

Important conventions:

| File | Responsibility |
| --------------- | -------------------------- |
| `page.tsx` | Route UI |
| `layout.tsx` | Shared route layout |
| `loading.tsx` | Loading UI |
| `error.tsx` | Route-level error handling |
| `not-found.tsx` | Not-found UI |
| `route.ts` | Route Handler |
| `template.tsx` | Re-created layout template |
| `default.tsx` | Parallel route fallback |

Use framework conventions rather than building custom routing mechanisms unnecessarily.

## 5. Server and Client Components

Use Server Components by default.

Prefer Client Components only when browser-side interactivity or client-specific capabilities are required.

### Server Component Responsibilities

Examples:

- Fetching server-side data.
- Reading server-only configuration.
- Accessing server-side services.
- Rendering content that does not require browser interaction.
- Keeping private dependencies out of client bundles.

Example:

```tsx
// src/app/dashboard/page.tsx

import { DashboardSummary } from "@/features/dashboard/components/dashboard-summary";
import { getDashboardSummary } from "@/features/dashboard/services/dashboard-service";

export default async function DashboardPage() {
  const summary = await getDashboardSummary();

  return <DashboardSummary summary={summary} />;
}
```

### Client Component Responsibilities

Examples:

- Interactive controls.
- Local UI state.
- Browser APIs.
- Event handlers.
- Client-side subscriptions.

Example:

```tsx
// src/components/shared/counter.tsx

"use client";

import { useState } from "react";

export function Counter() {
  const [count, setCount] = useState(0);

  return (
    <button type="button" onClick={() => setCount((current) => current + 1)}>
      Count: {count}
    </button>
  );
}
```

Do not add `"use client"` to a parent layout or page when a smaller interactive component boundary is sufficient.

## 6. Layouts and Route Organization

Use layouts to share UI across related routes.

Example:

```tsx
// src/app/layout.tsx

import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: {
    default: "Frontend Example",
    template: "%s | Frontend Example",
  },
  description: "A Next.js App Router engineering example.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
```

Route groups such as `(public)` help organize routes without adding URL segments.

Do not create route groups unless they improve organization or layout boundaries.

## 7. Data Fetching

Keep data fetching close to the server-side feature that owns it when appropriate.

Example:

```ts
// src/features/dashboard/services/dashboard-service.ts

export type DashboardSummary = {
  totalUsers: number;
  activeProjects: number;
};

export async function getDashboardSummary(): Promise<DashboardSummary> {
  const response = await fetch(`${process.env.API_BASE_URL}/dashboard/summary`);

  if (!response.ok) {
    throw new Error("Unable to load dashboard summary.");
  }

  return response.json() as Promise<DashboardSummary>;
}
```

This is an illustrative service.

A real implementation should:

- Validate external responses at runtime.
- Handle authentication where required.
- Use the correct environment configuration.
- Apply an appropriate caching strategy.
- Avoid exposing private service URLs or credentials to browser code.

Do not assume that TypeScript validates JSON returned by an API.

## 8. Loading and Error States

Use route-level loading and error boundaries when appropriate.

Example:

```tsx
// src/app/dashboard/loading.tsx

export default function DashboardLoading() {
  return (
    <div role="status" aria-live="polite">
      Loading dashboard...
    </div>
  );
}
```

Example:

```tsx
// src/app/dashboard/error.tsx

"use client";

type DashboardErrorProps = {
  error: Error & { digest?: string };
  reset: () => void;
};

export default function DashboardError({ reset }: DashboardErrorProps) {
  return (
    <section role="alert">
      <h2>Unable to load the dashboard.</h2>

      <button type="button" onClick={reset}>
        Try again
      </button>
    </section>
  );
}
```

Do not expose sensitive internal error details to users.

Provide useful recovery actions where possible.

## 9. Reusable Components

Keep reusable UI components independent of feature-specific business logic.

Example responsibilities:

```text
components/
├── ui/
│   ├── button.tsx
│   ├── input.tsx
│   └── dialog.tsx
├── layout/
│   ├── header.tsx
│   └── sidebar.tsx
└── shared/
    └── empty-state.tsx
```

Use composition instead of building components with excessive configuration props.

Follow native HTML semantics and accessibility requirements.

## 10. Styling

Use a consistent styling approach.

This example assumes Tailwind CSS.

Keep shared design tokens and global styles centralized.

Avoid:

- Duplicated global CSS.
- Arbitrary values without justification.
- Conflicting styling systems.
- Unnecessary CSS abstractions.
- Inconsistent spacing and typography.

Check the installed Tailwind version before using configuration or syntax from a different major version.

## 11. Environment Configuration

Example environment variables:

```dotenv
# .env.example

# Server-only
API_BASE_URL=

# Browser-exposed, only if the browser needs this URL
NEXT_PUBLIC_API_URL=
```

Keep secrets server-side.

Do not prefix private credentials with `NEXT_PUBLIC_`.

Validate required environment variables and separate development, staging and production configuration.

See `../../references/environment-configuration.md`.

## 12. Metadata and SEO

Use the Next.js Metadata API.

Consider:

- Default metadata.
- Page-specific metadata.
- Dynamic metadata.
- Canonical URLs.
- Open Graph information.
- Robots directives.
- Sitemap.
- Robots configuration.

Do not add SEO configuration to private dashboard routes as if they were public marketing pages.

See `../../references/seo-and-discoverability.md`.

## 13. Error Handling and Security

Apply:

- Server-side authorization.
- Input validation.
- Safe handling of external data.
- Secure environment configuration.
- Appropriate error boundaries.
- Secure API communication.
- Safe redirects.
- No secret exposure.

Never rely on frontend conditional rendering as the only authorization mechanism.

## 14. Testing

Use the project's chosen testing tools.

Possible checks:

- TypeScript.
- Lint.
- Component tests.
- Integration tests.
- End-to-end tests.
- Production build.

Prioritize important user journeys and failure conditions.

Do not add a complete testing framework solely for this example unless a runnable project requires it.

## 15. Version Compatibility

Before implementing this example:

1. Check the installed Next.js version.
1. Check the React version.
1. Check the TypeScript version.
1. Verify current App Router conventions.
1. Verify caching and rendering behavior.
1. Check package compatibility.
1. Use official documentation.

Do not blindly combine examples from different Next.js versions.

Framework defaults and caching behavior can change between releases.

## 16. Adaptation Guidelines

When using this example in an existing project:

1. Inspect the existing repository.
1. Identify current route and layout organization.
1. Review existing components and libraries.
1. Preserve existing conventions.
1. Reuse working functionality.
1. Adapt only relevant patterns.
1. Avoid unnecessary folder migrations.
1. Test affected routes and components.

Do not replace an existing architecture just to match this example's directory structure.

## 17. Verification Checklist

- [ ] App Router structure is correct.
- [ ] Server and Client Components are separated appropriately.
- [ ] No unnecessary client boundaries exist.
- [ ] Data fetching follows the application's caching requirements.
- [ ] Loading and error states exist where needed.
- [ ] External data is validated appropriately.
- [ ] Environment variables are handled safely.
- [ ] Metadata is appropriate for public routes.
- [ ] Components are accessible.
- [ ] Responsive behavior is checked.
- [ ] TypeScript and lint checks pass.
- [ ] Production build succeeds.

## 18. Related References

- `../../references/architecture-and-project-structure.md`
- `../../references/react-engineering.md`
- `../../references/nextjs-engineering.md`
- `../../references/rendering-and-caching-strategies.md`
- `../../references/typescript-and-code-quality.md`
- `../../references/reusable-ui-components.md`
- `../../references/frontend-security.md`
- `../../references/environment-configuration.md`
- `../../references/testing-strategy.md`
- `../../references/seo-and-discoverability.md`

## 19. Official Documentation

- Next.js App Router: https://nextjs.org/docs/app
- Next.js Project Structure: https://nextjs.org/docs/app/getting-started/project-structure
- Server and Client Components: https://nextjs.org/docs/app/getting-started/server-and-client-components
- Data Fetching: https://nextjs.org/docs/app/getting-started/fetching-data
- Error Handling: https://nextjs.org/docs/app/getting-started/error-handling
- Metadata: https://nextjs.org/docs/app/getting-started/metadata-and-og-images
- React: https://react.dev/
- TypeScript: https://www.typescriptlang.org/docs/
