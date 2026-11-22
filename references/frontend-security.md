# Frontend Security

## 1. Purpose

Define security standards for building, modifying, reviewing and maintaining secure frontend applications.

The agent must understand frontend security risks and recognize where protection must be enforced by the backend, infrastructure or browser.

This reference covers:

- OWASP security principles.
- Cross-Site Scripting (XSS).
- Cross-Site Request Forgery (CSRF).
- Authentication and authorization.
- Secure session handling.
- Browser storage.
- API communication.
- Content Security Policy (CSP).
- CORS.
- Input validation and output encoding.
- File uploads and downloads.
- Dependency and supply-chain security.
- Environment variables and secrets.
- Secure redirects and navigation.
- Security headers.
- Error handling and logging.
- Security testing.

Security must be considered throughout development, not added as a final cosmetic layer.

## 2. Inspect Before Making Security Changes

Before modifying an existing application:

1. Inspect the framework and installed versions.
1. Understand the authentication architecture.
1. Identify where sessions and tokens are stored.
1. Inspect API client configuration.
1. Review route protection and authorization.
1. Inspect environment variable handling.
1. Identify security-related middleware and headers.
1. Review existing dependencies.
1. Understand frontend and backend responsibilities.
1. Check existing security tests and deployment configuration.

For existing projects:

- Preserve working security mechanisms.
- Avoid introducing a second authentication system.
- Do not weaken existing protections.
- Do not remove security headers without justification.
- Avoid changing session behavior without understanding its impact.
- Investigate security issues at their actual trust boundary.

Do not assume that frontend code is the only place where a vulnerability must be fixed.

## 3. Security Principles

Follow these principles:

### Defense in Depth

Use multiple appropriate security controls rather than relying on a single mechanism.

### Least Privilege

Grant only the permissions required for a user or operation.

### Secure Defaults

Prefer restrictive and secure defaults.

### Fail Securely

When security checks fail, do not silently grant access.

### Never Trust Client Input

Treat data from users, URLs, browser storage, APIs and external services as untrusted.

### Server-Side Enforcement

The backend must enforce authentication, authorization and access to protected resources.

Frontend checks improve user experience but do not establish security boundaries.

### Minimize Sensitive Data

Avoid collecting, storing, transmitting or logging sensitive information unnecessarily.

## 4. OWASP Awareness

Use OWASP resources to understand common application security risks.

Relevant areas include:

- Broken access control.
- Cryptographic failures.
- Injection.
- Insecure design.
- Security misconfiguration.
- Vulnerable and outdated components.
- Identification and authentication failures.
- Security logging and monitoring failures.
- Cross-site scripting.
- Client-side security risks.

Use the OWASP Top 10 and OWASP Cheat Sheet Series as references.

Do not assume that a checklist alone proves an application is secure.

Official resources:

- https://owasp.org/www-project-top-ten/
- https://cheatsheetseries.owasp.org/
- https://owasp.org/www-project-top-10-client-side-security-risks/

## 5. Cross-Site Scripting (XSS)

XSS occurs when untrusted content is interpreted as executable browser content.

Common categories:

- Stored XSS.
- Reflected XSS.
- DOM-based XSS.

### Prevention

- Prefer framework-provided rendering and escaping.
- Avoid inserting untrusted HTML.
- Avoid unsafe DOM manipulation.
- Validate and sanitize content when HTML is genuinely required.
- Use a well-maintained HTML sanitization library when necessary.
- Apply an appropriate Content Security Policy.
- Review third-party scripts.
- Avoid unsafe dynamic script construction.

### React Considerations

React escapes text content by default.

However, unsafe patterns can still introduce XSS.

Avoid using:

```tsx
<div dangerouslySetInnerHTML={{ __html: userContent }} />
```

unless the HTML is trusted or has been sanitized with an appropriate, well-maintained sanitizer.

Never assume TypeScript types or frontend validation make HTML safe.

### DOM Security

Be careful with:

- `innerHTML`.
- `outerHTML`.
- `document.write`.
- `eval`.
- `new Function`.
- Dynamic script insertion.
- Untrusted URL assignment.
- Unsafe HTML parsing.

Do not use these mechanisms with untrusted content.

Prefer safe DOM APIs and framework rendering.

## 6. Cross-Site Request Forgery (CSRF)

CSRF attempts to make a user's browser perform an unwanted authenticated action.

It is particularly relevant when authentication relies on cookies that browsers automatically attach to requests.

Possible protections include:

- CSRF tokens.
- SameSite cookie configuration.
- Origin validation.
- Referer validation where appropriate.
- Restricting state-changing operations to appropriate HTTP methods.

### Important Considerations

- `SameSite=Lax` is useful but is not a universal CSRF solution.
- `SameSite=None` requires `Secure`.
- CORS is not a replacement for CSRF protection.
- A custom request header can help when the server strictly enforces the relevant origin and CORS policy.
- Protect sensitive state-changing endpoints according to the backend's authentication model.

For cookie-authenticated applications, coordinate CSRF protection with the backend.

Do not implement a frontend-only CSRF token check and assume the application is protected.

## 7. Authentication and Session Security

Authentication establishes who the user is.

Use established authentication systems and secure session management.

Consider:

- Secure login.
- Logout.
- Session expiration.
- Session renewal.
- Password recovery.
- Email verification.
- Multi-factor authentication.
- OAuth 2.0 and OpenID Connect.
- Secure session invalidation.

### Session Cookies

For browser-based session authentication, prefer appropriately configured cookies where the architecture supports them.

Important attributes:

- `HttpOnly`.
- `Secure`.
- `SameSite`.
- Appropriate `Path`.
- Appropriate `Domain`.
- Appropriate expiration.

Example:

```http
Set-Cookie: session=VALUE; HttpOnly; Secure; SameSite=Lax; Path=/
```

The backend should issue and manage secure session cookies.

### Token Storage

Do not automatically store authentication tokens in localStorage.

JavaScript-accessible storage can expose tokens to XSS.

Consider the application's architecture and threat model:

- HttpOnly cookies.
- In-memory token storage.
- Secure session-based authentication.
- Refresh token rotation where applicable.

Never store sensitive credentials in URLs.

Do not invent token refresh behavior or assume that an access token is valid indefinitely.

See `authentication-and-authorization.md`.

## 8. Authorization and Access Control

Frontend route guards and hidden buttons are not sufficient authorization.

The backend must verify permissions for every protected operation.

Examples:

- User ownership.
- Role-based access control.
- Resource-level permissions.
- Organization or tenant boundaries.
- Administrative operations.

Frontend responsibilities:

- Hide unavailable actions when appropriate.
- Display permission-aware navigation.
- Handle unauthorized responses.
- Avoid exposing unnecessary protected data.
- Provide understandable access-denied states.

Backend responsibilities:

- Verify the authenticated identity.
- Verify permissions.
- Validate resource ownership.
- Enforce tenant boundaries.
- Reject unauthorized operations.

Never rely on a role or permission value stored only in browser storage.

## 9. Browser Storage Security

Understand the differences between browser storage mechanisms.

| Storage | JavaScript accessible | Typical use |
| --------------- | --------------------- | --------------------------------------- |
| localStorage | Yes | Non-sensitive persistent preferences |
| sessionStorage | Yes | Non-sensitive session-scoped state |
| Cookies | Depends on attributes | Session and cookie-based authentication |
| IndexedDB | Yes | Structured client-side data |
| In-memory state | Yes | Temporary application state |

Guidelines:

- Do not store passwords in browser storage.
- Avoid storing sensitive personal data unnecessarily.
- Avoid storing long-lived authentication credentials in JavaScript-accessible storage.
- Do not treat browser storage as trusted.
- Validate stored values before using them.
- Handle malformed or unavailable storage safely.
- Clear appropriate application data on logout.

Remember that client-side encryption does not automatically protect data when the application itself can access the decryption key.

## 10. Input Validation and Output Encoding

Validate untrusted data at the appropriate boundaries.

### Frontend Validation

Useful for:

- Better user experience.
- Early feedback.
- Form constraints.
- Basic format checking.

### Backend Validation

Required for:

- Business rules.
- Authorization-sensitive operations.
- Database writes.
- Security-sensitive input.
- API contracts.

Never rely solely on frontend validation.

Use runtime schemas where appropriate.

Validate:

- Data types.
- Required fields.
- Length limits.
- Allowed values.
- Numeric ranges.
- File types and sizes.
- URL formats.
- Identifiers.

Output encoding must match the context in which data is rendered.

Do not assume that a value safe for plain text is also safe inside HTML, JavaScript, CSS or a URL.

See `forms-and-validation.md`.

## 11. Content Security Policy (CSP)

CSP is a browser security mechanism that restricts which resources a page can load or execute.

It can help reduce the impact of certain XSS attacks.

Possible directives:

- `default-src`.
- `script-src`.
- `style-src`.
- `img-src`.
- `font-src`.
- `connect-src`.
- `frame-src`.
- `object-src`.
- `base-uri`.
- `form-action`.
- `frame-ancestors`.

Example policy concept:

```http
Content-Security-Policy:
  default-src 'self';
  object-src 'none';
  base-uri 'self';
  frame-ancestors 'none';
```

This is an illustrative starting point, not a universal production policy.

### Guidelines

- Identify required external resources.
- Avoid broad wildcard permissions.
- Avoid `unsafe-eval`.
- Avoid `unsafe-inline` where a nonce or hash-based approach is practical.
- Use nonces or hashes where required by the framework.
- Test the policy before enforcing it.
- Consider report-only mode during rollout.
- Monitor violations.
- Avoid breaking legitimate application functionality.

For Next.js applications, follow the current framework guidance for CSP, nonce handling and rendering behavior.

Do not copy a generic CSP into production without checking the application's actual resource requirements.

## 12. Cross-Origin Resource Sharing (CORS)

CORS controls how browsers permit cross-origin requests.

It is enforced by browsers based on server response headers.

Important concepts:

- Allowed origins.
- Allowed methods.
- Allowed headers.
- Credentials.
- Preflight requests.
- Exposed response headers.

Security rules:

- Do not use unrestricted origins with credentialed requests.
- Do not treat CORS as authentication.
- Do not treat CORS as authorization.
- Configure allowed origins intentionally.
- Restrict methods and headers where appropriate.
- Coordinate frontend and backend configuration.

CORS must be configured on the server that handles the request.

A frontend application cannot independently grant itself permission to access another origin.

## 13. Secure API Communication

Use HTTPS for production application traffic.

Review:

- API base URLs.
- Authentication headers.
- Cookie behavior.
- Request methods.
- Error responses.
- Redirect handling.
- Content types.
- Data validation.
- Request timeouts.
- Retry behavior.

Avoid:

- Sending secrets to client-side APIs.
- Logging access tokens.
- Putting credentials in query parameters.
- Automatically retrying sensitive operations without considering idempotency.
- Trusting response data without validation.
- Exposing internal server errors to users.

Handle `401` and `403` responses appropriately.

Do not redirect users in a loop when authentication expires.

See `api-integration.md`.

## 14. URL and Redirect Security

Untrusted URLs can introduce phishing, open redirects and script execution risks.

Review:

- Redirect parameters.
- Return URLs.
- External links.
- Dynamic navigation.
- URL query parameters.
- Deep links.

Guidelines:

- Prefer relative internal paths.
- Validate external URLs against an appropriate allowlist.
- Reject dangerous URL schemes.
- Do not use arbitrary user-provided redirect destinations.
- Avoid placing sensitive information in URLs.
- Use safe link attributes when opening external pages in new tabs.

Example:

```tsx
<a href="https://example.com" target="_blank" rel="noopener noreferrer">
  External website
</a>
```

Do not blindly trust `returnUrl`, `redirect` or similar query parameters.

## 15. File Upload Security

Frontend checks improve usability but do not secure file uploads by themselves.

Consider:

- File size.
- Allowed extensions.
- MIME type.
- User permissions.
- Upload destination.
- File processing.
- Storage permissions.
- Malware scanning where appropriate.

Important:

- MIME types and extensions can be spoofed.
- The backend must validate actual file content.
- The backend should generate safe storage names.
- Do not trust client-provided file paths.
- Avoid rendering uploaded HTML or SVG as trusted content.
- Consider image processing and metadata removal where relevant.
- Enforce authorization for uploads and downloads.

For sensitive applications, consider private object storage and short-lived signed download URLs.

## 16. Third-Party Scripts and Dependencies

Third-party scripts execute in the application's browser context and may access data available to that context.

Before integrating external scripts:

1. Understand why they are needed.
1. Review the provider.
1. Check what data they access.
1. Evaluate permissions and tracking behavior.
1. Consider performance and privacy.
1. Use the smallest required integration.

For dependencies:

- Review package maintenance.
- Check known vulnerabilities.
- Avoid unnecessary dependencies.
- Keep dependencies updated appropriately.
- Review package lifecycle scripts when security-sensitive.
- Commit lockfiles.
- Use reproducible installation.
- Remove unused packages.
- Avoid untrusted packages with confusingly similar names.

Use automated dependency auditing where appropriate.

Do not blindly run automated dependency upgrades in production projects.

## 17. Environment Variables and Secrets

Separate public configuration from private secrets.

For Next.js:

- Variables prefixed with `NEXT_PUBLIC_` are intended to be exposed to the browser.
- Private environment variables must remain server-side.

For other frameworks, inspect their environment variable exposure rules.

Never expose:

- Database passwords.
- Private API keys.
- Signing secrets.
- Private OAuth client secrets.
- Service credentials.
- Internal infrastructure credentials.

Keep separate configuration for:

- Development.
- Staging.
- Production.

Do not commit `.env` files containing secrets.

Provide safe example configuration through `.env.example` with placeholder values only.

If a secret has been exposed, treat it as compromised and rotate it through the appropriate service.

See `environment-configuration.md`.

## 18. Next.js Security Boundaries

Next.js applications may contain both server-side and client-side code.

Understand the boundary before implementing sensitive functionality.

### Server-Side Code

Keep sensitive operations on the server:

- Secret access.
- Database access.
- Private API credentials.
- Authorization checks.
- Sensitive business logic.

### Client Components

Do not place private credentials or privileged server operations in Client Components.

Remember:

- Client-side code can be inspected by users.
- Client-side validation is not a security boundary.
- Server Actions require authorization checks.
- Route Handlers require appropriate authentication and authorization.
- Middleware or Proxy checks do not replace resource-level backend authorization.
- Server-rendered content must not expose sensitive data to unauthorized users.

Do not assume that a Server Component automatically makes every returned value safe.

Only return data the requesting user is authorized to receive.

## 19. Security Headers

Review the application's HTTP security headers.

Potential headers include:

- `Content-Security-Policy`.
- `Strict-Transport-Security`.
- `X-Content-Type-Options`.
- `Referrer-Policy`.
- `Permissions-Policy`.
- `frame-ancestors` through CSP.

Consider:

- HTTPS deployment.
- Reverse proxy configuration.
- Hosting provider behavior.
- Framework response configuration.
- External embedding requirements.

Avoid duplicating or conflicting header configuration across infrastructure and application code.

Do not set headers without understanding their browser behavior.

## 20. Error Handling and Logging

Security-sensitive information must not leak through errors or logs.

Avoid exposing:

- Stack traces to ordinary users.
- Database credentials.
- Access tokens.
- Session identifiers.
- Passwords.
- Internal API secrets.
- Private personal information.
- Sensitive request payloads.

Use meaningful user-facing messages.

Log appropriate diagnostic information through secure observability systems.

Redact sensitive values.

Do not silently swallow security-related failures.

See `observability-and-monitoring.md`.

## 21. Privacy and Data Handling

Consider what data the application collects and where it is stored.

Guidelines:

- Collect only necessary data.
- Avoid unnecessary browser persistence.
- Minimize third-party data sharing.
- Avoid sensitive information in analytics events.
- Avoid logging personal information unnecessarily.
- Apply appropriate retention rules.
- Provide clear user-facing privacy information where required.

Do not assume that frontend-only controls establish legal or regulatory compliance.

Consider applicable privacy requirements for the application's deployment regions and users.

## 22. Security Testing

Use appropriate security checks during development.

Possible tools and techniques:

- Dependency vulnerability auditing.
- Static analysis.
- ESLint security-related rules where appropriate.
- Type checking.
- OWASP ZAP.
- Browser security testing.
- CSP reporting.
- Manual XSS testing.
- Authentication and authorization tests.
- Secure cookie inspection.
- API access-control testing.

Test:

- Unauthorized access.
- Forbidden operations.
- Session expiration.
- CSRF behavior where relevant.
- XSS-sensitive rendering.
- Unsafe redirects.
- Invalid input.
- Upload restrictions.
- Sensitive data exposure.

Automated scans do not prove that an application is secure.

Use manual review for important trust boundaries and business permissions.

## 23. Existing Project Security Improvements

When improving security in an existing project:

1. Identify the actual vulnerability or risk.
1. Locate the relevant trust boundary.
1. Inspect frontend and backend responsibilities.
1. Review the current implementation.
1. Understand compatibility requirements.
1. Determine the smallest effective fix.
1. Add appropriate regression tests.
1. Avoid breaking legitimate workflows.
1. Run relevant security and functional checks.
1. Document any remaining limitations.

For security-sensitive changes:

- Do not weaken existing controls to fix unrelated problems.
- Do not replace authentication without a migration plan.
- Do not remove CSP restrictions simply to make a script work.
- Do not disable validation to bypass errors.
- Do not expose secrets to simplify integration.

If the actual vulnerability is in the backend or infrastructure, explain that and identify the required server-side change.

## 24. Common Security Anti-Patterns

Avoid:

- Storing passwords in browser storage.
- Treating hidden buttons as authorization.
- Trusting client-side validation.
- Exposing private API keys.
- Using unsafe HTML rendering.
- Allowing arbitrary redirects.
- Treating CORS as access control.
- Disabling CSP without justification.
- Logging credentials.
- Trusting file extensions alone.
- Using wildcard CORS with credentials.
- Hardcoding secrets.
- Ignoring dependency vulnerabilities.
- Returning sensitive data to unauthorized users.
- Assuming HTTPS alone prevents XSS or CSRF.

## 25. Security Decision Workflow

Before implementing security-related changes:

1. Identify the protected resource.
1. Identify the threat and trust boundary.
1. Determine whether the control belongs in the frontend, backend or infrastructure.
1. Inspect existing protections.
1. Select an appropriate security mechanism.
1. Check framework and browser compatibility.
1. Implement the smallest reliable change.
1. Add tests for important security behavior.
1. Verify the change.
1. Document remaining risks.

Do not claim complete security based on a limited frontend review.

## 26. Review Checklist

### Authentication and Authorization

- [ ] Authentication flow reviewed.
- [ ] Session handling is appropriate.
- [ ] Protected operations enforce server-side authorization.
- [ ] Logout and expiration are handled.
- [ ] Sensitive credentials are not exposed.

### Input and Output

- [ ] Untrusted input is validated.
- [ ] Output is safely rendered.
- [ ] Unsafe HTML usage is reviewed.
- [ ] URL and redirect handling is safe.
- [ ] Upload constraints are enforced by the backend.

### Browser and Network

- [ ] HTTPS is used in production.
- [ ] Cookie attributes are appropriate.
- [ ] CSRF protections are considered.
- [ ] CORS is configured intentionally.
- [ ] CSP is appropriate for the application.
- [ ] Security headers are reviewed.

### Dependencies and Configuration

- [ ] Dependencies are reviewed.
- [ ] Secrets remain server-side.
- [ ] Environment separation is respected.
- [ ] No secrets are committed.
- [ ] Error logs do not expose sensitive information.

### Verification

- [ ] Relevant security tests are executed.
- [ ] Important trust boundaries are reviewed.
- [ ] Functional regressions are checked.
- [ ] Unverified areas are disclosed.
- [ ] Remaining risks are documented.

## 27. Related References

- anti-ai-slop-and-engineering-quality.md
- authentication-and-authorization.md
- api-integration.md
- forms-and-validation.md
- environment-configuration.md
- accessibility-and-wcag.md
- testing-strategy.md
- package-selection-and-ecosystem.md
- observability-and-monitoring.md
- debugging-and-self-correction.md
- production-readiness.md

## 28. Official Resources

### OWASP

- https://owasp.org/www-project-top-ten/
- https://owasp.org/www-project-top-10-client-side-security-risks/
- https://cheatsheetseries.owasp.org/

### Browser Security

- MDN Web Security: https://developer.mozilla.org/en-US/docs/Web/Security
- MDN CSP: https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
- MDN CORS: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
- MDN Cookies: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies

### Framework Security

- Next.js Authentication: https://nextjs.org/docs/app/guides/authentication
- Next.js CSP: https://nextjs.org/docs/app/guides/content-security-policy
- React DOM: https://react.dev/reference/react-dom/components/common

### Testing and Dependencies

- OWASP ZAP: https://www.zaproxy.org/
- npm audit: https://docs.npmjs.com/cli/commands/npm-audit
- GitHub Dependabot: https://docs.github.com/en/code-security/dependabot

Always verify current official documentation against the installed framework and dependency versions.
