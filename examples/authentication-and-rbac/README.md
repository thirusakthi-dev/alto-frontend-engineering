# Authentication and Role-Based Access Control

## 1. Purpose

Demonstrate how to integrate authentication and authorization into a React or Next.js application.

This example covers:

- Authentication and authorization.
- Login and logout.
- Session management.
- Protected routes.
- Role-based access control (RBAC).
- Permission-based UI.
- Server-side authorization.
- API integration.
- Secure session handling.
- Loading and error states.

The goal is to demonstrate secure frontend integration without treating frontend checks as the application's security boundary.

## 2. Core Principles

1. Authentication identifies the user.
1. Authorization determines what the user can access.
1. The backend is responsible for enforcing permissions.
1. Frontend checks improve navigation and user experience.
1. Never trust client-provided roles or permissions.
1. Protect sensitive session data.
1. Use the existing authentication architecture when modifying a project.
1. Avoid unnecessary authentication dependencies.
1. Handle expired sessions and failed requests.
1. Test both permitted and denied access.

## 3. Authentication vs Authorization

| Concept | Responsibility |
| -------------- | ---------------------------------- |
| Authentication | Verifies who the user is |
| Authorization | Determines what the user can do |
| RBAC | Assigns access according to roles |
| Permissions | Represent specific allowed actions |
| Session | Maintains authenticated state |

Example:

A user may be authenticated but not authorized to access an administrative page.

Do not treat these concepts as interchangeable.

## 4. Example Roles and Permissions

Consider an internal application with two roles:

| Role | Permissions |
| -------------- | ---------------------------------------------------------- |
| ADMIN | Manage users, view reports, manage settings |
| SALES_EMPLOYEE | View assigned customers, update permitted customer records |

Example permission identifiers:

```ts
export const permissions = {
  usersRead: "users:read",
  usersManage: "users:manage",
  reportsRead: "reports:read",
  customersRead: "customers:read",
  customersUpdate: "customers:update",
} as const;

export type Permission = (typeof permissions)[keyof typeof permissions];
```

Define role-to-permission mappings only when the application has a stable permission model.

Do not scatter role-name comparisons throughout the application.

## 5. Suggested Structure

```text
src/
├── app/
│   ├── (auth)/
│   │   └── login/
│   │       └── page.tsx
│   ├── (protected)/
│   │   ├── layout.tsx
│   │   └── dashboard/
│   │       └── page.tsx
│   └── api/
├── components/
│   └── auth/
│       ├── login-form.tsx
│       └── permission-guard.tsx
├── features/
│   └── auth/
│       ├── components/
│       ├── hooks/
│       ├── services/
│       ├── types/
│       └── utils/
└── lib/
    └── auth/
        ├── permissions.ts
        └── session.ts
```

This structure is illustrative.

Adapt it to the framework, authentication provider and existing application architecture.

## 6. Authentication Flow

A typical authentication flow:

1. User submits login credentials.
1. Application sends credentials securely to the authentication service.
1. Server validates credentials.
1. Server creates an authenticated session.
1. Session information is returned or stored securely.
1. Application retrieves the authenticated user.
1. User accesses permitted application routes.
1. Logout invalidates the session.

The exact flow depends on the authentication architecture.

Never assume a successful frontend form submission means authentication succeeded.

## 7. Login Form

Keep login presentation and authentication responsibilities separated.

Example:

```tsx
"use client";

import { useState } from "react";

type LoginFormProps = {
  onSubmit: (credentials: { email: string; password: string }) => Promise<void>;
};

export function LoginForm({ onSubmit }: LoginFormProps) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setLoading(true);
    setError(null);

    try {
      await onSubmit({ email, password });
    } catch {
      setError("Unable to sign in. Check your credentials.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="email">Email</label>
      <input
        id="email"
        name="email"
        type="email"
        autoComplete="username"
        value={email}
        onChange={(event) => setEmail(event.target.value)}
        required
      />

      <label htmlFor="password">Password</label>
      <input
        id="password"
        name="password"
        type="password"
        autoComplete="current-password"
        value={password}
        onChange={(event) => setPassword(event.target.value)}
        required
      />

      {error && <p role="alert">{error}</p>}

      <button type="submit" disabled={loading}>
        {loading ? "Signing in..." : "Sign in"}
      </button>
    </form>
  );
}
```

This is a presentation example.

The parent or feature service should perform the actual authentication request.

A production implementation should also consider:

- Runtime input validation.
- Rate limiting on the server.
- Generic authentication failure messages.
- Password manager compatibility.
- Accessible validation feedback.
- CSRF protection where applicable.

## 8. Session Management

Choose session management according to the backend and authentication provider.

Common approaches:

- Server-managed sessions.
- Secure session cookies.
- OAuth access and refresh tokens.
- Managed authentication provider sessions.

For browser applications, prefer secure, HttpOnly cookies when using a compatible server-managed session architecture.

Cookie security attributes should be configured appropriately:

- HttpOnly.
- Secure.
- SameSite.
- Appropriate Path and Domain.
- Appropriate expiration.

Do not assume cookie configuration alone solves every session security concern.

## 9. Token Storage

Understand the trade-offs before choosing token storage.

| Storage | Considerations |
| --------------- | --------------------------------------------------------------------------- |
| HttpOnly cookie | Not directly accessible to JavaScript; requires appropriate CSRF protection |
| localStorage | Accessible to JavaScript; increases token exposure during XSS |
| sessionStorage | JavaScript-accessible and limited to the tab session |
| In-memory | Avoids persistent browser storage but requires lifecycle handling |

Do not store sensitive authentication tokens in browser storage without understanding the threat model.

Avoid inventing a token-refresh architecture when the existing backend already manages sessions.

## 10. Authenticated User

Define a clear user contract.

```ts
export type AuthenticatedUser = {
  id: string;
  email: string;
  roles: string[];
  permissions: string[];
};
```

This is an illustrative frontend type.

The application must obtain trusted identity and authorization data from the server.

Never treat values stored in localStorage, URL parameters or client-controlled state as authoritative permissions.

## 11. Permission Utilities

Centralize frontend permission checks.

```ts
export function hasPermission(
  userPermissions: readonly string[],
  requiredPermission: string,
): boolean {
  return userPermissions.includes(requiredPermission);
}
```

Usage:

```tsx
{
  hasPermission(user.permissions, "reports:read") && <ReportsLink />;
}
```

This controls presentation only.

The backend must independently validate every protected operation.

## 12. Protected Routes

Protected navigation should provide a good user experience.

Possible behaviors:

- Show a loading state while the session is checked.
- Redirect unauthenticated users to login.
- Preserve a safe return destination.
- Show an unauthorized page for authenticated users without permission.

Do not trust a client-side route guard as the security boundary.

Protect data access and server operations independently.

## 13. Next.js Server-Side Protection

In Next.js App Router applications:

- Read sessions using server-side mechanisms.
- Protect server-rendered pages where appropriate.
- Verify permissions in Route Handlers.
- Verify permissions in Server Actions.
- Avoid exposing private session data to Client Components.
- Treat Proxy or middleware checks as an additional layer, not the only authorization control.

Illustrative authorization helper:

```ts
// src/lib/auth/authorization.ts

import "server-only";

import { getCurrentUser } from "./session";

export async function requirePermission(permission: string) {
  const user = await getCurrentUser();

  if (!user) {
    throw new Error("UNAUTHENTICATED");
  }

  if (!user.permissions.includes(permission)) {
    throw new Error("FORBIDDEN");
  }

  return user;
}
```

`getCurrentUser()` is an application-specific server function and must be implemented using the actual authentication provider.

Use explicit application error handling rather than exposing internal exceptions directly to users.

## 14. Backend Authorization

Every protected backend operation must enforce authorization.

For example:

```ts
// Illustrative backend pseudocode

async function updateCustomer(request, response) {
  const user = await authenticateRequest(request);

  if (!user) {
    return response.status(401).json({
      message: "Unauthenticated",
    });
  }

  const allowed = await authorize(user, "customers:update");

  if (!allowed) {
    return response.status(403).json({
      message: "Forbidden",
    });
  }

  // Validate input and apply resource-level access rules.
}
```

The function names above are placeholders for backend implementation.

Also verify resource ownership, tenant boundaries and record-level permissions where required.

A valid role does not automatically grant access to every record.

## 15. Logout

Logout should invalidate the actual server session or authentication-provider session.

Consider:

- Clearing the session cookie.
- Revoking refresh tokens when supported.
- Clearing relevant client authentication state.
- Clearing sensitive cached data.
- Redirecting to a safe public route.

Do not only clear the frontend user state while leaving the server session active.

## 16. Expired Sessions

Handle expired sessions predictably.

Consider:

- Redirecting to login.
- Showing an appropriate session-expired message.
- Preventing repeated redirect loops.
- Clearing stale authentication state.
- Retrying requests only when safe.

Do not automatically retry non-idempotent operations without understanding their execution status.

## 17. OAuth and OpenID Connect

When integrating an external identity provider:

- Understand OAuth 2.0 and OpenID Connect responsibilities.
- Use Authorization Code Flow with PKCE where appropriate.
- Validate redirect destinations.
- Validate issuer, audience and token claims on the server.
- Use the provider's current recommended integration.
- Handle login cancellation and callback errors.
- Protect against CSRF and login-related attacks.

Do not implement cryptographic token validation manually when a maintained, appropriate library is available.

## 18. Additional Authentication Features

Depending on application requirements, consider:

- Password recovery.
- Email verification.
- Multi-factor authentication.
- Session revocation.
- Account lockout policies.
- Organization membership.
- SSO.
- Audit events.

Do not add authentication features that the product does not require.

## 19. Existing Authentication Changes

When working on an existing application:

1. Identify the current authentication provider.
1. Inspect session creation and validation.
1. Trace the API request flow.
1. Find route and server-side protection.
1. Review role and permission definitions.
1. Inspect token and cookie handling.
1. Check existing authorization tests.
1. Make the smallest safe change.
1. Verify both allowed and denied operations.

Do not replace an existing authentication system merely to match this example.

## 20. Testing

Test important security and user flows.

### Authentication

- Successful login.
- Invalid credentials.
- Expired session.
- Logout.
- Session restoration.
- Login callback failure.

### Authorization

- Unauthenticated access.
- Authenticated access.
- Allowed permission.
- Denied permission.
- Direct API access.
- Resource ownership.
- Cross-tenant access where applicable.

### UI

- Loading state.
- Login errors.
- Protected navigation.
- Unauthorized state.
- Accessible forms.

Test backend authorization independently of frontend visibility.

## 21. Common Anti-Patterns

Avoid:

- Treating authentication and authorization as the same thing.
- Trusting client-side roles.
- Protecting only navigation.
- Storing sensitive tokens without considering XSS.
- Assuming CORS provides authentication.
- Assuming SameSite cookies solve every CSRF scenario.
- Exposing secrets to Client Components.
- Returning sensitive error details.
- Replacing working authentication architecture unnecessarily.
- Duplicating permission logic across components.
- Skipping resource-level authorization.
- Building custom cryptographic authentication mechanisms without a justified need.

## 22. Review Checklist

### Authentication

- [ ] Login flow works.
- [ ] Session handling is secure.
- [ ] Logout invalidates the session.
- [ ] Expired sessions are handled.
- [ ] Sensitive tokens are protected.

### Authorization

- [ ] Permissions are clearly defined.
- [ ] Frontend checks are presentation-only.
- [ ] Backend authorization is enforced.
- [ ] Resource-level access is validated.
- [ ] Unauthorized operations are rejected.

### Integration

- [ ] Existing authentication architecture is understood.
- [ ] API contracts are respected.
- [ ] Error states are handled.
- [ ] Environment configuration is correct.

### Verification

- [ ] Authentication tests pass.
- [ ] Authorization tests pass.
- [ ] Direct API access is tested.
- [ ] TypeScript and lint checks pass.
- [ ] Production build succeeds.

## 23. Related References

- `../../references/authentication-and-authorization.md`
- `../../references/api-integration.md`
- `../../references/frontend-security.md`
- `../../references/environment-configuration.md`
- `../../references/state-management.md`
- `../../references/nextjs-engineering.md`
- `../../references/accessibility-and-wcag.md`
- `../../references/testing-strategy.md`
- `../../references/anti-ai-slop-and-engineering-quality.md`

## 24. Official Resources

- Next.js Authentication: https://nextjs.org/docs/app/guides/authentication
- OWASP Authentication Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
- OWASP Authorization Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
- OWASP Session Management: https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
- OAuth 2.0 Security Best Current Practice: https://www.rfc-editor.org/rfc/rfc9700
- OpenID Connect: https://openid.net/developers/how-connect-works/
