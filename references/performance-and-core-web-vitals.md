# Performance and Core Web Vitals

## 1. Purpose

Define standards for measuring, diagnosing, improving and maintaining frontend application performance.

The agent must optimize applications based on actual performance problems rather than assumptions or arbitrary optimization preferences.

This reference covers:

- Core Web Vitals.
- Performance measurement.
- Rendering performance.
- React performance.
- Next.js performance.
- JavaScript and bundle optimization.
- Image optimization.
- Font optimization.
- Network performance.
- API performance.
- Caching.
- Code splitting.
- Lazy loading.
- Memory management.
- Third-party scripts.
- Runtime monitoring.
- Performance testing.
- Existing project optimization.

The objective is to deliver applications that load quickly, respond smoothly and remain efficient without sacrificing correctness, accessibility or maintainability.

## 2. Inspect Before Optimizing

Before changing performance-related code:

1. Inspect the framework and installed versions.
1. Understand the application architecture.
1. Inspect package dependencies.
1. Review build configuration.
1. Identify large bundles.
1. Inspect rendering behavior.
1. Review data-fetching patterns.
1. Identify duplicate API requests.
1. Inspect image and font loading.
1. Review caching configuration.
1. Check third-party scripts.
1. Review existing performance measurements.

For existing projects:

- Identify the actual bottleneck.
- Preserve working functionality.
- Avoid unnecessary rewrites.
- Avoid replacing libraries without evidence.
- Measure before and after important optimizations.
- Check for regressions.

Do not optimize code simply because it looks inefficient.

## 3. Performance Fundamentals

Consider performance across several dimensions.

| Area | What to evaluate |
| ------------------- | -------------------------------------- |
| Loading | How quickly meaningful content appears |
| Interactivity | How quickly the application responds |
| Visual stability | Whether content unexpectedly moves |
| Rendering | How efficiently the UI updates |
| Network | Requests, payloads and latency |
| JavaScript | Download, parsing and execution cost |
| Memory | Allocation, retention and leaks |
| Backend interaction | API response time and data transfer |

Performance is not one metric.

A page can load quickly but still have poor interaction responsiveness.

A page can score well in a lab test but perform poorly for real users.

## 4. Core Web Vitals

Core Web Vitals measure important aspects of real user experience.

The current primary metrics are:

- Largest Contentful Paint (LCP).
- Interaction to Next Paint (INP).
- Cumulative Layout Shift (CLS).

Evaluate these metrics using the 75th percentile of real user experiences, segmented by device type where possible.

### 4.1 Largest Contentful Paint (LCP)

Measures when the largest visible content element in the viewport is rendered.

<badge color="success">Good: 2.5 seconds or less</badge>

| Rating | LCP |
| ----------------- | --------------- |
| Good | ≤ 2.5 seconds |
| Needs improvement | > 2.5s and ≤ 4s |
| Poor | > 4 seconds |

Common causes of poor LCP:

- Slow server response.
- Large hero images.
- Render-blocking resources.
- Unoptimized fonts.
- Client-side rendering delays.
- Excessive JavaScript.
- Network waterfalls.
- Delayed critical resource loading.

Possible improvements:

- Improve server response time.
- Optimize the main content image.
- Prioritize critical resources appropriately.
- Reduce render-blocking resources.
- Reduce unnecessary client-side JavaScript.
- Improve caching.
- Avoid unnecessary client-side data dependencies for initial content.

Do not lazy-load the primary above-the-fold LCP image.

### 4.2 Interaction to Next Paint (INP)

Measures responsiveness across interactions during a page visit.

<badge color="success">Good: 200 milliseconds or less</badge>

| Rating | INP |
| ----------------- | ------------------- |
| Good | ≤ 200 ms |
| Needs improvement | > 200ms and ≤ 500ms |
| Poor | > 500 ms |

Common causes:

- Long-running JavaScript tasks.
- Expensive event handlers.
- Excessive synchronous computation.
- Large React updates.
- Heavy third-party scripts.
- Unnecessary rendering.
- Main-thread blocking.

Possible improvements:

- Reduce long tasks.
- Break up expensive computations.
- Move suitable work to Web Workers.
- Avoid unnecessary state updates.
- Optimize expensive rendering.
- Defer non-critical work.
- Reduce unnecessary event listeners.
- Avoid excessive third-party JavaScript.

Do not optimize every event handler with memoization without evidence.

