# Observability and Monitoring

## 1. Purpose

Define standards for observing, monitoring and diagnosing frontend applications in development, staging and production.

Observability helps engineers understand application behavior using collected evidence.

This reference covers:

- Frontend error monitoring.
- Application logging.
- Performance monitoring.
- Real User Monitoring (RUM).
- API monitoring.
- Distributed tracing.
- Session and user context.
- Error reporting.
- Monitoring dashboards.
- Alerting.
- Privacy and security.
- Existing project monitoring improvements.

The objective is to detect meaningful problems, understand their causes and improve application reliability without collecting unnecessary data.

## 2. Inspect Before Implementation

Before adding monitoring:

1. Inspect the existing monitoring tools.
1. Review error reporting integrations.
1. Identify the frontend hosting platform.
1. Understand the backend architecture.
1. Review API communication.
1. Inspect existing logging conventions.
1. Check environment separation.
1. Identify existing performance measurements.
1. Review privacy requirements.
1. Understand alerting and incident workflows.

For existing applications:

- Reuse existing integrations where appropriate.
- Avoid duplicate error reporting.
- Preserve existing monitoring configuration.
- Avoid exposing secrets in logs.
- Do not introduce expensive monitoring services without justification.

Do not install multiple tools that perform the same monitoring function without a clear reason.

## 3. Observability Fundamentals

Understand the differences between monitoring and observability.

**Monitoring** tracks known conditions and signals.

**Observability** helps engineers investigate behavior and understand problems that were not necessarily anticipated.

Three commonly used observability signals are:

| Signal | Purpose |
| ------- | ---------------------------------------- |
| Logs | Records of application events |
| Metrics | Numerical measurements over time |
| Traces | The path of an operation across services |

Frontend applications can also collect:

- JavaScript errors.
- Unhandled promise rejections.
- API failures.
- Navigation timing.
- Core Web Vitals.
- User interaction failures.
- Browser and device context.

Collect only information that serves a clear operational purpose.

## 4. Environment-Aware Monitoring

Monitoring should distinguish between environments.

Typical environments:

- Development.
- Staging.
- Production.

Use environment-specific configuration.

Example:

```ts
export const monitoringConfig = {
  environment: process.env.NODE_ENV,
  enabled: process.env.NEXT_PUBLIC_MONITORING_ENABLED === "true",
};
```

This is illustrative. Use the project's actual environment configuration and framework conventions.

Guidelines:

- Avoid sending development noise into production dashboards.
- Use separate projects or environments when appropriate.
- Identify the application version.
- Include release information where supported.
- Avoid exposing internal environment variables to the browser.
- Do not enable production-only behavior accidentally in development.

See `environment-configuration.md`.

## 5. Frontend Error Monitoring

Frontend error monitoring helps detect problems affecting real users.

Common error categories:

- JavaScript runtime errors.
- Unhandled promise rejections.
- React rendering failures.
- Failed API requests.
- Resource loading failures.
- Chunk loading errors.
- Hydration errors.
- Authentication failures.
- Browser compatibility issues.

Useful tools include:

- Sentry.
- Bugsnag.
- Rollbar.
- Datadog RUM.
- New Relic Browser.
- Hosting-platform monitoring.

Choose based on the application's needs, budget and infrastructure.

### Error Boundaries

Use React Error Boundaries to handle rendering failures in appropriate component boundaries.

Example:

```tsx
"use client";

import { Component, type ErrorInfo, type ReactNode } from "react";

type Props = {
  children: ReactNode;
};

type State = {
  hasError: boolean;
};

export class ErrorBoundary extends Component<Props, State> {
  state: State = {
    hasError: false,
  };

  static getDerivedStateFromError(): State {
    return {
      hasError: true,
    };
  }

  componentDidCatch(error: Error, info: ErrorInfo) {
    reportError(error, {
      componentStack: info.componentStack,
    });
  }

  render() {
    if (this.state.hasError) {
      return <p>Something went wrong.</p>;
    }

    return this.props.children;
  }
}
```

`reportError` represents the application's monitoring integration. Implement it using the selected provider.

This example demonstrates the concept, not a complete production error boundary.

Guidelines:

- Show a useful fallback.
- Preserve application recovery options.
- Report meaningful error context.
- Avoid exposing internal stack traces to users.
- Provide retry or navigation options when appropriate.
- Avoid reporting the same error repeatedly.

An Error Boundary does not catch every possible error. Handle asynchronous errors, event-handler failures and server-side failures through appropriate mechanisms.

## 6. Global Error Handling

Capture important unhandled failures where appropriate.

Potential browser events include:

- `error`.
- `unhandledrejection`.

