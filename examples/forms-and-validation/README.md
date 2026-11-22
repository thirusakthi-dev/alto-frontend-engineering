# Forms and Validation Example

## 1. Purpose

Demonstrate how to design, implement and maintain forms in React and Next.js applications.

This example covers:

- Native HTML forms.
- Controlled and uncontrolled inputs.
- Form state management.
- Client-side validation.
- Server-side validation.
- Schema-based validation.
- Field-level errors.
- Submission states.
- Dynamic fields.
- Conditional fields.
- Multi-step forms.
- File uploads.
- Accessibility.
- API integration.
- Form testing.

The goal is to create forms that are predictable, accessible, secure and maintainable.

## 2. Core Principles

1. Prefer native HTML form behavior.
1. Choose a form library only when complexity justifies it.
1. Keep validation rules consistent.
1. Validate untrusted input on the server.
1. Provide useful field-level feedback.
1. Prevent accidental duplicate submissions.
1. Preserve user input when appropriate.
1. Make forms keyboard accessible.
1. Handle asynchronous submission failures.
1. Avoid unnecessary form abstractions.

## 3. Suggested Structure

```text id="2tvwxa"
src/
├── features/
│   └── customers/
│       ├── components/
│       │   ├── customer-form.tsx
│       │   └── customer-form-fields.tsx
│       ├── schemas/
│       │   └── customer-schema.ts
│       ├── services/
│       │   └── customer-api.ts
│       └── types/
│           └── customer.ts
├── components/
│   └── ui/
│       ├── input.tsx
│       ├── select.tsx
│       └── form-field.tsx
└── lib/
    └── validations/
```

This structure is illustrative.

Keep form logic near the feature that owns it.

Do not create separate schema, hook and service files for every small form without a real need.

## 4. Choose the Right Form Approach

Different forms need different levels of abstraction.

| Form complexity | Suitable approach |
| --------------- | ----------------------------------------------------- |
| Simple search | Native input and React state |
| Small form | Native form with controlled or uncontrolled fields |
| Medium form | Reusable field components and schema validation |
| Complex form | React Hook Form or another suitable form library |
| Multi-step form | Form library plus explicit step and persistence logic |

Consider the existing project's conventions before introducing a new library.

## 5. Native HTML Form

Start with native form semantics.

```tsx id="r32k7p"
"use client";

import { useState } from "react";

export function ContactForm() {
  const [email, setEmail] = useState("");

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();

    // Submit the validated form data.
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="email">Email address</label>

      <input
        id="email"
        name="email"
        type="email"
        autoComplete="email"
        value={email}
        onChange={(event) => setEmail(event.target.value)}
        required
      />

      <button type="submit">Submit</button>
    </form>
  );
}
```

Use native input attributes where appropriate.

Browser validation can improve user experience, but it does not replace application validation or server-side validation.

## 6. Controlled and Uncontrolled Inputs

### Controlled inputs

React owns the current value.

```tsx id="j59v3j"
const [name, setName] = useState("");

<input
  name="name"
  value={name}
  onChange={(event) => setName(event.target.value)}
/>;
```

Suitable when the application needs to react to input changes.

### Uncontrolled inputs

The browser owns the current value.

```tsx id="7jovjq"
<input name="name" defaultValue="" />
```

Suitable when the form does not need to synchronize every keystroke with React state.

Use `FormData` or a form library to retrieve values when appropriate.

Do not mix `value` and `defaultValue` for the same input.

## 7. Schema Validation

Use schemas when validation rules need to be shared, composed or maintained consistently.

Possible libraries:

- Zod.
- Valibot.
- Yup.
- ArkType.

Choose one based on existing project dependencies and requirements.

Example with Zod:

```ts id="8x69h1"
// src/features/customers/schemas/customer-schema.ts

import { z } from "zod";

export const customerSchema = z.object({
  name: z.string().trim().min(2, "Enter a valid name."),
  email: z.email("Enter a valid email address."),
  phone: z.string().trim().min(7, "Enter a valid phone number."),
});

export type CustomerFormValues = z.infer<typeof customerSchema>;
```

These rules are illustrative.

Real validation must reflect business requirements and backend constraints.

## 8. Validate Form Data

Example:

```ts id="4ex9i2"
const result = customerSchema.safeParse(formValues);

if (!result.success) {
  const errors = result.error.flatten().fieldErrors;

  // Display relevant field errors.
} else {
  // Submit result.data.
}
```

Prefer `safeParse` when invalid user input is an expected outcome.

Do not treat validation failures as unexpected application crashes.

## 9. React Hook Form

For complex forms, React Hook Form can reduce unnecessary form-state boilerplate.

Example installation:

```bash id="5e6gsa"
npm install react-hook-form zod @hookform/resolvers
```

Example:

```tsx id="8jix7s"
"use client";

import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";

import {
  customerSchema,
  type CustomerFormValues,
} from "../schemas/customer-schema";

export function CustomerForm() {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<CustomerFormValues>({
    resolver: zodResolver(customerSchema),
    defaultValues: {
      name: "",
      email: "",
      phone: "",
    },
  });

  async function onSubmit(values: CustomerFormValues) {
    // Call the actual feature service.
    console.log(values);
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)} noValidate>
      <label htmlFor="name">Name</label>
      <input id="name" {...register("name")} />

      {errors.name && <p role="alert">{errors.name.message}</p>}

      <label htmlFor="email">Email</label>
      <input id="email" type="email" {...register("email")} />

      {errors.email && <p role="alert">{errors.email.message}</p>}

      <label htmlFor="phone">Phone</label>
      <input id="phone" {...register("phone")} />

      {errors.phone && <p role="alert">{errors.phone.message}</p>}

      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? "Submitting..." : "Save"}
      </button>
    </form>
  );
}
```

This is an illustrative example.

A production implementation should also handle API failures, server validation errors, accessible error descriptions and successful submission feedback.

Do not add React Hook Form to a simple form that does not need it.

## 10. Field Components

Reusable form fields should support:

- Label.
- Input control.
- Required state.
- Help text.
- Validation message.
- Disabled state.
- Accessible relationships.

Example structure:

```text id="v11zod"
FormField
├── Label
├── Input
├── HelpText
└── ErrorMessage
```

Use unique IDs for every field instance.

Connect descriptions and errors through `aria-describedby` where appropriate.

Do not build an abstraction that prevents consumers from accessing native input attributes.

## 11. Validation Timing

Choose validation timing based on the form.

Possible approaches:

- On submit.
- On blur.
- On change.
- On touched fields.
- After a failed submission.

Avoid showing errors before the user has had a reasonable opportunity to complete a field.

Avoid validating expensive or asynchronous rules on every keystroke without a reason.

## 12. Server-Side Validation

Client-side validation is not a security boundary.

The backend must validate:

- Required fields.
- Data types.
- Length limits.
- Allowed values.
- Business rules.
- Resource permissions.
- File constraints.
- Relationships between fields.

Validate incoming data again on the server.

Do not trust a request because it passed a frontend schema.

## 13. Server Validation Errors

Map backend validation errors to the relevant fields.

Example API error:

```json id="t8kr65"
{
  "message": "Validation failed",
  "errors": {
    "email": ["Email is already registered."]
  }
}
```

Adapt the mapping to the actual backend response contract.

Do not invent an error format that the API does not provide.

Avoid exposing internal database errors to users.

## 14. Submission States

Forms should handle:

- Idle.
- Submitting.
- Success.
- Validation failure.
- Server failure.
- Network failure.

During submission:

- Disable duplicate submission where appropriate.
- Preserve input values.
- Provide useful progress feedback.
- Avoid losing user input after an error.
- Handle retries safely.

Do not show success before the server confirms the operation.

## 15. Reset and Default Values

Understand when to:

- Reset to initial values.
- Preserve values.
- Populate values from an existing record.
- Reset after successful creation.
- Keep dirty values during background updates.

For edit forms, avoid overwriting user changes when refreshed data arrives.

## 16. Dynamic and Conditional Fields

For dynamic forms:

- Use stable field identifiers.
- Validate conditional requirements.
- Preserve values when appropriate.
- Remove obsolete values when business rules require it.
- Avoid unnecessary component remounting.
- Handle array fields predictably.

Do not rely on hidden UI fields as the only enforcement of business rules.

## 17. Multi-Step Forms

For multi-step forms, consider:

- Step navigation.
- Per-step validation.
- Overall validation.
- Progress indication.
- Previous-step values.
- Recovery after refresh.
- Submission behavior.
- Back navigation.

Validate the complete payload on the server.

Do not make the workflow multi-step when a simple form would be clearer.

## 18. File Upload Forms

Consider:

- File size.
- Allowed file types.
- Upload progress.
- Cancellation.
- Server validation.
- Error recovery.
- Multiple file selection.

Do not trust file extensions or browser MIME types as the only security checks.

The backend must validate uploaded content and enforce access permissions.

## 19. Accessibility

Verify:

- Every input has an accessible name.
- Labels are correctly associated.
- Required fields are identified.
- Errors are associated with their fields.
- Keyboard navigation works.
- Focus moves appropriately after failed submission.
- Status updates are announced appropriately.
- Color is not the only error indicator.

Avoid placeholder-only labels.

Use appropriate autocomplete attributes for personal information.

## 20. Security and Data Handling

Consider:

- Server-side validation.
- CSRF protections where applicable.
- Output encoding.
- Sensitive field handling.
- File upload security.
- Rate limiting.
- Safe error messages.
- Avoiding sensitive values in logs.
- Authorization before processing protected operations.

Do not log passwords, authentication tokens or sensitive form payloads.

## 21. Existing Form Changes

When modifying an existing form:

1. Inspect its component and validation schema.
1. Identify all field usages.
1. Review the backend contract.
1. Check default values.
1. Inspect submission and error handling.
1. Review accessibility behavior.
1. Check existing tests.
1. Preserve existing form behavior.
1. Make the smallest reliable change.
1. Verify success and failure paths.

Do not replace the form library or validation system unnecessarily.

## 22. Testing

Test:

### Rendering

- Fields render correctly.
- Defaults are populated.
- Labels and descriptions are associated.

### Validation

- Required fields.
- Invalid formats.
- Minimum and maximum constraints.
- Conditional rules.
- Server validation errors.

### Submission

- Successful submission.
- Failed submission.
- Network failure.
- Duplicate submission prevention.
- Preserved values after failure.

### Accessibility

- Keyboard navigation.
- Accessible names.
- Error announcements.
- Focus management.

## 23. Common Anti-Patterns

Avoid:

- Client-only validation.
- Duplicated validation rules without a clear source of truth.
- Excessive controlled state.
- Unnecessary form libraries.
- Validation on every keystroke without reason.
- Placeholder-only labels.
- Missing field-level error feedback.
- Losing user input after failed submission.
- Ignoring server errors.
- Logging sensitive values.
- Trusting browser file validation.
- Overly complicated multi-step forms.

## 24. Review Checklist

### Architecture

- [ ] Form responsibilities are clear.
- [ ] Existing form conventions are reused.
- [ ] Dependencies are justified.
- [ ] Validation logic is maintainable.

### Validation

- [ ] Client-side validation works.
- [ ] Server-side validation exists.
- [ ] API errors map correctly.
- [ ] Business rules are enforced.

### User Experience

- [ ] Loading and success states work.
- [ ] Error feedback is useful.
- [ ] User input is preserved appropriately.
- [ ] Duplicate submissions are handled.

### Accessibility

- [ ] Labels are associated.
- [ ] Errors are accessible.
- [ ] Keyboard interaction works.
- [ ] Focus behavior is appropriate.

### Verification

- [ ] Form tests pass.
- [ ] TypeScript checks pass.
- [ ] Lint checks pass.
- [ ] Production build succeeds.

## 25. Related References

- `../../references/forms-and-validation.md`
- `../../references/reusable-ui-components.md`
- `../../references/accessibility-and-wcag.md`
- `../../references/api-integration.md`
- `../../references/frontend-security.md`
- `../../references/state-management.md`
- `../../references/testing-strategy.md`
- `../../references/typescript-and-code-quality.md`
- `../../references/anti-ai-slop-and-engineering-quality.md`

## 26. Official Resources

- React Forms: https://react.dev/reference/react-dom/components/form
- React Hook Form: https://react-hook-form.com/
- Zod: https://zod.dev/
- Valibot: https://valibot.dev/
- MDN Forms: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- WAI Forms Tutorial: https://www.w3.org/WAI/tutorials/forms/
