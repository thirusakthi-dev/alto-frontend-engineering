# Progressive Web Apps and Offline Support

## 1. Purpose

Define standards for building reliable Progressive Web Applications (PWAs) and providing offline capabilities.

A Progressive Web App uses web technologies to provide capabilities such as:

- Installability.
- App-like experiences.
- Offline access.
- Resource caching.
- Background capabilities.
- Push notifications.
- Responsive application experiences.

Not every frontend application needs to be a PWA.

Choose PWA features based on actual product requirements.

This reference covers:

- PWA fundamentals.
- Web app manifests.
- Service workers.
- Installability.
- Offline experiences.
- Cache Storage.
- Caching strategies.
- Background synchronization.
- Push notifications.
- Update lifecycle.
- Storage management.
- Security.
- Accessibility.
- Testing.
- Existing project PWA integration.

## 2. Inspect Before Implementation

Before adding PWA functionality:

1. Inspect the existing framework and version.
1. Understand the application routing architecture.
1. Check whether a service worker already exists.
1. Inspect the current web app manifest.
1. Review existing caching behavior.
1. Identify authentication and authorization requirements.
1. Understand API dependencies.
1. Inspect deployment and hosting configuration.
1. Check whether push notifications are required.
1. Review existing offline behavior.

For existing applications:

- Preserve existing service worker behavior.
- Avoid registering multiple service workers for the same scope.
- Check existing cache names and versions.
- Understand update behavior before changing it.
- Avoid clearing caches without understanding their contents.
- Verify that authenticated and private data is not exposed through shared caches.

Do not introduce a service worker simply to claim PWA support.

## 3. PWA Fundamentals

A PWA combines web application capabilities with selected browser and operating-system features.

Important technologies include:

| Technology | Purpose |
| ----------------- | --------------------------------------------------- |
| Web App Manifest | Application identity and installation metadata |
| Service Worker | Background request handling and caching |
| Cache Storage | Persistent request and response caching |
| IndexedDB | Structured browser-side storage |
| Notifications API | Browser notifications |
| Push API | Push message subscriptions |
| Background Sync | Deferred background synchronization where supported |

Browser support and installation behavior vary across platforms.

Do not assume every PWA capability works identically on every browser or operating system.

## 4. Web App Manifest

The web app manifest describes how an installable application should appear and behave.

Example:

```json
{
  "name": "Example Application",
  "short_name": "Example",
  "description": "An example progressive web application",
  "start_url": "/",
  "scope": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#111827",
  "icons": [
    {
      "src": "/icons/icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/icons/icon-512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
```

This is an example. Adjust the values to the actual application.

### Manifest Guidelines

- Use the real application name.
- Provide an appropriate short name.
- Use valid icon files.
- Define the correct `start_url`.
- Define an appropriate `scope`.
- Choose a suitable display mode.
- Keep theme colors consistent with the design system.
- Avoid placeholder metadata.

Do not assume the manifest alone makes an application installable.

The browser also evaluates applicable secure-context and installability requirements.

### Icons

Provide suitable application icons.

Consider:

- Standard square icons.
- Maskable icons where supported.
- High-resolution assets.
- Safe areas for maskable icons.
- Appropriate background treatment.

Do not simply stretch a small favicon into a large application icon.

## 5. Next.js PWA Setup

Next.js provides metadata conventions for web app manifests.

An App Router application can use:

```text
app/
├── layout.tsx
├── manifest.ts
└── ...
```

Example:

```ts
import type { MetadataRoute } from "next";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "Example Application",
    short_name: "Example",
    description: "An example progressive web application",
    start_url: "/",
    display: "standalone",
    background_color: "#ffffff",
    theme_color: "#111827",
    icons: [
      {
        src: "/icons/icon-192.png",
        sizes: "192x192",
        type: "image/png",
      },
      {
        src: "/icons/icon-512.png",
        sizes: "512x512",
        type: "image/png",
      },
    ],
  };
}
```

Check the installed Next.js version and current metadata conventions.

Service worker setup is separate from manifest generation.

Do not assume Next.js automatically provides complete service worker or offline functionality.

## 6. Service Workers

