# Layouts and Navigation

## 1. Purpose

Define standards for designing, building, modifying and maintaining frontend application layouts and navigation systems.

Support:

- New application layouts.
- Existing layout modifications.
- Responsive application shells.
- Sidebars and navigation drawers.
- Headers and toolbars.
- Breadcrumbs.
- Tabs and route navigation.
- Protected navigation.
- Nested layouts.
- Mobile navigation.
- Accessibility and keyboard interaction.

The goal is to create consistent, responsive and understandable application navigation.

## 2. Inspect Before Implementation

Before changing layouts or navigation:

1. Inspect the existing routing system.
1. Identify the framework and router version.
1. Review existing layouts and nested routes.
1. Understand the current application shell.
1. Inspect sidebar, header and navigation components.
1. Check responsive breakpoints and mobile behavior.
1. Identify authentication and authorization requirements.
1. Review existing navigation configuration.
1. Check whether navigation is generated from permissions or static configuration.

For existing projects, preserve the established layout architecture unless a change is necessary.

Do not introduce a new router or replace the application shell unnecessarily.

## 3. Application Layout Architecture

An application layout commonly contains:

- Application shell.
- Header.
- Sidebar or navigation.
- Main content.
- Optional footer.
- Optional secondary navigation.

Example:

```text
Application
├── AppShell
│   ├── Sidebar
│   ├── Header
│   │   ├── MobileMenuButton
│   │   ├── Breadcrumbs
│   │   └── UserActions
│   └── MainContent
│       └── CurrentRoute
└── OptionalGlobalOverlays
```

This is a conceptual structure, not a mandatory component hierarchy.

Keep layout components focused on structure and presentation.

Avoid putting unrelated feature-specific business logic inside the application shell.

## 4. Layout Types

Choose layouts according to application needs.

### Public layout

Commonly used for:

- Landing pages.
- Marketing pages.
- Public documentation.
- Public content.

Typical elements:

- Public header.
- Main content.
- Footer.

### Authentication layout

Commonly used for:

- Sign in.
- Sign up.
- Password recovery.
- Account verification.

Keep authentication pages visually focused.

### Dashboard layout

Commonly used for:

- Admin panels.
- Internal CRM applications.
- Analytics dashboards.
- Business applications.

Typical elements:

- Sidebar.
- Header.
- Main content.
- Breadcrumbs.
- Account controls.

### Minimal layout

Commonly used for:

- Full-screen workflows.
- Focused editors.
- Error pages.
- Special standalone experiences.

Do not force every page into the same layout.

## 5. Responsive Layout Strategy

Design layouts for different screen sizes.

Consider:

- Mobile phones.
- Tablets.
- Laptops.
- Desktop screens.
- Large displays.

Typical behavior:

| Element | Desktop | Mobile |
| ------------ | ------------------------- | ---------------------- |
| Sidebar | Persistent or collapsible | Drawer |
| Header | Full toolbar | Compact toolbar |
| Navigation | Expanded | Menu or drawer |
| Main content | Flexible width | Full width |
| Tables | Full layout | Responsive alternative |
| Actions | Inline | Reorganized or grouped |

Use the project's established breakpoints.

Avoid designing exclusively for specific device widths.

Test intermediate widths, not only desktop and mobile.

## 6. Sidebar Navigation

A sidebar should provide clear access to primary application sections.

Common features:

- Logo or application identity.
- Navigation groups.
- Active route indication.
- Expandable groups.
- Collapse and expand behavior.
- User or workspace controls.
- Optional bottom actions.

Guidelines:

- Keep navigation labels understandable.
- Use icons consistently.
- Group related destinations.
- Avoid excessive nesting.
- Clearly distinguish active and inactive routes.
- Provide tooltips when collapsed labels are unavailable.
- Preserve keyboard accessibility.

Do not use icons alone when labels are needed to understand navigation.

## 7. Header and Toolbar

A header may contain:

- Mobile navigation trigger.
- Page title or breadcrumbs.
- Search.
- Notifications.
- Theme control.
- User menu.
- Contextual actions.

Keep the header focused on global or page-level controls.

Do not overload it with every possible application action.

Use responsive behavior to prevent controls from overflowing on small screens.

## 8. Mobile Navigation

Mobile navigation may use:

- Drawer.
- Slide-over panel.
- Navigation sheet.
- Bottom navigation for suitable applications.