### 4.3 Cumulative Layout Shift (CLS)

Measures unexpected layout movement during the page lifecycle.

<badge color="success">Good: 0.1 or less</badge>

| Rating | CLS |
| ----------------- | ---------------- |
| Good | ≤ 0.1 |
| Needs improvement | > 0.1 and ≤ 0.25 |
| Poor | > 0.25 |

Common causes:

- Images without reserved dimensions.
- Dynamically inserted content.
- Late-loading fonts.
- Ads and embeds without reserved space.
- Layout changes after data loading.
- Unstable component dimensions.

Possible improvements:

- Provide image dimensions or aspect ratios.
- Reserve space for dynamic content.
- Avoid inserting content above existing content unexpectedly.
- Use appropriate font loading strategies.
- Stabilize loading and skeleton layouts.
- Avoid unnecessary layout changes.

Not every layout movement contributes to CLS. Evaluate actual user-visible unexpected shifts.

## 5. Additional Performance Metrics

Core Web Vitals are not the entire performance picture.

Useful diagnostic metrics include:

| Metric | Purpose |
| ---------------------------- | --------------------------------------- |
| Time to First Byte (TTFB) | Initial server response |
| First Contentful Paint (FCP) | First rendered content |
| Total Blocking Time (TBT) | Lab diagnostic for main-thread blocking |
| Speed Index | Visual loading progression |
| Long Tasks | Extended main-thread work |
| JavaScript execution time | Runtime cost |
| Bundle size | Download and parsing cost |

Use the metrics appropriate to the problem.

Do not treat every diagnostic metric as a Core Web Vital.

## 6. Measuring Performance

Measure before changing code.

Useful tools:

- Chrome DevTools.
- Lighthouse.
- PageSpeed Insights.
- WebPageTest.
- Chrome Performance panel.
- Chrome Coverage.
- Bundle analyzers.
- React Developer Tools.
- Real User Monitoring (RUM).

### Lab Measurements

Lab tools simulate page loading under controlled conditions.

Useful for:

- Reproducing issues.
- Comparing implementations.
- Finding expensive scripts.
- Inspecting layout shifts.
- Diagnosing long tasks.

### Field Measurements

Field data represents actual user experiences.

Useful for:

- Real device performance.
- Network variation.
- Real interaction behavior.
- Production performance trends.

Prefer field data when evaluating real user experience.

Lab scores and field scores may differ.

Do not claim production performance improvements based only on a local development build.

## 7. Performance Budgets

Define performance budgets where appropriate.

Possible budgets include:

- Initial JavaScript size.
- Total JavaScript size.
- Initial CSS size.
- Image transfer size.
- Number of critical requests.
- Font transfer size.
- Route loading time.
- Core Web Vitals targets.

Example:

```text
Performance Budget

Initial JavaScript: project-defined limit
Initial CSS: project-defined limit
Hero image: optimized for actual dimensions
Fonts: limited required weights
Third-party scripts: reviewed and justified
Core Web Vitals: Good thresholds
```

These are examples, not universal size limits.

Choose budgets based on:

- Application complexity.
- Target devices.
- Network conditions.
- User requirements.
- Existing architecture.

Track budget changes over time.

Do not introduce arbitrary limits that make important functionality impractical.

## 8. JavaScript and Bundle Optimization

JavaScript affects download, parsing, compilation and execution.

Review:

- Dependency size.
- Duplicate packages.
- Unused imports.
- Large libraries.
- Unnecessary polyfills.
- Heavy client components.
- Dynamic imports.
- Tree shaking.
- Code splitting.

### Code Splitting

Load code when it is needed rather than including every feature in the initial bundle.

Possible candidates:

- Rich text editors.
- Charts.
- Complex visualizations.
- Large configuration tools.
- Rarely used dialogs.
- Heavy administrative features.

Example:

```tsx
import dynamic from "next/dynamic";

const Chart = dynamic(() => import("./chart"), {
  loading: () => <p>Loading chart...</p>,
});
```

This is an illustrative Next.js pattern. Check the installed version and component rendering requirements.

Do not dynamically import every component.

### Tree Shaking

Use compatible module formats and build configurations so unused exports can be eliminated.

Avoid importing large modules when smaller entry points are available.

Inspect the actual production bundle instead of assuming tree shaking worked.

### Dependency Review

Before removing or replacing a dependency:

1. Inspect actual usage.
1. Identify bundle contribution.
1. Check alternative implementations.
1. Evaluate maintenance cost.
1. Consider functionality and accessibility.
1. Measure the resulting build.

Do not replace a useful dependency with complex custom code solely to reduce a small amount of bundle size.

See `package-selection-and-ecosystem.md`.

## 9. React Rendering Performance

React rendering should remain predictable and efficient.

Understand:

- Component rendering.
- State ownership.
- Parent-child updates.
- Context propagation.
- Reconciliation.
- Expensive calculations.
- Lists and keys.
- Suspense.
- Server and Client Components.

### Avoid Unnecessary State

Do not store values that can be derived from existing state.

Example:

```tsx
const fullName = `${firstName} ${lastName}`;
```

Prefer deriving the value rather than maintaining another state variable synchronized through an effect.

### React.memo

Consider `React.memo` when:

- A component renders frequently.
- Its props remain stable.
- Rendering is meaningfully expensive.
- Profiling indicates an improvement.

Do not wrap every component in `React.memo`.

### useMemo and useCallback

Use memoization when it solves an actual problem.

Possible cases:

- Expensive calculations.
- Stable callback requirements for optimized children.
- Dependency stability for other hooks.
- Avoiding unnecessary expensive recomputation.

Do not add `useMemo` and `useCallback` everywhere.

### React Compiler

When a project uses React Compiler, understand which optimizations it already provides.

Do not introduce manual memoization patterns blindly.

Verify compiler configuration and installed versions before relying on compiler behavior.

### Large Lists

For very large lists, consider virtualization.

Possible libraries include:

- TanStack Virtual.
- React Virtuoso.

Do not virtualize small lists unnecessarily.

See `react-engineering.md`.

## 10. Next.js Performance

Next.js provides framework-level performance capabilities.

Use the features appropriate to the installed version and application architecture.

Consider:

- Server Components.
- Client Components.
- Streaming.
- Suspense.
- Static generation.
- Dynamic rendering.
- Caching.
- Image optimization.
- Font optimization.
- Dynamic imports.
- Route-level code splitting.

### Server and Client Components

Use Server Components where they reduce unnecessary client JavaScript and suit the feature.

Use Client Components when browser interaction or client-side state is required.

Avoid marking large component trees as Client Components without a reason.

Keep client boundaries as focused as practical.

### Data Fetching

Avoid:

- Duplicate requests.
- Unnecessary waterfalls.
- Fetching unused data.
- Fetching the same resource independently across multiple components without understanding caching behavior.

Consider:

- Parallel data fetching.
- Appropriate caching.
- Streaming.
- Pagination.
- Server-side aggregation.
- Request deduplication where supported.

Do not assume all framework requests are cached by default.

Check the installed Next.js version and current caching model.

### Rendering and Caching

Understand the application's configured rendering and cache behavior.

Distinguish between:

- Request memoization.
- Data caching.
- Route output caching.
- Browser caching.
- Client-side query caching.

For Next.js Cache Components, understand APIs such as:

- `use cache`.
- `cacheLife`.
- `cacheTag`.

For applications using the previous caching model, understand the relevant fetch and route configuration.

Do not mix caching approaches without understanding the project's configuration.

See `rendering-and-caching-strategies.md`.

## 11. Image Optimization

Images frequently contribute significantly to page transfer size and LCP.

Consider:

- Image dimensions.
- Format.
- Compression.
- Responsive sizing.
- Lazy loading.
- Priority.
- Aspect ratio.
- CDN delivery.
- Browser caching.

### Recommended Formats

Consider:

- AVIF.
- WebP.
- JPEG.
- PNG.
- SVG for suitable vector graphics.

Choose formats based on browser support, transparency requirements and image content.

### Guidelines

- Use appropriately sized images.
- Avoid delivering desktop-sized images to small mobile viewports unnecessarily.
- Reserve layout space.
- Avoid unnecessary image transformations.
- Lazy-load suitable below-the-fold images.
- Prioritize important above-the-fold images when justified.
- Avoid loading duplicate image variants unnecessarily.

### Next.js Image

Use the framework's image optimization capabilities where appropriate.

Example:

```tsx
import Image from "next/image";

export function ProductImage() {
  return (
    <Image
      src="/images/product.webp"
      alt="Wireless headphones"
      width={800}
      height={600}
      sizes="(max-width: 768px) 100vw, 50vw"
    />
  );
}
```

