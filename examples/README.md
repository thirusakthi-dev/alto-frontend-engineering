# Theme System Example

## 1. Purpose

Demonstrate how to implement a consistent and maintainable theme system in a React application.

The example covers:

- Light theme.
- Dark theme.
- System preference.
- Semantic design tokens.
- CSS variables.
- Theme persistence.
- Theme switching.
- Initial theme handling.
- Hydration considerations.
- Accessible theme controls.
- Component-level theme compatibility.

The goal is to build one consistent theme system rather than implementing separate styling logic inside every component.

## 2. Core Principles

1. Use semantic design tokens.
1. Keep theme values centralized.
1. Support light and dark themes consistently.
1. Respect the user's system preference.
1. Avoid unnecessary theme state duplication.
1. Prevent incorrect initial theme rendering.
1. Make theme controls accessible.
1. Preserve existing styling conventions.
1. Avoid hardcoded colors throughout components.
1. Test all supported themes.

## 3. Suggested Structure

```text
src/
├── app/
│   ├── layout.tsx
│   └── globals.css
├── components/
│   └── theme/
│       ├── theme-provider.tsx
│       └── theme-toggle.tsx
├── hooks/
│   └── use-theme.ts
└── lib/
    └── theme/
        └── theme-config.ts
```

This structure is illustrative.

Do not create a separate theme abstraction if the framework or existing project already provides an appropriate solution.

## 4. Theme Modes

Support three user preferences:

| Mode | Behavior |
| ------ | -------------------------------------- |
| Light | Always use the light theme |
| Dark | Always use the dark theme |
| System | Follow the operating system preference |

The selected preference and the currently resolved theme are different concepts.

For example:

- Selected preference: `system`
- Resolved theme: `dark`

Keep this distinction clear in the implementation.

## 5. Semantic Design Tokens

Define semantic CSS variables instead of using raw colors throughout components.

Example:

```css
/* src/app/globals.css */

:root {
  color-scheme: light;

  --background: #ffffff;
  --foreground: #171717;
  --surface: #f8fafc;
  --surface-muted: #f1f5f9;
  --border: #e2e8f0;

  --text-primary: #171717;
  --text-secondary: #64748b;

  --primary: #2563eb;
  --primary-foreground: #ffffff;

  --success: #15803d;
  --warning: #b45309;
  --danger: #dc2626;
}

[data-theme="dark"] {
  color-scheme: dark;

  --background: #09090b;
  --foreground: #fafafa;
  --surface: #18181b;
  --surface-muted: #27272a;
  --border: #3f3f46;

  --text-primary: #fafafa;
  --text-secondary: #a1a1aa;

  --primary: #60a5fa;
  --primary-foreground: #09090b;

  --success: #4ade80;
  --warning: #fbbf24;
  --danger: #f87171;
}

body {
  background: var(--background);
  color: var(--foreground);
}
```

These colors are illustrative.

Choose colors based on the application's design requirements and verify contrast.

## 6. Use Tokens in Components

Prefer semantic tokens.

```css
.card {
  background: var(--surface);
  border: 1px solid var(--border);
  color: var(--text-primary);
  border-radius: 0.75rem;
  padding: 1rem;
}
```

Avoid:

```css
.card {
  background: white;
  color: black;
}
```

Hardcoded colors can create inconsistent behavior when themes change.

Not every color must be a global token. Use component-specific values when they have a genuine local purpose.

## 7. Theme Configuration

Define the supported preference values in one place.

```ts
// src/lib/theme/theme-config.ts

export const themeModes = ["light", "dark", "system"] as const;

export type ThemeMode = (typeof themeModes)[number];

export type ResolvedTheme = "light" | "dark";

export const defaultThemeMode: ThemeMode = "system";

export const themeStorageKey = "app-theme";
```

Validate stored values instead of trusting arbitrary browser storage data.

## 8. Theme Persistence

Choose a persistence strategy based on application requirements.

Possible options:

| Storage | Suitable use |
| ----------------- | ------------------------------------- |
| localStorage | Browser-only theme preference |
| Cookie | Server-readable initial preference |
| User profile | Authenticated cross-device preference |
| System preference | Follow OS settings |

Do not implement multiple persistence mechanisms unless the application requires them.

For a browser-only application, localStorage may be sufficient.

For server-rendered applications, consider a cookie when the server needs to render the correct initial theme.

Never store sensitive information in theme preferences.

## 9. System Preference

Use the browser's `prefers-color-scheme` media query.

```ts
const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");

const prefersDark = mediaQuery.matches;
```

When the selected mode is `system`, listen for changes to the operating system preference.

Remove event listeners when they are no longer needed.

Do not override an explicitly selected light or dark preference when the operating system changes.

## 10. Theme Provider Responsibilities

A theme provider should:

- Expose the selected preference.
- Expose the resolved theme.
- Allow preference changes.
- Apply the theme consistently.
- Handle system preference changes.
- Persist the selected preference.
- Clean up event listeners.

Keep the provider focused.

Do not turn it into a global application state container for unrelated features.

Example public contract:

```ts
type ThemeContextValue = {
  theme: ThemeMode;
  resolvedTheme: ResolvedTheme;
  setTheme: (theme: ThemeMode) => void;
};
```

Implement the provider according to the project's React and framework versions.

Avoid duplicating theme state across unrelated components.

## 11. Applying the Theme

Use one consistent theme attribute or class.

For example:

```html
<html data-theme="dark"></html>
```

The attribute can control the semantic CSS variables throughout the application.

Use the same strategy consistently.

Do not mix multiple theme mechanisms without a clear reason.

## 12. Theme Switching Component

Provide an accessible theme control.

Example:

```tsx
"use client";

import type { ThemeMode } from "@/lib/theme/theme-config";

type ThemeToggleProps = {
  theme: ThemeMode;
  onThemeChange: (theme: ThemeMode) => void;
};

export function ThemeToggle({ theme, onThemeChange }: ThemeToggleProps) {
  return (
    <label>
      <span>Appearance</span>

      <select
        value={theme}
        onChange={(event) => onThemeChange(event.target.value as ThemeMode)}
      >
        <option value="system">System</option>
        <option value="light">Light</option>
        <option value="dark">Dark</option>
      </select>
    </label>
  );
}
```

This is a minimal presentation example.

A production implementation should validate the selected value at runtime or use a strongly constrained control whose options guarantee valid values.

Use an accessible name and visible focus state.

Do not rely only on color or an unlabeled icon to communicate the current theme.

## 13. Preventing Incorrect Initial Rendering

Server-rendered applications need special attention.

Potential problems:

- Incorrect initial theme.
- Flash of the wrong theme.
- Hydration mismatches.
- Server and browser preference differences.

Choose an approach appropriate to the framework:

1. Read a theme cookie on the server when available.
1. Render the initial theme consistently.
1. Use a carefully designed early theme initialization script when necessary.
1. Avoid accessing browser-only APIs during server rendering.
1. Keep the initial server and client output compatible.

Do not disable hydration warnings simply to hide an incorrect implementation.

## 14. Next.js Considerations

For Next.js App Router:

- Keep the root layout as a Server Component when possible.
- Use a Client Component for interactive theme context.
- Pass only necessary configuration across the boundary.
- Consider cookie-based theme resolution when server rendering needs the preference.
- Avoid turning the entire application into a Client Component.
- Verify the installed Next.js version and the chosen theme library's current integration instructions.

Tailwind CSS projects may use a theme attribute with a custom dark variant.

For Tailwind CSS v4, one possible configuration is:

```css
@import "tailwindcss";

@custom-variant dark (&:where([data-theme="dark"], [data-theme="dark"] *));
```

For Tailwind CSS v3, configure the dark mode strategy using the installed version's configuration conventions.

Do not mix Tailwind v3 and v4 configuration examples.