A service worker is a background script that can intercept supported network requests and manage caching.

Common responsibilities:

- Cache application resources.
- Provide offline responses.
- Handle selected network requests.
- Manage cache versions.
- Receive push events.
- Handle notification interactions.

A service worker runs separately from the page's main JavaScript context.

It does not have direct access to the DOM.

### Service Worker Lifecycle

Understand the lifecycle:

1. Registration.
1. Download.
1. Installation.
1. Waiting.
1. Activation.
1. Fetch and event handling.
1. Update.

An updated service worker may wait until existing controlled pages are closed before taking control.

Do not force activation without understanding the consequences.

### Registration

Example:

```ts
if ("serviceWorker" in navigator) {
  window.addEventListener("load", async () => {
    try {
      await navigator.serviceWorker.register("/sw.js");
    } catch (error) {
      console.error("Service worker registration failed", error);
    }
  });
}
```

This is a basic browser example.

For production applications:

- Use an appropriate registration lifecycle.
- Handle registration failures.
- Avoid duplicate registrations.
- Verify the service worker scope.
- Handle update notifications.
- Avoid registering in unsupported environments.
- Consider development and production behavior separately.

Do not copy this registration pattern blindly into a framework-managed PWA setup.

## 7. Service Worker Scope

A service worker controls pages and requests within its permitted scope.

For example:

```text
/sw.js
```

Typically controls requests within the root scope.

A service worker at:

```text
/app/sw.js
```

typically controls the `/app/` scope.

The scope depends on its script location and registration options, subject to browser restrictions.

Verify scope when implementing:

- Applications under a subpath.
- Multiple frontend applications.
- Multi-tenant routes.
- Separate public and authenticated areas.

Do not broaden the scope unnecessarily.

## 8. Caching Fundamentals

Cache Storage stores request and response pairs.

It is separate from:

- HTTP browser caching.
- Framework data caches.
- IndexedDB.
- JavaScript memory caches.
- TanStack Query caches.

Understand which layer owns each resource.

Do not cache everything indiscriminately.

### Common Cache Strategies

| Strategy | Behavior | Suitable use |
| ---------------------- | -------------------------------------- | -------------------------------------- |
| Cache First | Use cache, then network | Versioned static assets |
| Network First | Try network, then cache | Selected content and API data |
| Stale While Revalidate | Return cache and refresh in background | Suitable frequently accessed resources |
| Network Only | Always use network | Sensitive or real-time operations |
| Cache Only | Use an existing cache entry | Precached resources |

Choose a strategy based on data freshness and sensitivity.

## 9. Cache First

Cache First is useful for resources that can safely be reused.

Typical examples:

- Versioned images.
- Static fonts.
- Versioned CSS.
- Versioned JavaScript assets.

Conceptual flow:

```text
Request
  |
  v
Check Cache
  |
  +-- Found --> Return Cached Response
  |
  +-- Missing --> Fetch Network
                    |
                    v
                Cache Response
                    |
                    v
                Return Response
```

Be careful with cache invalidation and application versioning.

Do not keep outdated application code indefinitely.

## 10. Network First

Network First prioritizes fresh network data.

Typical candidates:

- Selected non-sensitive content.
- Public content feeds.
- Content where a recent cached response is acceptable as fallback.

Conceptual flow:

```text
Request
  |
  v
Try Network
  |
  +-- Success --> Update Cache --> Return Response
  |
  +-- Failure --> Check Cache
                   |
                   +-- Found --> Return Cached Response
                   |
                   +-- Missing --> Offline Fallback
```

Do not use a stale fallback when it would mislead users about important current information.

## 11. Stale While Revalidate

This strategy can return a cached response immediately while updating the cache in the background.

Suitable examples may include:

- Public content.
- Non-critical reference data.
- Resources that tolerate short-lived staleness.

Do not use it indiscriminately for:

- Account balances.
- Payment status.
- Permissions.
- Sensitive personal records.
- Frequently changing operational data.

Freshness requirements must determine the strategy.

## 12. Cache Versioning and Cleanup

Use clear cache names and versions.

Example:

```js
const CACHE_NAME = "app-static-v1";
```

When cache behavior or assets change:

1. Introduce an appropriate new cache version.
1. Precache required resources.
1. Activate the new service worker.
1. Remove obsolete caches owned by the application.
1. Verify the new application behavior.

Example cleanup:

```js
const CURRENT_CACHES = ["app-static-v2"];

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches
      .keys()
      .then((keys) =>
        Promise.all(
          keys
            .filter((key) => !CURRENT_CACHES.includes(key))
            .map((key) => caches.delete(key)),
        ),
      ),
  );
});
```

This is illustrative.

In a production application, filter cache names carefully.

Do not delete unrelated caches that may belong to other applications or integrations on the same origin.

## 13. Offline Experience

Offline support should be intentional.

Identify which features should work without a network connection.

Possible offline capabilities:

- Application shell.
- Previously viewed public content.
- Saved reference information.
- Draft forms.
- Locally available documents.
- Offline status indicators.

Possible online-only capabilities:

- Payments.
- Account changes.
- Live data.
- Permission-sensitive actions.
- Operations requiring server confirmation.

### Offline UX

Provide clear feedback.

Consider:

- Offline status indicator.
- Cached content indicator.
- Retry action.
- Last updated time.
- Offline fallback page.
- Unsaved changes warning.
- Synchronization status.

Do not silently show stale information as if it were live.

Do not show a successful result for an operation that has not reached the server.

## 14. Offline Fallback Pages

A useful offline fallback should explain:

- The connection is unavailable.
- Which content may still be accessible.
- Whether the current operation was saved.
- How to retry.

Example:

```text
You're offline.

Some previously viewed content may still be available.
Reconnect to continue this operation.
```

Use the application's actual tone and design system.

Do not create a generic offline page that hides the current task or loses user input.

## 15. Offline Data Storage

Use appropriate storage for different needs.

| Storage | Suitable purpose |
| -------------- | ----------------------------------- |
| Cache Storage | Request and response resources |
| IndexedDB | Structured offline application data |
| localStorage | Small synchronous preferences |
| sessionStorage | Short-lived tab/session state |

Avoid storing large datasets in localStorage.

### IndexedDB

Consider IndexedDB for:

- Drafts.
- Structured offline records.
- Queued operations.
- Locally saved content.

Define:

- Schema.
- Version upgrades.
- Cleanup.
- Storage limits.
- Conflict behavior.
- Sensitive data handling.

Browser storage can be evicted.

Do not treat browser storage as permanent or guaranteed storage.

## 16. Offline Form Submissions

Offline submissions require careful design.

A possible workflow:

1. Validate user input.
1. Save a draft locally.
1. Mark the operation as pending.
1. Detect network availability.
1. Submit when connectivity returns.
1. Confirm server success.
1. Update local state.
1. Handle conflicts or failures.

Important considerations:

- Duplicate submissions.
- Idempotency.
- Authentication expiry.
- Server validation.
- Data conflicts.
- User cancellation.
- Retry limits.

Do not assume that `navigator.onLine` guarantees the server is reachable.

It indicates browser connectivity information, not successful API access.

Always handle actual request failures.

## 17. Background Synchronization

Background Sync can defer selected work until connectivity returns in supporting browsers.

Potential use cases:

- Retrying queued submissions.
- Synchronizing non-critical user actions.
- Sending pending data.

Support varies across browsers and platforms.

Provide a fallback when Background Sync is unavailable.

Do not make essential application behavior depend entirely on Background Sync.

For important operations, provide a visible retry or synchronization mechanism.

## 18. Push Notifications

Push notifications can deliver messages even when the application page is not open, subject to browser and operating-system support.

They typically involve:

1. User permission.
1. Push subscription.
1. Application server.
1. Push service.
1. Service worker.
1. Notification interaction.

### Permission UX

- Explain why notifications are useful.
- Request permission after meaningful user interaction.
- Avoid requesting permission immediately on page load.
- Respect denial.
- Provide notification preferences.
- Avoid repeatedly prompting users.

### Security

- Keep push credentials on the server.
- Validate subscription ownership.
- Avoid sensitive information in notification payloads.
- Authenticate subscription management.
- Remove expired subscriptions.
- Avoid sending notifications to unauthorized users.

