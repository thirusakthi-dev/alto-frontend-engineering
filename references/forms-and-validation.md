# Forms and Validation

## 1. Purpose

Define standards for building, modifying, validating, testing and maintaining forms in frontend applications.

Support:

- Native HTML forms.
- React form handling.
- Controlled and uncontrolled inputs.
- Client-side validation.
- Server-side validation.
- Schema-based validation.
- Form libraries.
- Error handling.
- File inputs and uploads.
- Multi-step forms.
- Dynamic fields.
- Accessible form experiences.
- Form submission and API integration.

The objective is to create forms that are accessible, predictable, maintainable and reliable.

## 2. Inspect Before Implementation

Before building or modifying forms:

1. Inspect existing form components.
1. Identify the current form library.
1. Check validation libraries and schemas.
1. Review input and field components.
1. Understand API request requirements.
1. Inspect existing error-handling patterns.
1. Review form submission behavior.
1. Check existing accessibility conventions.
1. Identify reusable form utilities.

For existing projects, reuse the established form architecture where practical.

Do not introduce another form library without a clear reason.

## 3. Form Architecture

Keep form responsibilities organized.

A typical structure:

```text
Feature
├── components/
│   └── user-form.tsx
├── schemas/
│   └── user.schema.ts
├── hooks/
│   └── use-user-form.ts
├── api/
│   └── users.api.ts
└── types/
    └── user.types.ts
```

Possible responsibilities:

| Layer | Responsibility |
| --------------- | ---------------------------------- |
| Form component | Input rendering and layout |
| Field component | Label, input, hint and error |
| Schema | Validation rules |
| Hook | Form state and submission behavior |
| API service | Backend communication |
| Backend | Authoritative validation |

Adapt the structure to the project.

Do not create unnecessary files for small forms.

## 4. Native HTML Forms

Use semantic HTML form elements.

Common elements:

- `<form>`
- `<label>`
- `<input>`
- `<textarea>`
- `<select>`
- `<button>`
- `<fieldset>`
- `<legend>`

Use the correct input type.

Examples:

| Input type | Purpose |
| ---------- | ------------------------------- |
| text | General text |
| email | Email address |
| password | Password |
| number | Numeric input |
| tel | Telephone number |
| date | Date |
| checkbox | Multiple independent selections |
| radio | One selection from a group |
| file | File selection |

Use native browser behavior where it provides a useful baseline.

Do not replace native semantics with generic clickable elements.

## 5. Controlled and Uncontrolled Inputs

### Controlled inputs

React state controls the input value.

```tsx
const [email, setEmail] = useState("");

<input
  type="email"
  value={email}
  onChange={(event) => setEmail(event.target.value)}
/>;
```

Use controlled inputs when the UI needs immediate access to the current value.

### Uncontrolled inputs

The browser maintains the input value.

```tsx
const inputRef = useRef<HTMLInputElement>(null);

<input ref={inputRef} name="email" type="email" />;
```

Use uncontrolled inputs when direct DOM access or native form submission is sufficient.

### Decision

Choose based on requirements.

Do not make every input controlled automatically.

Avoid switching an input between controlled and uncontrolled states.

## 6. React Form Handling

Use React's form capabilities appropriately.

Consider:

- Native form submission.
- Controlled input state.
- FormData.
- Server Actions where supported.
- Existing form libraries.
- React 19 form actions where appropriate.

Example using FormData:

```tsx
function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
  event.preventDefault();

  const formData = new FormData(event.currentTarget);

  const email = formData.get("email");

  console.log(email);
}
```

Do not use `console.log` for sensitive production form data.

Always prevent unintended page reloads when handling submissions through client-side logic.

Do not disable native form behavior without a reason.

## 7. Form Libraries

Choose a form library based on actual complexity.

Common options:

- React Hook Form.
- Formik.
- TanStack Form.

### React Hook Form

Useful for:

- Complex forms.
- Validation integration.
- Reducing unnecessary re-renders.
- Dynamic fields.
- Large forms.

### Formik

An established form management library with state and validation support.

Use when already adopted or when it fits the project.

### TanStack Form

Provides a type-safe form state and validation approach.

Evaluate its fit with the existing architecture.

### Decision

- Small forms: native HTML and simple React state may be sufficient.
- Medium forms: use a consistent shared approach.
- Complex forms: consider a dedicated form library.

Do not introduce multiple form libraries without a strong migration or integration reason.

## 8. Validation Strategy

Use multiple validation layers.

### Client-side validation

Provides immediate feedback.

Examples:

- Required fields.
- Email format.
- Minimum and maximum length.
- Password requirements.
- Numeric ranges.
- Date constraints.
- File type and size.

### Server-side validation

Provides authoritative validation.

The backend must validate incoming data regardless of frontend validation.

Client-side validation is for user experience, not security.

Never trust frontend validation as the only protection.

## 9. Schema-Based Validation

Use schemas when validation logic is reusable or complex.

Common libraries:

- Zod.
- Valibot.
- Yup.
- ArkType.

Example using Zod:

```tsx
import { z } from "zod";

export const userSchema = z.object({
  name: z.string().min(2).max(100),

  email: z.string().email(),

  age: z.number().int().min(18).optional(),
});

export type UserFormValues = z.infer<typeof userSchema>;
```

Guidelines:

- Keep validation rules close to their domain.
- Reuse schemas when appropriate.
- Avoid duplicating identical rules across components.
- Keep frontend and backend contracts aligned.
- Understand differences between browser input values and parsed data.

For example, an HTML number input usually provides a string value. Convert and validate it deliberately.

## 10. Validation Timing

Validation can happen:

- On submit.
- On blur.
- On change.
- After a failed submission.
- Through explicit validation actions.

Choose timing based on the field and user experience.

Recommended considerations:

- Required fields can be validated on submit.
- Complex fields may be validated on blur.
- Avoid displaying errors before users have interacted with a field.
- Avoid excessive validation on every keystroke.
- Clear outdated errors when the relevant value changes.

Do not make validation behavior inconsistent across similar forms.

## 11. Field Components

Reusable fields should provide consistent behavior.

A field may contain:

- Label.
- Input.
- Description.
- Required indicator.
- Validation error.
- Optional helper action.

Example:

```tsx
interface FieldProps {
  id: string;
  label: string;
  error?: string;
  hint?: string;
  required?: boolean;
}
```

Guidelines:

- Associate labels with controls.
- Use stable IDs.
- Connect hints and errors using `aria-describedby`.
- Use `aria-invalid` when appropriate.
- Keep error messages understandable.
- Preserve native keyboard behavior.

Do not build a single oversized field component with excessive conditional props.

## 12. Error Handling

Handle different error sources separately.

### Client validation errors

Display near the affected field.

### Server validation errors

Map backend field errors to their corresponding inputs when possible.

### General API errors

Display a clear form-level message.

### Network errors

Explain that the request could not be completed and provide an appropriate retry action.

### Conflict errors

Explain when the submitted information conflicts with existing data.

Do not silently discard backend errors.

Do not expose internal server messages or stack traces.

## 13. Submission State

A reliable form should handle:

- Idle.
- Submitting.
- Success.
- Validation failure.
- General failure.

Example:

```tsx
<button type="submit" disabled={isSubmitting}>
  {isSubmitting ? "Saving..." : "Save"}
</button>
```

Guidelines:

- Prevent accidental duplicate submissions.
- Show useful progress feedback.
- Preserve user-entered data after recoverable failures.
- Avoid resetting the form before success is confirmed.
- Handle slow network responses.
- Provide clear success feedback.

Do not use a loading state that makes the form inaccessible.

## 14. Reset and Default Values

Consider:

- Initial values.
- Edit form data.
- Reset behavior.
- Default selections.
- Asynchronous data loading.
- Dirty state.

For edit forms, distinguish between:

- Initial loading.
- Loaded server data.
- User modifications.
- Resetting to the latest loaded values.

Do not overwrite user edits when background data changes unexpectedly.

## 15. Dynamic Forms and Field Arrays

Some forms need fields that users can add or remove.

Examples:

- Multiple phone numbers.
- Addresses.
- Product variants.
- Experience records.
- Dynamic questions.

Guidelines:

- Use stable identifiers as keys.
- Preserve field values during reordering.
- Validate each item.
- Handle empty arrays.
- Provide accessible add/remove controls.
- Confirm destructive removal when appropriate.

Avoid using array indexes as keys when list items can be reordered or removed.

## 16. Multi-Step Forms

Use multi-step forms when a long form can be divided into meaningful stages.

Typical flow:

```text
Step 1: Basic Information
          |
          v
Step 2: Details
          |
          v
Step 3: Review
          |
          v
Step 4: Submit
```

Consider:

- Step navigation.
- Progress indicators.
- Per-step validation.
- Previous and next actions.
- Preserving entered values.
- Final review.
- Submission failure.
- Browser refresh behavior.

Validate the current step before moving forward.

Validate the complete payload before final submission.

Do not assume hiding a step removes its values from the form.

## 17. Conditional Fields

Some fields depend on previous answers.

Examples:

- Company details when account type is business.
- Additional address fields.
- Conditional payment details.

Guidelines:

- Render only relevant fields.
- Define what happens to hidden field values.
- Validate only applicable fields.
- Avoid stale hidden values being submitted unintentionally.
- Make conditional behavior understandable.

## 18. File Inputs

For file selection:

- Validate allowed types.
- Validate maximum size.
- Show selected file information.
- Support removal or replacement.
- Handle upload progress.
- Handle failed uploads.
- Provide accessible descriptions.

Example:

```tsx
<input type="file" accept="image/png,image/jpeg" onChange={handleFileChange} />
```

The `accept` attribute is a user-interface hint, not a security boundary.

Validate files on the backend too.

Do not trust filenames, extensions or browser-provided MIME types as proof of file safety.

See `api-integration.md` for upload implementation.

## 19. Accessibility

Forms must work with keyboards and assistive technologies.

Guidelines:

- Every input has an accessible label.
- Related controls use fieldset and legend.
- Required status is communicated clearly.
- Error messages are programmatically associated with fields.
- Focus is managed after failed submissions when appropriate.
- Validation is not communicated using color alone.
- Controls have visible focus indicators.
- Custom controls support keyboard interaction.
- Dynamic error announcements use appropriate live regions.

For a failed submission, consider moving focus to an error summary or the first invalid field.

Do not move focus unexpectedly during ordinary typing.

## 20. Security

Treat all form data as untrusted.

Important practices:

- Validate on the server.
- Enforce authorization on the backend.
- Protect cookie-authenticated state-changing requests against CSRF where applicable.
- Avoid exposing sensitive values in logs.
- Avoid placing secrets in browser code.
- Sanitize untrusted content before rendering as HTML.
- Apply file upload security controls.
- Avoid leaking sensitive data in URLs.
- Use secure transport in production.

Frontend validation does not replace backend validation or authorization.

## 21. Form Performance

For large forms:

- Avoid unnecessary re-renders.
- Use appropriate controlled or uncontrolled inputs.
- Split complex forms into meaningful sections.
- Subscribe only to required field state where supported.
- Avoid expensive validation on every keystroke.
- Lazy-load genuinely heavy optional sections when useful.

Do not optimize simple forms without evidence of a performance problem.

## 22. Existing Form Modification

When changing an existing form:

1. Inspect its component and field structure.
1. Identify the form library and validation schema.
1. Review existing API payload requirements.
1. Check default values and reset behavior.
1. Trace server error mapping.
1. Identify dependent fields.
1. Preserve existing form behavior.
1. Make the smallest reliable change.
1. Update relevant tests.
1. Verify keyboard and accessibility behavior.

Do not replace a working form architecture for a small UI change.

## 23. Testing

Test realistic form behavior.

### Unit tests

- Validation schemas.
- Input transformations.
- Helper functions.
- Default values.

### Integration tests

- Field interactions.
- Validation messages.
- Submission.
- Server error mapping.
- Reset behavior.
- Conditional fields.
- Dynamic field arrays.

### End-to-end tests

- Successful form submission.
- Invalid input.
- Network failure.
- Multi-step navigation.
- File upload.
- Duplicate submission prevention.
- Keyboard navigation.

Use the existing testing framework.

Prefer testing observable user behavior rather than implementation details.

## 24. Common Anti-Patterns

Avoid:

- Forms without associated labels.
- Client-side-only validation.
- Duplicated validation rules.
- Excessive controlled state.
- Unnecessary form libraries.
- Multiple form libraries without a reason.
- Clearing values after failed submissions.
- Submitting hidden stale values.
- Index keys for dynamic fields.
- Ignoring server validation errors.
- Disabling all form controls without a reason.
- Using color alone to communicate errors.
- Trusting client-side file validation.
- Logging passwords or sensitive form data.

## 25. Decision Workflow

Before implementing a form:

1. Inspect existing form conventions.
1. Understand the backend payload.
1. Identify required fields and constraints.
1. Choose an appropriate form strategy.
1. Define validation rules.
1. Implement accessible fields.
1. Handle submission and server errors.
1. Add loading and success feedback.
1. Verify reset and default-value behavior.
1. Test realistic user workflows.

Prefer simple native solutions when they meet the requirements.

## 26. Review Checklist

### Architecture

- [ ] Existing form conventions are respected.
- [ ] Components have clear responsibilities.
- [ ] Validation is reusable where appropriate.

### Validation

- [ ] Required fields are validated.
- [ ] Client and server validation are handled.
- [ ] Server errors map correctly.
- [ ] Invalid data cannot bypass backend validation.

### UX

- [ ] Loading and submission states work.
- [ ] Duplicate submissions are prevented.
- [ ] User data is preserved after recoverable failures.
- [ ] Reset behavior is correct.

### Accessibility

- [ ] Inputs have labels.
- [ ] Errors are associated with fields.
- [ ] Keyboard navigation works.
- [ ] Focus behavior is appropriate.

### Verification

- [ ] Relevant tests pass.
- [ ] Type checking passes.
- [ ] Build passes.

## 27. Related References

- reusable-ui-components.md
- api-integration.md
- authentication-and-authorization.md
- state-management.md
- typescript-and-code-quality.md
- frontend-security.md
- accessibility-and-wcag.md
- testing-strategy.md

## 28. Official Resources

- MDN Forms: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms
- React Forms: https://react.dev/reference/react-dom/components/form
- React Input: https://react.dev/reference/react-dom/components/input
- React Hook Form: https://react-hook-form.com/
- TanStack Form: https://tanstack.com/form/latest
- Formik: https://formik.org/
- Zod: https://zod.dev/
- Valibot: https://valibot.dev/
- W3C Forms Tutorial: https://www.w3.org/WAI/tutorials/forms/
- OWASP Input Validation Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
