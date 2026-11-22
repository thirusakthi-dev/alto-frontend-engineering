# Modals and Notifications

## 1. Purpose

Demonstrate how to build and maintain accessible overlay and notification systems in React applications.

This example covers:

- Dialogs and modals.
- Confirmation dialogs.
- Drawers and sheets.
- Popovers and dropdown menus.
- Toast notifications.
- Inline notifications.
- Notification centers.
- Browser notifications.
- Web Push considerations.
- Focus management.
- Keyboard interaction.
- Responsive behavior.

The goal is to provide predictable, accessible interactions without introducing unnecessary overlay or notification libraries.

## 2. Core Principles

1. Prefer native browser behavior or established accessible primitives.
1. Use the correct interaction pattern for each component.
1. Manage focus correctly.
1. Support keyboard interaction.
1. Prevent background interaction when a modal requires it.
1. Provide clear dismissal behavior.
1. Keep notification messages meaningful.
1. Avoid excessive notifications.
1. Handle asynchronous operations honestly.
1. Preserve existing component and design-system conventions.

## 3. Component Categories

| Component | Purpose |
| -------------------- | ---------------------------------------- |
| Dialog | Focused interaction requiring attention |
| Confirmation dialog | Confirm a potentially destructive action |
| Drawer | Side-panel interaction |
| Popover | Contextual content |
| Dropdown menu | Action or navigation menu |
| Tooltip | Short supplementary information |
| Toast | Temporary status feedback |
| Inline alert | Persistent contextual feedback |
| Notification center | Collection of application notifications |
| Browser notification | OS-level notification |
| Web Push | Server-initiated browser notification |

Do not use a modal for every interaction.

Choose the simplest pattern that supports the user's task.

## 4. Suggested Structure

```text
src/
├── components/
│   ├── ui/
│   │   ├── dialog.tsx
│   │   ├── alert-dialog.tsx
│   │   ├── drawer.tsx
│   │   ├── popover.tsx
│   │   └── tooltip.tsx
│   └── feedback/
│       ├── toast.tsx
│       ├── toast-provider.tsx
│       └── inline-alert.tsx
├── features/
│   └── notifications/
│       ├── components/
│       ├── services/
│       ├── hooks/
│       └── types/
└── lib/
    └── notifications/
        └── notification-config.ts
```

This is an illustrative structure.

Do not create all these files when the application only needs one or two components.

## 5. Inspect Existing Components First

Before implementing overlays or notifications:

1. Check whether the project already has a dialog primitive.
1. Inspect the existing UI library.
1. Review existing toast behavior.
1. Check global stacking and z-index conventions.
1. Review theme tokens.
1. Identify existing focus-management utilities.
1. Inspect existing tests.
1. Reuse the existing implementation where appropriate.

Do not introduce a second overlay or notification system unnecessarily.

## 6. Dialogs and Modals

Use dialogs for interactions that require focused attention.

Examples:

- Editing a record.
- Confirming an important action.
- Viewing focused details.
- Completing a short workflow.

A modal dialog typically requires:

- An accessible name.
- Appropriate dialog semantics.
- Focus moved into the dialog.
- Focus contained while open.
- Escape handling when appropriate.
- Focus restored when closed.
- Background interaction prevented.

Use a well-maintained accessible primitive when building custom dialog behavior would be unnecessary or risky.

## 7. Native Dialog Example

The browser's native `<dialog>` element can provide useful modal behavior.

```tsx
"use client";

import { useEffect, useRef } from "react";

type DialogProps = {
  open: boolean;
  onClose: () => void;
  title: string;
  children: React.ReactNode;
};

export function Dialog({ open, onClose, title, children }: DialogProps) {
  const dialogRef = useRef<HTMLDialogElement>(null);

  useEffect(() => {
    const dialog = dialogRef.current;

    if (!dialog) return;

    if (open && !dialog.open) {
      dialog.showModal();
    }

    if (!open && dialog.open) {
      dialog.close();
    }
  }, [open]);

  return (
    <dialog ref={dialogRef} aria-labelledby="dialog-title" onClose={onClose}>
      <h2 id="dialog-title">{title}</h2>

      {children}

      <button type="button" onClick={onClose}>
        Close
      </button>
    </dialog>
  );
}
```

This is an illustrative starting point, not a complete production dialog.

A production implementation should also:

- Prevent duplicate or conflicting close callbacks.
- Handle native `cancel` and `close` behavior correctly.
- Define initial focus.
- Restore focus appropriately.
- Support multiple dialog instances without duplicate IDs.
- Handle controlled state consistently.
- Provide suitable responsive styling.

Do not assume that rendering a `<dialog>` element alone completes every accessibility requirement.

## 8. Confirmation Dialogs

Use confirmation dialogs when an action has meaningful consequences.

Examples:

- Deleting a record.
- Removing a team member.
- Discarding unsaved changes.

Provide:

- A clear title.
- A concise explanation.
- A specific action label.
- A cancel action.
- A disabled or loading state while processing.

Avoid vague actions such as "OK" when a more specific label is possible.

Do not make ordinary, easily reversible interactions unnecessarily difficult with confirmation prompts.

## 9. Drawers and Sheets

Use drawers when users need to interact with secondary content without losing the current page context.

Examples:

- Mobile navigation.
- Filter panels.
- Record details.
- Editing forms.

Consider:

- Focus management.
- Keyboard interaction.
- Close behavior.
- Responsive width.
- Scroll behavior.
- Background interaction.
- Touch interaction.

A drawer that behaves like a modal should follow modal accessibility expectations.

A non-modal side panel has different interaction requirements.

## 10. Popovers and Dropdown Menus

Do not treat popovers, tooltips and menus as interchangeable.

Choose the correct pattern:

- Popover: contextual content or controls.
- Menu: a collection of commands or actions.
- Listbox: selecting an option.
- Tooltip: supplementary descriptive information.

Implement keyboard interaction according to the chosen pattern.

Prefer established accessible primitives instead of implementing complex keyboard behavior from scratch.

## 11. Toast Notifications

Use toast notifications for short-lived feedback.

Examples:

- Record saved.
- Changes updated.
- File uploaded.
- Request failed.
- Link copied.

Keep toast messages:

- Concise.
- Specific.
- Actionable when necessary.
- Consistent with application language.

Avoid displaying sensitive information in notifications.

## 12. Toast API

A notification system should expose a simple and predictable API.

Illustrative contract:

```ts
export type ToastVariant = "success" | "error" | "warning" | "info";

export type ToastInput = {
  title: string;
  description?: string;
  variant?: ToastVariant;
  duration?: number;
};

export type ToastAPI = {
  show: (toast: ToastInput) => void;
  dismiss: (id: string) => void;
  dismissAll: () => void;
};
```

The implementation should manage:

- Unique notification identifiers.
- Automatic dismissal.
- Manual dismissal.
- Multiple notifications.
- Appropriate duration.
- Cleanup.
- Accessibility announcements.

Do not create a global state library just to display a small number of toasts.

## 13. Notification Accessibility

Consider:

- Appropriate live-region behavior.
- Screen reader announcement timing.
- Non-interruptive status messages.
- Keyboard accessibility for interactive notifications.
- Sufficient display time.
- Pause behavior when appropriate.
- Visible dismissal controls.

Use `role="status"` for non-urgent status updates where suitable.

Use `role="alert"` for important, time-sensitive information that needs immediate announcement.

Do not announce every minor state change as an alert.

Avoid placing essential information only in a temporary toast.

## 14. Inline Alerts

Use inline alerts for information that should remain visible in context.

Examples:

- Form validation errors.
- Permission warnings.
- Network problems.
- Important account notices.

Do not use a temporary toast when the user needs the message to remain available while resolving an issue.

## 15. Asynchronous Operations

Notifications should reflect actual operation results.

Example:

```tsx
async function handleSave() {
  try {
    await saveChanges();

    toast.show({
      title: "Changes saved",
      variant: "success",
    });
  } catch {
    toast.show({
      title: "Unable to save changes",
      description: "Please try again.",
      variant: "error",
    });
  }
}
```

`saveChanges` and `toast` represent application-specific functions.

Do not show a success notification before the operation has succeeded.

Prevent duplicate submissions where appropriate.

## 16. Browser Notifications

The Notifications API can display OS-level notifications.

Before requesting permission:

1. Explain why notifications are useful.
1. Ask after a meaningful user interaction.
1. Request permission only when needed.
1. Respect denied permission.
1. Provide an alternative in-app notification experience.

Do not request notification permission immediately when the application loads.

Check browser support and permission state before using the API.

## 17. Web Push

Web Push enables a server to send notifications through a browser push service.

A typical architecture includes:

- Service worker.
- Push subscription.
- Application server.
- VAPID keys.
- Push delivery.
- Notification click handling.

Keep private VAPID keys on the server.

Do not expose private credentials to browser code.

Store subscriptions securely and support subscription revocation.

Web Push is a separate capability from ordinary in-app toast notifications.

See `../../references/notifications-and-push.md`.

## 18. Z-Index and Stacking Contexts

Manage overlay stacking consistently.

Consider:

- Header and navigation layers.
- Dropdown menus.
- Popovers.
- Tooltips.
- Drawers.
- Dialogs.
- Toast notifications.

Use centralized z-index tokens where the project needs them.

Remember that CSS stacking contexts can affect expected layering.

Do not keep increasing arbitrary z-index values to solve an incorrectly structured overlay.

## 19. Scroll Management

When a modal is open:

- Prevent unwanted background scrolling where appropriate.
- Allow dialog content to scroll.
- Preserve page scroll position.
- Restore expected scrolling after dismissal.

Test on mobile browsers as well as desktop.

Avoid global scroll-lock implementations that break nested overlays or existing page behavior.

## 20. Responsive Behavior and Motion

Verify overlays at different viewport sizes.

Consider:

- Mobile drawers.
- Dialog maximum height.
- Safe areas.
- Touch targets.
- On-screen keyboards.
- Content overflow.
- Reduced-motion preferences.

Use animation only when it improves the interaction.

Do not make dismissal or important feedback dependent on animation completion.

## 21. Existing Overlay and Notification Changes

When modifying an existing implementation:

1. Inspect its public API.
1. Find all component usages.
1. Review focus behavior.
1. Check event handling.
1. Inspect z-index and portals.
1. Review theme compatibility.
1. Inspect notification timing.
1. Check existing tests.
1. Preserve existing consumers.
1. Verify affected interactions.

Avoid replacing a working dialog library just to use a different API.

## 22. Testing

### Dialogs and Drawers

- Open and close behavior.
- Escape handling.
- Initial focus.
- Focus containment.
- Focus restoration.
- Keyboard interaction.
- Background interaction.
- Responsive behavior.

### Toasts

- Correct message.
- Correct status.
- Automatic dismissal.
- Manual dismissal.
- Multiple notifications.
- Screen reader announcements.

### Browser Notifications

- Permission request.
- Permission denied.
- Unsupported browser.
- Subscription failure.
- Notification click behavior.

Use automated accessibility checks together with manual keyboard and screen reader testing.

## 23. Common Anti-Patterns

Avoid:

- Inaccessible custom dialogs.
- Missing focus management.
- Clickable non-semantic elements.
- Excessive toast notifications.
- Success messages before operations finish.
- Essential errors shown only temporarily.
- Notification permission requests on initial page load.
- Duplicate notification systems.
- Arbitrary z-index escalation.
- Broken background scroll behavior.
- Unnecessary animation.
- Rebuilding accessible primitives without a real need.

## 24. Review Checklist

### Overlays

- [ ] Correct interaction pattern is used.
- [ ] Accessible name exists.
- [ ] Focus management works.
- [ ] Keyboard interaction works.
- [ ] Dismissal behavior is predictable.
- [ ] Responsive layout works.

### Notifications

- [ ] Messages are accurate.
- [ ] Notification timing is appropriate.
- [ ] Important information remains available.
- [ ] Live-region behavior is appropriate.
- [ ] Dismissal works.

### Engineering Quality

- [ ] Existing primitives are reused.
- [ ] No duplicate notification system exists.
- [ ] Async results are handled correctly.
- [ ] No unnecessary global state exists.
- [ ] Relevant tests pass.

## 25. Related References

- `../../references/dialogs-modals-and-overlays.md`
- `../../references/notifications-and-push.md`
- `../../references/reusable-ui-components.md`
- `../../references/accessibility-and-wcag.md`
- `../../references/global-styles-and-design-tokens.md`
- `../../references/theming-and-dark-mode.md`
- `../../references/state-management.md`
- `../../references/testing-strategy.md`
- `../../references/anti-ai-slop-and-engineering-quality.md`

## 26. Official Resources

- MDN Dialog Element: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog
- MDN Notifications API: https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API
- MDN Push API: https://developer.mozilla.org/en-US/docs/Web/API/Push_API
- WAI-ARIA Authoring Practices: https://www.w3.org/WAI/ARIA/apg/
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- React: https://react.dev/
- Radix UI: https://www.radix-ui.com/primitives
- React Aria: https://react-spectrum.adobe.com/react-aria/
