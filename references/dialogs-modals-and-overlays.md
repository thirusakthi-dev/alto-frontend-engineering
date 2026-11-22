# Dialogs, Modals and Overlays

## 1. Purpose

Define standards for designing, implementing, modifying and maintaining frontend overlays.

Support:

- Dialogs.
- Confirmation modals.
- Alert dialogs.
- Drawers and sheets.
- Popovers.
- Dropdown menus.
- Tooltips.
- Context menus.
- Command menus.
- Full-screen overlays.
- Focus management.
- Keyboard accessibility.

The objective is to create accessible, predictable and consistent overlay interactions.

## 2. Inspect Before Implementation

Before implementing an overlay:

1. Inspect the existing UI component library.
1. Check whether an accessible dialog or overlay primitive already exists.
1. Review the project's styling and design tokens.
1. Identify existing overlay components.
1. Understand how overlays are opened and closed.
1. Check existing focus management.
1. Review keyboard interaction behavior.
1. Identify responsive requirements.
1. Check whether the overlay needs to support nested interactions.

For existing projects, extend the established implementation where possible.

Do not introduce another overlay library without a clear reason.

## 3. Choose the Correct Pattern

Different overlays serve different interaction needs.

| Pattern | Appropriate use |
| ------------- | --------------------------------------------- |
| Dialog | Focused interaction requiring attention |
| Alert dialog | Important decision requiring confirmation |
| Drawer | Supporting content or actions in a side panel |
| Bottom sheet | Compact mobile-oriented interaction |
| Popover | Contextual content near a trigger |
| Dropdown menu | A list of actions or commands |
| Tooltip | Brief supplementary information |
| Context menu | Actions related to a selected item |
| Command menu | Searchable application commands |

Do not use a modal for every interaction.

Choose the least disruptive pattern that satisfies the requirement.

## 4. Dialog

A dialog presents focused content above the current page.

Common use cases:

- Create or edit forms.
- User details.
- Settings.
- Multi-step workflows.
- Important information.

A dialog commonly includes:

- Title.
- Description.
- Main content.
- Optional footer actions.
- Close control.

Guidelines:

- Give the dialog a meaningful title.
- Provide a description when useful.
- Make its purpose clear.
- Keep content focused.
- Prevent unintended background interaction for modal dialogs.
- Provide an understandable close action.
- Support keyboard interaction.

Avoid oversized dialogs for simple interactions.

## 5. Confirmation and Alert Dialogs

Use confirmation dialogs for consequential actions.

Examples:

- Delete a record.
- Cancel a subscription.
- Discard unsaved changes.
- Remove a user.
- Perform an irreversible operation.

Guidelines:

- Explain what will happen.
- Identify the affected item when relevant.
- Use clear action labels.
- Distinguish destructive actions visually.
- Avoid vague labels such as "OK" when a specific action name is clearer.
- Prevent duplicate submissions.
- Display an appropriate loading state.
- Handle failures without silently closing the dialog.

Example:

```text
Delete customer?

This action will permanently delete the selected customer.

[Cancel] [Delete customer]
```

Do not ask for confirmation for every harmless action.

Use confirmation when the impact justifies the interruption.

## 6. Drawer and Sheet

Drawers display content in a panel attached to an edge of the screen.

Common use cases:

- Mobile navigation.
- Filters.
- Details panels.
- Shopping carts.
- Secondary forms.
- Contextual editing.

Guidelines:

- Choose an appropriate opening direction.
- Keep the panel width responsive.
- Support a clear dismissal action.
- Manage focus appropriately.
- Prevent background interaction when modal.
- Handle long content and scrolling.
- Avoid covering essential actions.

For mobile layouts, a bottom sheet may be more suitable than a narrow side panel.

Do not assume every drawer must be modal.

## 7. Popovers

Popovers display contextual content near a trigger.

Examples:

- Date selection.
- Filter controls.
- User details.
- Small contextual forms.
- Formatting options.

Guidelines:

- Position the popover relative to its trigger.
- Handle viewport boundaries.
- Avoid clipping inside scroll containers.
- Support keyboard navigation.
- Close appropriately after interaction.
- Ensure the trigger has an accessible name.
- Manage focus based on the interaction pattern.

Do not use a popover for content that needs a full-page workflow.

## 8. Dropdown Menus

Dropdown menus present a list of actions or options.

Examples:

- Account actions.
- More actions.
- Table row actions.
- Export options.
- Navigation actions.

Guidelines:

