# Theming and Dark Mode

## 1. Purpose

Define a maintainable theme system for modern frontend applications.

Support:

- Light theme.
- Dark theme.
- System preference.
- Theme switching.
- Theme persistence.
- Initial theme detection.
- Flash prevention.
- Semantic CSS variables.
- Component theme compatibility.
- Accessibility.

The theme system must work for both new and existing projects.

## 2. Inspect Before Implementation

Before introducing or modifying a theme system:

1. Inspect existing global CSS.
1. Identify existing CSS variables and design tokens.
1. Check whether a theme provider already exists.
1. Inspect Tailwind configuration and version.
1. Identify theme persistence mechanisms.
1. Check existing UI component libraries.
1. Understand server-side rendering requirements.
1. Identify how the application currently selects its theme.

Do not introduce a second theme system if the project already has a suitable implementation.

For existing projects, prefer improving the current implementation over replacing it.

## 3. Theme Modes

Support three user preferences where required.

| Mode | Behavior |
| ------ | ---------------------------------- |
| Light | Always use light theme |
| Dark | Always use dark theme |
| System | Follow operating system preference |

System preference can be detected using:

```ts
const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");

const isDark = mediaQuery.matches;
```

Listen for changes when the selected mode is `system`.

Do not override an explicitly selected light or dark preference when the operating system theme changes.

## 4. Semantic Theme Variables

Use semantic CSS variables instead of hardcoding colors throughout components.

Example:

```css
:root {
  color-scheme: light;

  --background: #ffffff;
  --foreground: #171717;

  --surface: #f8f9fa;
  --surface-muted: #f1f3f5;

  --text-primary: #171717;
  --text-secondary: #666666;

  --border: #e5e7eb;

  --accent: #2563eb;
  --accent-foreground: #ffffff;

  --destructive: #dc2626;
  --success: #15803d;

  --focus-ring: #2563eb;
}

[data-theme="dark"] {
  color-scheme: dark;

  --background: #111111;
  --foreground: #f5f5f5;

  --surface: #1b1b1b;
  --surface-muted: #262626;

  --text-primary: #f5f5f5;
  --text-secondary: #a3a3a3;

  --border: #333333;

  --accent: #60a5fa;
  --accent-foreground: #111111;

  --destructive: #f87171;
  --success: #4ade80;

  --focus-ring: #60a5fa;
}
```

These values are examples. Adapt the palette to the actual design direction.

Use the same semantic token names across themes.

Components should not need separate implementations for light and dark modes.

## 5. Theme Preference Storage

Persist the user's selected mode when required.

Possible storage approaches:

| Storage | Suitable use |
| ----------------- | -------------------------------------------------------- |
| localStorage | Client-side applications |
| Cookie | Server-readable theme preference |
| User profile | Authenticated applications with cross-device preferences |
| System preference | Default when no explicit preference exists |

Choose based on the application architecture.

Important:

- Validate stored values.
- Handle unavailable browser storage.
- Avoid unnecessary storage synchronization.
- Define precedence when multiple preference sources exist.
- Do not store sensitive information in localStorage.

A common preference precedence is:

1. Explicit user selection.
1. Saved preference.
1. System preference.

Adapt this order when the application has a trusted server-side user preference.

## 6. Theme Switching

Provide a clear theme control.

Example:

```tsx
type ThemeMode = "light" | "dark" | "system";

interface ThemeSwitcherProps {
  value: ThemeMode;
  onChange: (mode: ThemeMode) => void;
}
```

The switching control should:

- Clearly communicate the selected mode.
- Support keyboard navigation.
- Have an accessible label.
- Avoid unexpected page reloads.
- Update the interface consistently.
- Persist the preference where appropriate.

Do not use an icon-only theme control without an accessible name.

## 7. Theme Application

Apply the active theme using a consistent mechanism.

For example:

```ts
document.documentElement.dataset.theme = "dark";
```

Or:

```ts
document.documentElement.classList.toggle("dark", isDark);
```

Choose the approach compatible with the existing styling system.

Do not mix multiple theme-application mechanisms without a clear reason.

## 8. Prevent Theme Flash

Avoid showing the wrong theme briefly during initial page rendering.

A flash can happen when the page renders with the default theme before reading the saved preference.

Consider:

- Applying the initial theme before visible content renders.
- Reading a cookie on the server when available.
- Using a small initialization script when appropriate.
- Using framework-supported theme initialization.
- Keeping server and client theme assumptions consistent.

For Next.js:

- Consider server-readable cookies for persisted preferences.
- Be careful with hydration mismatches.
- Use `suppressHydrationWarning` only where appropriate.
- Do not suppress hydration warnings to hide unrelated rendering problems.

For client-only applications, initialize the theme before the main interface becomes visible where practical.

Do not assume a theme provider automatically prevents every flash.

## 9. React Theme Provider

A shared provider can manage theme state when multiple components need access.

Example contract:

```tsx
type ThemeMode = "light" | "dark" | "system";

interface ThemeContextValue {
  theme: ThemeMode;
  resolvedTheme: "light" | "dark";
  setTheme: (theme: ThemeMode) => void;
}
```

Separate:

- User preference.
- Resolved theme.
- Theme application.
- Persistence.
- System preference subscription.

Avoid duplicating theme state across unrelated components.

Use an existing theme library when it already meets project requirements.

Do not introduce a provider or dependency for a trivial application that does not need one.

## 10. Tailwind Integration

Identify the installed Tailwind version.

### Tailwind CSS v4

Use the CSS-first configuration model.

Example:

```css
@import "tailwindcss";

@custom-variant dark (&:where([data-theme="dark"], [data-theme="dark"] *));
```

This allows dark variants to respond to the selected data attribute.

Alternatively, use a compatible class-based approach if the project already uses one.

### Tailwind CSS v3

Use the existing `darkMode` configuration, such as class-based dark mode.

Do not copy v3 configuration into a v4 project.

Keep the CSS variable system as the source of semantic theme values where practical.

## 11. Component Theme Compatibility

Every shared component should work in all supported themes.

Review:

- Backgrounds.
- Text.
- Borders.
- Icons.
- Focus indicators.
- Hover states.
- Active states.
- Disabled states.
- Selected states.
- Validation states.
- Loading indicators.
- Overlays and portals.

Avoid hardcoded colors that break dark mode.

Use semantic tokens for component styling.

Third-party components must also be checked for theme compatibility.

## 12. Theme Transitions

Theme transitions should feel predictable.

Avoid applying expensive transitions to every property.

If animated transitions are used:

- Keep them subtle.
- Respect reduced-motion preferences.
- Avoid flashing or abrupt contrast changes.
- Prevent transitions from interfering with initial theme application.

Do not animate the entire interface unnecessarily.

## 13. Accessibility

Verify:

- Sufficient text contrast in every theme.
- Visible keyboard focus.
- Readable disabled states.
- Clear selected states.
- Accessible theme controls.
- Consistent status indicators.
- Compatibility with forced-colors mode where appropriate.

Do not assume that a color palette accessible in light mode is automatically accessible in dark mode.

Test both themes independently.

## 14. Existing Project Modification

When adding theme support to an existing application:

1. Inspect current theme implementation.
1. Identify hardcoded colors.
1. Map existing colors to semantic tokens.
1. Preserve the current visual identity.
1. Update shared components incrementally.
1. Check third-party components.
1. Verify persistence behavior.
1. Test server/client rendering where applicable.
1. Test all supported theme modes.
1. Remove obsolete styling only after verifying it is unused.

Do not rewrite every component just to introduce theme support.

## 15. Common Anti-Patterns

Avoid:

- Duplicating entire stylesheets for each theme.
- Hardcoding colors in every component.
- Maintaining multiple independent theme states.
- Ignoring system preference.
- Overwriting explicit user preference.
- Reading browser storage unsafely during server rendering.
- Hiding hydration problems with warning suppression.
- Introducing unnecessary theme libraries.
- Using different semantic token names across themes.
- Ignoring portals and third-party components.
- Using inaccessible theme controls.
- Applying excessive theme-transition animations.

## 16. Decision Workflow

Before implementing a theme system:

1. Inspect existing theme architecture.
1. Identify framework and styling versions.
1. Define supported theme modes.
1. Establish semantic theme tokens.
1. Select a preference storage strategy.
1. Decide how the initial theme is resolved.
1. Implement switching and persistence.
1. Integrate existing components.
1. Verify hydration and initial rendering.
1. Test accessibility in every theme.

Prefer the simplest reliable implementation that fits the application.

## 17. Review Checklist

### Theme behavior

- [ ] Light theme works.
- [ ] Dark theme works.
- [ ] System preference works.
- [ ] Explicit preferences are preserved.
- [ ] Theme changes apply consistently.

### Persistence

- [ ] Preference storage is appropriate.
- [ ] Invalid stored values are handled.
- [ ] Initial theme is resolved correctly.
- [ ] Theme flash is prevented where practical.

### Components

- [ ] Shared components support all themes.
- [ ] Hover and focus states are visible.
- [ ] Portals and overlays use correct colors.
- [ ] Third-party components are checked.

### Accessibility

- [ ] Contrast is checked independently.
- [ ] Keyboard navigation works.
- [ ] Theme controls have accessible labels.
- [ ] Reduced motion is respected.

### Existing projects

- [ ] Existing visual identity is preserved.
- [ ] Existing theme functionality is reused.
- [ ] Unrelated components are not unnecessarily rewritten.

## 18. Related References

- global-styles-and-design-tokens.md
- reusable-ui-components.md
- layouts-and-navigation.md
- dialogs-modals-and-overlays.md
- ui-design-quality-and-impeccable.md
- accessibility-and-wcag.md
- architecture-and-project-structure.md

## 19. Official Resources

- MDN prefers-color-scheme: https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme
- MDN CSS Custom Properties: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties
- Tailwind CSS Dark Mode: https://tailwindcss.com/docs/dark-mode
- Tailwind CSS Theme Variables: https://tailwindcss.com/docs/theme
- React Context: https://react.dev/reference/react/useContext
- Next.js Cookies: https://nextjs.org/docs/app/api-reference/functions/cookies
- WCAG: https://www.w3.org/TR/WCAG22/