Do not assume permission guarantees delivery.

Push delivery is not guaranteed.

See `notifications-and-push.md`.

## 19. Installability and Install Experience

A PWA may be installable through supported browser and operating-system experiences.

Consider:

- Valid manifest.
- Suitable icons.
- Secure context.
- Appropriate start URL and scope.
- Service worker requirements where applicable.
- Browser-specific installation criteria.

### Install Prompt

Some browsers expose an installation prompt event.

Do not assume that event exists everywhere.

Use progressive enhancement:

- Detect support.
- Explain installation benefits.
- Provide platform-appropriate guidance.
- Avoid blocking application usage when installation is unavailable.

Do not create a fake install button that does nothing.

## 20. Application Updates

Service worker updates need careful handling.

A user may keep an older application version open while a new version is available.

Consider:

- Update detection.
- User notification.
- Refresh behavior.
- Cache cleanup.
- Compatibility between cached frontend and backend APIs.
- In-progress user work.

Example update message:

```text
A new version is available.
Refresh to update the application.
```

Avoid automatically refreshing users during important work.

Do not force immediate activation unless the application can safely handle existing clients and cached resources.

## 21. Security and Privacy

Service workers have powerful request-handling capabilities.

Follow security best practices.

- Serve the application over HTTPS in production.
- Validate all server-side operations.
- Avoid caching sensitive authenticated responses.
- Avoid storing credentials in Cache Storage.
- Do not trust client-side authorization.
- Use appropriate cache-control headers.
- Keep service worker scripts under application control.
- Avoid caching arbitrary third-party content.
- Review offline data retention.
- Protect private information in IndexedDB.
- Handle logout and account switching safely.

### Authentication and Caching

Be particularly careful with:

- Account-specific API responses.
- User profile information.
- Private documents.
- Authorization-dependent content.
- Shared-device sessions.

A shared browser cache can expose data across sessions if implemented incorrectly.

For sensitive resources, network-only behavior may be more appropriate.

Clear application-owned private data on logout when required.

Do not confuse clearing a client cache with revoking server authorization.

See `frontend-security.md` and `authentication-and-authorization.md`.

## 22. Development, Staging and Production

PWA behavior should be tested across environments.

Consider:

### Development

- Service worker debugging.
- Cache inspection.
- Hot reload compatibility.
- Avoiding stale development assets.

### Staging

- Production-like service worker behavior.
- Manifest validation.
- Offline tests.
- Update tests.
- HTTPS configuration.

### Production

- Correct service worker scope.
- Cache versioning.
- Update strategy.
- HTTPS.
- Monitoring.
- Rollback strategy.

Do not accidentally ship development caching behavior into production.

Do not assume a service worker update has propagated to every active user immediately.

See `environment-configuration.md`.

## 23. Performance Considerations

PWA functionality should not make the application slower.

Review:

- Service worker startup.
- Precache size.
- Cache storage usage.
- Network requests.
- Install prompt behavior.
- Background processing.
- Bundle size.
- Image and font caching.

Avoid precaching the entire application without a clear reason.

Precache only resources necessary for the intended offline experience.

Do not cache resources that are already efficiently handled by another appropriate caching layer unless there is a justified need.

See `performance-and-core-web-vitals.md`.

## 24. Testing and Debugging

Test PWA functionality in supported browsers and actual deployment environments.

### Functional Testing

Verify:

- Manifest is served correctly.
- Icons load.
- Service worker registers.
- Scope is correct.
- Resources are cached.
- Offline fallback works.
- Updates are handled.
- Push permission flows work where supported.
- Logout and account switching are safe.

### Browser Tools

Use:

- Chrome DevTools Application panel.
- Service worker inspection.
- Cache Storage inspection.
- IndexedDB inspection.
- Network throttling.
- Offline mode.
- Lighthouse PWA diagnostics where applicable.

### Device Testing

Test on actual target devices when possible.

Check:

- Installation behavior.
- Launch behavior.
- Offline navigation.
- Update behavior.
- Notification permission.
- Storage limitations.

Do not claim cross-browser support after testing only one desktop browser.

## 25. Existing Project PWA Integration

When introducing or modifying PWA functionality:

1. Inspect existing service worker registrations.
1. Inspect manifest and icon assets.
1. Understand cache ownership.
1. Identify offline requirements.
1. Define public and private resource policies.
1. Select suitable caching strategies.
1. Implement service worker changes incrementally.
1. Test installation and updates.
1. Test offline and online transitions.
1. Verify authentication and logout behavior.
1. Test supported browsers.
1. Check production deployment behavior.

Do not replace an existing service worker without reviewing its responsibilities.

Avoid unrelated changes to application architecture.

## 26. Common Anti-Patterns

Avoid:

- Adding a service worker without a requirement.
- Caching every request.
- Caching private responses publicly.
- Treating browser storage as permanent.
- Assuming `navigator.onLine` proves API availability.
- Claiming a queued operation succeeded before server confirmation.
- Registering multiple competing service workers.
- Deleting unrelated caches.
- Forcing refresh during important user work.
- Requesting notification permission immediately.
- Depending entirely on unsupported background capabilities.
- Pre-caching unnecessarily large assets.
- Ignoring logout and account switching.
- Assuming all browsers have identical installability behavior.
- Treating PWA support as proof of offline functionality.

## 27. Implementation Workflow

1. Identify actual PWA requirements.
1. Inspect the existing application.
1. Define offline functionality.
1. Design the manifest.
1. Choose a service worker approach.
1. Define cache ownership and strategies.
1. Implement offline experiences.
1. Add storage and synchronization only when needed.
1. Implement update handling.
1. Add push notifications only when required.
1. Review security and privacy.
1. Test supported browsers and devices.
1. Verify deployment and production behavior.

Prefer the simplest implementation that meets the requirements.

## 28. Review Checklist

### Manifest and Installation

- [ ] Manifest is valid.
- [ ] Application metadata is correct.
- [ ] Icons are appropriate.
- [ ] Start URL and scope are correct.
- [ ] Installability is tested on target platforms.

### Service Worker

- [ ] Registration is correct.
- [ ] Scope is understood.
- [ ] Update lifecycle is handled.
- [ ] Cache names are versioned.
- [ ] Obsolete caches are cleaned safely.

### Offline Behavior

- [ ] Offline requirements are defined.
- [ ] Cached content is identified clearly.
- [ ] Offline fallback works.
- [ ] Pending operations are handled honestly.
- [ ] Retry behavior is reliable.

### Security

- [ ] Sensitive responses are not cached publicly.
- [ ] Authentication behavior is tested.
- [ ] Logout cleanup is appropriate.
- [ ] Private local data is protected.
- [ ] Server authorization remains authoritative.

### Verification

- [ ] Online behavior works.
- [ ] Offline behavior works.
- [ ] Update behavior is tested.
- [ ] Target browsers are tested.
- [ ] Production configuration is checked.
- [ ] Unverified capabilities are reported honestly.

## 29. Related References

- anti-ai-slop-and-engineering-quality.md
- architecture-and-project-structure.md
- nextjs-engineering.md
- rendering-and-caching-strategies.md
- authentication-and-authorization.md
- api-integration.md
- state-management.md
- notifications-and-push.md
- frontend-security.md
- performance-and-core-web-vitals.md
- testing-strategy.md
- environment-configuration.md
- production-readiness.md

## 30. Official Resources

### PWA

- MDN Progressive Web Apps: https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps
- web.dev PWA: https://web.dev/explore/progressive-web-apps

### Web App Manifest

- MDN Manifest: https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest
- W3C Web App Manifest: https://www.w3.org/TR/appmanifest/

### Service Workers

- MDN Service Worker API: https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API
- web.dev Service Workers: https://web.dev/learn/pwa/service-workers

### Caching and Storage

- MDN Cache API: https://developer.mozilla.org/en-US/docs/Web/API/Cache
- MDN IndexedDB: https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API
- MDN Storage: https://developer.mozilla.org/en-US/docs/Web/API/Storage_API

### Push Notifications

- MDN Push API: https://developer.mozilla.org/en-US/docs/Web/API/Push_API
- MDN Notifications API: https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API

Always verify current browser support, framework integration and platform-specific installation behavior before implementation.