Example:

```ts
window.addEventListener("unhandledrejection", (event) => {
  reportError(event.reason);
});
```

This is an illustrative pattern.

Before adding global handlers:

- Check whether the monitoring SDK already installs them.
- Avoid duplicate reports.
- Filter expected failures.
- Avoid reporting user-cancelled operations as application errors.
- Avoid exposing sensitive information.

Do not use global error handlers as a replacement for proper local error handling.

## 7. Application Logging

Logs should provide useful diagnostic information.

Common levels:

| Level | Purpose |
| ----- | ---------------------------------------------- |
| Debug | Detailed development information |
| Info | Expected application events |
| Warn | Unexpected but recoverable situations |
| Error | Failed operations requiring attention |
| Fatal | Critical application failures, where supported |

Logging should be structured where practical.

Example:

```ts
logger.error("Failed to load dashboard", {
  route: "/dashboard",
  operation: "load_dashboard",
  errorCode: "DASHBOARD_LOAD_FAILED",
});
```

Avoid logging:

- Passwords.
- Access tokens.
- Refresh tokens.
- Session identifiers.
- API secrets.
- Payment details.
- Sensitive personal information.
- Unnecessary request or response bodies.

### Production Logging

Production logs should be:

- Meaningful.
- Structured.
- Environment-aware.
- Safe.
- Searchable.
- Consistent.

Avoid excessive console logging in production.

Do not suppress all console output without understanding whether it contains useful diagnostics.

## 8. API Monitoring

Frontend applications depend on backend services.

Monitor important API behavior.

Useful measurements:

- Request count.
- Response time.
- Failure rate.
- Timeout rate.
- HTTP status distribution.
- Retry count.
- Payload size.
- Endpoint-level performance.

Example:

```ts
async function monitoredRequest<T>(
  operation: () => Promise<T>,
  operationName: string,
): Promise<T> {
  const startedAt = performance.now();

  try {
    return await operation();
  } catch (error) {
    reportError(error, {
      operation: operationName,
    });

    throw error;
  } finally {
    const duration = performance.now() - startedAt;

    recordMetric("api_request_duration", duration, {
      operation: operationName,
    });
  }
}
```

This is illustrative. Implement `reportError` and `recordMetric` through the chosen monitoring provider.

Guidelines:

- Use consistent operation names.
- Avoid logging sensitive query parameters.
- Avoid recording full authorization headers.
- Distinguish expected failures from application defects.
- Monitor slow endpoints.
- Track repeated failures.
- Preserve meaningful error information.

Do not record every request indefinitely if it creates unnecessary cost or privacy risk.

See `api-integration.md`.

## 9. Performance Monitoring

Monitor real application performance.

Important measurements include:

- LCP.
- INP.
- CLS.
- TTFB.
- Route navigation time.
- API latency.
- Resource loading time.
- JavaScript errors.

Use Real User Monitoring (RUM) to understand actual user experiences.

Possible tools:

- web-vitals.
- Sentry.
- Vercel Speed Insights.
- Datadog RUM.
- New Relic Browser.

Track meaningful performance changes over time.

Do not use one synthetic Lighthouse score as the only production performance measurement.

See `performance-and-core-web-vitals.md`.

## 10. Distributed Tracing

A user action may involve multiple services.

Example:

```text
User Interaction
      |
      v
Frontend
      |
      v
API Gateway
      |
      v
Backend Service
      |
      v
Database
```

Distributed tracing helps follow an operation across service boundaries.

Consider:

- Trace identifiers.
- Span identifiers.
- Request correlation.
- Service boundaries.
- Timing information.
- Error propagation.

### Trace Context

Use standardized trace propagation where supported.

W3C Trace Context defines headers such as:

- `traceparent`.
- `tracestate`.

Do not generate incompatible custom tracing formats when standardized propagation is available.

Ensure trace identifiers do not expose sensitive information.

Do not assume a frontend trace alone provides complete visibility into backend or database behavior.

## 11. OpenTelemetry

OpenTelemetry provides vendor-neutral instrumentation and telemetry standards.

It supports:

- Traces.
- Metrics.
- Logs.
- Context propagation.

Consider OpenTelemetry when:

- The application has multiple services.
- Distributed tracing is needed.
- Vendor neutrality matters.
- Existing infrastructure supports it.

Before introducing it:

1. Check the existing monitoring architecture.
1. Verify browser instrumentation support.
1. Review SDK maturity.
1. Review bundle and runtime costs.
1. Understand data collection.
1. Configure sampling appropriately.

Do not assume every server-side OpenTelemetry package is suitable for browser execution.