## 15. Component Compatibility

Every component should use semantic tokens where appropriate.

Check:

- Backgrounds.
- Text colors.
- Borders.
- Input surfaces.
- Buttons.
- Dropdowns.
- Dialogs.
- Tooltips.
- Tables.
- Charts.
- Disabled states.
- Focus indicators.
- Hover states.
- Selected states.

Do not assume that changing the page background automatically makes the entire application theme-compatible.

## 16. Transitions and Motion

Use subtle transitions where they improve the experience.

Respect reduced-motion preferences.

Avoid:

- Flashing effects.
- Long theme transitions.
- Unnecessary animations.
- Animating layout properties without a reason.
- Theme changes that reduce readability.

A theme switch should feel immediate and predictable.

## 17. Accessibility

Verify:

- Text contrast.
- Control contrast.
- Visible focus indicators.
- Accessible theme selection.
- Readable disabled states.
- Consistent interaction states.
- Reduced-motion support.

Do not use color as the only indicator of status or meaning.

See `../../references/accessibility-and-wcag.md`.

## 18. Existing Project Theme Changes

When adding or modifying a theme system in an existing application:

1. Inspect global styles.
1. Identify existing design tokens.
1. Check whether a theme provider already exists.
1. Find hardcoded colors in affected components.
1. Inspect existing persistence behavior.
1. Check server-rendering and hydration behavior.
1. Preserve the existing styling system.
1. Migrate incrementally.
1. Verify all affected components.

Do not replace an existing design system just to match this example.

## 19. Testing

Test:

- Light mode.
- Dark mode.
- System mode.
- Manual preference changes.
- Persistence after reload.
- System preference changes.
- Initial rendering.
- Hydration behavior.
- Component contrast.
- Keyboard accessibility.

For server-rendered applications, test both initial rendering and browser hydration.

## 20. Common Anti-Patterns

Avoid:

- Hardcoded colors throughout components.
- Duplicated theme state.
- Multiple competing theme providers.
- Unnecessary theme dependencies.
- Browser API access during server rendering.
- Incorrect hydration handling.
- Ignoring system preferences.
- Inconsistent semantic tokens.
- Theme-specific styles scattered across components.
- Animations that make switching uncomfortable.
- Replacing an existing design system unnecessarily.

## 21. Review Checklist

### Architecture

- [ ] Theme responsibilities are clearly separated.
- [ ] Existing styling conventions are preserved.
- [ ] Theme state is not duplicated.
- [ ] Persistence strategy is appropriate.

### Appearance

- [ ] Light theme is complete.
- [ ] Dark theme is complete.
- [ ] Semantic tokens are consistent.
- [ ] Interactive states work in both themes.

### Reliability

- [ ] System preference works.
- [ ] Preference persists correctly.
- [ ] Initial rendering is correct.
- [ ] Hydration issues are not hidden.

### Accessibility

- [ ] Theme control has an accessible name.
- [ ] Contrast is sufficient.
- [ ] Keyboard interaction works.
- [ ] Reduced motion is respected.

### Verification

- [ ] TypeScript checks pass.
- [ ] Relevant tests pass.
- [ ] Production build succeeds.

## 22. Related References

- `../../references/global-styles-and-design-tokens.md`
- `../../references/theming-and-dark-mode.md`
- `../../references/reusable-ui-components.md`
- `../../references/nextjs-engineering.md`
- `../../references/accessibility-and-wcag.md`
- `../../references/testing-strategy.md`
- `../../references/anti-ai-slop-and-engineering-quality.md`

## 23. Official Resources

- MDN Color Scheme: https://developer.mozilla.org/en-US/docs/Web/CSS/color-scheme
- MDN prefers-color-scheme: https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme
- React: https://react.dev/
- Next.js App Router: https://nextjs.org/docs/app
- Tailwind CSS: https://tailwindcss.com/docs
- WCAG: https://www.w3.org/TR/WCAG22/
