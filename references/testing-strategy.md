# Testing Strategy

## 1. Purpose

Define standards for designing, implementing, running, debugging and maintaining frontend tests.

Support:

- Unit testing.
- Component testing.
- Integration testing.
- End-to-end testing.
- Accessibility testing.
- Visual regression testing.
- API mocking.
- Test data management.
- Test coverage.
- CI testing.
- Existing project regression testing.

The objective is to verify that frontend applications behave correctly, remain maintainable and do not introduce regressions.

Testing should be part of development, not an optional final step.

## 2. Inspect Before Testing

Before adding or modifying tests:

1. Inspect existing test configuration.
1. Identify the test runner.
1. Review existing test conventions.
1. Check installed testing libraries.
1. Inspect test scripts in `package.json`.
1. Identify existing mocks and fixtures.
1. Review CI test commands.
1. Understand the feature's expected behavior.

For existing projects, extend the current testing approach where practical.

Do not introduce another testing framework without a clear reason.

Do not replace existing tests simply because a different testing style is preferred.

## 3. Testing Pyramid

Use different test levels for different responsibilities.

<escape>
             E2E Tests
          Integration Tests
             Unit Tests
</escape>

| Test level | Purpose |
| ----------- | ----------------------------------- |
| Unit | Verify isolated functions and logic |
| Component | Verify component behavior |
| Integration | Verify interactions between modules |
| E2E | Verify complete user workflows |

A balanced test suite usually contains more focused unit and component tests than expensive end-to-end tests.

Do not follow a fixed test-count ratio blindly.

Choose tests based on risk, complexity and expected behavior.

## 4. Testing Tools

Choose tools based on the project's framework and existing dependencies.

### Vitest

Useful for:

- Vite applications.
- Unit tests.
- Component tests.
- Mocking.
- Coverage.

Documentation: https://vitest.dev/

### Jest

Useful for:

- Unit testing.
- Component testing.
- Mocking.
- Existing Jest-based projects.

Documentation: https://jestjs.io/

### React Testing Library

Useful for testing React components through user-visible behavior.

Documentation: https://testing-library.com/docs/react-testing-library/intro/

### Playwright

Useful for:

- End-to-end testing.
- Browser automation.
- Cross-browser testing.
- Screenshot testing.
- Accessibility-related checks.

Documentation: https://playwright.dev/

### Cypress

An alternative for browser-based end-to-end and component testing.

Documentation: https://docs.cypress.io/

### MSW

Useful for mocking API requests at the network boundary.

Documentation: https://mswjs.io/

Do not install every tool listed here.

Use the smallest suitable testing stack.

## 5. Unit Testing

Unit tests verify isolated logic.

Good candidates:

- Utility functions.
- Data transformations.
- Validation helpers.
- Date formatting.
- Permission calculations.
- Filtering and sorting.
- URL construction.
- Business rules.

Example:

```tsx
import { describe, expect, it } from "vitest";

function calculateTotal(price: number, quantity: number): number {
  return price * quantity;
}

describe("calculateTotal", () => {
  it("calculates the total correctly", () => {
    expect(calculateTotal(100, 3)).toBe(300);
  });

  it("handles zero quantity", () => {
    expect(calculateTotal(100, 0)).toBe(0);
  });
});
```

Guidelines:

- Test expected behavior.
- Include important edge cases.
- Keep tests independent.
- Avoid testing trivial implementation details.
- Use descriptive test names.
- Keep setup simple.

Do not write tests that simply repeat the implementation logic.

## 6. Component Testing

Test components through their observable behavior.

Examples:

- Rendering.
- User interactions.
- Form submission.
- Loading states.
- Error states.
- Conditional content.
- Keyboard interactions.
- Accessible names.

Example:

```tsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";

function SaveButton({ onSave }: { onSave: () => void }) {
  return <button onClick={onSave}>Save</button>;
}

describe("SaveButton", () => {
  it("calls the save handler when clicked", async () => {
    const user = userEvent.setup();
    const onSave = vi.fn();

    render(<SaveButton onSave={onSave} />);

    await user.click(screen.getByRole("button", { name: "Save" }));

    expect(onSave).toHaveBeenCalledOnce();
  });
});
```

Guidelines:

- Prefer queries by role and accessible name.
- Use realistic user interactions.
- Test visible results.
- Avoid accessing component internals.
- Avoid unnecessary snapshots.
- Use async queries for asynchronous UI.

A component test should describe what users can observe, not how the component is implemented internally.

## 7. Integration Testing

Integration tests verify that multiple parts work together.

Examples:

- Form and validation schema.
- Component and API service.
- Query hook and cache.
- Authentication and protected navigation.
- Dialog and form submission.
- Filters and pagination.

Test:

- Successful interactions.
- Failed requests.
- Validation errors.
- Loading behavior.
- Data synchronization.
- Permission restrictions.
- Error recovery.

Avoid mocking every internal function.

Mock external boundaries when appropriate so integration behavior remains meaningful.

## 8. End-to-End Testing

E2E tests verify complete user workflows in a real browser.

Examples:

- Login and logout.
- Registration.
- Creating a record.
- Editing a record.
- Deleting a record.
- Searching and filtering.
- Pagination.
- File upload.
- Role-based navigation.

Example using Playwright:

```tsx
import { test, expect } from "@playwright/test";

test("user can open the dashboard", async ({ page }) => {
  await page.goto("/dashboard");

  await expect(
    page.getByRole("heading", {
      name: "Dashboard",
    }),
  ).toBeVisible();
});
```

Guidelines:

- Test important user journeys.
- Prefer stable locators.
- Avoid unnecessary fixed waits.
- Use independent test data.
- Handle authentication deliberately.
- Clean up test-created data.
- Keep tests reliable and repeatable.

Do not use E2E tests for every small utility function.

## 9. Test Behavior, Not Implementation

Prefer assertions about observable behavior.

Good examples:

- The dialog opens after clicking its trigger.
- A validation message appears for invalid input.
- The user sees updated results after applying a filter.
- Unauthorized users cannot access a protected action.

Avoid excessive assertions about:

- Internal state variable names.
- Private helper functions.
- Component implementation structure.
- Exact internal hook call counts.

Tests should allow safe refactoring without requiring unnecessary test rewrites.

## 10. Test Naming and Organization

Use a consistent naming convention.

Possible structure:

```text
src/
└── features/
    └── users/
        ├── components/
        │   ├── user-form.tsx
        │   └── user-form.test.tsx
        ├── api/
        │   ├── users.api.ts
        │   └── users.api.test.ts
        └── utils/
            ├── user.utils.ts
            └── user.utils.test.ts
```

Or use a centralized test directory if the project already follows that convention.

Possible naming patterns:

- `*.test.ts`
- `*.test.tsx`
- `*.spec.ts`
- `*.spec.tsx`

Follow the existing project conventions.

Keep test files close to the code they verify when that improves maintainability.

## 11. Test Data and Fixtures

Use predictable test data.

Consider:

- Factories.
- Fixtures.
- Mock responses.
- Test database records.
- Seed data.
- Dedicated test accounts.

Guidelines:

- Avoid production data.
- Do not hardcode real credentials.
- Avoid sharing mutable test objects.
- Make tests independent.
- Use meaningful test scenarios.
- Clean up temporary records.

Do not make tests dependent on execution order.

## 12. API Mocking

Mock API boundaries when tests need deterministic responses.

Possible approaches:

- MSW.
- Playwright route interception.
- Existing project mock utilities.
- Controlled test API environments.

Test:

- Successful responses.
- Validation failures.
- Unauthorized responses.
- Forbidden responses.
- Not-found responses.
- Server errors.
- Network failures.
- Slow responses.
- Empty responses.

Do not mock every API call in every test.

Use real backend integration tests where the project requires contract verification.

## 13. Authentication Testing

Test authentication workflows deliberately.

Important scenarios:

- Successful login.
- Invalid credentials.
- Expired session.
- Logout.
- Protected routes.
- Unauthorized requests.
- Forbidden operations.
- Token or session refresh where applicable.
- Role-specific navigation.

Frontend visibility tests do not prove backend authorization.

Verify that protected backend operations also enforce permissions.

Never use real production credentials in tests.

See `authentication-and-authorization.md`.

## 14. Form Testing

Test forms as users interact with them.

Important scenarios:

- Initial values.
- Required fields.
- Invalid inputs.
- Valid submission.
- Server validation errors.
- Submission loading state.
- Duplicate submission prevention.
- Reset behavior.
- Conditional fields.
- File selection.
- Multi-step navigation.

Use accessible queries and realistic input interactions.

See `forms-and-validation.md`.

## 15. Accessibility Testing

Include accessibility checks in the testing strategy.

Possible tools:

- axe-core.
- Playwright accessibility checks.
- Lighthouse.
- Storybook accessibility addon.

Check:

- Accessible names.
- Semantic roles.
- Form labels.
- Invalid ARIA.
- Keyboard interactions.
- Focus behavior.
- Contrast where automated checks support it.

Automated tools cannot replace manual accessibility testing.

See `accessibility-and-wcag.md`.

## 16. Visual Regression Testing

Visual regression testing compares rendered UI against approved references.

Useful for:

- Design systems.
- Shared components.
- Complex layouts.
- Critical pages.
- Theme changes.
- Responsive interfaces.

Possible tools:

- Playwright screenshots.
- Chromatic.
- Percy.

Consider:

- Viewport sizes.
- Browser differences.
- Fonts.
- Animation.
- Dynamic content.
- Image loading.
- Time-dependent content.

Avoid accepting every screenshot difference automatically.

Review whether the change is intentional.

## 17. Responsive Testing

Test important layouts at different viewport sizes.

Consider:

- Mobile navigation.
- Tablet layouts.
- Desktop layouts.
- Overflow.
- Dialog dimensions.
- Forms.
- Tables.
- Long text.
- Touch interactions.

Do not test only at one desktop resolution.

Use representative breakpoints based on actual layout behavior.

## 18. Async and Race Condition Testing

Test asynchronous behavior deliberately.

Examples:

- Slow API responses.
- Failed requests.
- Request cancellation.
- Search race conditions.
- Background refetching.
- Duplicate mutations.
- Loading transitions.

Use controllable promises, network interception or the project's existing mocking tools.

Avoid fixed timeouts when deterministic synchronization is possible.

## 19. Error Boundary Testing

Where error boundaries are used, verify:

- Expected fallback UI.
- Recovery behavior.
- Error logging integration.
- Navigation after failure.
- Unaffected parts of the application.

Remember that React error boundaries do not catch every type of error, such as ordinary event-handler errors or arbitrary asynchronous callback failures.

Handle those cases through their appropriate mechanisms.

## 20. Test Coverage

Coverage measures which code is executed by tests.

Common metrics:

- Statement coverage.
- Branch coverage.
- Function coverage.
- Line coverage.

Use coverage to identify untested areas.

Do not treat a high coverage percentage as proof of correctness.

Prioritize:

- Critical business logic.
- Permission-sensitive behavior.
- Data transformations.
- Error handling.
- Complex state transitions.
- High-impact user workflows.

Avoid writing low-value tests solely to increase coverage.

## 21. Test Environment Configuration

Keep test configuration separate from development, staging and production.

Consider:

- Environment variables.
- API endpoints.
- Mock services.
- Test database.
- Authentication fixtures.
- Build configuration.
- Browser configuration.

Never run destructive tests against production systems.

Do not expose production secrets in test logs or CI output.

See `environment-configuration.md`.

## 22. Running Tests

Inspect available scripts before running commands.

Common commands:

```bash
npm run test
```

```bash
npm run test -- --run
```

```bash
npm run test:coverage
```

```bash
npm run test:e2e
```

These are illustrative.

Use the actual scripts and package manager configured in the repository.

Do not assume a script exists just because it is common.

## 23. Existing Project Regression Testing

When modifying an existing application:

1. Identify the affected feature.
1. Inspect existing tests.
1. Understand expected behavior.
1. Identify related consumers and dependencies.
1. Reproduce the issue when possible.
1. Add or update a test for the expected behavior.
1. Implement the smallest reliable change.
1. Run focused tests.
1. Run relevant broader regression tests.
1. Run type checking, linting and build checks.

For bug fixes, a regression test should reproduce the original failure when practical.

Do not rewrite unrelated tests during a small feature change.

## 24. Debugging Failed Tests

When a test fails:

1. Read the complete failure output.
1. Identify the failing assertion or setup.
1. Determine whether the failure is in the application or test.
1. Reproduce the failure.
1. Inspect relevant code and test fixtures.
1. Fix the root cause.
1. Run the focused test again.
1. Run related tests.

Do not:

- Delete a failing test without understanding it.
- Weaken assertions merely to make tests pass.
- Add arbitrary waits.
- Mock away the behavior being tested.
- Ignore flaky tests.
- Claim tests passed when they were not run.

If an environment limitation prevents execution, report it honestly.

## 25. CI Testing

Run appropriate checks in continuous integration.

Typical pipeline:

```text
Install Dependencies
        |
        v
Lint
        |
        v
Type Check
        |
        v
Unit and Integration Tests
        |
        v
Build
        |
        v
E2E Tests
        |
        v
Deployment
```

The actual sequence depends on the project.

Guidelines:

- Use reproducible dependency installation.
- Use the committed lockfile.
- Keep test configuration consistent.
- Avoid exposing secrets.
- Preserve test artifacts when useful.
- Fail the pipeline on required checks.

Do not deploy when required quality checks fail unless an explicitly approved exception exists.

See `ci-cd-and-deployment.md`.

## 26. Test Performance and Reliability

A useful test suite should be reliable and maintainable.

Improve test reliability by:

- Avoiding shared mutable state.
- Using deterministic fixtures.
- Cleaning up after tests.
- Avoiding unnecessary network dependencies.
- Avoiding arbitrary waits.
- Limiting unnecessary E2E coverage.
- Running tests independently where possible.

Do not sacrifice meaningful coverage solely to make the test suite faster.

## 27. Common Anti-Patterns

Avoid:

- Testing only the happy path.
- Testing implementation details excessively.
- Overusing snapshots.
- Mocking every internal dependency.
- Depending on production data.
- Hardcoded real credentials.
- Fixed sleeps in E2E tests.
- Tests that depend on execution order.
- Ignoring flaky tests.
- Deleting failing tests without investigation.
- Treating coverage as correctness.
- Claiming verification without execution.

## 28. Decision Workflow

Before writing tests:

1. Understand expected behavior.
1. Inspect existing test infrastructure.
1. Identify the appropriate test level.
1. Define realistic success and failure cases.
1. Use existing utilities and fixtures.
1. Write behavior-focused assertions.
1. Run focused tests.
1. Run relevant regression tests.
1. Check quality gates.
1. Report results accurately.

Choose tests that provide meaningful confidence with manageable maintenance cost.

## 29. Review Checklist

### Test Design

- [ ] Test level matches the requirement.
- [ ] Expected behavior is clear.
- [ ] Success and failure cases are covered.
- [ ] Tests are independent.

### Quality

- [ ] Assertions focus on observable behavior.
- [ ] Fixtures are predictable.
- [ ] Mocking is appropriate.
- [ ] Flaky tests are investigated.

### Coverage

- [ ] Important business logic is tested.
- [ ] Critical workflows are covered.
- [ ] Accessibility checks are considered.
- [ ] Regression tests exist for important bug fixes.

### Verification

- [ ] Focused tests pass.
- [ ] Relevant regression tests pass.
- [ ] Type checking passes.
- [ ] Linting passes.
- [ ] Build passes.

### Reporting

- [ ] Executed checks are identified.
- [ ] Failed checks are reported.
- [ ] Unavailable checks are disclosed.
- [ ] No unsupported success claims are made.

## 30. Related References

- architecture-and-project-structure.md
- react-engineering.md
- nextjs-engineering.md
- typescript-and-code-quality.md
- accessibility-and-wcag.md
- frontend-security.md
- api-integration.md
- forms-and-validation.md
- state-management.md
- debugging-and-self-correction.md
- ci-cd-and-deployment.md

## 31. Official Resources

- Vitest: https://vitest.dev/
- Jest: https://jestjs.io/
- React Testing Library: https://testing-library.com/docs/react-testing-library/intro/
- Playwright: https://playwright.dev/docs/intro
- Cypress: https://docs.cypress.io/
- MSW: https://mswjs.io/
- Testing Library User Event: https://testing-library.com/docs/user-event/intro/
- axe-core: https://github.com/dequelabs/axe-core
- Web Vitals: https://web.dev/articles/vitals
