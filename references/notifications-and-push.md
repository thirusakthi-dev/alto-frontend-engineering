# Notifications and Push

## 1. Purpose

Define standards for implementing, modifying and maintaining frontend notification systems.

Support:

- Toast notifications.
- In-app notification centers.
- Notification badges.
- Success, error, warning and information messages.
- Browser notifications.
- Web Push.
- Service worker integration.
- Notification preferences.
- Permission management.
- Notification accessibility.
- Error handling and delivery states.

The objective is to provide timely, useful and accessible feedback without overwhelming users.

## 2. Understand Notification Types

Not all notifications serve the same purpose.

| Type | Purpose | Example |
| -------------------- | ----------------------------- | ------------------------ |
| Toast | Temporary feedback | Changes saved |
| Inline message | Feedback within a page | Invalid form input |
| Notification center | Persistent in-app updates | New assignment |
| Badge | Indicates pending activity | 3 unread messages |
| Browser notification | System-level notification | New message received |
| Web Push | Server-initiated notification | Important account update |

Choose the notification type according to the information's importance, urgency and expected lifetime.

Do not use a toast for every application event.

## 3. Inspect Before Implementation

Before building or changing notifications:

1. Inspect existing notification components.
1. Check installed toast or notification libraries.
1. Identify the application's state management approach.
1. Review existing API and event integrations.
1. Check whether a service worker already exists.
1. Inspect PWA configuration.
1. Identify backend notification capabilities.
1. Review authentication and authorization requirements.
1. Check existing notification preferences.

For existing projects, extend the current implementation where practical.

Do not introduce another notification library or service worker unnecessarily.

## 4. Toast Notifications

Toasts provide temporary feedback after an action.

Common examples:

- Record created.
- Changes saved.
- File uploaded.
- Request failed.
- Connection restored.
- Operation completed.

Guidelines:

- Keep messages short and understandable.
- Use clear success and failure descriptions.
- Avoid technical error messages.
- Provide a dismissal option where appropriate.
- Prevent excessive duplicate messages.
- Use appropriate durations.
- Allow important errors to remain visible longer.
- Avoid interrupting critical user workflows.

A toast should not be the only way to communicate essential information.

For important or persistent errors, use inline messages or a dedicated error state.

## 5. Notification Categories

Use a consistent notification model.

Common categories:

- Success.
- Error.
- Warning.
- Information.
- Loading.

Example:

```tsx
type NotificationType = "success" | "error" | "warning" | "info" | "loading";
```

Use consistent icons, colors and message styles.

Do not communicate notification meaning through color alone.

## 6. Notification API Design

Keep notification APIs simple and predictable.

Example:

```tsx
interface ToastOptions {
  title?: string;
  description?: string;
  duration?: number;
}

interface ToastAPI {
  success(message: string, options?: ToastOptions): void;
  error(message: string, options?: ToastOptions): void;
  warning(message: string, options?: ToastOptions): void;
  info(message: string, options?: ToastOptions): void;
}
```

This is an illustrative API, not a mandatory implementation.

Guidelines:

- Avoid excessive configuration.
- Keep notification types consistent.
- Allow persistent notifications when necessary.
- Support loading-to-success or loading-to-error updates where useful.
- Avoid exposing internal implementation details to consumers.

Reuse the project's existing notification API when available.

## 7. Notification Placement and Behavior

Choose placement according to the application layout.

Common positions:

- Top-right.
- Top-center.
- Bottom-right.
- Bottom-center.

Guidelines:

- Avoid covering important controls.
- Consider mobile safe areas.
- Handle multiple simultaneous messages.
- Limit visible notification stacks.
- Maintain readable spacing.
- Avoid unnecessary movement.
- Respect reduced-motion preferences.

Use a consistent notification container instead of rendering independent toast systems across features.

## 8. Accessibility

Notifications must be accessible.

Consider:

- Appropriate live regions.
- `role="status"` for non-urgent status updates.
- `role="alert"` for important messages that require immediate attention.
- Keyboard-accessible dismissal controls.
- Meaningful accessible names.
- Screen reader announcement timing.
- Sufficient color contrast.

Do not announce every minor update through an assertive live region.

Avoid repeated announcements that interrupt users.

A notification should remain understandable without relying only on an icon or color.

## 9. In-App Notification Center

A notification center stores and displays application notifications.

Common features:

- Notification list.
- Unread indicator.
- Read/unread state.
- Timestamp.
- Notification category.
- Related resource link.
- Mark as read.
- Mark all as read.
- Delete or dismiss.
- Pagination or infinite scrolling.

Possible data model:

```tsx
interface AppNotification {
  id: string;
  title: string;
  message: string;
  type: "info" | "success" | "warning" | "error";
  readAt: string | null;
  createdAt: string;
  href?: string;
}
```

Adapt the model to the actual backend contract.