Guidelines:

- Provide an accessible menu trigger.
- Support keyboard interaction.
- Manage focus when opening and closing modal drawers.
- Close navigation after route selection when appropriate.
- Prevent unintended background interaction for modal drawers.
- Ensure the drawer does not cover important content without a clear dismissal method.

Use a modal or non-modal pattern based on the interaction requirements.

Do not implement a custom drawer when the project already has a suitable accessible primitive.

## 9. Navigation Configuration

For larger applications, centralize repeated navigation definitions when appropriate.

Example:

```tsx
interface NavigationItem {
  label: string;
  href: string;
  icon?: React.ReactNode;
  requiredPermissions?: string[];
  children?: NavigationItem[];
}
```

Example configuration:

```tsx
const navigationItems: NavigationItem[] = [
  {
    label: "Dashboard",
    href: "/dashboard",
  },
  {
    label: "Users",
    href: "/users",
    requiredPermissions: ["users:read"],
  },
];
```

This is illustrative.

Guidelines:

- Keep route definitions consistent.
- Avoid duplicating navigation across layouts.
- Use stable route identifiers.
- Separate labels from authorization logic where necessary.
- Avoid overly complex configuration systems for small applications.

Never treat hidden navigation items as a security boundary.

Backend authorization must still protect restricted resources.

## 10. Active Route Handling

Active navigation should reflect the current route.

Consider:

- Exact route matches.
- Nested routes.
- Dynamic routes.
- Query parameters.
- Trailing slashes.
- Route groups.

Avoid naive string matching that marks unrelated routes as active.

For nested navigation, distinguish between:

- Exact active item.
- Parent section containing the active route.
- Expanded navigation group.

Use the router's existing route matching capabilities.

## 11. Breadcrumbs

Breadcrumbs communicate the current page's position within an application hierarchy.

Example:

```text
Dashboard / Users / User Details
```

Guidelines:

- Use meaningful labels.
- Keep hierarchy understandable.
- Make navigable ancestors links.
- Represent the current page as the current location.
- Avoid displaying technical route identifiers.
- Handle dynamic route labels using actual data when available.

Use semantic navigation markup and an accessible label.

Do not add breadcrumbs when they provide no meaningful navigation value.

## 12. Tabs and Navigation

Understand the difference between tabs and route navigation.

Use tabs when switching between related views within the same context.

Use links when navigating to another route or resource.

Consider:

- Keyboard interaction.
- Focus management.
- Selected state.
- URL synchronization when appropriate.
- Browser history behavior.
- Loading and error states.

Do not use tabs merely to make unrelated pages look organized.

## 13. Next.js Layouts

For Next.js App Router projects:

- Understand the `app` directory.
- Use root layouts appropriately.
- Use nested layouts for shared route sections.
- Use route groups when they improve organization.
- Preserve layouts across navigation when intended.
- Keep Server and Client Component boundaries deliberate.
- Use `loading.tsx` and `error.tsx` where appropriate.
- Understand parallel and intercepting routes before introducing them.

Example:

```text
app/
├── layout.tsx
├── (public)/
│   ├── layout.tsx
│   └── page.tsx
└── (dashboard)/
    ├── layout.tsx
    ├── dashboard/
    │   └── page.tsx
    └── users/
        └── page.tsx
```

Route groups do not add URL segments.

Do not introduce route groups just to create more folders.

Check the installed Next.js version and current official documentation before using version-sensitive APIs.

## 14. React Router and Other Routers

For React applications using a client-side router:

- Preserve the existing router.
- Use nested routes where appropriate.
- Separate route definitions from page components when useful.
- Use route-level layouts when supported.
- Handle not-found routes.
- Handle navigation errors.
- Support browser history.
- Use lazy loading where beneficial.

Do not assume every React application uses Next.js or React Router.

Follow the project's actual routing framework.

## 15. Protected Navigation

Navigation may depend on:

- Authentication.
- User roles.
- Permissions.
- Workspace membership.
- Feature availability.

Guidelines:

1. Understand the application's authorization model.
1. Reuse existing permission definitions.
1. Display only appropriate navigation items.
1. Handle inaccessible routes.
1. Provide appropriate unauthorized states.
1. Keep authorization enforcement on the server or trusted backend.

Hiding a navigation link does not prevent direct URL access.

Never rely on frontend checks alone for security.

## 16. Layout Styling

Use the existing design system and styling conventions.

Consider:

- Consistent spacing.
- Sidebar width.
- Header height.
- Content max-width.
- Responsive padding.
- Scroll behavior.
- Sticky positioning.
- Z-index layers.
- Theme compatibility.

Use semantic design tokens instead of scattering hardcoded values.

Avoid unnecessary fixed dimensions that break at different viewport sizes.

## 17. Scrolling and Overflow

Decide which regions should scroll.

Examples:

- Entire page scrolling.
- Sidebar scrolling independently.
- Main content scrolling.
- Full-screen editor scrolling.

Avoid accidental nested scrolling.

Check:

- Long navigation lists.
- Large tables.
- Small screen heights.
- Sticky headers.
- Dialogs and drawers.
- Mobile browser viewport behavior.

Use overflow rules deliberately.

## 18. Existing Layout Modification

When modifying an existing application layout:

1. Inspect the current layout hierarchy.
1. Identify shared layouts and route groups.
1. Find all affected routes.
1. Check navigation consumers.
1. Understand responsive behavior.
1. Identify state and styling dependencies.
1. Make the smallest appropriate change.
1. Verify affected routes and screen sizes.

Preserve existing navigation behavior unless the task requires changing it.

Avoid rebuilding the entire sidebar or application shell to solve a localized issue.

## 19. Performance

Consider:

- Route-level code splitting.
- Lazy-loaded pages.
- Large navigation dependencies.
- Expensive sidebar rendering.
- Unnecessary context updates.
- Client-side JavaScript.
- Layout shifts.
- Unnecessary hydration.

Do not turn an entire layout into a Client Component when only a small interactive section requires client-side behavior.

Use the rendering model supported by the framework.

## 20. Common Anti-Patterns

Avoid:

- One layout for every unrelated page.
- Duplicated navigation definitions.
- Excessively nested sidebars.
- Icons without accessible names.
- Incorrect active route matching.
- Using buttons for navigation.
- Using links for actions.
- Frontend-only authorization.
- Unnecessary client-side layout state.
- Accidental nested scrolling.
- Fixed widths that break responsive behavior.
- Rewriting existing route architecture without a reason.

## 21. Decision Workflow

Before implementing layout or navigation changes:

1. Inspect the router and layout hierarchy.
1. Understand the requested page structure.
1. Identify shared versus feature-specific UI.
1. Determine desktop and mobile behavior.
1. Choose appropriate navigation patterns.
1. Preserve existing conventions.
1. Implement accessible interactions.
1. Check authorization requirements.
1. Test relevant routes and viewport sizes.
1. Verify that existing navigation still works.

## 22. Review Checklist

### Architecture

- [ ] Layout responsibilities are clear.
- [ ] Existing routing conventions are preserved.
- [ ] Shared layouts are reused appropriately.
- [ ] Feature-specific UI is separated.

### Navigation

- [ ] Active routes are correct.
- [ ] Links navigate correctly.
- [ ] Breadcrumbs are meaningful.
- [ ] Nested routes behave correctly.
- [ ] Protected navigation is handled.

### Responsive behavior

- [ ] Sidebar works on mobile.
- [ ] Header adapts to screen size.
- [ ] Content does not overflow.
- [ ] Scrolling behaves correctly.

### Accessibility

- [ ] Semantic navigation is used.
- [ ] Keyboard interaction works.
- [ ] Focus is managed appropriately.
- [ ] Accessible names are provided.

### Verification

- [ ] Relevant routes are tested.
- [ ] Existing navigation is not broken.
- [ ] Type checking and linting pass.
- [ ] Relevant tests pass.

## 23. Related References

- architecture-and-project-structure.md
- nextjs-engineering.md
- reusable-ui-components.md
- global-styles-and-design-tokens.md
- theming-and-dark-mode.md
- dialogs-modals-and-overlays.md
- accessibility-and-wcag.md
- frontend-security.md
- testing-strategy.md

## 24. Official Resources

- Next.js Layouts and Pages: https://nextjs.org/docs/app/getting-started/layouts-and-pages
- Next.js Linking and Navigation: https://nextjs.org/docs/app/getting-started/linking-and-navigating
- React Router: https://reactrouter.com/
- WAI-ARIA Authoring Practices: https://www.w3.org/WAI/ARIA/apg/
- MDN Navigation: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav
