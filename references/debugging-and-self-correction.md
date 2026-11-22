# Debugging and Self-Correction

## 1. Purpose

Define a systematic engineering approach for investigating problems, identifying root causes, implementing fixes and verifying results.

The agent must behave like a careful engineer rather than repeatedly guessing at possible solutions.

This reference applies to:

- Runtime errors.
- Build failures.
- TypeScript errors.
- Lint failures.
- React rendering problems.
- Next.js errors.
- Hydration mismatches.
- API failures.
- Authentication issues.
- State management bugs.
- CSS and layout problems.
- Accessibility defects.
- Performance issues.
- Dependency problems.
- Configuration errors.
- Deployment failures.
- Existing project maintenance.
- AI-generated implementation mistakes.

The objective is to solve the actual problem with the smallest reliable change and verify that the solution works.

## 2. Core Debugging Principles

Follow these principles:

1. Understand the problem before changing code.
1. Reproduce the issue when possible.
1. Collect evidence before forming conclusions.
1. Identify the actual failure location.
1. Trace the relevant data and execution flow.
1. Distinguish symptoms from root causes.
1. Prefer targeted fixes.
1. Preserve unrelated behavior.
1. Verify the result.
1. Report limitations honestly.

Do not make random code changes until the error disappears.

A disappearing error does not automatically mean the underlying problem is solved.

## 3. Understand the Reported Problem

Start by understanding the user's request and available evidence.

Identify:

- Expected behavior.
- Actual behavior.
- Affected feature or route.
- Error message.
- Steps to reproduce.
- Relevant environment.
- Recent changes.
- Browser or device context.
- Frequency and severity.

Not every bug report contains all these details.

Use available evidence first.

Ask a clarification question only when an essential missing detail prevents meaningful investigation.

Do not ask the user to repeat information already available in the conversation or project.

## 4. Inspect Before Debugging

For an existing project:

1. Inspect the project structure.
1. Identify the framework and installed versions.
1. Read relevant source files.
1. Follow imports and dependencies.
1. Inspect related components and hooks.
1. Trace API and state interactions.
1. Review configuration.
1. Inspect relevant tests.
1. Check recent changes when available.
1. Review the exact error output.

Do not read the entire repository unnecessarily.

Focus on the affected feature and its dependencies.

Do not assume the reported file is necessarily the source of the bug.

## 5. Reproduce the Problem

Reproduction helps distinguish real defects from assumptions.

Possible methods:

- Run the affected route.
- Execute the failing command.
- Reproduce a user interaction.
- Run the relevant test.
- Inspect browser console output.
- Inspect network requests.
- Compare development and production behavior.
- Test the same operation with different inputs.

Record the conditions under which the issue occurs.

If the problem cannot be reproduced:

- Inspect available logs.
- Review relevant code paths.
- Identify likely failure conditions.
- Add a targeted diagnostic test when appropriate.
- Clearly state what remains unverified.

Do not claim a bug is reproduced when it is only inferred from code.

## 6. Read Error Messages Carefully

Use the full error output whenever possible.

Inspect:

- Error type.
- Message.
- Stack trace.
- Source file.
- Line and column.
- Nested causes.
- Related network failures.
- Framework warnings.

Do not focus only on the last visible line.

Build tools and frameworks often provide useful context earlier in the output.

Avoid blindly following an error message's suggested fix without understanding the surrounding code.

## 7. Identify the Root Cause

A root cause explains why the problem happens.

Example:

**Symptom:** A dashboard displays stale data.

Possible root causes:

- Incorrect query key.
- Missing cache invalidation.
- Incorrect API response mapping.
- Stale local state.
- Incorrect caching configuration.
- Request race condition.

Changing a loading indicator does not solve these problems.

### Root-Cause Workflow

1. Identify the failing behavior.
1. Trace its execution path.
1. Inspect inputs and outputs.
1. Identify relevant state and dependencies.
1. Find the earliest incorrect assumption or operation.
1. Determine why it fails.
1. Confirm the hypothesis with evidence.
1. Implement the correction.

Do not stop at the first plausible explanation.

## 8. Debugging React Applications

Investigate:

- Component rendering.
- State updates.
- Props.
- Context.
- Effects.
- Event handlers.
- Keys.
- Component lifecycle.
- Suspense.
- Error Boundaries.

### Common Problems

| Problem | Areas to investigate |
| ------------------------- | ------------------------------------------------------ |
| Component does not update | State mutation, props, memoization |
| Unexpected rerender | Parent updates, context, unstable values |
| Infinite render loop | State updates during rendering or effects |
| Stale values | Closures, effect dependencies, asynchronous operations |
| Incorrect list rendering | Keys and list identity |
| UI flickering | State transitions, loading behavior, effects |
| Missing interaction | Event handlers, disabled states, overlays |

### State Mutation

Avoid directly mutating React state.

Incorrect:

```tsx
items.push(newItem);
setItems(items);
```

Correct:

```tsx
setItems((current) => [...current, newItem]);
```

Use immutable updates where required by the state architecture.

### Effects

Investigate whether an effect is actually necessary.

Avoid using effects to synchronize values that can be derived during rendering.

Check:

- Dependencies.
- Cleanup.
- Repeated execution.
- Stale closures.
- External subscriptions.
- Async request cancellation.

Do not remove dependencies simply to silence a lint warning.

Understand the dependency relationship first.

## 9. Debugging Next.js Applications

Investigate the rendering and execution environment.

Common issues:

- Server Component importing browser-only APIs.
- Client Component boundaries.
- Hydration mismatches.
- Incorrect route parameters.
- Invalid server/client data flow.
- Incorrect cache behavior.
- Server Action failures.
- Route Handler errors.
- Authentication redirects.
- Metadata problems.
- Streaming and Suspense behavior.

### Server and Client Boundaries

Check:

- Where code executes.
- Whether browser APIs are used on the server.
- Whether server-only modules enter client bundles.
- Whether data crosses the server/client boundary safely.
- Whether serialization requirements are satisfied.

Do not add `"use client"` to an entire application section merely to bypass an error.

Find the smallest appropriate client boundary.

### Hydration Mismatches

Investigate differences between server-rendered output and initial client-rendered output.

Possible causes:

- Browser-only values during rendering.
- Current time or random values.
- Locale differences.
- Invalid HTML nesting.
- Different initial state.
- External content changing between renders.
- Incorrect server/client data assumptions.

Do not suppress hydration warnings without understanding their cause.

See `nextjs-engineering.md` and `rendering-and-caching-strategies.md`.

## 10. Debugging TypeScript Errors

Read the complete compiler message.

Investigate:

- Incorrect types.
- Missing properties.
- Nullability.
- Generic constraints.
- Union narrowing.
- Function signatures.
- Incorrect imports.
- Incompatible package types.
- Framework type changes.

Prefer fixing the underlying type relationship.

Avoid:

- `any`.
- `@ts-ignore`.
- Unnecessary type assertions.
- Broad type weakening.
- Disabling strict compiler options.

If a type assertion is necessary, verify that the value actually satisfies the asserted type.

Use runtime validation for untrusted external data.

See `typescript-and-code-quality.md`.

## 11. Debugging API and Network Problems

Inspect requests using browser developer tools.

Check:

- Request URL.
- HTTP method.
- Headers.
- Query parameters.
- Request body.
- Response status.
- Response body.
- Response headers.
- Timing.
- CORS behavior.
- Authentication.
- Cancellation.
- Network failures.

### Common HTTP Issues

| Status | Investigation |
| ------ | ------------------------------------- |
| 400 | Invalid request or validation failure |
| 401 | Authentication missing or invalid |
| 403 | Authorization failure |
| 404 | Incorrect route or missing resource |
| 409 | Conflict or state mismatch |
| 422 | Validation failure where used |
| 429 | Rate limiting |
| 500 | Server-side failure |
| 502 | Upstream gateway failure |
| 503 | Service unavailable |
| 504 | Gateway timeout |

Actual behavior depends on the backend contract.

Do not assume every API follows identical error semantics.

### CORS

Investigate:

- Origin.
- Allowed methods.
- Allowed headers.
- Credential configuration.
- Preflight requests.
- Server response headers.

Do not attempt to fix server CORS configuration by adding arbitrary frontend headers.

CORS is primarily controlled by the server response.

### Authentication

Check:

- Session state.
- Cookie attributes.
- Token expiry.
- Refresh behavior.
- Redirect logic.
- Permission checks.

Never print tokens or secrets into debugging output.

See `api-integration.md` and `authentication-and-authorization.md`.

## 12. Debugging CSS and Layout Problems

Investigate:

- Computed styles.
- CSS specificity.
- Inheritance.
- Cascade layers.
- Parent layout.
- Flexbox and Grid constraints.
- Overflow.
- Positioning.
- Stacking contexts.
- Responsive breakpoints.
- Container dimensions.
- Font loading.

Use browser DevTools to inspect the actual computed styles.

Do not randomly add:

- `!important`.
- Arbitrary margins.
- Fixed heights.
- Negative positioning.
- Extra wrappers.

Identify which layout rule causes the problem.

For visual issues, compare:

- Expected layout.
- Actual layout.
- Different viewport sizes.
- Light and dark themes.
- Keyboard focus.
- RTL direction where supported.

## 13. Debugging Performance Problems

Performance issues require measurement.

Investigate:

- JavaScript execution.
- Rendering.
- Layout and paint.
- Network waterfalls.
- API latency.
- Large images.
- Font loading.
- Long tasks.
- Memory usage.
- Third-party scripts.

Use appropriate browser profiling tools.

Do not introduce memoization, virtualization or Web Workers without identifying a relevant bottleneck.

Measure after implementing the change.

See `performance-and-core-web-vitals.md`.

## 14. Debugging Build and Dependency Problems

When a build fails:

1. Read the full build output.
1. Identify the first meaningful error.
1. Check the affected module.
1. Inspect installed package versions.
1. Review relevant configuration.
1. Check recent dependency changes.
1. Verify package manager consistency.
1. Reproduce with the documented project command.

Avoid deleting lockfiles or reinstalling every dependency as the first response.

Before changing a dependency:

- Inspect its installed version.
- Review compatibility.
- Check peer dependencies.
- Understand breaking changes.
- Preserve the package manager lockfile.

Do not upgrade the entire dependency tree to fix one isolated issue.

## 15. Debugging Environment and Deployment Issues

A problem may occur only in one environment.

Compare:

- Development.
- Staging.
- Production.

Inspect:

- Environment variables.
- Build configuration.
- Runtime version.
- API base URL.
- CORS settings.
- Authentication domains.
- Deployment configuration.
- CDN behavior.
- Cache state.
- Hosting restrictions.

Never expose secret values while comparing environments.

Verify the variable's presence and intended configuration without printing its value.

Do not assume a local success proves production behavior.

See `environment-configuration.md` and `ci-cd-and-deployment.md`.

## 16. Use Tests to Confirm the Cause

Tests help establish whether a problem is understood.

Consider:

- Unit tests.
- Component tests.
- Integration tests.
- End-to-end tests.
- Regression tests.

A good regression test should:

1. Reproduce the original failure.
1. Fail before the fix where practical.
1. Pass after the fix.
1. Check expected behavior.
1. Avoid testing irrelevant implementation details.

Do not change a test simply to make an incorrect implementation pass.

See `testing-strategy.md`.

## 17. AI Agent Self-Correction

An AI coding agent must evaluate its own work critically.

Before considering an implementation complete, review:

- Did I understand the actual requirement?
- Did I inspect the existing architecture?
- Did I change the correct files?
- Did I preserve existing behavior?
- Did I introduce unnecessary abstractions?
- Did I invent an API or configuration option?
- Did I add an unnecessary dependency?
- Did I handle loading, empty and error states?
- Did I consider accessibility?
- Did I introduce security or performance problems?
- Did I verify the implementation?

Do not treat generated code as correct simply because it looks plausible.

### Self-Correction Process

1. Review the original request.
1. Review the implemented changes.
1. Compare the changes with existing conventions.
1. Inspect relevant diffs.
1. Identify unsupported assumptions.
1. Check error handling and edge cases.
1. Run appropriate verification.
1. Correct discovered problems.
1. Re-run affected checks.
1. Report the final result honestly.

## 18. When a Fix Fails

If the first fix does not work:

1. Stop repeating the same approach.
1. Re-examine the original evidence.
1. Identify which assumption was incorrect.
1. Inspect additional relevant context.
1. Narrow the failing condition.
1. Consider alternative root causes.
1. Make one targeted change.
1. Reproduce and verify again.

Avoid making multiple unrelated changes in one attempt.

Keep a clear distinction between:

- Confirmed cause.
- Likely cause.
- Unverified hypothesis.

Do not pretend a failed attempt succeeded.

## 19. Avoid Destructive Debugging

Do not:

- Delete files without understanding their purpose.
- Replace project configuration unnecessarily.
- Remove lockfiles casually.
- Disable linting or TypeScript checks to hide errors.
- Suppress runtime errors.
- Remove tests that expose defects.
- Change unrelated features.
- Overwrite user modifications.
- Reset project state without permission.
- Delete caches or data that may be user-owned without understanding the impact.

When a destructive operation is genuinely necessary, explain its impact and obtain permission where appropriate.

## 20. Debugging Workflow for Existing Projects

Use this sequence:

1. Understand the reported problem.
1. Inspect the repository and affected feature.
1. Reproduce the issue.
1. Collect error and runtime evidence.
1. Trace the relevant code path.
1. Identify the root cause.
1. Choose the smallest reliable fix.
1. Implement the change.
1. Add or update regression tests.
1. Run targeted verification.
1. Run broader checks when appropriate.
1. Review the final diff.
1. Report the result and any limitations.

Preserve unrelated functionality.

Do not rewrite a feature merely because the current implementation is unfamiliar.

## 21. Debugging Workflow for New Projects

When building a new application:

1. Verify the project setup.
1. Inspect generated files and configuration.
1. Run the initial application.
1. Validate core dependencies.
1. Implement features incrementally.
1. Test important flows.
1. Inspect browser and terminal errors.
1. Fix issues close to their source.
1. Verify the production build.
1. Review the final application behavior.

Avoid introducing multiple unverified features simultaneously.

## 22. Common Debugging Anti-Patterns

Avoid:

- Guessing without evidence.
- Fixing symptoms instead of causes.
- Making unrelated changes.
- Repeating failed fixes.
- Suppressing useful errors.
- Disabling type safety.
- Removing tests to hide failures.
- Reinstalling all packages unnecessarily.
- Rewriting entire components without justification.
- Adding arbitrary delays to fix race conditions.
- Using `setTimeout` as a substitute for understanding lifecycle problems.
- Ignoring cleanup and stale closures.
- Logging secrets.
- Claiming an issue is fixed without verification.

## 23. Completion Report

After debugging, communicate:

### Problem

Describe the observed issue.

### Root Cause

Explain the confirmed cause, or clearly label it as a likely cause if not confirmed.

### Changes

List the relevant files and meaningful modifications.

### Verification

List the commands and tests actually executed, with their results.

### Remaining Limitations

Mention anything that could not be reproduced, tested or verified.

Do not claim success when the required verification was not performed.

## 24. Review Checklist

### Investigation

- [ ] Expected and actual behavior understood.
- [ ] Relevant files inspected.
- [ ] Error output reviewed.
- [ ] Issue reproduced where possible.
- [ ] Root cause identified or uncertainty documented.

### Implementation

- [ ] Smallest reliable fix selected.
- [ ] Existing conventions preserved.
- [ ] Unrelated behavior preserved.
- [ ] Errors handled appropriately.
- [ ] Security and accessibility considered.

### Verification

- [ ] Regression test added or updated where appropriate.
- [ ] Relevant checks executed.
- [ ] Final diff reviewed.
- [ ] Fix verified under relevant conditions.
- [ ] Remaining limitations documented.

### Communication

- [ ] Root cause explained.
- [ ] Changed files identified.
- [ ] Actual test results reported.
- [ ] No unsupported completion claims.

## 25. Related References

- anti-ai-slop-and-engineering-quality.md
- architecture-and-project-structure.md
- react-engineering.md
- nextjs-engineering.md
- typescript-and-code-quality.md
- api-integration.md
- state-management.md
- frontend-security.md
- testing-strategy.md
- performance-and-core-web-vitals.md
- observability-and-monitoring.md
- environment-configuration.md
- ci-cd-and-deployment.md
- production-readiness.md

## 26. Official Resources

### React

- React Developer Tools: https://react.dev/learn/react-developer-tools
- React Error Boundaries: https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary

### Next.js

- Next.js Errors: https://nextjs.org/docs/app/getting-started/error-handling
- Next.js Debugging: https://nextjs.org/docs/app/guides/debugging

### TypeScript

- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html

### Browser Debugging

- Chrome DevTools: https://developer.chrome.com/docs/devtools/
- Chrome DevTools Console: https://developer.chrome.com/docs/devtools/console/
- Chrome DevTools Network: https://developer.chrome.com/docs/devtools/network/

### Testing

- Vitest: https://vitest.dev/guide/
- Playwright: https://playwright.dev/docs/intro
- Testing Library: https://testing-library.com/docs/

### Monitoring

- Sentry: https://docs.sentry.io/
- OpenTelemetry: https://opentelemetry.io/docs/

Always verify current framework behavior, error messages and tool documentation before implementing a fix.