Do not invent API fields or assume a particular notification storage design.

## 10. Notification Data and State

Separate server notification data from temporary UI feedback.

Examples:

- Toast visibility: local UI state.
- Notification list: server state.
- Unread count: derived or server-provided state.
- Notification preferences: persisted user settings.

For server-backed notifications:

- Reuse the existing API client.
- Handle loading and error states.
- Update read status through the appropriate API.
- Avoid unnecessary refetching.
- Keep unread counts consistent.
- Handle stale or duplicate events.

Use the project's established server-state solution.

## 11. Real-Time Notifications

Applications may receive updates through:

- WebSockets.
- Server-Sent Events.
- Polling.
- Existing real-time infrastructure.

Choose based on product requirements.

Consider:

- Connection lifecycle.
- Authentication.
- Reconnection.
- Duplicate events.
- Event ordering.
- Offline behavior.
- Resource usage.
- Cleanup when components unmount.

Do not create a persistent WebSocket connection inside every notification component.

Prefer a shared connection or existing real-time service where appropriate.

## 12. Browser Notifications

The browser Notifications API can display system-level notifications.

Before using it:

1. Check browser support.
1. Check the current notification permission.
1. Request permission only after a clear user action.
1. Explain why permission is useful.
1. Handle denied permissions gracefully.
1. Avoid repeatedly requesting permission.

Example:

```tsx
async function requestNotificationPermission() {
  if (!("Notification" in window)) {
    return "unsupported";
  }

  if (Notification.permission === "granted") {
    return "granted";
  }

  if (Notification.permission === "denied") {
    return "denied";
  }

  return Notification.requestPermission();
}
```

This code is intended for a browser environment.

Do not execute browser-only APIs during server rendering.

Do not assume permission will be granted.

## 13. Notification Permission UX

Permission should be requested when the user understands the benefit.

A good flow:

1. Explain the notification feature.
1. Let the user enable it.
1. Request browser permission following the user action.
1. Store the application's preference separately.
1. Show appropriate guidance if permission is denied.

Distinguish:

- Browser permission.
- Application preference.
- Server-side push subscription.

These are separate concepts.

Do not repeatedly prompt users who have declined permission.

## 14. Web Push Architecture

Web Push enables a server to send notifications to a subscribed browser even when the application page is not open, subject to browser and platform support.

Typical architecture:

```text
User
  |
  v
Frontend
  |
  | Request permission
  | Register service worker
  | Subscribe to push
  v
Browser Push Service
  |
  | Subscription details
  v
Backend
  |
  | Store subscription
  | Send push message
  v
Browser Push Service
  |
  v
Service Worker
  |
  v
System Notification
```

A typical implementation requires:

- HTTPS in production.
- A service worker.
- Notification permission.
- Push subscription.
- VAPID keys.
- Backend subscription storage.
- A server-side push sender.

Localhost is generally treated as a secure context for development.

Web Push is not simply a frontend-only feature.

## 15. Service Worker Responsibilities

A service worker can handle push events and notification clicks.

Common responsibilities:

- Receive push events.
- Parse notification payloads.
- Display notifications.
- Handle notification clicks.
- Open or focus relevant application pages.
- Handle notification actions where supported.

Keep service worker code focused.

Avoid putting unrelated application business logic into the service worker.

Check the project's existing service worker and PWA setup before creating another one.

## 16. Push Subscription Management

A push subscription contains information needed by the backend to send notifications.

Typical workflow:

1. Register the service worker.
1. Request notification permission.
1. Subscribe using the Push API.
1. Send subscription details to the backend.
1. Store the subscription securely.
1. Associate it with the authenticated user.
1. Remove or update subscriptions when necessary.

Consider:

- Subscription expiration.
- Multiple devices.
- Multiple browsers.
- User logout.
- Account changes.
- Permission revocation.
- Unsubscribe behavior.

Do not assume one user has only one subscription.

## 17. VAPID and Backend Integration

VAPID is used to identify the application server to push services.

Guidelines:

- Generate keys using an appropriate tool.
- Keep the private key on the server.
- Expose only the public key to the frontend.
- Validate subscription ownership.
- Authenticate subscription management endpoints.
- Handle expired subscriptions.
- Remove invalid subscriptions when appropriate.

Never expose the VAPID private key in frontend code.

Never commit private keys or credentials to source control.

Use the backend's established environment configuration.

## 18. Push Notification Security

Treat push payloads as untrusted input.

Consider:

- Authentication.
- Authorization.
- Subscription ownership.
- Payload validation.
- Rate limiting.
- Abuse prevention.
- Sensitive data exposure.
- Secure transport.
- Subscription cleanup.

Do not put passwords, access tokens or unnecessary sensitive information in notification payloads.

Notifications may appear on a locked device or shared screen.

Prefer minimal content and require authentication before showing protected information.

