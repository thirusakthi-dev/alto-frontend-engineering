# API Integration

## 1. Purpose

Define standards for designing, implementing, modifying, debugging and maintaining frontend-to-backend integrations.

Support:

- REST API integration.
- HTTP methods and status codes.
- API client architecture.
- Request and response handling.
- Type-safe API contracts.
- Runtime validation.
- Authentication integration.
- Error handling.
- Request cancellation.
- Retries and timeouts.
- Pagination and filtering.
- File uploads and downloads.
- Caching and synchronization.
- Real-time communication.
- API documentation integration.

The objective is to build reliable, secure and maintainable frontend integrations without duplicating networking logic across features.

## 2. Inspect Before Integration

Before implementing an API integration:

1. Inspect the existing API client.
1. Identify the backend framework and API architecture.
1. Review existing endpoint definitions.
1. Check request and response formats.
1. Understand authentication requirements.
1. Review environment-specific API URLs.
1. Identify existing API types and schemas.
1. Inspect error handling conventions.
1. Check caching and data-fetching libraries.
1. Review existing backend documentation.

For existing projects, reuse established API infrastructure where practical.

Never invent endpoint paths, request fields, response properties, authentication headers or status codes.

If the backend contract is unavailable, clearly identify assumptions and request the necessary information when it blocks implementation.

## 3. API Architecture

Separate networking concerns from UI components.

A common architecture:

```text id="3qu9c4"
Feature Component
      |
      v
Feature Hook
      |
      v
API Service
      |
      v
Shared API Client
      |
      v
Backend API
```

Possible responsibilities:

| Layer | Responsibility |
| ---------- | -------------------------------------------- |
| Component | UI and user interactions |
| Hook | Feature-level data and mutation state |
| Service | Endpoint-specific operations |
| API client | HTTP configuration and shared behavior |
| Backend | Validation, business logic and authorization |

Adapt the architecture to the project.

Do not introduce unnecessary layers for a small application.

## 4. HTTP Fundamentals

Understand HTTP methods and their intended semantics.

| Method | Common purpose |
| ------- | ----------------------------------------- |
| GET | Retrieve a resource |
| POST | Create a resource or perform an operation |
| PUT | Replace a resource representation |
| PATCH | Partially modify a resource |
| DELETE | Remove a resource |
| HEAD | Retrieve response headers |
| OPTIONS | Discover communication options |

Follow the backend's documented API contract.

Important distinctions:

- GET is safe and should not perform state-changing operations.
- PUT is generally idempotent.
- DELETE is defined as idempotent in HTTP semantics, although repeated responses may differ.
- POST is not inherently idempotent.
- PATCH semantics depend on the patch format and API contract.

Do not select a method based only on frontend convenience.

## 5. HTTP Status Codes

Understand common response statuses.

| Status | Meaning |
| ------ | ------------------------------- |
| 200 | OK |
| 201 | Created |
| 202 | Accepted |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized or unauthenticated |
| 403 | Forbidden |
| 404 | Not Found |
| 405 | Method Not Allowed |
| 409 | Conflict |
| 413 | Content Too Large |
| 415 | Unsupported Media Type |
| 422 | Unprocessable Content |
| 429 | Too Many Requests |
| 500 | Internal Server Error |
| 502 | Bad Gateway |
| 503 | Service Unavailable |
| 504 | Gateway Timeout |

The exact status behavior depends on the backend contract.

Do not assume every API uses 422 for validation errors or 200 for every successful operation.

Handle empty responses such as 204 correctly.

## 6. Shared API Client

Use a shared API client when the application has repeated networking requirements.

Common responsibilities:

- Base URL.
- Default headers.
- Credential handling.
- Request serialization.
- Response parsing.
- Error normalization.
- Timeouts.
- Request cancellation.
- Authentication integration.

Example using `fetch`:

```tsx id="x9xyc3"
interface ApiError {
  message: string;
  status: number;
}

async function apiRequest<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}${path}`, {
    ...init,
    headers: {
      Accept: "application/json",
      ...init?.headers,
    },
  });

  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }

  if (response.status === 204) {
    return undefined as T;
  }

  return response.json() as Promise<T>;
}
```

This is a simplified illustration, not a universal production implementation.

A production API client should also consider:

- URL construction.
- Content types.
- Structured error responses.
- Network failures.
- Abort signals.
- Credentials.
- Request body handling.
- Runtime response validation.

Do not use the example without adapting it to the actual backend contract.

## 7. Fetch and Axios

Both native `fetch` and Axios can be appropriate.

### Fetch

Advantages:

- Built into modern browsers.
- No additional dependency.
- Supports AbortController.
- Supports streaming responses.
- Works with standard Request and Response APIs.

Considerations:

- HTTP error statuses do not automatically reject the promise.
- Response bodies must be consumed deliberately.
- Timeout handling requires an appropriate cancellation strategy.

### Axios

Advantages:

- Configurable instances.
- Interceptors.
- Convenient request and response handling.
- Built-in timeout configuration.
- Established ecosystem.

Considerations:

- Additional dependency.
- Interceptor behavior must be managed carefully.
- Configuration should remain consistent.

Choose based on existing project conventions and actual requirements.

Do not replace a working API client without a measurable benefit.

## 8. Request and Response Types

Use explicit TypeScript types for API contracts.

Example:

```tsx id="6dqzom"
interface User {
  id: string;
  name: string;
  email: string;
}

