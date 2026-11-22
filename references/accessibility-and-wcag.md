# Accessibility and WCAG

## 1. Purpose

Define standards for building, improving, reviewing and maintaining accessible frontend applications.

Support:

- Semantic HTML.
- Keyboard accessibility.
- Screen reader compatibility.
- ARIA attributes and roles.
- Focus management.
- Color contrast.
- Accessible forms.
- Accessible dialogs and overlays.
- Responsive accessibility.
- Motion and animation preferences.
- WCAG compliance.
- Accessibility testing.
- Existing application accessibility improvements.

The objective is to make applications usable by people with different abilities, devices and interaction methods.

Accessibility must be considered throughout development, not added as a final patch.

## 2. Inspect Before Implementation

Before implementing or modifying UI:

1. Inspect existing semantic HTML.
1. Review shared UI components.
1. Check keyboard interactions.
1. Inspect focus indicators.
1. Review labels and accessible names.
1. Check color contrast.
1. Identify existing ARIA usage.
1. Review dialog and navigation behavior.
1. Check responsive behavior and zoom.
1. Inspect existing accessibility tests.

For existing projects, improve the actual accessibility problems while preserving established architecture and functionality.

Do not replace native elements with custom controls without a clear reason.

## 3. WCAG Fundamentals

Use the Web Content Accessibility Guidelines (WCAG) as the primary accessibility reference.

WCAG is organized around four principles:

| Principle | Meaning |
| -------------- | ------------------------------------------- |
| Perceivable | Users can perceive the information |
| Operable | Users can operate the interface |
| Understandable | Content and interactions are understandable |
| Robust | Content works with assistive technologies |

These are known as POUR.

### Conformance levels

- A: Minimum level of conformance.
- AA: Common target for accessible products and legal requirements.
- AAA: More stringent requirements.

Use WCAG 2.2 Level AA as a practical target unless the project specifies another standard.

Do not claim WCAG compliance based only on automated scans.

## 4. Semantic HTML

Prefer native HTML elements that describe their purpose.

Examples:

| Purpose | Semantic element |
| ------------------- | ---------------- |
| Main navigation | `<nav>` |
| Main content | `<main>` |
| Page header | `<header>` |
| Page footer | `<footer>` |
| Independent content | `<article>` |
| Related content | `<section>` |
| Interactive action | `<button>` |
| Navigation | `<a>` |
| Form | `<form>` |

Use headings in a meaningful hierarchy.

Example:

```html
<main>
  <h1>Account Settings</h1>

  <section aria-labelledby="profile-heading">
    <h2 id="profile-heading">Profile</h2>
    <p>Manage your profile information.</p>
  </section>
</main>
```

Guidelines:

- Use buttons for actions.
- Use links for navigation.
- Use headings to describe content sections.
- Use lists for groups of related items.
- Use tables for tabular data.
- Use native controls whenever possible.

Do not use generic `<div>` elements for every interaction.

## 5. Keyboard Accessibility

All interactive functionality must be usable with a keyboard.

Common keyboard interactions:

| Key | Expected behavior |
| ----------- | ------------------------------------------- |
| Tab | Move focus forward |
| Shift + Tab | Move focus backward |
| Enter | Activate links and buttons |
| Space | Activate buttons and applicable controls |
| Escape | Close dismissible overlays when appropriate |
| Arrow keys | Navigate supported composite controls |

Guidelines:

- Every interactive element must be reachable.
- Focus order must be logical.
- Do not create keyboard traps.
- Do not remove visible focus indicators.
- Support standard keyboard behavior.
- Ensure custom controls follow their expected interaction pattern.

Do not implement custom keyboard behavior when native HTML already provides it.

## 6. Focus Management

Focus should remain predictable.

Important scenarios:

- Opening dialogs.
- Closing dialogs.
- Navigating between application sections.
- Displaying validation errors.
- Opening menus.
- Updating content dynamically.

For dialogs:

1. Move focus into the dialog.
1. Keep keyboard interaction within a modal dialog.
1. Support Escape where appropriate.
1. Restore focus to the triggering element when closed, when possible.

For route changes, consider moving focus to the new page heading or main content when the navigation pattern requires it.

Avoid unexpected focus movement during normal interactions.

## 7. Visible Focus Indicators

Keyboard users must be able to identify the currently focused element.

Example:

```css
:focus-visible {
  outline: 2px solid var(--focus-ring);
  outline-offset: 3px;
}
```

Guidelines:

- Keep focus indicators visible.
- Provide sufficient contrast.
- Do not rely only on subtle color changes.
- Ensure focus is not hidden behind sticky headers or overlays.
- Respect existing design tokens.

Do not remove browser focus styles without providing a suitable replacement.

## 8. Screen Reader Support

Use semantic HTML and accessible names to communicate interface purpose.

Important concepts:

- Accessible name.
- Accessible description.
- Role.
- State.
- Relationships.
- Live announcements.

Examples:

```html
<button type="button" aria-label="Close dialog">
  <svg aria-hidden="true"></svg>
</button>
```

For icon-only buttons, provide an accessible name.

Decorative images should use empty alternative text:

```html
<img src="/decorative-shape.svg" alt="" />
```

Meaningful images should have useful alternative text.

Do not repeat visible text unnecessarily in accessible labels.

Do not assume that adding ARIA automatically makes an interface accessible.

## 9. ARIA Usage

Prefer native semantic HTML before adding ARIA.

Important attributes include:

- `aria-label`
- `aria-labelledby`
- `aria-describedby`
- `aria-hidden`
- `aria-expanded`
- `aria-controls`
- `aria-current`
- `aria-invalid`
- `aria-live`
- `aria-pressed`
- `aria-selected`

Example:

```html
<button type="button" aria-expanded="false" aria-controls="navigation-menu">
  Menu
</button>
```

Guidelines:

- Use ARIA according to the relevant interaction pattern.
- Keep state attributes synchronized with actual UI state.
- Do not apply roles unnecessarily.
- Do not hide important content from assistive technologies.
- Avoid invalid or conflicting ARIA combinations.

Follow the WAI-ARIA Authoring Practices Guide for complex widgets.

## 10. Images and Alternative Text

Use alternative text based on image purpose.

### Informative images

Describe the meaningful information conveyed by the image.

### Functional images

Describe the action or destination when an image functions as a control.

### Decorative images

Use empty alternative text when the image adds no meaningful information.

### Complex images

Provide an appropriate textual explanation of important data.

Do not use filenames as alternative text.

Avoid descriptions such as "image of" when unnecessary.

## 11. Color and Contrast

Do not communicate important information through color alone.

Examples:

- Error states.
- Success states.
- Required fields.
- Selected navigation.
- Status indicators.

Use text, icons, shapes or other visual indicators alongside color.

For WCAG 2.2 AA, common contrast requirements include:

| Content | Minimum contrast |
| ---------------------------------------------- | ---------------- |
| Normal text | 4.5:1 |
| Large text | 3:1 |
| UI components and meaningful graphical objects | 3:1 |

Large text generally means at least 18pt regular or 14pt bold.

Evaluate actual foreground and background combinations, including hover, disabled and focus states.

Do not assume that a visually attractive color palette automatically provides sufficient contrast.

## 12. Accessible Forms

Forms must communicate labels, instructions and validation.

Guidelines:

- Associate labels with inputs.
- Use appropriate input types.
- Identify required fields.
- Provide useful instructions.
- Associate errors with their fields.
- Communicate invalid states.
- Preserve keyboard accessibility.
- Avoid placeholder-only labels.

Example:

```html
<label for="email">Email address</label>

<input
  id="email"
  name="email"
  type="email"
  aria-describedby="email-help email-error"
  aria-invalid="true"
/>

<p id="email-help">Enter the email address associated with your account.</p>

<p id="email-error">Enter a valid email address.</p>
```

Do not display validation errors only through color.

For large forms, consider an error summary and appropriate focus management.

See `forms-and-validation.md`.

## 13. Dialogs and Overlays

Accessible overlays must support predictable interaction.

Consider:

- Dialog semantics.
- Accessible title.
- Accessible description.
- Initial focus.
- Focus containment for modal dialogs.
- Escape handling.
- Focus restoration.
- Background interaction.
- Scroll management.

Use an established accessible primitive when suitable.

Do not build a custom modal without understanding focus management and keyboard behavior.

For non-modal popovers and menus, follow their appropriate interaction patterns rather than applying modal behavior indiscriminately.

See `dialogs-modals-and-overlays.md`.

## 14. Navigation Accessibility

Navigation must communicate structure and current location.

Guidelines:

- Use semantic navigation landmarks.
- Provide meaningful link names.
- Indicate the current page where appropriate.
- Support keyboard navigation.
- Maintain visible focus.
- Use buttons for expandable menus.
- Keep menu state synchronized.
- Provide a skip link for bypassing repeated navigation.

Example:

```html
<a href="#main-content" class="skip-link"> Skip to main content </a>

<nav aria-label="Primary navigation">
  <a href="/dashboard" aria-current="page"> Dashboard </a>
</nav>

<main id="main-content">
  <h1>Dashboard</h1>
</main>
```

Do not use `aria-current` on every navigation link.

See `layouts-and-navigation.md`.

## 15. Tables and Data Visualization

For tables:

- Use proper table structure.
- Provide column and row headers.
- Use captions where helpful.
- Preserve understandable reading order.
- Avoid using tables for visual layout.

For charts:

- Provide meaningful titles.
- Provide text summaries.
- Make important values available without relying only on color.
- Consider an accessible data table.
- Ensure interactive chart controls work with keyboards.

Do not assume a chart is accessible simply because its container has an accessible label.

## 16. Motion and Animation

Respect users who prefer reduced motion.

Use:

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    scroll-behavior: auto;
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

Adapt this example carefully to the application.

Guidelines:

- Avoid unnecessary motion.
- Avoid flashing content.
- Provide reduced-motion alternatives.
- Do not communicate information only through animation.
- Avoid motion that interferes with reading or interaction.

Do not remove all meaningful interaction feedback without considering usability.

## 17. Responsive and Zoom Accessibility

Accessibility must work across screen sizes and zoom levels.

Check:

- Mobile navigation.
- Touch target sizes.
- Text resizing.
- Content reflow.
- Horizontal scrolling.
- Focus visibility.
- Dialog sizing.
- Form usability.
- Orientation changes.

WCAG 2.2 AA includes a 24 by 24 CSS pixel minimum target-size criterion, subject to its defined exceptions.

A larger practical target is often better for touch interaction.

Do not assume responsive design automatically means accessible design.

## 18. Accessible Loading and Dynamic Updates

Communicate important state changes.

Examples:

- Loading data.
- Saving a form.
- Search results updated.
- File upload progress.
- Success or failure.
- Notifications.

Use appropriate live regions when announcements are needed.

Example:

```html
<p role="status" aria-live="polite">Results updated.</p>
```

For urgent errors, an assertive announcement may be appropriate, but use it sparingly.

Do not announce every minor visual update.

Ensure loading indicators do not create confusing or repetitive screen reader announcements.

## 19. Authentication and Accessibility

Authentication interfaces should support:

- Keyboard navigation.
- Password managers.
- Appropriate autocomplete attributes.
- Clear validation messages.
- Accessible MFA workflows.
- Password visibility controls.
- Recovery flows.

Do not block password managers or normal paste functionality without a compelling security requirement.

Avoid inaccessible CAPTCHA-only verification flows.

See `authentication-and-authorization.md`.

## 20. Automated Accessibility Testing

Use automated tools to detect common problems.

Possible tools:

- axe-core.
- axe DevTools.
- Lighthouse.
- Playwright accessibility testing.
- Storybook accessibility addon.

Automated checks can identify issues such as:

- Missing accessible names.
- Invalid ARIA.
- Some contrast failures.
- Missing form labels.
- Certain semantic problems.

Automated tools cannot detect every accessibility issue.

They cannot reliably judge whether all content and interactions are understandable to real users.

## 21. Manual Accessibility Testing

Perform manual testing where practical.

### Keyboard testing

- Navigate using Tab and Shift + Tab.
- Activate controls using keyboard keys.
- Test dialogs and menus.
- Check focus restoration.
- Check for keyboard traps.

### Screen reader testing

Use available assistive technologies, such as:

- NVDA.
- VoiceOver.
- TalkBack.

Check:

- Page landmarks.
- Heading navigation.
- Link and button names.
- Form labels.
- Error announcements.
- Dialog behavior.
- Dynamic updates.

### Visual testing

Check:

- Text contrast.
- Focus indicators.
- Zoom.
- Reduced motion.
- Layout at narrow widths.
- Text resizing.

Do not claim full accessibility verification when only automated checks were performed.

## 22. Existing Project Accessibility Improvements

When improving accessibility in an existing application:

1. Inspect the affected pages and shared components.
1. Identify actual accessibility issues.
1. Prioritize issues that block interaction or access to information.
1. Check whether the problem originates in a shared component.
1. Fix the root cause where practical.
1. Preserve existing functionality and visual conventions.
1. Update related components if necessary.
1. Test keyboard and screen reader behavior.
1. Run automated accessibility checks.
1. Document remaining limitations.

Prefer fixing a shared component once over adding separate workarounds to every page.

Do not make broad markup changes without checking their effect on existing styling and behavior.

## 23. Common Anti-Patterns

Avoid:

- Using clickable `<div>` elements instead of buttons.
- Using links for actions without destinations.
- Removing focus outlines.
- Missing form labels.
- Placeholder-only labels.
- Missing alternative text for meaningful images.
- Unnecessary ARIA roles.
- Incorrect ARIA state attributes.
- Color-only error indicators.
- Keyboard traps.
- Dialogs without focus management.
- Inaccessible custom dropdowns.
- Motion without reduced-motion support.
- Automated scans as the only accessibility test.
- Claiming WCAG compliance without sufficient verification.

## 24. Decision Workflow

Before implementing or reviewing a UI feature:

1. Inspect its semantic structure.
1. Identify keyboard interactions.
1. Define accessible names and descriptions.
1. Check focus behavior.
1. Review contrast and visual indicators.
1. Handle dynamic announcements.
1. Respect reduced-motion preferences.
1. Test responsive behavior.
1. Run automated checks.
1. Perform manual verification where practical.

Accessibility should be part of the definition of done.

## 25. Review Checklist

### Semantics

- [ ] Semantic HTML is used.
- [ ] Heading hierarchy is meaningful.
- [ ] Buttons and links have appropriate purposes.
- [ ] Navigation landmarks are clear.

### Keyboard

- [ ] All interactive elements are reachable.
- [ ] Focus order is logical.
- [ ] Focus indicators are visible.
- [ ] Dialogs and menus support expected keyboard behavior.

### Screen Readers

- [ ] Controls have accessible names.
- [ ] Images have appropriate alternative text.
- [ ] Form errors are associated with fields.
- [ ] Dynamic updates are communicated appropriately.

### Visual Accessibility

- [ ] Contrast requirements are considered.
- [ ] Color is not the only indicator.
- [ ] Reduced motion is supported.
- [ ] Zoom and reflow are checked.

### Verification

- [ ] Automated accessibility checks were performed where available.
- [ ] Manual checks were performed where practical.
- [ ] Known limitations are documented.
- [ ] No unverified compliance claim is made.

## 26. Related References

- reusable-ui-components.md
- layouts-and-navigation.md
- dialogs-modals-and-overlays.md
- notifications-and-push.md
- forms-and-validation.md
- authentication-and-authorization.md
- ui-design-quality-and-impeccable.md
- testing-strategy.md
- performance-and-core-web-vitals.md

## 27. Official Resources

- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- WAI Introduction: https://www.w3.org/WAI/fundamentals/accessibility-intro/
- WAI-ARIA: https://www.w3.org/WAI/standards-guidelines/aria/
- ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/
- WAI Tutorials: https://www.w3.org/WAI/tutorials/
- MDN Accessibility: https://developer.mozilla.org/en-US/docs/Web/Accessibility
- axe-core: https://github.com/dequelabs/axe-core
- Lighthouse: https://developer.chrome.com/docs/lighthouse/
- Playwright Accessibility: https://playwright.dev/docs/accessibility-testing
