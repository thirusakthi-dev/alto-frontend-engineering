# API Integration Example

## 1. Purpose

Demonstrate how to structure API communication in a modern frontend application.

This example covers:

- API client architecture.
- HTTP requests and responses.
- Request and response typing.
- Runtime data validation.
- Authentication integration.
- Error handling.
- Request cancellation.
- Pagination and filtering.
- File uploads and downloads.
- Environment configuration.
- API documentation.
- Development, staging and production environments.

The goal is to create predictable API communication that is easy to test, maintain and extend.

## 2. Core Principles

1. Separate API communication from UI components.
1. Reuse existing API clients and conventions.
1. Use clear request and response contracts.
1. Validate untrusted external data at runtime when appropriate.
1. Handle HTTP errors consistently.
1. Avoid unnecessary retries.
1. Support request cancellation where useful.
1. Keep credentials and secrets secure.
1. Separate environment configuration.
1. Test important success and failure cases.

## 3. Suggested Structure

```text
src/
├── lib/
│   └── api/
│       ├── client.ts
│       ├── errors.ts
│       └── types.ts
├── features/
│   └── customers/
│       ├── services/
│       │   └── customer-api.ts
│       ├── types/
│       │   └── customer.ts
│       └── components/
│           └── customer-list.tsx
├── config/
│   └── env.ts
└── types/
```

This is illustrative.

Do not create separate layers or folders unless the application needs them.

## 4. Inspect the Existing API Architecture

Before implementation, identify:

- Existing HTTP client.
- Base URL configuration.
- Authentication mechanism.
- Request interceptors or wrappers.
- Error handling conventions.
- API response format.
- Runtime validation approach.
- Data-fetching library.
- Environment configuration.
- Existing tests and mocks.

Do not introduce Axios when the existing project already uses a suitable Fetch-based client.

Do not create a second API client unnecessarily.

## 5. HTTP Fundamentals

Use HTTP methods according to their semantics.

| Method | Typical purpose |
| ------ | -------------------------------------- |
| GET | Retrieve resources |
| POST | Create resources or perform operations |
| PUT | Replace a resource |
| PATCH | Partially update a resource |
| DELETE | Delete a resource |

Understand common status codes:

| Status | Meaning |
| ------ | ------------------------------------------- |
| 200 | Successful request |
| 201 | Resource created |
| 204 | Successful request without response content |
| 400 | Invalid request |
| 401 | Unauthenticated |
| 403 | Forbidden |
| 404 | Resource not found |
| 409 | Conflict |
| 422 | Validation failure, where used by the API |
| 429 | Too many requests |
| 500 | Server error |

Follow the actual backend API contract.

Do not assume every API uses the same error response format.

## 6. API Error Type

Define a consistent error representation.

```ts
// src/lib/api/errors.ts

export type ApiErrorDetails = {
  code?: string;
  message: string;
  status?: number;
  details?: unknown;
};

export class ApiError extends Error {
  readonly status?: number;
  readonly code?: string;
  readonly details?: unknown;

  constructor({ message, status, code, details }: ApiErrorDetails) {
    super(message);

    this.name = "ApiError";
    this.status = status;
    this.code = code;
    this.details = details;
  }
}
```

Avoid exposing internal server errors or sensitive response details directly to users.

## 7. Shared Fetch Client

A small shared client can centralize common request behavior.

```ts
// src/lib/api/client.ts

import { ApiError } from "./errors";

type RequestOptions = Omit<RequestInit, "body"> & {
  body?: BodyInit | null;
};

export async function apiRequest<T>(
  path: string,
  options: RequestOptions = {},
): Promise<T> {
  const baseUrl = process.env.NEXT_PUBLIC_API_URL;

  if (!baseUrl) {
    throw new Error("API URL is not configured.");
  }

  const response = await fetch(new URL(path, baseUrl), {
    ...options,
    headers: {
      Accept: "application/json",
      ...options.headers,
    },
  });

  if (!response.ok) {
    throw new ApiError({
      message: "API request failed.",
      status: response.status,
    });
  }

  if (response.status === 204) {
    return undefined as T;
  }

  return response.json() as Promise<T>;
}
```

This is an illustrative client, not a universal production implementation.

Before using it:

- Handle different content types.
- Support `FormData` without manually setting its boundary.
- Validate response data when needed.
- Add authentication according to the real session architecture.
- Handle timeouts and cancellation.
- Avoid assuming all successful responses contain JSON.
- Decide how absolute and relative URLs should be handled.
- Separate server-only and browser-safe configuration.