- Use menu semantics when implementing an actual action menu.
- Support keyboard navigation.
- Provide an appropriate trigger.
- Highlight the active item.
- Handle disabled items correctly.
- Close after an action when appropriate.
- Avoid nested menus unless they provide real value.

Do not use an action menu as a substitute for a form select.

A form select and an action menu have different interaction and accessibility requirements.

## 9. Tooltips

Tooltips provide short supplementary information.

Examples:

- Explaining an icon-only action.
- Describing a disabled control.
- Clarifying an abbreviation.

Guidelines:

- Keep tooltip content brief.
- Show tooltips through appropriate pointer and keyboard interactions.
- Do not make essential instructions available only through tooltips.
- Avoid interactive controls inside ordinary tooltips.
- Ensure tooltips do not obscure important content.
- Use accessible relationships such as `aria-describedby` when appropriate.

Do not use tooltips as the only accessible label for an action.

## 10. Context Menus

Context menus expose actions related to a selected item or region.

Common triggers:

- Right-click.
- Keyboard context-menu key.
- Dedicated action trigger.

Guidelines:

- Support keyboard access.
- Provide a clear set of contextual actions.
- Position menus within viewport boundaries.
- Dismiss when appropriate.
- Keep actions relevant to the selected item.
- Do not make important actions available exclusively through right-click.

## 11. Focus Management

Focus management is essential for accessible overlays.

For modal dialogs:

1. Move focus into the dialog when opened.
1. Keep keyboard focus within the modal interaction.
1. Support expected keyboard navigation.
1. Restore focus to the trigger when closed, when appropriate.
1. Ensure the dialog has an accessible name.

For non-modal popovers and other overlays, use the focus behavior appropriate to their interaction pattern.

Do not apply modal focus trapping to every overlay.

## 12. Keyboard Interaction

Support expected keyboard behavior.

Common expectations:

| Key | Typical behavior |
| ----------- | ----------------------------------------------- |
| Tab | Move to the next focusable element |
| Shift + Tab | Move to the previous focusable element |
| Escape | Dismiss a dismissible overlay |
| Enter | Activate the focused action |
| Space | Activate applicable controls |
| Arrow keys | Navigate menu or list options where appropriate |

Exact behavior depends on the overlay pattern.

Follow the relevant WAI-ARIA Authoring Practices instead of inventing custom keyboard behavior.

## 13. Overlay Stacking and Z-Index

Define a consistent layering strategy.

Possible layers:

```text
Base content
Sticky header
Dropdown and popover
Drawer
Modal backdrop
Modal dialog
Critical notification
```

The actual order should follow the application's interaction requirements.

Guidelines:

- Reuse centralized z-index tokens.
- Avoid arbitrary large z-index values.
- Understand stacking contexts.
- Consider transformed and positioned ancestors.
- Use portals when appropriate.
- Ensure overlays are not clipped by parent containers.

Do not assume increasing z-index always solves overlay positioning problems.

## 14. Portals

Portals can render overlays outside the normal component DOM hierarchy.

Useful for:

- Dialogs.
- Drawers.
- Dropdown menus.
- Popovers.
- Tooltips.

Consider:

- Event propagation.
- Focus management.
- Server-side rendering.
- Hydration.
- Stacking contexts.
- Cleanup when unmounted.

Use the existing library's portal mechanism when available.

Do not introduce portals unnecessarily for ordinary inline UI.

## 15. Scroll Management

Modal overlays may need to prevent background scrolling.

Guidelines:

- Prevent unintended background scrolling.
- Preserve the dialog's own scrolling.
- Restore the previous scroll behavior on close.
- Handle nested overlays safely.
- Consider mobile browser behavior.
- Avoid layout shifts when scrollbars disappear.

Do not apply global overflow changes without understanding their side effects.

## 16. Form Dialogs

When dialogs contain forms:

- Use meaningful labels.
- Show validation feedback.
- Preserve entered values when appropriate.
- Prevent duplicate submissions.
- Disable or guard actions while submitting.
- Display server errors clearly.
- Close only after the intended operation succeeds.
- Handle unsaved changes when necessary.

Keep form validation and business logic separate from generic dialog presentation.

See `forms-and-validation.md` for form engineering standards.

## 17. Animation and Motion

Use motion to communicate state changes.

Examples:

- Dialog fade and scale.
- Drawer slide.
- Popover appearance.
- Backdrop transition.

Guidelines:

- Keep transitions short and purposeful.
- Avoid excessive movement.
- Support reduced-motion preferences.
- Do not delay important interactions unnecessarily.
- Avoid animations that create layout instability.

Follow the project's existing animation system.