Use real image dimensions and appropriate `sizes` values.

Do not disable image optimization globally without understanding the consequences.

See the official Next.js Image documentation.

## 12. Font Optimization

Fonts can affect loading and layout stability.

Consider:

- Font file size.
- Number of weights.
- Variable fonts.
- Subsetting.
- Font formats.
- Preloading.
- Fallback fonts.
- `font-display`.
- Layout shifts.

Guidelines:

- Load only required font weights.
- Prefer efficient font formats.
- Avoid importing multiple unnecessary font families.
- Use appropriate fallbacks.
- Avoid unnecessary remote font requests.
- Reserve appropriate layout behavior.

For Next.js, consider `next/font` where suitable.

Do not preload every font file.

Preload only critical resources.

## 13. CSS and Animation Performance

Review expensive styling and animation behavior.

Prefer animating:

- `transform`.
- `opacity`.

Be cautious with frequent animation of:

- `width`.
- `height`.
- `top`.
- `left`.
- Layout-dependent properties.

These may trigger expensive layout or painting.

Guidelines:

- Avoid unnecessary continuous animations.
- Respect reduced-motion preferences.
- Avoid expensive blur and filter effects on large areas.
- Avoid excessive box shadows.
- Avoid unnecessary DOM complexity.
- Avoid layout thrashing.
- Batch layout reads and writes when writing imperative DOM code.

Use browser performance tools to identify actual rendering bottlenecks.

See `ui-design-quality-and-impeccable.md`.

## 14. Network Performance

Network requests can dominate loading time.

Review:

- Request count.
- Request size.
- Latency.
- Compression.
- Cache headers.
- Connection reuse.
- Request waterfalls.
- Third-party requests.
- Duplicate API calls.

Possible improvements:

- Reduce unnecessary requests.
- Fetch independent resources in parallel.
- Compress responses.
- Optimize payload sizes.
- Use pagination.
- Avoid over-fetching.
- Use suitable CDN delivery.
- Apply caching where safe.
- Cancel obsolete requests where appropriate.

Do not make requests sequentially when they are independent.

Do not introduce parallel requests when one request depends on another.

## 15. API and Data Performance

Frontend performance also depends on backend communication.

Consider:

- API response size.
- Pagination.
- Filtering.
- Sorting.
- Query duplication.
- Request cancellation.
- Debouncing.
- Caching.
- Optimistic updates.
- Background refetching.

### Avoid Over-Fetching

Request only the information required by the feature.

Use server-side pagination for large datasets when appropriate.

Do not download thousands of records simply to filter them in the browser.

### Avoid Request Waterfalls

When independent requests can execute concurrently, use an appropriate parallel approach.

### Search Requests

For search inputs:

- Consider debouncing.
- Cancel obsolete requests where supported.
- Avoid rendering stale responses.
- Handle empty and failed results.
- Keep user interaction responsive.

See `api-integration.md` and `state-management.md`.

## 16. Caching Strategy

Caching can improve response time and reduce repeated work.

Understand the different layers.

### Browser Cache

Uses HTTP caching behavior and response headers.

Consider:

- `Cache-Control`.
- `ETag`.
- `Last-Modified`.
- `Expires`.

### CDN Cache

Useful for distributing public static resources and appropriately cacheable responses.

### Framework Cache

Framework-specific data and route caching.

### Client Cache

Examples include TanStack Query and other server-state libraries.

### Important Rules

- Define cache ownership.
- Choose appropriate freshness.
- Understand invalidation.
- Avoid caching sensitive user-specific responses publicly.
- Avoid stale authorization data.
- Consider read-after-write requirements.
- Avoid duplicate cache layers without a clear purpose.

Caching must preserve data correctness and access control.

See `rendering-and-caching-strategies.md`.

## 17. Third-Party Script Performance

Third-party scripts may affect:

- Main-thread execution.
- Network requests.
- Page loading.
- Privacy.
- Layout stability.

Examples:

- Analytics.
- Advertising.
- Chat widgets.
- Customer support tools.
- Embedded media.
- Tracking scripts.

Guidelines:

- Review whether the script is necessary.
- Load it only where required.
- Defer or delay non-critical scripts where appropriate.
- Monitor its impact.
- Avoid duplicate integrations.
- Review data collection and security implications.