The generic type `T` does not validate the server response.

Do not use a TypeScript cast as a substitute for runtime validation of untrusted data.

## 8. Runtime Validation

Use a schema validator when external response data needs runtime guarantees.

Example with Zod:

```ts
// src/features/customers/types/customer.ts

import { z } from "zod";

export const customerSchema = z.object({
  id: z.string(),
  name: z.string(),
  email: z.email(),
});

export type Customer = z.infer<typeof customerSchema>;
```

Validate a response:

```ts
const rawData: unknown = await response.json();

const customer = customerSchema.parse(rawData);
```

Choose a validator that fits the existing project.

Do not validate the same trusted data repeatedly without a reason.

## 9. Feature-Level API Services

Keep feature-specific endpoints near the feature that owns them.

Example:

```ts
// src/features/customers/services/customer-api.ts

import { apiRequest } from "@/lib/api/client";
import type { Customer } from "../types/customer";

export function getCustomers(signal?: AbortSignal) {
  return apiRequest<Customer[]>("/customers", {
    method: "GET",
    signal,
  });
}

export function getCustomer(id: string) {
  return apiRequest<Customer>(`/customers/${encodeURIComponent(id)}`);
}
```

In a production implementation, validate returned data against the corresponding schemas.

Avoid placing all application endpoints into one enormous API service.

## 10. Request Cancellation

Support cancellation for requests that may become unnecessary.

Examples:

- Search suggestions.
- Route changes.
- Component unmounting.
- Repeated filter changes.

Use `AbortController` or pass an existing `AbortSignal`.

Do not show cancellation as an ordinary server failure.

## 11. Authentication Integration

Use the application's existing authentication mechanism.

Possible approaches:

- Secure session cookies.
- Server-managed authentication.
- OAuth access tokens.
- Authentication provider SDKs.

For cookie-based cross-origin requests, configure credentials and server-side CORS and CSRF protections correctly.

For token-based authentication, follow the established token lifecycle.

Do not automatically attach credentials to arbitrary external URLs.

Never expose private credentials through browser bundles.

## 12. Error Handling

Handle errors according to their meaning.

Examples:

| Error | Expected behavior |
| --------------- | --------------------------------------------- |
| Network failure | Explain that the service could not be reached |
| 400 / 422 | Display relevant validation feedback |
| 401 | Handle authentication state |
| 403 | Display an appropriate permission message |
| 404 | Show missing-resource UI |
| 409 | Handle conflicting data |
| 429 | Respect rate limits and retry guidance |
| 500 | Display a safe failure message |

Do not turn every error into the same generic success-looking UI.

Do not silently swallow failed requests.

## 13. Retries and Timeouts

Retry only when appropriate.

Consider:

- Whether the operation is idempotent.
- Whether the error is temporary.
- Server-provided retry guidance.
- Rate limits.
- Network conditions.
- Maximum retry attempts.
- Exponential backoff and jitter.

Avoid automatically retrying mutations that may already have succeeded.

Use request timeouts where the application needs a bounded waiting period.

## 14. Pagination and Filtering

Represent query parameters explicitly.

Example:

```ts
type CustomerQuery = {
  page: number;
  limit: number;
  search?: string;
  status?: "active" | "inactive";
};
```

Use `URLSearchParams` to construct query strings.

Consider:

- Server pagination.
- Sorting.
- Search.
- Filters.
- Empty results.
- Invalid page numbers.
- Total record counts.

Keep URL state synchronized with filters when users need shareable or restorable views.

## 15. File Uploads

Use `FormData` for multipart uploads.

Example:

```ts
const formData = new FormData();

formData.append("file", file);

await fetch("/api/files", {
  method: "POST",
  body: formData,
});
```

Do not manually set the multipart `Content-Type` header when using browser `FormData`.

The browser must generate the correct boundary.

The backend must independently validate file size, content, type and access permissions.

## 16. File Downloads

For downloads, consider:

- Response content type.
- Content disposition.
- File naming.
- Large-file memory usage.
- Authorization.
- Error responses.

Do not assume every response can safely be converted into a Blob.

Use streaming approaches when large files require them.

## 17. Data Fetching and Caching

Choose the fetching approach based on the application.

| Approach | Typical use |
| -------------------- | ------------------------------------- |
| Server-side Fetch | Server-rendered data |
| Native browser Fetch | Simple client requests |
| TanStack Query | Client-side server-state management |
| SWR | Client-side data fetching and caching |
| GraphQL client | GraphQL API integration |

Avoid duplicating caching and fetching responsibilities between multiple layers.

For Next.js, understand the installed version's rendering and caching behavior before configuring Fetch options.

See:

- `../../references/rendering-and-caching-strategies.md`
- `../../references/state-management.md`

## 18. Environment Separation

Keep development, staging and production configurations separate.

Example:

```dotenv
# .env.example

# Server-only
API_BASE_URL=

# Browser-exposed, if required
NEXT_PUBLIC_API_URL=
```

Consider:

- Different API endpoints.
- Environment-specific credentials.
- Feature flags.
- Local development services.
- Production secrets.
- Build-time versus runtime configuration.

In Next.js, `NEXT_PUBLIC_` values are exposed to browser code and generally inlined at build time.

Never put API secrets in public variables.

See `../../references/environment-configuration.md`.

## 19. API Documentation

Use the backend's actual API contract.

Possible documentation approaches:

- OpenAPI.
- Swagger UI.
- Scalar.
- Generated TypeScript clients.
- GraphQL schemas.

Do not invent endpoints, request fields or response formats.

Generate types from a maintained API schema when that improves consistency.

Verify generated types against the backend contract.

## 20. Existing API Integration Changes

When modifying an existing API integration:

1. Find all relevant request call sites.
1. Inspect the shared client.
1. Trace the complete request and response flow.
1. Check authentication behavior.
1. Review error handling.
1. Inspect query caching and invalidation.
1. Review environment configuration.
1. Check existing mocks and tests.
1. Make the smallest reliable change.
1. Verify affected consumers.

Do not replace the HTTP client or response contract without a justified migration plan.

## 21. Testing

Test:

- Successful responses.
- Empty responses.
- Invalid response data.
- Network failures.
- HTTP errors.
- Authentication failures.
- Permission failures.
- Request cancellation.
- Query parameter construction.
- File uploads.
- Pagination and filtering.

Use MSW or the project's existing API mocking strategy where appropriate.

Avoid tests that depend on a live production API.

## 22. Common Anti-Patterns

Avoid:

- HTTP requests directly inside every UI component.
- Duplicate API clients.
- Unvalidated external data.
- Hardcoded environment URLs.
- Exposed secrets.
- Inconsistent error handling.
- Unnecessary retries.
- Retrying unsafe mutations.
- Incorrect request cancellation.
- Manual multipart boundaries.
- Duplicated server-state caches.
- Invented backend contracts.
- Excessive API abstraction layers.

## 23. Review Checklist

### Architecture

- [ ] API responsibilities are separated.
- [ ] Existing clients are reused.
- [ ] Feature services have clear boundaries.
- [ ] No unnecessary abstraction exists.

### Reliability

- [ ] Request errors are handled.
- [ ] Response data is validated where required.
- [ ] Cancellation is supported where useful.
- [ ] Retry behavior is safe.

### Security

- [ ] Secrets remain server-side.
- [ ] Authentication follows the real session model.
- [ ] Backend authorization is enforced.
- [ ] External URLs do not receive credentials accidentally.

### Environments

- [ ] Development configuration works.
- [ ] Staging configuration is separate.
- [ ] Production configuration is safe.
- [ ] Build-time and runtime configuration are understood.

### Verification

- [ ] API tests pass.
- [ ] Error cases are covered.
- [ ] TypeScript checks pass.
- [ ] Lint checks pass.
- [ ] Production build succeeds.

## 24. Related References

- `../../references/api-integration.md`
- `../../references/authentication-and-authorization.md`
- `../../references/environment-configuration.md`
- `../../references/frontend-security.md`
- `../../references/state-management.md`
- `../../references/rendering-and-caching-strategies.md`
- `../../references/testing-strategy.md`
- `../../references/typescript-and-code-quality.md`
- `../../references/anti-ai-slop-and-engineering-quality.md`

## 25. Official Resources

- MDN Fetch API: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
- MDN AbortController: https://developer.mozilla.org/en-US/docs/Web/API/AbortController
- MDN FormData: https://developer.mozilla.org/en-US/docs/Web/API/FormData
- HTTP Semantics: https://www.rfc-editor.org/rfc/rfc9110
- OpenAPI: https://spec.openapis.org/oas/latest.html
- Zod: https://zod.dev/
- TanStack Query: https://tanstack.com/query/latest/docs/framework/react/overview
- Next.js Data Fetching: https://nextjs.org/docs/app/getting-started/fetching-data