Never trust a notification click URL without validating its destination.

## 19. Notification Preferences

Users should control notification behavior where appropriate.

Possible preferences:

- Enable or disable browser notifications.
- Product updates.
- Account activity.
- Security alerts.
- Marketing messages.
- Email notifications.
- Push notifications.

Keep browser permission separate from application-level preferences.

Respect user preferences on both frontend and backend.

Do not send notifications for disabled categories unless a clearly defined mandatory security or service requirement applies.

## 20. Offline and Failure Handling

Handle:

- Unsupported browsers.
- Denied permission.
- Missing service worker.
- Failed subscription.
- Expired subscriptions.
- Network failures.
- Backend errors.
- Invalid payloads.
- Push delivery failures.

Do not make the application unusable when push notifications are unavailable.

Provide an appropriate fallback, such as an in-app notification center.

Do not claim a push notification was delivered merely because the backend accepted a send request.

Distinguish between queued, accepted, delivered and displayed states when the infrastructure provides that information.

## 21. Existing Notification System Modification

When changing an existing notification system:

1. Inspect the current implementation.
1. Identify toast and persistent notification mechanisms.
1. Review event and API integrations.
1. Check service worker registration.
1. Understand subscription storage.
1. Review permission handling.
1. Identify affected components.
1. Make the smallest reliable change.
1. Test permission, delivery and failure paths.
1. Verify existing notification behavior.

Do not register multiple competing service workers for the same scope.

Do not replace existing real-time infrastructure without a clear reason.

## 22. Testing

Test notification behavior at different levels.

### Component tests

- Toast rendering.
- Dismissal.
- Notification variants.
- Unread indicators.
- Loading and error states.
- Accessible announcements.

### Integration tests

- API integration.
- Mark-as-read behavior.
- Unread count updates.
- Permission handling.
- Subscription creation and removal.

### Browser tests

- Service worker registration.
- Push event handling.
- Notification click behavior.
- Permission denial.
- Unsupported browser behavior.

Use mocks carefully for browser APIs.

Verify actual push delivery in an appropriate test environment when the project supports it.

## 23. Common Anti-Patterns

Avoid:

- Toasts for every event.
- Duplicate notification systems.
- Repeated permission prompts.
- Requesting permission without context.
- Browser API access during server rendering.
- Exposing VAPID private keys.
- Sensitive information in push payloads.
- Unauthenticated subscription endpoints.
- Duplicate service worker registrations.
- Unmanaged real-time connections.
- Treating push acceptance as delivery confirmation.
- Making push mandatory for basic application functionality.

## 24. Decision Workflow

Before implementing notifications:

1. Identify whether feedback is temporary or persistent.
1. Select the correct notification type.
1. Inspect existing notification infrastructure.
1. Design an accessible notification experience.
1. Separate UI state from server state.
1. Determine whether real-time delivery is necessary.
1. Add browser permission only when justified.
1. Implement service worker and backend integration if required.
1. Secure subscription and payload handling.
1. Test success, failure and unsupported scenarios.

Start with in-app notifications when system-level push is not a requirement.

## 25. Review Checklist

### In-app notifications

- [ ] Messages are clear.
- [ ] Duplicate messages are controlled.
- [ ] Loading and failure states are handled.
- [ ] Accessibility announcements are appropriate.

### Notification center

- [ ] Read/unread behavior works.
- [ ] Unread count stays consistent.
- [ ] API failures are handled.
- [ ] Navigation targets are valid.

### Browser notifications

- [ ] Permission is requested after user intent.
- [ ] Denied permissions are handled.
- [ ] Unsupported browsers have a fallback.
- [ ] Browser APIs are used only in supported environments.

### Web Push

- [ ] Service worker is correctly registered.
- [ ] Subscription lifecycle is handled.
- [ ] Private credentials remain server-side.
- [ ] Backend endpoints are protected.
- [ ] Payloads avoid sensitive information.

### Verification

- [ ] Relevant tests pass.
- [ ] Existing notification behavior is preserved.
- [ ] Failure scenarios are tested.

## 26. Related References

- reusable-ui-components.md
- dialogs-modals-and-overlays.md
- layouts-and-navigation.md
- theming-and-dark-mode.md
- frontend-security.md
- api-integration.md
- testing-strategy.md
- environment-configuration.md

## 27. Official Resources

- MDN Notifications API: https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API
- MDN Push API: https://developer.mozilla.org/en-US/docs/Web/API/Push_API
- MDN Service Workers: https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API
- MDN Notification.requestPermission: https://developer.mozilla.org/en-US/docs/Web/API/Notification/requestPermission_static
- MDN PushManager: https://developer.mozilla.org/en-US/docs/Web/API/PushManager
- Web Push Protocol: https://datatracker.ietf.org/doc/html/rfc8030
- VAPID: https://datatracker.ietf.org/doc/html/rfc8292