Do not delay essential functionality just to improve a synthetic performance score.

## 18. Memory and Resource Management

Watch for memory leaks and unnecessary resource retention.

Potential problems:

- Unremoved event listeners.
- Unmanaged subscriptions.
- Timers without cleanup.
- Unreleased object URLs.
- Large retained data structures.
- Unnecessary cached data.
- Repeated observer creation.
- Long-lived references to unused components or data.

Clean up resources when their lifecycle ends.

Example:

```tsx
useEffect(() => {
  const controller = new AbortController();

  fetch("/api/data", {
    signal: controller.signal,
  });

  return () => {
    controller.abort();
  };
}, []);
```

Handle abort errors appropriately in the actual application.

Do not add cleanup code for resources that do not require it.

## 19. Web Workers and Expensive Computation

Consider Web Workers for CPU-intensive operations that can be moved away from the main thread.

Possible use cases:

- Large data processing.
- Complex calculations.
- Parsing large files.
- Image processing.
- Computationally expensive transformations.

Do not use workers for trivial calculations.

Consider:

- Data transfer cost.
- Serialization.
- Worker lifecycle.
- Error handling.
- Browser compatibility.

Keep the implementation proportional to the computational benefit.

## 20. Responsive Performance

Test performance across different devices and network conditions.

Consider:

- Lower-powered mobile devices.
- Slower networks.
- Smaller viewports.
- Touch interactions.
- Image delivery.
- Font loading.
- Large JavaScript bundles.

Do not optimize exclusively for a high-end desktop.

Use responsive image delivery and avoid loading unnecessary desktop-only functionality on mobile where practical.

## 21. Monitoring Real User Performance

For production applications, consider Real User Monitoring (RUM).

Useful metrics:

- LCP.
- INP.
- CLS.
- TTFB.
- Navigation timing.
- Resource timing.
- JavaScript errors.
- Route-level performance.

Possible tools:

- web-vitals.
- Vercel Analytics.
- Vercel Speed Insights.
- Sentry.
- Datadog RUM.
- New Relic.

Choose tools based on the application's hosting and monitoring architecture.

Avoid installing multiple monitoring tools that duplicate the same purpose without justification.

### web-vitals

The `web-vitals` library can collect supported Core Web Vitals.

Example:

```tsx
import { onCLS, onINP, onLCP } from "web-vitals";

onCLS(console.log);
onINP(console.log);
onLCP(console.log);
```

This is a basic illustration.

In production:

- Send measurements to an appropriate endpoint.
- Associate metrics with useful route and device context.
- Avoid collecting unnecessary personal data.
- Do not send sensitive information.
- Avoid using console logging as the monitoring solution.

## 22. Performance Testing

Use different testing approaches.

### Lighthouse

Useful for:

- Lab performance audits.
- Identifying common issues.
- Comparing builds.

### PageSpeed Insights

Useful for:

- Field data where available.
- Lab diagnostics.
- Core Web Vitals analysis.

### Chrome DevTools

Useful for:

- Performance traces.
- Network inspection.
- Memory profiling.
- Coverage.
- Rendering diagnostics.

### Bundle Analyzers

Useful for:

- Identifying large dependencies.
- Understanding bundle composition.
- Finding duplicate packages.
- Comparing production builds.

### Production Monitoring

Useful for:

- Real user performance.
- Route-level issues.
- Device-specific problems.
- Performance regressions.

Do not treat one Lighthouse score as complete performance verification.

## 23. Performance Regression Prevention

For important applications, establish ongoing performance checks.

Consider:

- Bundle size comparisons.
- Performance budgets.
- Lighthouse CI.
- Route-level performance checks.
- Real user monitoring.
- Dependency review.
- Build analysis.

Avoid blocking every deployment on unstable synthetic performance scores.

Use meaningful thresholds and repeatable environments.

## 24. Existing Project Performance Improvements

When optimizing an existing application:

1. Identify the affected route or feature.
1. Reproduce the performance issue.
1. Collect a baseline measurement.
1. Inspect rendering and network behavior.
1. Identify the largest bottleneck.
1. Choose the smallest effective change.
1. Implement the optimization.
1. Run relevant functional tests.
1. Measure again under comparable conditions.
1. Check for regressions.
1. Report measured results and limitations.

Prioritize high-impact issues.

Examples:

- Large initial JavaScript bundle.
- Slow LCP image.
- Repeated API requests.
- Long-running event handlers.
- Layout shifts.
- Expensive list rendering.

Do not rewrite the entire application to fix one performance bottleneck.

## 25. Common Performance Anti-Patterns

Avoid:

- Optimizing without measurement.
- Excessive memoization.
- Unnecessary `useEffect` usage.
- Large client component boundaries.
- Loading every feature immediately.
- Unnecessary dynamic imports.
- Oversized images.
- Lazy-loading critical content.
- Loading unnecessary font weights.
- Duplicate API requests.
- Sequential independent requests.
- Excessive third-party scripts.
- Over-fetching data.
- Unnecessary global state updates.
- Uncontrolled cache invalidation.
- Caching private responses publicly.
- Optimizing only for Lighthouse scores.
- Sacrificing accessibility for speed.

## 26. Performance Decision Workflow

Before optimizing:

1. Identify the performance problem.
1. Measure the current behavior.
1. Determine the responsible layer.
1. Inspect relevant code and dependencies.
1. Understand the trade-offs.
1. Choose the smallest effective change.
1. Implement the optimization.
1. Run functional and regression tests.
1. Measure the result again.
1. Document meaningful improvements.

Do not optimize based solely on assumptions.

## 27. Review Checklist

### Measurement

- [ ] Baseline measurements collected where appropriate.
- [ ] Actual bottlenecks identified.
- [ ] Lab and field metrics distinguished.
- [ ] Target devices considered.

### Loading

- [ ] Initial JavaScript reviewed.
- [ ] Critical images optimized.
- [ ] Fonts reviewed.
- [ ] Unnecessary requests removed.
- [ ] Code splitting considered where appropriate.

### Runtime

- [ ] Expensive rendering reviewed.
- [ ] Long tasks investigated.
- [ ] Large lists handled appropriately.
- [ ] Memory and cleanup considered.
- [ ] Third-party scripts reviewed.

### Data and Caching

- [ ] Duplicate requests investigated.
- [ ] API payloads are appropriate.
- [ ] Caching behavior understood.
- [ ] Cache invalidation is correct.
- [ ] Sensitive responses are not publicly cached.

### User Experience

- [ ] LCP considered.
- [ ] INP considered.
- [ ] CLS considered.
- [ ] Responsive performance considered.
- [ ] Accessibility is preserved.

### Verification

- [ ] Functional tests executed.
- [ ] Relevant build checks executed.
- [ ] Performance measured after changes.
- [ ] Regressions checked.
- [ ] Results and limitations reported honestly.

## 28. Related References

- anti-ai-slop-and-engineering-quality.md
- architecture-and-project-structure.md
- react-engineering.md
- nextjs-engineering.md
- rendering-and-caching-strategies.md
- typescript-and-code-quality.md
- global-styles-and-design-tokens.md
- package-selection-and-ecosystem.md
- api-integration.md
- state-management.md
- testing-strategy.md
- frontend-security.md
- observability-and-monitoring.md
- debugging-and-self-correction.md
- production-readiness.md

## 29. Official Resources

### Core Web Vitals

- https://web.dev/articles/vitals
- https://web.dev/articles/lcp
- https://web.dev/articles/inp
- https://web.dev/articles/cls

### Performance Measurement

- Lighthouse: https://developer.chrome.com/docs/lighthouse/
- PageSpeed Insights: https://pagespeed.web.dev/
- Chrome DevTools: https://developer.chrome.com/docs/devtools/performance/
- WebPageTest: https://www.webpagetest.org/

### React and Next.js

- React Performance: https://react.dev/reference/react/Profiler
- React Compiler: https://react.dev/learn/react-compiler
- Next.js Performance: https://nextjs.org/docs/app/guides/production-checklist
- Next.js Image: https://nextjs.org/docs/app/api-reference/components/image
- Next.js Font: https://nextjs.org/docs/app/getting-started/fonts

### Web Platform

- MDN Performance: https://developer.mozilla.org/en-US/docs/Web/Performance
- MDN Web Workers: https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API
- Resource Timing: https://developer.mozilla.org/en-US/docs/Web/API/Performance_API/Resource_timing

### Monitoring

- web-vitals: https://github.com/GoogleChrome/web-vitals
- Sentry: https://docs.sentry.io/
- Vercel Speed Insights: https://vercel.com/docs/speed-insights

Always verify current framework APIs and browser capabilities before implementation.