interface CreateUserInput {
  name: string;
  email: string;
}

interface ApiResponse<T> {
  data: T;
  message?: string;
}
```

Separate:

- API request types.
- API response types.
- Domain types.
- Form input types.
- UI-specific view models.

These types may differ.

Do not assume that a form model is identical to the backend response.

Avoid `any`.

Use `unknown` for untrusted data and narrow it before use.

## 9. Runtime Validation

TypeScript types do not validate network responses at runtime.

API responses are external data.

Use runtime validation when correctness or safety requires it.

Possible libraries include:

- Zod.
- Valibot.
- ArkType.

Reuse an existing validation library when available.

Example:

```tsx id="7kw3ys"
import { z } from "zod";

const UserSchema = z.object({
  id: z.string(),
  name: z.string(),
  email: z.string().email(),
});

type User = z.infer<typeof UserSchema>;
```

Validate important untrusted data at appropriate boundaries.

Do not add runtime schemas for every trivial response without considering project requirements.

## 10. API Service Organization

Keep endpoint-specific operations organized.

Example:

```text id="skq15q"
features/
└── users/
    ├── api/
    │   └── users.api.ts
    ├── hooks/
    │   └── use-users.ts
    ├── components/
    └── types/
        └── users.types.ts
```

Example service:

```tsx id="1ihvzb"
export const usersApi = {
  getAll: () => apiRequest<User[]>("/users"),

  getById: (id: string) => apiRequest<User>(`/users/${encodeURIComponent(id)}`),
};
```

Guidelines:

- Keep endpoint logic out of presentation components.
- Reuse shared networking behavior.
- Avoid giant service files.
- Keep feature boundaries clear.
- Avoid creating abstractions without repeated need.

Follow the existing project structure.

## 11. Query Parameters

Use query parameters for supported filtering, sorting, searching and pagination.

Example:

```text id="8w1h4m"
GET /users?page=1&limit=10&search=thiru
```

Use URLSearchParams for safe construction.

Example:

```tsx id="krc39y"
const params = new URLSearchParams({
  page: "1",
  limit: "10",
  search: "thiru",
});

const url = `/users?${params.toString()}`;
```

Do not manually concatenate untrusted values into URLs.

Do not assume that every backend uses the same filtering convention.

## 12. Pagination

Common pagination strategies:

- Offset-based pagination.
- Page-based pagination.
- Cursor-based pagination.

Understand the backend's actual response contract.

Example:

```tsx id="8bjx7p"
interface PaginatedResponse<T> {
  items: T[];
  page: number;
  limit: number;
  total: number;
  totalPages: number;
}
```

This is illustrative.

Consider:

- Empty results.
- Last page.
- Changing page size.
- Filters resetting pagination.
- Search changes.
- Loading states.
- Concurrent requests.
- Duplicate records.

Use cursor pagination for suitable large or frequently changing datasets when supported by the backend.

## 13. Filtering and Sorting

Implement filtering and sorting according to the API contract.

Consider:

- Search text.
- Multiple filters.
- Date ranges.
- Status filters.
- Sort field.
- Sort direction.
- Reset behavior.
- URL synchronization.

Use debouncing for search when appropriate.

Do not assume that filtering on the frontend is sufficient for large datasets or security-sensitive queries.

Never rely on frontend filtering to restrict access to records.

## 14. Error Handling

Normalize API errors where useful.

Possible error categories:

- Validation error.
- Authentication error.
- Authorization error.
- Not found.
- Conflict.
- Rate limit.
- Server error.
- Network failure.
- Timeout.
- Cancelled request.

Example:

```tsx id="yq1qke"
interface ApiError {
  message: string;
  status?: number;
  code?: string;
  details?: unknown;
}
```

Guidelines:

- Preserve useful backend error information.
- Display understandable messages.
- Avoid exposing stack traces or internal server details.
- Handle validation errors at the appropriate form fields.
- Distinguish network failures from HTTP errors.
- Avoid silently swallowing exceptions.
- Log only appropriate diagnostic information.

Do not show raw backend error objects directly to users.

## 15. Retry and Timeout Strategy

Retries can improve resilience but may create duplicate operations.

Consider retrying suitable transient failures:

- Temporary network errors.
- Selected 5xx responses.
- 429 responses according to server guidance.

Respect `Retry-After` when provided.

Do not blindly retry:

- Validation errors.
- Authorization failures.
- User-cancelled requests.
- Non-idempotent mutations.

For mutations, retry only when the operation's semantics and backend support make it safe.

Use idempotency keys where the backend supports them for operations that require duplicate protection.

Avoid infinite retries.

## 16. Request Cancellation and Race Conditions

Use AbortController or the existing data-fetching library's cancellation mechanisms.

Important scenarios:

- User changes search text.
- User navigates away.
- Component unmounts.
- A newer request replaces an older one.
- A slow request returns after newer data.

Avoid displaying stale results because an older request completed later.

Do not confuse cancellation with server-side rollback.

Aborting a browser request does not guarantee that the backend stopped processing it.

## 17. Authentication Integration

Use the existing authentication mechanism.

Consider:

- Cookie credentials.
- Authorization headers.
- Session expiration.
- Token refresh.
- Logout.
- Permission errors.

Do not expose access tokens unnecessarily.

Do not implement authentication separately in every API service.

See `authentication-and-authorization.md`.

## 18. File Uploads

For file uploads:

- Validate file type.
- Validate file size.
- Provide upload progress where useful.
- Handle cancellation where supported.
- Display upload failures.
- Prevent duplicate submissions.
- Use appropriate multipart handling.

Example:

```tsx id="mfn6x7"
const formData = new FormData();

formData.append("file", file);

await fetch("/api/upload", {
  method: "POST",
  body: formData,
});
```

Do not manually set the multipart `Content-Type` header when using browser FormData.

The browser must generate the appropriate boundary.

Client-side file validation improves UX but does not replace backend validation.

## 19. File Downloads

For downloads, consider:

- Content type.
- Content disposition.
- File name.
- Blob handling.
- Large file size.
- Authentication.
- Expired download links.
- Error responses.

Do not expose private storage URLs unnecessarily.

Use server-authorized downloads or short-lived signed URLs when appropriate.

## 20. Caching and Server State

Distinguish API communication from server-state management.

Server state includes:

- API data.
- Loading state.
- Error state.
- Cache.
- Background refetch.
- Mutations.
- Synchronization.

Possible approaches:

- TanStack Query.
- SWR.
- Framework-native data fetching.
- Native fetch for simpler cases.

Use the existing project approach.

Avoid duplicating server data across unrelated state systems.

Consider:

- Cache keys.
- Cache invalidation.
- Stale data.
- Refetch behavior.
- Mutation updates.
- Optimistic updates.
- Pagination.
- Authentication changes.

See `state-management.md` and `rendering-and-caching-strategies.md`.

## 21. Optimistic Updates

Optimistic updates display an expected result before the backend confirms it.

Use when:

- The expected result is predictable.
- The operation is suitable for optimistic behavior.
- Failure can be handled safely.

Typical flow:

1. Save the previous cached state.
1. Apply the optimistic change.
1. Send the mutation.
1. Confirm or update the result.
1. Roll back or reconcile on failure.

Do not use optimistic updates for every mutation.

For high-impact operations, confirmed server responses may be more appropriate.

## 22. Real-Time API Integration

Possible communication approaches:

### Polling

Periodically requests updates.

Suitable for simple or low-frequency synchronization.

### Server-Sent Events

Provides a server-to-client event stream over HTTP.

Useful for one-way live updates.

### WebSockets

Provides bidirectional communication.

Useful for chat, collaborative features and interactive real-time systems.

Choose according to requirements.

Consider:

- Connection management.
- Authentication.
- Reconnection.
- Duplicate events.
- Event ordering.
- Cleanup.
- Offline behavior.
- Server resource usage.

Do not use WebSockets when ordinary HTTP requests are sufficient.

## 23. GraphQL and Other API Styles

REST is common, but not universal.

Other approaches include:

- GraphQL.
- tRPC.
- RPC-style APIs.
- gRPC-web.
- Framework-specific server functions.

Inspect the existing architecture before choosing an integration approach.

Do not force REST into an existing GraphQL application or introduce GraphQL without a clear requirement.

Use the API style already supported by the backend unless a migration is explicitly justified.

## 24. Environment Configuration

Keep API configuration environment-specific.

Common environments:

- Development.
- Staging.
- Production.

Consider:

- API base URL.
- Public application URL.
- Feature flags.
- Authentication callback URLs.
- Upload configuration.

Guidelines:

- Never hardcode production API URLs throughout the application.
- Never commit secrets.
- Validate required configuration.
- Keep public and private environment variables separate.
- Avoid exposing backend credentials to browser bundles.
- Verify configuration in each deployment environment.

Do not use one environment's credentials or API URL accidentally in another.

## 25. API Documentation

Use the backend's actual API documentation.

Possible formats:

- OpenAPI.
- Swagger.
- Scalar.
- Postman collections.
- GraphQL schema documentation.

Use documentation to verify:

- Endpoint paths.
- Methods.
- Request schemas.
- Response schemas.
- Authentication.
- Error responses.
- Query parameters.
- File upload requirements.

Do not invent API contracts when documentation exists.

For production deployments, avoid unintentionally exposing internal API documentation or administrative endpoints.

Follow environment-specific documentation access rules.

## 26. Existing API Integration Modification

When modifying existing API integrations:

1. Identify the affected endpoint.
1. Inspect its service and consumers.
1. Review the backend contract.
1. Trace request and response data flow.
1. Check cache keys and invalidation.
1. Identify authentication dependencies.
1. Check loading and error handling.
1. Make the smallest reliable change.
1. Update affected types and consumers.
1. Test success and failure scenarios.

Preserve existing endpoint behavior and response expectations where possible.

Do not change API contracts without coordinating with the backend requirements.

## 27. Testing

Test API integrations at appropriate levels.

### Unit tests

- URL construction.
- Data transformations.
- Error normalization.
- Validation helpers.
- Query parameter handling.

### Integration tests

- Request configuration.
- Response handling.
- Authentication behavior.
- Loading and error states.
- Mutation behavior.
- Cache invalidation.

### End-to-end tests

- Actual user workflows.
- Search and filtering.
- Pagination.
- Upload and download.
- Permission handling.
- Network failure behavior.

Use the project's existing mocking and testing tools.

Do not rely only on mocked success responses.

## 28. Common Anti-Patterns

Avoid:

- API requests directly inside large presentation components.
- Duplicated API client logic.
- Invented endpoint contracts.
- Unchecked response assumptions.
- Excessive retries.
- Retrying non-idempotent operations blindly.
- Ignoring request cancellation.
- Exposing secrets in client code.
- Displaying raw backend errors.
- Duplicating server state.
- Incorrect cache invalidation.
- Setting multipart headers manually for FormData.
- Treating frontend validation as backend security.
- Replacing existing API infrastructure unnecessarily.

## 29. Decision Workflow

Before implementing an API integration:

1. Inspect the existing API architecture.
1. Verify the backend contract.
1. Identify authentication requirements.
1. Define request and response types.
1. Choose the existing networking approach.
1. Implement the service layer.
1. Handle errors and cancellation.
1. Integrate server-state management.
1. Verify environment configuration.
1. Test realistic success and failure cases.

Keep networking behavior consistent across the application.

## 30. Review Checklist

### Architecture

- [ ] Existing API client is reused.
- [ ] API services follow project conventions.
- [ ] Networking is separated from presentation.
- [ ] Backend contracts are verified.

### Data

- [ ] Request types are defined.
- [ ] Response types are accurate.
- [ ] Runtime validation is considered.
- [ ] Pagination and filtering are handled correctly.

### Reliability

- [ ] Loading and error states work.
- [ ] Cancellation is handled.
- [ ] Retries are safe.
- [ ] Cache invalidation is correct.

### Security

- [ ] Secrets are not exposed.
- [ ] Authentication is handled correctly.
- [ ] Backend authorization remains authoritative.
- [ ] Upload and download handling is safe.

### Verification

- [ ] Relevant tests pass.
- [ ] Existing API consumers work.
- [ ] Type checking passes.
- [ ] Build passes.

## 31. Related References

- architecture-and-project-structure.md
- authentication-and-authorization.md
- forms-and-validation.md
- state-management.md
- typescript-and-code-quality.md
- frontend-security.md
- environment-configuration.md
- rendering-and-caching-strategies.md
- testing-strategy.md

## 32. Official Resources

- MDN Fetch API: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
- MDN HTTP Methods: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods
- MDN HTTP Status Codes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
- MDN AbortController: https://developer.mozilla.org/en-US/docs/Web/API/AbortController
- TanStack Query: https://tanstack.com/query/latest/docs/framework/react/overview
- Axios: https://axios-http.com/docs/intro
- OpenAPI Specification: https://spec.openapis.org/oas/latest.html
- Zod: https://zod.dev/
- OWASP REST Security Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html