Use browser-compatible packages and follow their official guidance.

Official documentation: https://opentelemetry.io/docs/

## 12. Session and User Context

Context can make error investigation easier.

Potentially useful context:

- Application version.
- Environment.
- Route.
- Browser family.
- Operating system.
- Device category.
- Locale.
- Feature name.
- Non-sensitive account or tenant reference where justified.

Avoid collecting unnecessary identity information.

Use pseudonymous identifiers where appropriate.

Do not include:

- Passwords.
- Tokens.
- Full personal records.
- Sensitive form values.
- Private API payloads.

Do not assume a user's identity is necessary to diagnose every error.

## 13. Session Replay

Session replay can help reproduce user-facing issues.

It may capture:

- Navigation.
- Clicks.
- UI transitions.
- Form interactions.
- Visual state changes.

Before enabling session replay:

- Review privacy requirements.
- Mask sensitive fields.
- Exclude authentication inputs.
- Exclude payment information.
- Review recording permissions.
- Configure sampling.
- Limit retention.
- Inform users where required.

Never capture passwords or sensitive data for convenience.

Session replay is optional and should be justified by a real debugging need.

## 14. Monitoring Dashboards

Dashboards should answer operational questions.

Useful dashboard sections:

### Application Health

- Application availability.
- JavaScript error rate.
- Failed navigation count.
- Error trends.
- Release comparison.

### Performance

- LCP.
- INP.
- CLS.
- TTFB.
- Route-level loading.
- API response times.

### API Health

- Request volume.
- Failure rate.
- Slow endpoints.
- Timeout count.
- HTTP status distribution.

### Release Health

- New errors after deployment.
- Regression trends.
- Version comparisons.
- Affected application versions.

Avoid dashboards containing many metrics without a clear purpose.

## 15. Alerting

Alerts should identify actionable problems.

Possible alerts:

- Sudden increase in JavaScript errors.
- High API failure rate.
- Critical endpoint latency.
- Application availability issues.
- Significant Core Web Vitals regression.
- Unusual authentication failure patterns.

Define:

- Severity.
- Threshold.
- Evaluation window.
- Responsible team.
- Notification channel.
- Expected response.

Avoid alerts for every small fluctuation.

Too many noisy alerts reduce the value of monitoring.

Use appropriate thresholds based on actual application traffic and behavior.

## 16. Release and Version Tracking

Associate telemetry with application releases.

Useful information:

- Release identifier.
- Commit reference.
- Deployment environment.
- Build version.
- Deployment timestamp.

This helps answer:

- Did a new release introduce this error?
- Which version is affected?
- Did performance regress after deployment?
- Did a rollback resolve the issue?

Do not expose sensitive deployment information publicly.

Ensure source maps are uploaded securely when the monitoring provider supports them.

Avoid publicly exposing source maps if they reveal internal implementation details unnecessarily.

## 17. Privacy and Security

Observability must follow security and privacy requirements.

Guidelines:

- Minimize collected data.
- Redact sensitive values.
- Protect monitoring credentials.
- Restrict dashboard access.
- Use suitable data retention.
- Review third-party monitoring providers.
- Avoid unnecessary user tracking.
- Apply consent requirements where applicable.
- Prevent secrets from entering logs.
- Protect telemetry transport.

Monitoring systems can become a source of sensitive data exposure.

Treat telemetry as potentially sensitive application data.

See `frontend-security.md`.

## 18. Cost and Sampling

Monitoring can generate significant event volume.

Consider:

- Error event sampling.
- Trace sampling.
- Session replay sampling.
- Retention limits.
- High-volume endpoint filtering.
- Duplicate event suppression.
- Environment filtering.

Do not discard all low-frequency errors automatically.

Prioritize events based on user impact and diagnostic value.

Review provider pricing and quotas before enabling high-volume features.

## 19. Development and Staging

Monitoring behavior should differ appropriately across environments.

### Development

- Useful local diagnostics.
- No unnecessary production alerts.
- Avoid sending sensitive local data.
- Preserve readable error messages.

### Staging

- Validate production-like instrumentation.
- Verify source maps.
- Test alerts where appropriate.
- Confirm environment labels.
- Verify release identification.

### Production

- Monitor real user impact.
- Protect telemetry.
- Track releases.
- Review alerts.
- Maintain incident visibility.

Do not assume that working local instrumentation guarantees working production monitoring.

## 20. Incident Investigation Workflow

When an incident occurs:

1. Identify the affected environment.
1. Determine the affected route or feature.
1. Review the time window.
1. Check error and performance trends.
1. Identify affected releases.
1. Inspect relevant traces and logs.
1. Reproduce the issue where possible.
1. Identify the root cause.
1. Implement a targeted fix.
1. Verify the fix.
1. Monitor after deployment.
1. Record important findings.

Do not immediately hide an error or suppress an alert without understanding its cause.

## 21. Existing Project Monitoring Improvements

When improving monitoring in an existing application:

1. Inspect current integrations.
1. Identify monitoring gaps.
1. Review privacy and data exposure.
1. Define the most important signals.
1. Avoid duplicate instrumentation.
1. Introduce changes incrementally.
1. Verify event collection.
1. Test environment separation.
1. Test source map and release integration.
1. Verify dashboards and alerts.
1. Measure monitoring overhead.
1. Document limitations.

Preserve existing telemetry where useful.

Do not replace a functioning monitoring system solely because another tool is more popular.

## 22. Common Anti-Patterns

Avoid:

- Installing multiple overlapping monitoring SDKs.
- Logging secrets or personal data.
- Reporting every expected cancellation as an error.
- Ignoring production JavaScript errors.
- Collecting telemetry without a clear purpose.
- Treating console logging as complete observability.
- Creating noisy alerts.
- Monitoring only backend services.
- Monitoring only synthetic performance scores.
- Ignoring release identifiers.
- Uploading sensitive source maps publicly.
- Enabling session replay without privacy review.
- Assuming frontend traces represent the entire backend operation.
- Hiding errors instead of investigating them.
- Claiming monitoring works without verifying event delivery.

## 23. Implementation Workflow

1. Understand the application architecture.
1. Inspect current monitoring.
1. Identify operational requirements.
1. Choose a suitable provider.
1. Configure environment separation.
1. Add error reporting.
1. Add meaningful performance metrics.
1. Instrument important API operations.
1. Add trace propagation where justified.
1. Configure release tracking.
1. Create actionable dashboards.
1. Configure appropriate alerts.
1. Review privacy and security.
1. Test in staging.
1. Verify production telemetry.

Prefer the smallest monitoring setup that provides sufficient operational visibility.

## 24. Review Checklist

### Error Monitoring

- [ ] Runtime errors are captured.
- [ ] Unhandled failures are considered.
- [ ] Duplicate reports are avoided.
- [ ] Useful diagnostic context is included.
- [ ] User-facing errors remain safe.

### Logging and Metrics

- [ ] Logs are meaningful.
- [ ] Sensitive values are excluded.
- [ ] API failures are monitored.
- [ ] Important performance metrics are tracked.
- [ ] Monitoring is environment-aware.

### Tracing and Releases

- [ ] Trace propagation is configured where needed.
- [ ] Release identifiers are available.
- [ ] Source maps are handled securely.
- [ ] Deployment regressions can be investigated.

### Privacy and Operations

- [ ] Telemetry collection is justified.
- [ ] Sensitive data is masked.
- [ ] Retention and access are appropriate.
- [ ] Alerts are actionable.
- [ ] Monitoring overhead is reasonable.

### Verification

- [ ] Events reach the intended provider.
- [ ] Staging behavior is tested.
- [ ] Production configuration is checked.
- [ ] Monitoring failures are handled.
- [ ] Unverified behavior is reported honestly.

## 25. Related References

- anti-ai-slop-and-engineering-quality.md
- architecture-and-project-structure.md
- nextjs-engineering.md
- api-integration.md
- frontend-security.md
- performance-and-core-web-vitals.md
- debugging-and-self-correction.md
- testing-strategy.md
- ci-cd-and-deployment.md
- environment-configuration.md
- production-readiness.md

## 26. Official Resources

### Monitoring and Error Reporting

- Sentry: https://docs.sentry.io/
- Datadog RUM: https://docs.datadoghq.com/real_user_monitoring/
- New Relic Browser: https://docs.newrelic.com/docs/browser/

### OpenTelemetry

- Documentation: https://opentelemetry.io/docs/
- JavaScript: https://opentelemetry.io/docs/languages/js/

### Web Performance

- web-vitals: https://github.com/GoogleChrome/web-vitals
- Performance API: https://developer.mozilla.org/en-US/docs/Web/API/Performance_API
- Resource Timing: https://developer.mozilla.org/en-US/docs/Web/API/Performance_API/Resource_timing

### Browser Error Handling

- Window error event: https://developer.mozilla.org/en-US/docs/Web/API/Window/error_event
- Unhandled rejection: https://developer.mozilla.org/en-US/docs/Web/API/Window/unhandledrejection_event

### Distributed Tracing

- W3C Trace Context: https://www.w3.org/TR/trace-context/

Always verify provider APIs, pricing, browser compatibility and privacy requirements before implementation.
