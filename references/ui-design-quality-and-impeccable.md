# UI Design Quality and Impeccable

## 1. Purpose

Define standards for building visually polished, usable, consistent, accessible, and production-ready frontend interfaces.

This reference covers:

- Visual design quality.
- User experience and interaction design.
- Design consistency and design systems.
- Typography and visual hierarchy.
- Layout, spacing, and color.
- Component states and behavior.
- Responsive design.
- UI inspection and refinement.
- Optional Impeccable integration.

The agent must be capable of producing high-quality interfaces independently.

Impeccable is an optional design workflow that can support UI development and review. It is not a mandatory dependency and does not replace frontend engineering practices.

## 2. Core Design Principles

Every interface should prioritize the following principles.

### Clarity

Users should understand:

- What the page or application is for.
- Which information matters.
- What actions are available.
- How to complete important tasks.
- What happens after an interaction.

### Consistency

Maintain consistency across:

- Typography.
- Spacing.
- Colors.
- Component appearance.
- Interaction behavior.
- Navigation.
- Visual hierarchy.
- Responsive patterns.

### Usability

Make important tasks easy to discover and complete.

Avoid unnecessary steps, confusing controls, unclear labels, and decorative elements that interfere with functionality.

### Accessibility

Design for different abilities and interaction methods.

Consider:

- Semantic HTML.
- Keyboard access.
- Screen reader support.
- Color contrast.
- Visible focus states.
- Readable content.
- Reduced motion preferences.

Follow the project's accessibility requirements and the relevant guidance in `accessibility-and-wcag.md`.

### Responsiveness

Adapt the interface to different screen sizes without sacrificing important content or functionality.

### Visual quality

Make deliberate visual decisions based on the product's purpose and identity.

Avoid relying on generic templates, fashionable effects, or decoration as substitutes for thoughtful design.

## 3. Inspect Before Designing

Before creating or modifying an interface:

1. Inspect the existing application and relevant files.
1. Understand its purpose and target users.
1. Identify primary user workflows.
1. Review existing design tokens and conventions.
1. Inspect typography, colors, spacing, and layouts.
1. Identify reusable components.
1. Understand responsive behavior.
1. Review accessibility requirements.
1. Identify existing visual inconsistencies.
1. Determine which existing decisions must be preserved.

For existing projects:

- Understand what already works.
- Identify the actual problem.
- Preserve established branding and useful patterns.
- Limit changes to the requested scope.
- Avoid unnecessary redesigns or migrations.

Do not assume that a new visual direction is required simply because the existing interface could look different.

## 4. Product and User Context

Base design decisions on the product's purpose, users, and requirements.

Understand relevant context:

- Target audience.
- Primary user tasks.
- Application type.
- Business requirements.
- Brand identity.
- Content structure.
- User expectations.
- Technical constraints.

Different products require different visual approaches.

| Product | Design considerations |
| ----------------- | --------------------------------------------- |
| SaaS dashboard | Information hierarchy and efficient workflows |
| E-commerce | Product discovery and purchase flow |
| Portfolio | Visual storytelling and personal identity |
| Admin panel | Data density and operational clarity |
| Developer tool | Precision and information accessibility |
| Marketing website | Messaging, trust, and conversion |

Do not apply the same visual template to every product.

When product information is missing, inspect the available evidence and ask only when an important design decision cannot reasonably be made.

Never invent brand requirements, user research, or business facts.

## 5. Visual Hierarchy

Visual hierarchy helps users understand what matters first.

Use these elements intentionally:

- Typography scale.
- Font weight.
- Spacing.
- Contrast.
- Alignment.
- Position.
- Size.
- Grouping.

Establish clear relationships between:

- Page title.
- Section headings.
- Supporting descriptions.
- Primary content.
- Secondary information.
- Primary and secondary actions.

Avoid making every element equally prominent.

Use emphasis to communicate importance, not merely to decorate the page.

## 6. Typography

Typography affects readability, hierarchy, and product identity.

Consider:

- Font family.
- Font size.
- Font weight.
- Line height.
- Letter spacing.
- Text width.
- Heading scale.
- Font loading behavior.

Guidelines:

- Use a deliberate typography system.
- Keep body text comfortable to read.
- Establish clear heading levels.
- Avoid excessive font sizes and weights.
- Limit unnecessary font families.
- Use appropriate line lengths.
- Check text wrapping on smaller screens.
- Avoid layout shifts caused by font loading.
- Respect existing brand typography.

Do not automatically choose the same font for every project.

## 7. Color and Contrast

Use colors intentionally and establish clear semantic roles.

Typical roles include:

- Background.
- Surface.
- Primary text.
- Secondary text.
- Muted text.
- Border.
- Primary action.
- Secondary action.
- Success.
- Warning.
- Error.
- Information.

Guidelines:

- Reuse semantic design tokens.
- Maintain readable contrast.
- Avoid color-only communication.
- Make interactive states distinguishable.
- Support light and dark themes when required.
- Consider disabled and selected states.
- Avoid arbitrary gradients and decorative color combinations.

Do not select colors only because they are fashionable.

Follow the existing visual identity unless the task explicitly requires a redesign.

See `theming-and-dark-mode.md` for theme implementation guidance.

## 8. Layout and Spacing

Use a consistent layout system.

Consider:

- Content width.
- Grid structure.
- Alignment.
- Spacing scale.
- Section separation.
- Component density.
- Responsive breakpoints.
- Content priority.

Guidelines:

- Group related content.
- Separate unrelated sections.
- Align elements consistently.
- Avoid excessive whitespace without purpose.
- Avoid overcrowding.
- Reuse predictable spacing tokens.
- Keep important content visible.
- Account for long and variable content.

Do not use cards for every section.

Use cards when they communicate meaningful grouping, separation, or interaction.

## 9. Component Visual Quality

Reusable components should have consistent appearance and predictable behavior.

Consider relevant component states:

- Default.
- Hover.
- Focus.
- Active.
- Disabled.
- Loading.
- Selected.
- Error.
- Success.

Important components include:

- Buttons.
- Inputs.
- Selects.
- Checkboxes.
- Switches.
- Cards.
- Tables.
- Dialogs.
- Navigation.
- Tabs.
- Dropdowns.
- Toasts.

Do not introduce visual inconsistencies between components that serve similar purposes.

Use existing shared components and design tokens where appropriate.

See:

- `reusable-ui-components.md`
- `dialogs-modals-and-overlays.md`
- `notifications-and-push.md`

## 10. Interaction Design

Every interactive element should communicate its purpose and behavior.

Guidelines:

- Use clear action labels.
- Provide visible interaction feedback.
- Prevent accidental destructive actions.
- Show loading states for asynchronous operations.
- Communicate success and failure.
- Preserve user input when appropriate.
- Avoid unexpected navigation.
- Provide practical touch targets.
- Support keyboard interaction.
- Prevent repeated submissions where necessary.
- Make disabled states understandable.

Do not make decorative elements look interactive.

Do not use animation as a substitute for clear feedback.

Animations should support understanding and interaction rather than delay important tasks.

## 11. Responsive Design Quality

Responsive design is more than shrinking desktop layouts.

Consider:

- Content priority.
- Navigation changes.
- Column rearrangement.
- Typography scaling.
- Touch interactions.
- Table overflow.
- Image cropping.
- Dialog sizing.
- Sidebar behavior.
- Mobile browser viewport constraints.
- Long content and dynamic data.

Review:

- Small mobile screens.
- Large mobile screens.
- Tablets.
- Laptops.
- Desktop screens.

Test intermediate widths rather than checking only a few predefined device sizes.

Avoid hiding essential functionality simply to make a layout fit.

Use appropriate layout techniques such as flexible grids, fluid sizing, and content-driven breakpoints.

## 12. Visual Design Anti-Patterns

Watch for generic or repetitive design decisions.

Examples include:

- Unnecessary gradient backgrounds.
- Excessive rounded cards.
- Cards nested inside cards.
- Repeated icon tiles above every heading.
- Too many shadows.
- Excessive borders.
- Inconsistent spacing.
- Weak typography hierarchy.
- Low-contrast text.
- Decorative elements without purpose.
- Excessive animations.
- Unnecessary glassmorphism.
- Generic dashboard layouts unrelated to the product.
- Overuse of the same accent color.
- Buttons without clear action labels.
- Unnecessary visual complexity.

These are warning signs, not absolute prohibitions.

A design decision should be judged by context, usability, product identity, and implementation quality—not by a fixed aesthetic rule.

See `anti-ai-slop-and-engineering-quality.md` for the cross-cutting engineering quality standard.

## 13. Improving Existing Interfaces

When improving an existing interface:

1. Understand the current design and architecture.
1. Identify the requested improvement.
1. Inspect affected pages and components.
1. Identify existing reusable tokens and patterns.
1. Preserve established branding.
1. Identify actual visual and usability problems.
1. Prioritize issues by impact.
1. Make targeted changes.
1. Review responsive behavior.
1. Check for functional and visual regressions.

Do not redesign unrelated sections.

Do not replace working components simply to make the implementation look different.

Preserve existing functionality, user workflows, and useful design decisions.

## 14. UI Review and Verification

Review interfaces across multiple dimensions.

### Visual review

Check:

- Typography.
- Color.
- Spacing.
- Alignment.
- Visual hierarchy.
- Component consistency.
- Content density.
- Image quality and cropping.

### UX review

Check:

- User flows.
- Navigation clarity.
- Action discoverability.
- Interaction feedback.
- Error prevention.
- Empty states.
- Loading states.
- Destructive action handling.

### Technical review

Check:

- Accessibility.
- Responsive behavior.
- Rendering.
- Performance.
- Browser compatibility.
- Console errors.
- Broken interactions.
- Layout stability.

### Production review

Consider realistic conditions:

- Real content.
- Long text.
- Empty data.
- Large datasets.
- Slow networks.
- Failed requests.
- Permission restrictions.
- Different user roles.
- Different application states.

A visually attractive screenshot does not prove that an interface works correctly.

## 15. Impeccable Integration

### 15.1 What Is Impeccable?

Impeccable is an open-source design skill and workflow for AI coding agents.

It provides design vocabulary, guidance, and workflows for:

- Creating interfaces.
- Reviewing visual quality.
- Improving typography.
- Refining layouts.
- Improving interaction feedback.
- Reviewing accessibility and technical quality.
- Identifying generic design patterns.
- Reducing unnecessary visual complexity.

Official resources:

- Website: https://impeccable.style/
- Documentation: https://impeccable.style/docs/
- GitHub: https://github.com/pbakaus/impeccable

### 15.2 Optional Integration Rule

Impeccable is optional.

The frontend engineering skill must remain fully usable without it.

Before using Impeccable:

1. Check whether it is installed or available through the current coding tool.
1. Identify the supported invocation syntax.
1. Read the installed skill instructions.
1. Check its available commands and references.
1. Inspect relevant project context.
1. Use it only when it provides value to the task.

Never:

- Assume Impeccable is installed.
- Claim a command ran without executing it.
- Invent commands or command options.
- Assume every coding agent uses identical syntax.
- Install or update it without user authorization.
- Make the frontend skill dependent on Impeccable.
- Treat its recommendations as automatically correct.

If Impeccable is unavailable, follow this reference and the other frontend engineering references directly.

### 15.3 Installation

The official documentation currently provides this installation method:

```bash
npx impeccable install
```

The installer guides the user through selecting a supported coding tool and installation scope.

The current documented CLI requirement is Node.js 18.19 or later.

After installation, reload the coding tool as instructed.

Other installation routes may be available depending on the coding tool, including plugin or shared Agent Skill installation.

Important:

- Do not install it automatically.
- Do not add it as a project runtime dependency.
- Do not assume Node.js is already installed.
- Check the official installation documentation before giving current setup instructions.
- Explain that installation may create tool-specific files or integrations.

Official installation guide:

https://impeccable.style/tutorials/getting-started/

### 15.4 Invocation and Project Context

Most supported agents use:

```text
/impeccable
```

Codex uses:

```text
$impeccable
```

Exact invocation depends on the coding tool and installed integration.

The official workflow includes:

```text
/impeccable init
```

Initialization reads the project and helps establish product context in `PRODUCT.md`.

For documenting an existing visual system, the official workflow also provides:

```text
/impeccable document
```

This can help capture existing design decisions in `DESIGN.md`.

Guidelines:

- Inspect generated files before relying on them.
- Correct inaccurate assumptions.
- Preserve existing product and brand requirements.
- Do not overwrite useful project documentation blindly.
- Do not invent missing product facts.
- Do not assume these files exist before checking.
- Keep generated documentation consistent with the actual application.

Official references:

- Getting started: https://impeccable.style/tutorials/getting-started/
- Initialization: https://impeccable.style/docs/init/

### 15.5 Useful Impeccable Workflows

Use focused workflows when they match the task.

Examples of documented commands include:

| Command | Purpose |
| ---------- | --------------------------------------- |
| `init` | Establish product context |
| `document` | Document the existing design system |
| `critique` | Review UX and visual design quality |
| `audit` | Review implementation quality |
| `polish` | Refine an interface |
| `typeset` | Improve typography |
| `layout` | Improve layout and spacing |
| `animate` | Improve motion and interaction feedback |
| `distill` | Remove unnecessary complexity |
| `adapt` | Improve responsive behavior |
| `harden` | Address edge cases and robustness |
| `optimize` | Review performance |

Example usage:

```text
/impeccable critique the dashboard

/impeccable audit the settings page

/impeccable polish the user management page

/impeccable adapt the navigation for mobile
```

These are examples, not a permanent command specification.

Always inspect the installed version's instructions before invoking a command. Available commands, descriptions, and syntax can change.

Official command documentation:

https://impeccable.style/docs/

### 15.6 When to Use Impeccable

Consider using it when:

- Creating a new visual direction.
- Improving an existing page.
- Reviewing an interface before release.
- Refining typography and spacing.
- Improving responsive behavior.
- Identifying generic visual patterns.
- Documenting an existing design system.
- Performing a focused UI quality pass.

It is not necessary for every small frontend change.

For a simple bug fix, content update, or backend-only task, do not invoke design workflows without a reason.

Prefer focused reviews of the affected page or component over broad reviews that produce unrelated changes.

### 15.7 Impeccable in Existing Projects

When using Impeccable in an existing project:

1. Inspect the application first.
1. Understand its current design system.
1. Identify the requested target.
1. Review existing `PRODUCT.md` and `DESIGN.md`, if present.
1. Use the relevant design workflow.
1. Review recommendations against actual project requirements.
1. Preserve existing functionality.
1. Implement only justified changes.
1. Verify the implementation in the application.
1. Run relevant engineering checks.

Do not allow a design refinement workflow to trigger an unnecessary application rewrite.

### 15.8 Impeccable Does Not Replace Engineering Verification

Impeccable can support design and UI quality work.

It does not replace:

- Type checking.
- Linting.
- Automated tests.
- Accessibility testing.
- Security review.
- Browser testing.
- Build verification.
- Runtime debugging.
- API validation.

The frontend engineering skill remains responsible for verifying actual code changes.

## 16. Screenshot and Browser Review

When browser or screenshot tools are available, inspect the actual rendered interface.

Review:

- Desktop layout.
- Mobile layout.
- Navigation.
- Interaction states.
- Overflow.
- Typography.
- Spacing.
- Dialog behavior.
- Loading states.
- Empty states.
- Error states.

Compare the implementation against the intended design and actual product requirements.

Do not claim visual verification if the application was not rendered or inspected.

If browser tools are unavailable:

- Perform code-level checks.
- Inspect styles and component structure.
- Run available automated checks.
- Clearly report what could not be visually verified.

Do not treat source-code inspection as equivalent to browser verification.

## 17. Final Quality Pass

Before considering a UI task complete, verify the relevant requirements:

### Design

- [ ] Visual hierarchy is clear.
- [ ] Typography is consistent.
- [ ] Colors are intentional.
- [ ] Spacing and alignment are consistent.
- [ ] Components follow existing design conventions.
- [ ] Decorative elements serve a purpose.

### UX

- [ ] Main user tasks are clear.
- [ ] Navigation is understandable.
- [ ] Actions provide appropriate feedback.
- [ ] Empty and error states are handled.
- [ ] Interactions behave predictably.
- [ ] Destructive actions are handled safely.

### Accessibility

- [ ] Semantic markup is used.
- [ ] Contrast is sufficient.
- [ ] Keyboard navigation works.
- [ ] Focus states are visible.
- [ ] Motion preferences are respected.

### Responsive behavior

- [ ] Mobile behavior is usable.
- [ ] Tablet layout is considered.
- [ ] Desktop layout is consistent.
- [ ] Content does not overflow.
- [ ] Important functionality remains available.

### Verification

- [ ] Relevant interactions were tested.
- [ ] Relevant tests pass.
- [ ] Type checking passes when available.
- [ ] Linting passes when available.
- [ ] Build passes when relevant.
- [ ] Visual verification is reported accurately.

Do not perform endless visual changes after the interface satisfies its requirements.

## 18. Decision Workflow

### For new interfaces

1. Understand the product and users.
1. Inspect project architecture and existing conventions.
1. Identify the required user workflows.
1. Establish or reuse design tokens.
1. Define an appropriate visual direction.
1. Build the layout and components.
1. Implement interactions and states.
1. Review responsive behavior.
1. Perform accessibility and quality checks.
1. Use Impeccable if installed and useful.
1. Verify the implementation.

### For existing interfaces

1. Inspect the current implementation.
1. Understand what must be preserved.
1. Identify the actual design and usability problems.
1. Prioritize improvements by impact.
1. Modify existing components safely.
1. Review the rendered interface when possible.
1. Test affected functionality.
1. Check for regressions.
1. Report completed and unverified checks.

Choose the smallest workflow that adequately satisfies the task.

## 19. Related References

- `anti-ai-slop-and-engineering-quality.md`
- `architecture-and-project-structure.md`
- `theming-and-dark-mode.md`
- `reusable-ui-components.md`
- `layouts-and-navigation.md`
- `dialogs-modals-and-overlays.md`
- `notifications-and-push.md`
- `accessibility-and-wcag.md`
- `performance-and-core-web-vitals.md`
- `testing-strategy.md`

## 20. Official Resources

- Impeccable: https://impeccable.style/
- Impeccable documentation: https://impeccable.style/docs/
- Getting started: https://impeccable.style/tutorials/getting-started/
- Impeccable GitHub: https://github.com/pbakaus/impeccable
- WCAG guidelines: https://www.w3.org/WAI/standards-guidelines/wcag/
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- MDN Responsive Design: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design