Do not add an animation dependency for a few simple transitions without a clear benefit.

## 18. Responsive Behavior

Check overlay behavior on:

- Mobile phones.
- Tablets.
- Desktop screens.
- Small viewport heights.
- Zoomed interfaces.

Consider:

- Dialog width.
- Maximum height.
- Internal scrolling.
- Touch targets.
- Close controls.
- Drawer direction.
- On-screen keyboards.
- Safe areas on mobile devices.

Avoid dialogs that become inaccessible on short screens.

## 19. Overlay Libraries

Prefer established accessible primitives for complex interactions.

Possible options:

- Radix UI.
- React Aria.
- Headless UI.
- Existing framework or component-library primitives.

Before choosing:

1. Inspect existing dependencies.
1. Verify framework compatibility.
1. Check accessibility behavior.
1. Review customization options.
1. Consider bundle impact.
1. Check maintenance and version support.

Do not install multiple libraries for overlapping overlay functionality.

## 20. Existing Overlay Modification

When changing an existing overlay:

1. Find its implementation.
1. Identify all consumers.
1. Understand its current public API.
1. Inspect focus and keyboard behavior.
1. Check stacking and portal behavior.
1. Identify responsive constraints.
1. Make the smallest reliable change.
1. Test opening, interaction and dismissal.
1. Check related overlays for regressions.

Preserve existing behavior unless the request requires a change.

Do not replace the overlay implementation just to change its visual appearance.

## 21. Testing

Verify:

- Opening and closing.
- Trigger behavior.
- Escape dismissal.
- Focus entry and restoration.
- Keyboard navigation.
- Background interaction.
- Form submission.
- Error handling.
- Duplicate submission prevention.
- Viewport positioning.
- Mobile behavior.
- Nested overlay behavior where supported.

Use automated tests and manual keyboard checks where appropriate.

## 22. Common Anti-Patterns

Avoid:

- Using modals for every interaction.
- Missing dialog titles.
- Inaccessible icon-only triggers.
- Incorrect focus trapping.
- Missing focus restoration.
- Broken Escape behavior.
- Uncontrolled body scroll locking.
- Arbitrary z-index values.
- Tooltips containing essential information.
- Using action menus as form selects.
- Nested overlays without a clear reason.
- Closing forms before successful submission.
- Replacing accessible primitives with custom inaccessible markup.

## 23. Decision Workflow

Before implementing an overlay:

1. Identify the interaction's purpose.
1. Select the appropriate overlay pattern.
1. Inspect existing primitives and components.
1. Define opening and dismissal behavior.
1. Design keyboard and focus behavior.
1. Plan responsive positioning.
1. Handle loading and error states.
1. Implement using established conventions.
1. Test accessibility and interaction.
1. Verify existing consumers.

Prefer established accessible behavior over custom interaction implementations.

## 24. Review Checklist

### Architecture

- [ ] Correct overlay pattern selected.
- [ ] Existing components reused.
- [ ] Responsibilities remain focused.
- [ ] Stacking behavior is predictable.

### Accessibility

- [ ] Accessible name and description exist where needed.
- [ ] Keyboard interaction works.
- [ ] Focus is managed correctly.
- [ ] Dismissal behavior is clear.

### Interaction

- [ ] Opening and closing work.
- [ ] Background behavior is correct.
- [ ] Forms handle errors and loading.
- [ ] Duplicate actions are prevented.

### Responsive behavior

- [ ] Overlay fits small screens.
- [ ] Content scrolls correctly.
- [ ] Touch interactions work.
- [ ] Viewport boundaries are respected.

### Verification

- [ ] Relevant tests pass.
- [ ] Existing consumers still work.
- [ ] No unrelated behavior is broken.

## 25. Related References

- reusable-ui-components.md
- layouts-and-navigation.md
- global-styles-and-design-tokens.md
- theming-and-dark-mode.md
- forms-and-validation.md
- accessibility-and-wcag.md
- testing-strategy.md
- performance-and-core-web-vitals.md

## 26. Official Resources

- WAI-ARIA Authoring Practices: https://www.w3.org/WAI/ARIA/apg/
- WAI-ARIA Dialog Pattern: https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
- WAI-ARIA Menu Button Pattern: https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/
- WAI-ARIA Tooltip Pattern: https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/
- Radix UI Dialog: https://www.radix-ui.com/primitives/docs/components/dialog
- Radix UI Popover: https://www.radix-ui.com/primitives/docs/components/popover
- React Aria Components: https://react-spectrum.adobe.com/react-aria/components.html
- MDN Dialog: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog
