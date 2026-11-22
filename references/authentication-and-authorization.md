# Authentication and Authorization

## 1. Purpose

Define standards for implementing, modifying, debugging and maintaining frontend authentication and authorization systems.

Support:

- Login and logout.
- User registration.
- Email verification.
- Password recovery and reset.
- Session management.
- Token-based authentication.
- Cookie-based authentication.
- Role-based access control (RBAC).
- Permission-based access control.
- Protected routes.
- Account and profile management.
- Multi-factor authentication.
- Frontend/backend authorization boundaries.
- Authentication error handling.

The objective is to build secure, predictable authentication experiences while keeping authorization enforcement on trusted backend systems.

## 2. Core Concepts

Understand the difference between authentication and authorization.

### Authentication

Authentication determines who the user is.

Examples:

- Email and password login.
- OAuth login.
- Social login.
- Multi-factor authentication.
- Session verification.

### Authorization

Authorization determines what an authenticated user is allowed to do.

Examples:

- View a dashboard.
- Create a record.
- Edit a customer.
- Delete a user.
- Access administrative functionality.

Authentication does not automatically grant permission to access every resource.

## 3. Inspect Before Implementation

Before implementing or modifying authentication:

1. Inspect the existing authentication architecture.
1. Identify the backend authentication mechanism.
1. Check the framework and router.
1. Review installed authentication libraries.
1. Identify session and token storage.
1. Inspect API client configuration.
1. Review login, logout and registration flows.
1. Understand existing roles and permissions.
1. Inspect protected routes and layouts.
1. Review environment variables and deployment configuration.

For existing projects, preserve the current authentication architecture where possible.

Do not introduce a second authentication provider or replace working authentication without a clear reason.

Never invent backend endpoints, token formats, cookie names or permission contracts.

## 4. Authentication Architecture

A typical frontend authentication flow:

```text
User
  |
  v
Frontend Login Form
  |
  v
Authentication API
  |
  v
Backend Validation
  |
  v
Session or Token Issued
  |
  v
Frontend Receives Result
  |
  v
Authenticated Application
```

The exact implementation depends on the backend.

Possible authentication mechanisms:

- Server-managed sessions.
- Secure cookies.
- Access and refresh tokens.
- OAuth 2.0 / OpenID Connect.
- External identity providers.

Do not mix authentication mechanisms without understanding the backend requirements.

## 5. Login and Registration

Authentication forms should provide:

- Clear labels.
- Appropriate input types.
- Validation.
- Loading states.
- Error feedback.
- Keyboard accessibility.
- Password visibility controls where useful.
- Appropriate autocomplete attributes.

Example:

```tsx
<input
  type="email"
  name="email"
  autoComplete="email"
  required
/>

<input
  type="password"
  name="password"
  autoComplete="current-password"
  required
/>
```

For registration, use appropriate autocomplete values such as `new-password`.

Guidelines:

- Validate input before submission.
- Treat backend validation as authoritative.
- Prevent duplicate submissions.
- Preserve user input when safe.
- Avoid exposing sensitive information in error messages.
- Do not log passwords or credentials.

## 6. Password Handling

Passwords must be handled carefully.

Frontend guidelines:

- Never store passwords in local storage.
- Never store passwords in session storage.
- Never include passwords in URLs.
- Never log passwords.
- Use HTTPS in production.
- Avoid unnecessary password persistence.
- Clear sensitive form state when appropriate.
- Use appropriate password autocomplete attributes.

Password hashing, password verification and password storage belong on the backend.

Never implement password hashing as a replacement for secure backend authentication.

## 7. Session Management

Understand how the application establishes and maintains authenticated sessions.

Possible approaches:

- Server-side sessions.
- Secure session cookies.
- Access and refresh token pairs.
- External identity provider sessions.

Consider:

- Session expiration.
- Session renewal.
- Logout.
- Multiple browser tabs.
- Account switching.
- Revoked sessions.
- Expired credentials.
- Network failures.

Do not assume a session is valid merely because a user object exists in frontend state.

The backend must remain authoritative.

## 8. Token Storage

Token storage is a security-sensitive decision.

### HttpOnly cookies

HttpOnly cookies cannot be read through ordinary JavaScript.

When appropriately configured, they can reduce the risk of JavaScript-based token theft.

Important cookie attributes include:

- `HttpOnly`
- `Secure`
- `SameSite`
- `Path`
- Appropriate expiration.

Cookie configuration must match the application's domain and deployment architecture.

Cookie-based authentication still requires appropriate CSRF protection.

### Local storage

Avoid storing long-lived authentication credentials in local storage when a safer architecture is available.

JavaScript running in the same origin can access local storage.

An XSS vulnerability can expose stored credentials.

### In-memory storage

In-memory storage avoids persistent browser storage but has lifecycle and refresh limitations.

Choose the approach based on the actual authentication architecture and threat model.

Do not copy a token storage strategy from another project without evaluating its security implications.

## 9. Access and Refresh Tokens

When the backend uses token-based authentication, understand:

- Access token lifetime.
- Refresh token lifetime.
- Refresh endpoint behavior.
- Token rotation.
- Revocation.
- Expiration handling.
- Concurrent refresh requests.

Guidelines:

- Do not expose tokens in URLs.
- Do not log token values.
- Handle expired access tokens deliberately.
- Prevent multiple simultaneous refresh operations when appropriate.
- Avoid infinite refresh loops.
- Handle failed refresh operations.
- Clear invalid authentication state when required.

Never assume every HTTP 401 response should automatically trigger a refresh.

The backend's authentication contract determines the correct behavior.

## 10. API Client Integration

Centralize authentication behavior in the existing API client.

Common responsibilities:

- Base URL configuration.
- Credentials handling.
- Authentication headers where required.
- Request serialization.
- Response parsing.
- Error normalization.
- Session expiration handling.

Avoid implementing independent authentication logic in every feature.

Do not expose secrets through frontend environment variables.

In frameworks such as Next.js, public environment variables may be included in client-side bundles.

Only expose values intended to be public.

## 11. Logout

Logout should follow the backend's authentication mechanism.

Consider:

- Invalidating the server session.
- Revoking refresh credentials when supported.
- Clearing local authentication state.
- Resetting user-specific cached data.
- Closing or invalidating authenticated connections.
- Redirecting to an appropriate page.

Do not treat a frontend redirect as proof that the server session has been invalidated.

Handle logout failures according to the application's security requirements.

Avoid leaving private user data visible after account switching.

## 12. Authentication State

Keep authentication state consistent.

Possible information:

- Current user.
- Authentication status.
- Session status.
- Loading state.
- User roles.
- User permissions.

Avoid storing duplicate copies of authentication data in multiple state systems.

Consider these states:

```text
unknown
  |
  v
checking
  |
  +----> authenticated
  |
  +----> unauthenticated
  |
  +----> error
```

Do not briefly render protected content while authentication status is still being determined.

Use the appropriate server-side or client-side authentication checks for the framework.

## 13. Protected Routes

Protected routes prevent unauthenticated users from accessing authenticated application pages through the intended navigation flow.

Examples:

- Dashboard.
- Account settings.
- Internal CRM.
- User management.
- Administrative pages.

Guidelines:

- Check authentication before exposing protected content.
- Preserve intended redirect destinations safely.
- Provide appropriate loading states.
- Redirect unauthenticated users to the correct authentication page.
- Handle expired sessions.
- Avoid redirect loops.
- Support direct URL navigation.

Frontend route protection improves user experience.

It is not a security boundary.

The backend must independently validate authentication and authorization for protected resources.

## 14. Role-Based Access Control (RBAC)

RBAC determines access according to assigned roles.

Example roles:

- ADMIN.
- MANAGER.
- EMPLOYEE.
- VIEWER.

A role can grant a collection of permissions.

Example:

```text
ADMIN
  - users:read
  - users:create
  - users:update
  - users:delete

EMPLOYEE
  - users:read
  - customers:read
  - customers:update
```

These are illustrative permissions, not a required application contract.

Guidelines:

- Use the backend's actual role definitions.
- Avoid inventing role names.
- Keep role handling consistent.
- Understand whether users can have multiple roles.
- Avoid scattering role comparisons throughout components.
- Do not assume role names imply identical permissions across products.

## 15. Permission-Based Access Control

Permission checks are often more flexible than role-only checks.

Example:

```tsx
interface UserPermissions {
  canReadUsers: boolean;
  canCreateUsers: boolean;
  canUpdateUsers: boolean;
  canDeleteUsers: boolean;
}
```

An alternative is a permission list:

```tsx
type Permission =
  | "users:read"
  | "users:create"
  | "users:update"
  | "users:delete";
```

Choose a model consistent with the backend.

Centralize permission checks where appropriate.

Avoid duplicating permission logic across pages and components.

## 16. UI-Level Authorization

The frontend may use permissions to control:

- Navigation visibility.
- Button visibility.
- Action availability.
- Page access.
- Read-only states.
- Feature availability.

Example:

```tsx
if (!canEditUser) {
  return <ReadOnlyUserDetails />;
}

return <UserEditor />;
```

The frontend should provide a useful experience for users without access.

However:

- Hidden buttons do not secure APIs.
- Disabled controls do not secure APIs.
- Protected routes do not secure backend resources.
- Client-side role checks can be manipulated.

The backend must authorize every protected operation.

## 17. Multi-Tenant Applications

Some applications separate data by:

- Organization.
- Workspace.
- Company.
- Tenant.
- Project.

Consider:

- Current tenant.
- Membership.
- Tenant-specific roles.
- Resource ownership.
- Tenant switching.
- Data isolation.
- Tenant-specific navigation.

Never assume that a user can access every organization associated with their account.

Do not rely on a frontend tenant identifier as proof of authorization.

The backend must validate tenant membership and resource access.

## 18. OAuth and OpenID Connect

OAuth 2.0 and OpenID Connect support delegated authorization and identity.

Understand the distinction:

- OAuth 2.0 is an authorization framework.
- OpenID Connect adds an identity layer.

For browser-based applications, use an established provider SDK or a correctly implemented authorization code flow with PKCE when appropriate.

Guidelines:

- Validate redirect URIs.
- Use `state` to protect authorization flows against CSRF.
- Use `nonce` where required by the OpenID Connect flow.
- Use PKCE where appropriate.
- Validate issuer, audience and token claims on the trusted side.
- Do not expose client secrets in browser code.
- Handle cancellation and provider errors.
- Validate redirect destinations.

Do not implement a custom OAuth protocol flow when a maintained provider integration is suitable.

## 19. Multi-Factor Authentication

MFA adds another verification step.

Possible methods include:

- Authenticator applications.
- Passkeys.
- Security keys.
- Email verification codes.
- SMS codes where appropriate.

Frontend responsibilities:

- Present the correct verification flow.
- Handle challenge states.
- Support retry and expiration.
- Provide accessible feedback.
- Avoid exposing verification secrets.
- Handle recovery flows.

The backend or identity provider must validate MFA challenges.

Do not treat a frontend-entered verification code as authenticated until the trusted service confirms it.

## 20. Password Recovery and Email Verification

Support appropriate flows for:

- Forgot password.
- Password reset.
- Email verification.
- Verification resend.
- Expired links.
- Invalid tokens.

Guidelines:

- Use backend-generated verification links or tokens.
- Avoid exposing tokens in application logs.
- Handle expired and invalid links.
- Show understandable status messages.
- Avoid account enumeration through overly specific recovery responses.
- Do not assume an email address is verified because a frontend form was submitted.

Follow the backend's actual API contract.

## 21. Next.js Authentication Considerations

For Next.js App Router projects:

- Understand Server Components and Client Components.
- Perform sensitive session checks in trusted server-side code.
- Avoid exposing protected data before authorization.
- Use server-side data access patterns where appropriate.
- Protect Route Handlers and Server Actions.
- Avoid relying only on client-side layouts or navigation checks.
- Understand the installed Next.js version and its routing and request-interception APIs.

A layout-level redirect can improve navigation behavior, but it does not replace authorization at the data access or mutation boundary.

Do not turn the entire application into a Client Component just to manage authentication state.

## 22. React SPA Authentication Considerations

For React single-page applications:

- Centralize authentication state.
- Reuse the existing API client.
- Handle initial session checks.
- Manage protected routes.
- Handle expired sessions.
- Reset user-specific state on logout.
- Avoid storing sensitive data in persistent client storage.
- Prevent redirect loops.

Use the existing router and state management conventions.

Do not introduce a new state library solely for authentication.

## 23. Security Requirements

Follow these principles:

- Use HTTPS in production.
- Validate authentication on the backend.
- Enforce authorization on every protected operation.
- Protect cookie-based flows against CSRF.
- Prevent XSS.
- Validate and sanitize untrusted input appropriately.
- Protect authentication endpoints with appropriate rate limits.
- Avoid credential leakage.
- Do not expose private environment variables.
- Use secure cookie attributes.
- Handle session expiration.
- Validate redirect destinations.
- Avoid sensitive information in logs.
- Avoid revealing unnecessary account information.

Review the actual authentication architecture rather than applying isolated frontend fixes to backend security problems.

## 24. Existing Authentication Modification

When changing an existing authentication system:

1. Identify the current authentication provider.
1. Trace login and logout flows.
1. Inspect session and token handling.
1. Identify protected routes.
1. Review API authentication behavior.
1. Inspect role and permission definitions.
1. Find all affected consumers.
1. Understand security implications.
1. Make the smallest safe change.
1. Test success and failure paths.

Preserve existing API contracts where possible.

Do not rewrite authentication just to change a login screen.

Do not silently change token storage, cookie configuration or session lifetime.

## 25. Testing

Test authentication at multiple levels.

### Component tests

- Login form validation.
- Password visibility.
- Loading states.
- Error messages.
- Disabled actions.
- Accessible labels.

### Integration tests

- Login API integration.
- Logout behavior.
- Session restoration.
- Token refresh where applicable.
- Permission-based UI.
- Protected navigation.
- Authentication error handling.

### End-to-end tests

- Login.
- Logout.
- Registration.
- Password recovery.
- Direct protected-route access.
- Session expiration.
- Role-specific workflows.
- Unauthorized operations.

### Security verification

- Backend rejects unauthenticated requests.
- Backend rejects unauthorized operations.
- Client-side permission manipulation does not grant access.
- Sensitive credentials are not exposed.
- Redirect handling is safe.

Do not treat frontend-only tests as proof of backend authorization security.

## 26. Common Anti-Patterns

Avoid:

- Confusing authentication with authorization.
- Storing passwords in browser storage.
- Exposing secrets in frontend code.
- Assuming hidden buttons provide security.
- Trusting frontend role checks.
- Duplicating authentication state.
- Inventing backend permission contracts.
- Implementing custom OAuth flows unnecessarily.
- Ignoring session expiration.
- Infinite refresh retries.
- Leaving private cached data after logout.
- Redirect loops.
- Replacing working authentication without a reason.
- Claiming a frontend-only implementation is secure.

## 27. Decision Workflow

Before implementing authentication or authorization:

1. Inspect the current authentication architecture.
1. Identify the trusted authentication provider.
1. Understand the session or token mechanism.
1. Confirm the backend API contract.
1. Understand the authorization model.
1. Define the required frontend behavior.
1. Implement the appropriate user experience.
1. Enforce backend security independently.
1. Test authentication and authorization paths.
1. Verify existing user workflows.

Security-sensitive decisions must be based on the actual system, not assumptions.

## 28. Review Checklist

### Authentication

- [ ] Login and logout work.
- [ ] Session state is consistent.
- [ ] Expiration is handled.
- [ ] Credentials are not exposed.
- [ ] Password recovery is handled.

### Authorization

- [ ] Roles and permissions match the backend.
- [ ] Protected routes behave correctly.
- [ ] UI actions reflect permissions.
- [ ] Backend authorization remains authoritative.
- [ ] Tenant boundaries are respected where applicable.

### Security

- [ ] HTTPS is used in production.
- [ ] Cookie and token handling is appropriate.
- [ ] CSRF and XSS risks are considered.
- [ ] Secrets remain server-side.
- [ ] Redirect destinations are validated.

### Verification

- [ ] Relevant tests pass.
- [ ] Failure paths are tested.
- [ ] Existing authentication flows remain functional.
- [ ] No unauthorized access is introduced.

## 29. Related References

- architecture-and-project-structure.md
- nextjs-engineering.md
- api-integration.md
- environment-configuration.md
- frontend-security.md
- forms-and-validation.md
- state-management.md
- testing-strategy.md

## 30. Official Resources

- OWASP Authentication Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
- OWASP Session Management Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
- OWASP Authorization Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
- OAuth 2.0: https://oauth.net/2/
- OpenID Connect: https://openid.net/developers/how-connect-works/
- Auth.js: https://authjs.dev/
- Next.js Authentication Guide: https://nextjs.org/docs/app/guides/authentication
- MDN HTTP Cookies: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies
