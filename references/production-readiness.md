# Production Readiness

## 1. Purpose

Define the standards an application should meet before being released to production.

Production readiness is not simply a successful build or a visually complete interface.

An application must be reliable, secure, accessible, maintainable, performant, observable and deployable.

This reference applies to:

- New frontend applications.
- Existing application improvements.
- Production releases.
- Major feature releases.
- Deployment preparation.
- Pre-release reviews.
- Technical audits.
- Production incident prevention.

The agent must evaluate the actual project and its requirements rather than blindly applying every checklist item.

## 2. Production Readiness Principles

Follow these principles:

1. Verify functionality before release.
1. Prioritize security and user data protection.
1. Preserve accessibility.
1. Measure performance.
1. Validate critical user journeys.
1. Keep environments separated.
1. Ensure errors are observable.
1. Prepare recovery procedures.
1. Avoid unnecessary infrastructure.
1. Report unresolved risks honestly.

A production-ready application is one whose important behaviors and operational requirements have been verified.

## 3. Inspect the Application

Before performing a production review, understand:

- Application purpose.
- Target users.
- Framework and runtime.
- Application architecture.
- Main user journeys.
- Authentication and authorization.
- API integrations.
- Database dependencies.
- External services.
- Environment configuration.
- Hosting platform.
- CI/CD workflows.
- Monitoring and logging.
- Existing tests.
- Current technical limitations.

For existing applications, inspect the actual implementation.

Do not assume that every feature is complete because it appears in the UI.

## 4. Functional Completeness

Verify that important features work as intended.

Check:

- Navigation.
- Forms.
- Authentication.
- Authorization.
- API integration.
- Search and filtering.
- Pagination.
- Data creation and editing.
- File uploads.
- Dialogs and overlays.
- Notifications.
- Settings.
- Responsive interactions.
- Empty states.
- Loading states.
- Error states.

### Functional UI Requirements

Every interactive element must have a meaningful behavior.

Avoid:

- Buttons without actions.
- Links pointing to `#` without a valid purpose.
- Fake API responses presented as real data.
- Placeholder functionality presented as complete.
- Forms that never submit.
- Loading indicators that never resolve.
- Error messages that hide actual failures.

Verify success, failure and boundary conditions.

## 5. Application Architecture

Review:

- Clear component boundaries.
- Appropriate feature organization.
- Consistent routing.
- Reusable UI primitives.
- Separation of UI and business logic where useful.
- Appropriate state management.
- API client consistency.
- Type safety.
- Configuration management.
- Dependency direction.
- Maintainability.

For existing projects:

- Preserve the established architecture where appropriate.
- Identify structural problems that materially affect reliability.
- Avoid unnecessary migrations.
- Avoid rewriting working functionality without justification.

Do not introduce architecture complexity solely to satisfy a checklist.

## 6. TypeScript and Code Quality

Verify:

- TypeScript checks pass.
- Strictness is maintained according to project standards.
- No unnecessary `any`.
- External data is validated where necessary.
- Errors are handled appropriately.
- Dead code is removed when relevant.
- Imports and dependencies are correct.
- No accidental debugging code remains.
- No unexplained lint suppressions exist.

Do not weaken type safety or disable lint rules simply to obtain a successful build.

Review the actual changed files and important application boundaries.

## 7. Accessibility

Check the application against its intended accessibility requirements.

Recommended baseline: WCAG 2.2 AA.

Verify:

- Semantic HTML.
- Keyboard navigation.
- Visible focus.
- Accessible names.
- Form labels.
- Validation messages.
- Dialog focus management.
- Appropriate ARIA usage.
- Color contrast.
- Alternative text.
- Screen reader announcements.
- Reduced motion.
- Responsive zoom behavior.
- Accessible navigation.

Run automated checks where appropriate and perform manual keyboard testing.

Automated accessibility tools cannot detect every usability or accessibility problem.

See `accessibility-and-wcag.md`.

## 8. Frontend Security

Review:

- Authentication.
- Authorization.
- Session handling.
- Token storage.
- XSS prevention.
- CSRF protection where relevant.
- Input validation.
- Output encoding.
- Content Security Policy.
- CORS configuration.
- Security headers.
- Redirect validation.
- File upload restrictions.
- Dependency security.
- Secret exposure.
- Third-party scripts.
- Sensitive information in logs.

Important:

- Frontend authorization is not a replacement for backend authorization.
- Public environment variables are not secret.
- CORS is not authentication.
- Hiding a UI element does not protect its underlying API.

Never expose private keys or credentials in browser code.

See `frontend-security.md`.

## 9. Authentication and Authorization

Verify:

- Login and logout.
- Session persistence.
- Session expiry.
- Unauthorized API handling.
- Protected routes.
- Role and permission behavior.
- Token refresh where applicable.
- Password recovery where implemented.
- OAuth callback handling where implemented.
- Multi-tenant access boundaries where applicable.

Test both permitted and denied access.

Backend services must enforce access control independently.

See `authentication-and-authorization.md`.

## 10. API and Data Reliability

Review:

- API base URLs.
- Request and response contracts.
- Runtime response validation.
- Error handling.
- Timeouts.
- Cancellation.
- Retry behavior.
- Rate limiting behavior.
- Pagination.
- Cache invalidation.
- Optimistic updates.
- Data consistency.
- Loading and empty states.

Test important API failure scenarios.

Do not silently convert failed requests into successful empty responses.

Ensure the interface communicates relevant failures clearly.

See `api-integration.md` and `state-management.md`.

## 11. Performance

Measure performance instead of relying on assumptions.

Review:

- Core Web Vitals.
- JavaScript bundle size.
- Initial page load.
- Rendering behavior.
- Image optimization.
- Font loading.
- API waterfalls.
- Third-party scripts.
- Long tasks.
- Mobile performance.
- Memory usage.

Current Core Web Vitals good thresholds:

| Metric | Good threshold |
| ------ | ------------------------ |
| LCP | 2.5 seconds or less |
| INP | 200 milliseconds or less |
| CLS | 0.1 or less |

These are field measurement thresholds evaluated at the 75th percentile.

Use appropriate real-user and laboratory measurements.

Do not claim that an application meets these thresholds without relevant measurement data.

See `performance-and-core-web-vitals.md`.

## 12. SEO and Discoverability

For publicly discoverable pages, verify:

- Page titles.
- Meta descriptions.
- Canonical URLs.
- Sitemap.
- Robots configuration.
- Appropriate indexing directives.
- Semantic headings.
- Internal links.
- Open Graph metadata.
- Structured data where appropriate.
- Image alternative text.
- Correct HTTP status codes.

Ensure private application routes are not unintentionally indexed.

SEO requirements depend on the application type.

A private CRM dashboard does not need the same indexing strategy as a public marketing website.

Metadata does not guarantee search ranking or indexing.

See `seo-and-discoverability.md`.

## 13. Responsive and Cross-Browser Quality

Test important application flows across:

- Mobile.
- Tablet.
- Desktop.
- Different viewport sizes.
- Supported browsers.
- Touch interactions.
- Keyboard interactions.

Inspect:

- Navigation.
- Tables.
- Forms.
- Dialogs.
- Sidebars.
- Images.
- Typography.
- Overflow.
- Layout shifts.

Do not assume responsive behavior is correct simply because the layout uses responsive CSS classes.

## 14. Internationalization and Content

For applications supporting multiple locales, verify:

- Correct translations.
- Locale routing.
- Date and time formatting.
- Currency and number formatting.
- Pluralization.
- Text expansion.
- RTL layouts.
- Language switching.
- Locale-specific metadata.
- Font coverage.

Do not introduce unnecessary localization infrastructure into a single-language application.

See `internationalization-and-rtl.md`.

## 15. PWA and Offline Behavior

For applications implementing PWA functionality, verify:

- Web App Manifest.
- Installability.
- Service worker registration.
- Cache behavior.
- Offline fallback.
- Cache versioning.
- Update behavior.
- Data synchronization.
- Push notification permissions.
- Secure service worker scope.

Do not claim an application supports offline operation simply because it has a manifest.

Verify actual offline functionality.

See `pwa-and-offline-support.md`.

## 16. Testing and Verification

Use a testing strategy appropriate to the application.

Review:

- Unit tests.
- Component tests.
- Integration tests.
- End-to-end tests.
- Regression tests.
- Accessibility checks.
- Critical user journeys.

Prioritize:

- Authentication.
- Authorization.
- Data submission.
- Important business operations.
- Payment flows where applicable.
- Navigation.
- Error handling.

Run the available project checks.

Typical commands may include:

```bash
npm run lint
npm run typecheck
npm test
npm run build
```

These are examples.

Use the project's actual scripts and package manager.

Do not claim tests passed unless they were executed successfully.

See `testing-strategy.md`.

## 17. Environment and Configuration

Verify separate configurations for:

- Development.
- Staging.
- Production.

Check:

- API URLs.
- Database connections.
- Authentication settings.
- Public and private variables.
- Feature flags.
- Monitoring configuration.
- Third-party integrations.
- Build-time configuration.
- Runtime configuration.

Never expose production secrets to browser-side code.

Never use a production database as a development test environment without an explicitly approved and safe process.

See `environment-configuration.md`.

## 18. CI/CD and Deployment

Verify:

- CI workflows.
- Required quality gates.
- Build configuration.
- Deployment triggers.
- Hosting compatibility.
- Environment-specific deployment settings.
- HTTPS.
- Domain configuration.
- Rollback strategy.
- Deployment permissions.

A successful CI pipeline does not guarantee correct runtime behavior.

Perform post-deployment smoke checks for important application journeys.

See `ci-cd-and-deployment.md`.

## 19. Observability and Monitoring

A production application should provide sufficient visibility into failures and important performance problems.

Depending on project requirements, consider:

- Frontend error monitoring.
- Backend error monitoring.
- Structured logs.
- API latency.
- Core Web Vitals.
- Release tracking.
- Health checks.
- Alerting.
- Distributed tracing.
- User-impact analysis.

Protect user privacy.

Do not collect sensitive information unnecessarily.

Ensure source maps and monitoring credentials are configured appropriately.

See `observability-and-monitoring.md`.

## 20. Error Handling and Recovery

Verify:

- Application-level error boundaries.
- Route-level error handling.
- API failure handling.
- Network failure behavior.
- Session expiry handling.
- Retry behavior.
- Useful user-facing messages.
- Diagnostic logging.
- Recovery paths.

Do not expose stack traces, internal secrets or sensitive backend details to users.

Avoid hiding errors behind generic success states.

See `debugging-and-self-correction.md`.

## 21. Dependencies and Third-Party Integrations

Review:

- Installed package versions.
- Unused dependencies.
- Known vulnerabilities.
- Framework compatibility.
- License considerations.
- Third-party scripts.
- External service availability.
- API usage limits.
- Package maintenance.

Remove or replace dependencies only when justified.

Avoid adding new packages merely because they are popular.

See `package-selection-and-ecosystem.md`.

## 22. Database and Backend Coordination

For full-stack applications, frontend readiness also depends on backend compatibility.

Verify:

- API contract compatibility.
- Authentication behavior.
- Authorization enforcement.
- Database migration coordination.
- Error response consistency.
- File upload limits.
- Pagination contracts.
- CORS.
- Rate limiting.
- Health checks.

Do not assume frontend deployment alone makes the complete system production-ready.

Database migrations and destructive data changes require their own review and recovery plan.

## 23. Release Readiness

Before release, identify:

- Version or release identifier.
- Included changes.
- Known issues.
- Environment.
- Deployment target.
- Required approvals.
- Database migration requirements.
- Monitoring availability.
- Rollback plan.

For important releases, use a staged rollout where supported.

Do not release an unverified critical change simply because the deadline is close.

Communicate unresolved risks.

## 24. Existing Project Production Review

When reviewing an existing application:

1. Understand its architecture and deployment model.
1. Identify critical user journeys.
1. Inspect existing tests and monitoring.
1. Review security and environment boundaries.
1. Measure actual performance.
1. Identify important gaps.
1. Separate critical risks from optional improvements.
1. Prioritize fixes.
1. Make targeted changes when requested.
1. Verify all changes.
1. Report remaining risks.

Do not automatically rewrite the application to match an idealized architecture.

Preserve working functionality and existing conventions.

## 25. Production Readiness Levels

Use these categories to communicate status.

### Ready

Critical functionality and required quality gates have been verified, with no known release-blocking issues within the reviewed scope.

### Ready with Known Limitations

The application is usable for its intended release, but documented limitations remain and have been accepted.

### Not Ready

One or more critical requirements remain incomplete, unsafe, broken or unverified.

### Not Fully Verified

There is insufficient evidence to make a reliable readiness determination.

Do not classify an application as production-ready solely because it builds successfully.

## 26. Prioritization of Findings

Classify findings by impact.

| Priority | Meaning |
| -------- | ------------------------------------------------------------------------- |
| Critical | Security exposure, data loss, major outage, or core functionality failure |
| High | Important user journey broken or significant reliability issue |
| Medium | Limited feature defect or notable quality issue |
| Low | Minor polish or non-critical improvement |

Priorities should reflect actual impact and context.

Do not inflate minor visual issues into critical production blockers.

## 27. Production Readiness Checklist

### Application

- [ ] Critical features work.
- [ ] Interactive elements have real behavior.
- [ ] Loading, empty and error states are handled.
- [ ] Important user journeys are verified.

### Architecture and Code

- [ ] Project architecture is maintainable.
- [ ] Type checks pass.
- [ ] Lint checks pass.
- [ ] No unnecessary debugging code remains.

### Security

- [ ] Authentication and authorization work correctly.
- [ ] Private secrets are protected.
- [ ] Input and output handling are appropriate.
- [ ] Sensitive data is not exposed.
- [ ] Dependencies are reviewed.

### Accessibility and UI

- [ ] Keyboard navigation works.
- [ ] Important flows are accessible.
- [ ] Responsive layouts are tested.
- [ ] No critical UI defects remain.

### Performance and SEO

- [ ] Important performance bottlenecks are reviewed.
- [ ] Core Web Vitals are measured where applicable.
- [ ] Public pages have appropriate SEO configuration.
- [ ] Private pages are protected from unintended indexing.

### Testing and Reliability

- [ ] Relevant tests pass.
- [ ] Critical user journeys are tested.
- [ ] Important failures have recovery behavior.
- [ ] Monitoring is configured where required.

### Deployment

- [ ] Development, staging and production are separated.
- [ ] Required environment variables are configured.
- [ ] CI/CD quality gates are active.
- [ ] HTTPS is configured.
- [ ] Deployment and rollback strategies exist.

### Final Review

- [ ] Known limitations are documented.
- [ ] Critical risks are addressed.
- [ ] Final changes are reviewed.
- [ ] Verification results are accurate.

## 28. Completion Report

When performing a production readiness review, provide:

### Scope

What application, routes, features and environments were reviewed?

### Findings

What issues were identified?

### Priorities

Which issues are critical, high, medium or low?

### Changes

What was actually modified?

### Verification

Which commands, tests and manual checks were executed?

### Remaining Risks

What remains incomplete, unverified or dependent on external systems?

### Readiness Assessment

Choose the appropriate readiness level and explain why.

Do not invent monitoring results, performance scores, security audit outcomes or deployment success.

## 29. Related References

- anti-ai-slop-and-engineering-quality.md
- architecture-and-project-structure.md
- typescript-and-code-quality.md
- accessibility-and-wcag.md
- frontend-security.md
- authentication-and-authorization.md
- api-integration.md
- testing-strategy.md
- performance-and-core-web-vitals.md
- seo-and-discoverability.md
- internationalization-and-rtl.md
- pwa-and-offline-support.md
- observability-and-monitoring.md
- debugging-and-self-correction.md
- ci-cd-and-deployment.md
- environment-configuration.md

## 30. Official Resources

### Web Standards

- Web Content Accessibility Guidelines: https://www.w3.org/WAI/standards-guidelines/wcag/
- MDN Web Docs: https://developer.mozilla.org/

### Security

- OWASP: https://owasp.org/
- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/

### Performance

- Web Vitals: https://web.dev/articles/vitals
- PageSpeed Insights: https://pagespeed.web.dev/

### Testing

- Playwright: https://playwright.dev/
- Vitest: https://vitest.dev/

### Frameworks

- React: https://react.dev/
- Next.js: https://nextjs.org/docs

### Deployment

- GitHub Actions: https://docs.github.com/en/actions
- Docker: https://docs.docker.com/

Production readiness must be based on actual evidence, project requirements and the risks of the intended release.
