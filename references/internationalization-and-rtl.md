# Internationalization and Right-to-Left (RTL)

## 1. Purpose

Define standards for building frontend applications that support multiple languages, regions and writing directions.

Internationalization (i18n) prepares an application to support different languages and regional conventions.

Localization (l10n) adapts the application for a particular language, region or audience.

This reference covers:

- Internationalization architecture.
- Localization.
- Locale-aware routing.
- Translation management.
- Language switching.
- Date and time formatting.
- Number and currency formatting.
- Pluralization.
- Time zones.
- Right-to-left (RTL) layouts.
- Font support.
- Content expansion.
- Accessibility.
- SEO for multilingual applications.
- Existing project internationalization.

The objective is to make multilingual support reliable without introducing unnecessary complexity.

## 2. Inspect Before Implementation

Before introducing internationalization:

1. Inspect the framework and installed version.
1. Understand the existing routing architecture.
1. Identify supported languages and regions.
1. Inspect existing translation files or libraries.
1. Review application layouts and navigation.
1. Inspect date, number and currency formatting.
1. Identify hardcoded user-facing strings.
1. Review authentication and user preferences.
1. Inspect existing SEO and metadata.
1. Check whether RTL support is required.

For existing projects:

- Preserve current routes where possible.
- Avoid changing URL structures without a migration plan.
- Identify all affected user-facing content.
- Reuse existing localization infrastructure.
- Avoid introducing multiple translation systems.

Do not assume every application requires multilingual support.

## 3. Internationalization Fundamentals

Understand the following concepts.

| Concept | Meaning |
| -------------------- | -------------------------------------------------- |
| Internationalization | Preparing software for different locales |
| Localization | Adapting content for a particular locale |
| Locale | Language and regional conventions |
| Translation | Converting text between languages |
| Formatting | Displaying dates, numbers and currencies correctly |
| RTL | Right-to-left writing direction |
| LTR | Left-to-right writing direction |

Examples of locale identifiers:

- `en-US` — English, United States.
- `en-GB` — English, United Kingdom.
- `ta-IN` — Tamil, India.
- `hi-IN` — Hindi, India.
- `ar-SA` — Arabic, Saudi Arabia.
- `fr-FR` — French, France.

A language and a locale are not always interchangeable.

For example, English can have different regional formatting conventions.

## 4. Locale Architecture

Define supported locales centrally.

Example:

```ts
export const locales = ["en", "ta", "hi"] as const;

export type Locale = (typeof locales)[number];

export const defaultLocale: Locale = "en";
```

For applications that need regional variants, use complete locale identifiers such as `en-US` and `en-GB`.

Avoid duplicating locale definitions across unrelated files.

A centralized configuration can contain:

- Supported locales.
- Default locale.
- Locale labels.
- Text direction.
- Fallback behavior.
- Route configuration.

Example:

```ts
export const localeConfig = {
  en: {
    label: "English",
    direction: "ltr",
  },
  ta: {
    label: "தமிழ்",
    direction: "ltr",
  },
  ar: {
    label: "العربية",
    direction: "rtl",
  },
} as const;
```

Keep configuration types consistent with the actual supported locales.

## 5. Translation Architecture

Keep translations organized and maintainable.

Example structure:

```text
src/
├── i18n/
│   ├── config.ts
│   ├── routing.ts
│   ├── request.ts
│   └── dictionaries/
│       ├── en.json
│       ├── ta.json
│       └── hi.json
```

The exact structure depends on the framework and translation library.

### Translation Guidelines

- Use meaningful translation keys.
- Keep translations organized by feature or namespace.
- Avoid duplicating common strings.
- Keep placeholders consistent.
- Avoid constructing sentences by concatenating translated fragments.
- Support pluralization.
- Provide a clear fallback strategy.
- Avoid exposing missing translation keys to users.
- Keep translations synchronized across locales.

Example:

```json
{
  "common": {
    "save": "Save",
    "cancel": "Cancel"
  },
  "dashboard": {
    "welcome": "Welcome, {name}"
  }
}
```

Usage depends on the selected translation library.

Do not assume every library uses the same placeholder syntax.

### Translation Keys

Prefer:

```text
dashboard.welcome
profile.update_success
auth.invalid_credentials
```

Avoid:

```text
text1
message2
label3
```

Translation keys should describe their meaning.

## 6. Translation Libraries

Choose a library based on framework compatibility and application requirements.

Possible options:

| Library | Typical use |
| --------------------- | ----------------------------------------------- |
| next-intl | Next.js applications |
| i18next | General JavaScript and React applications |
| react-i18next | React integration for i18next |
| FormatJS / React Intl | ICU message formatting and internationalization |
| Paraglide JS | Type-safe, compile-time-oriented localization |

Before selecting a library:

1. Check framework compatibility.
1. Check the installed framework version.
1. Review server and client support.
1. Review message formatting.
1. Review pluralization.
1. Review loading and fallback behavior.
1. Check maintenance and documentation.
1. Compare bundle and runtime costs.

Do not install multiple translation libraries without a justified requirement.

See `package-selection-and-ecosystem.md`.

## 7. Locale-Aware Routing

Multilingual applications may use locale-based URL structures.

Examples:

```text
/en/products
/ta/products
/hi/products
```

Another approach uses domain-based localization:

```text
example.com
example.fr
example.de
```

Choose a routing strategy based on:

- SEO requirements.
- Supported locales.
- Domain architecture.
- Existing route structure.
- User expectations.
- Hosting configuration.

### Routing Guidelines

- Keep locale detection predictable.
- Preserve the current page when changing languages where possible.
- Handle unsupported locales.
- Avoid redirect loops.
- Provide a valid default locale.
- Keep query parameters where appropriate.
- Handle localized and unavailable routes explicitly.

Do not assume browser language always determines the user's preferred application language.

Allow users to change their language preference.

## 8. Next.js Internationalization

For Next.js App Router applications, locale-based route segments are one available approach.

Example:

```text
app/
└── [locale]/
    ├── layout.tsx
    ├── page.tsx
    ├── products/
    │   └── page.tsx
    └── about/
        └── page.tsx
```

The locale segment can be used to load the appropriate dictionary and metadata.

Example:

```tsx
type Props = {
  params: Promise<{
    locale: string;
  }>;
};

export default async function Page({ params }: Props) {
  const { locale } = await params;

  return (
    <main>
      <h1>Localized content</h1>
    </main>
  );
}
```

This is an illustrative App Router pattern. Check the installed Next.js version and its current route parameter conventions.

### Locale Layout

The root localized layout should establish the appropriate document language and writing direction.

Example:

```tsx
<html lang={locale} dir={direction}>
  <body>{children}</body>
</html>
```

Ensure the document structure is valid for the application's root layout architecture.

### Middleware and Proxy

Locale detection and redirects may be implemented through framework-supported request interception.

The correct file and API depend on the installed Next.js version.

Do not copy older middleware examples into newer projects without checking the current documentation.

## 9. Language Switching

A language selector should be understandable and accessible.

Consider:

- Displaying the language's native name.
- Preserving the current route when possible.
- Preserving relevant query parameters.
- Handling unavailable translations.
- Updating the document language.
- Updating text direction.
- Persisting the user's preference when appropriate.

Example labels:

```text
English
தமிழ்
हिन्दी
العربية
```

Avoid flags as the only language identifier.

A flag represents a country, not necessarily a language.

### Preference Strategy

A possible preference order:

1. Explicit user preference.
1. Persisted application preference.
1. Locale from the current URL.
1. Browser language preference.
1. Application default.

The correct precedence depends on the application's routing and product requirements.

Avoid unexpectedly overriding an explicit user selection.

## 10. Date and Time Formatting

Never assume a single date format is appropriate for every locale.

Examples:

```ts
const date = new Date();

const usDate = new Intl.DateTimeFormat("en-US").format(date);

const ukDate = new Intl.DateTimeFormat("en-GB").format(date);

const indianDate = new Intl.DateTimeFormat("en-IN").format(date);
```

Use `Intl.DateTimeFormat` for locale-aware formatting.

Consider:

- Date ordering.
- Month names.
- Calendar conventions.
- Time zones.
- 12-hour and 24-hour clocks.
- Relative time.
- Daylight saving time.

### Time Zone Handling

Do not confuse locale with time zone.

For example, `en-IN` does not automatically establish the correct time zone for every user.

Use explicit time zone information when required.

Example:

```ts
const formatter = new Intl.DateTimeFormat("en-IN", {
  dateStyle: "medium",
  timeStyle: "short",
  timeZone: "Asia/Kolkata",
});
```

Store timestamps using an appropriate consistent representation, commonly UTC, and format them for the user's intended time zone.

Do not parse ambiguous date strings without understanding their format.

## 11. Number and Currency Formatting

Use `Intl.NumberFormat` instead of manually inserting separators or currency symbols.

Example:

```ts
const amount = 125000;

const indianFormat = new Intl.NumberFormat("en-IN").format(amount);

const usd = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
}).format(amount);

const inr = new Intl.NumberFormat("en-IN", {
  style: "currency",
  currency: "INR",
}).format(amount);
```

Consider:

- Decimal separators.
- Grouping separators.
- Currency symbols.
- Currency codes.
- Fraction digits.
- Percentage formatting.
- Measurement units.

Do not assume a currency symbol uniquely identifies a currency.

Use explicit currency codes for financial values.

## 12. Pluralization and Message Formatting

Languages have different pluralization rules.

Avoid manually appending `s` to translated words.

Use the translation library's pluralization support or ICU message syntax where appropriate.

Example:

```text
{count, plural,
  =0 {No notifications}
  one {# notification}
  other {# notifications}
}
```

Support:

- Singular.
- Plural.
- Zero.
- Context-dependent messages.
- Variable interpolation.
- Gender or grammatical variations where required by the language.

Do not build complex translated sentences through string concatenation.

## 13. Right-to-Left Layouts

RTL languages include Arabic, Hebrew, Persian and Urdu.

A multilingual application may need to support both LTR and RTL layouts.

Set document direction correctly.

Example:

```html
<html lang="ar" dir="rtl"></html>
```

Do not implement RTL by reversing every CSS property manually.

### Logical CSS Properties

Prefer logical properties.

| Physical property | Logical alternative |
| ----------------- | -------------------- |
| margin-left | margin-inline-start |
| margin-right | margin-inline-end |
| padding-left | padding-inline-start |
| padding-right | padding-inline-end |
| left | inset-inline-start |
| right | inset-inline-end |
| text-align: left | text-align: start |
| text-align: right | text-align: end |

Example:

```css
.card {
  padding-inline: 1rem;
  margin-inline-start: 0.5rem;
  text-align: start;
}
```

Logical properties adapt to writing direction.

### Direction-Aware Styling

Use direction-aware selectors where required.

Example:

```css
[dir="rtl"] .icon {
  transform: scaleX(-1);
}
```

Only mirror icons when their meaning requires it.

Examples of potentially directional icons:

- Back and forward arrows.
- Previous and next navigation.
- Directional navigation indicators.

Do not mirror every icon.

### Mixed-Direction Content

Some content may contain both RTL and LTR text.

Examples:

- Email addresses.
- URLs.
- Phone numbers.
- Product identifiers.
- English technical terms.

Use appropriate isolation techniques when required.

HTML:

```html
<bdi>user@example.com</bdi>
```

CSS:

```css
.identifier {
  direction: ltr;
  unicode-bidi: isolate;
}
```

Avoid forcing the entire application into one direction when individual content requires isolation.

## 14. RTL Component Compatibility

Review the entire component system.

Check:

- Sidebars.
- Navigation.
- Dropdown menus.
- Dialogs.
- Drawers.
- Tooltips.
- Form fields.
- Breadcrumbs.
- Tables.
- Pagination.
- Icons.
- Animations.
- Charts.
- Date pickers.

Avoid hardcoded left/right positioning where logical alternatives work.

Test both directions rather than assuming the layout is correct.

Some third-party libraries may not support RTL fully. Verify compatibility before adopting them.

## 15. Typography and Fonts

Different scripts require different font coverage.

Review:

- Character coverage.
- Font family availability.
- Font weight support.
- Line height.
- Glyph rendering.
- Fallback behavior.
- Font loading.
- Text wrapping.

Do not assume one font supports every required language.

Choose fonts based on the actual supported scripts.

Check whether line height and spacing need adjustment for specific writing systems.

Avoid loading multiple large font families unnecessarily.

## 16. Content Expansion and Layout

Translated content may be longer or shorter than the source language.

Design layouts that tolerate content expansion.

Consider:

- Buttons.
- Navigation labels.
- Headings.
- Cards.
- Tables.
- Dialogs.
- Form validation messages.
- Mobile layouts.

Avoid fixed widths for text-heavy controls.

Allow text wrapping where appropriate.

Do not truncate important translated content without a suitable accessible alternative.

Test long strings and longer translations.

## 17. Accessibility

Internationalization must preserve accessibility.

Guidelines:

- Set the correct document `lang`.
- Set the correct document `dir`.
- Use meaningful translated accessible names.
- Keep keyboard navigation functional.
- Ensure screen readers announce localized content correctly.
- Provide language names that users can recognize.
- Avoid communicating meaning through flags alone.
- Ensure RTL reading order remains logical.
- Support text resizing and zoom.
- Check translated form labels and validation messages.

For embedded content in another language, use the appropriate language attribute where practical.

See `accessibility-and-wcag.md`.

## 18. SEO for Multilingual Applications

Search engines need clear language and regional signals.

Consider:

- Locale-specific URLs.
- Localized metadata.
- Canonical URLs.
- `hreflang`.
- Localized sitemaps.
- Internal links.
- Language-specific structured data where applicable.

Example:

```html
<link rel="alternate" hreflang="en" href="https://example.com/en/products" />

<link rel="alternate" hreflang="ta" href="https://example.com/ta/products" />
```

Include valid reciprocal language alternatives where required.

Do not use `hreflang` as a substitute for proper localized page content.

Avoid indexing multiple duplicate versions without an intentional SEO strategy.

See `seo-and-discoverability.md`.

## 19. Translation Loading and Performance

Translation resources should not unnecessarily increase initial application cost.

Consider:

- Route-level translation loading.
- Feature-based namespaces.
- Server-side loading.
- Dynamic resource loading.
- Translation bundle size.
- Caching.
- Fallback behavior.

Avoid downloading every language dictionary for every user.

Load only the resources required by the current locale and feature where supported.

Do not introduce complicated lazy-loading architecture for a very small translation set without a measurable reason.

## 20. Translation Management

For larger applications, consider a translation management workflow.

Possible tools:

- Crowdin.
- Lokalise.
- Phrase.
- POEditor.

Evaluate:

- Translation collaboration.
- Review workflows.
- Version control integration.
- Missing translation detection.
- Machine translation support.
- Cost.
- Export formats.

Machine translation should not automatically be treated as final approved content.

For important user-facing content, use an appropriate review process.

## 21. Existing Project Internationalization

When adding internationalization to an existing project:

1. Inspect the current route architecture.
1. Identify all user-facing text.
1. Determine supported locales.
1. Select a compatible translation approach.
1. Define locale configuration.
1. Establish translation key conventions.
1. Introduce locale-aware formatting.
1. Add language switching.
1. Handle document language and direction.
1. Update relevant metadata and SEO.
1. Test every supported locale.
1. Check layouts with long translated content.
1. Verify existing routes and deep links.
1. Check authentication and redirects.
1. Run relevant tests and production build.

Implement incrementally.

Avoid translating every internal identifier, API field or database value.

Do not change backend data contracts unnecessarily to introduce frontend translations.

Preserve existing user preferences and URL behavior unless a deliberate migration is required.

## 22. Common Anti-Patterns

Avoid:

- Hardcoded user-facing strings throughout components.
- Treating language and locale as identical.
- Assuming browser language is the user's final preference.
- Using flags as the only language selector.
- Concatenating translated sentence fragments.
- Manually formatting dates and currencies.
- Assuming locale determines time zone.
- Using physical CSS properties everywhere.
- Reversing the entire layout for RTL without review.
- Mirroring all icons.
- Loading all dictionaries on every route.
- Ignoring longer translated text.
- Forgetting document language attributes.
- Translating internal API identifiers unnecessarily.
- Adding a translation library without inspecting existing infrastructure.
- Claiming complete language support without testing the actual content.

## 23. Implementation Workflow

1. Understand localization requirements.
1. Inspect the existing application.
1. Identify required locales and writing directions.
1. Select an appropriate architecture.
1. Define locale configuration.
1. Establish translation conventions.
1. Implement locale-aware routing.
1. Add translation loading.
1. Add language switching.
1. Implement locale-aware formatting.
1. Add RTL support where required.
1. Update SEO and accessibility.
1. Test all supported locales.
1. Verify performance and regressions.

Keep the implementation proportional to actual product requirements.

## 24. Review Checklist

### Architecture

- [ ] Supported locales are defined centrally.
- [ ] Default locale is clear.
- [ ] Translation architecture is consistent.
- [ ] Existing routing conventions are preserved.
- [ ] Fallback behavior is defined.

### Translation

- [ ] User-facing strings use translations.
- [ ] Translation keys are meaningful.
- [ ] Pluralization is handled correctly.
- [ ] Variables and placeholders are consistent.
- [ ] Missing translations are handled.

### Formatting

- [ ] Dates are locale-aware.
- [ ] Time zones are handled explicitly.
- [ ] Numbers are formatted correctly.
- [ ] Currency uses explicit codes.
- [ ] Relative time is localized where required.

### RTL

- [ ] Document direction is correct.
- [ ] Logical CSS properties are preferred.
- [ ] Components work in both directions.
- [ ] Icons are mirrored only when appropriate.
- [ ] Mixed-direction content is handled.

### Accessibility and SEO

- [ ] Document language is correct.
- [ ] Accessible names are translated.
- [ ] Keyboard interaction works.
- [ ] Localized metadata is present.
- [ ] Language alternatives are configured where needed.

### Verification

- [ ] Every supported locale is tested.
- [ ] Long translated strings are tested.
- [ ] Mobile layouts are checked.
- [ ] Existing routes continue to work.
- [ ] Tests and builds are executed.
- [ ] Unverified behavior is reported honestly.

## 25. Related References

- anti-ai-slop-and-engineering-quality.md
- architecture-and-project-structure.md
- nextjs-engineering.md
- global-styles-and-design-tokens.md
- theming-and-dark-mode.md
- reusable-ui-components.md
- layouts-and-navigation.md
- accessibility-and-wcag.md
- seo-and-discoverability.md
- performance-and-core-web-vitals.md
- testing-strategy.md
- package-selection-and-ecosystem.md

## 26. Official Resources

### Internationalization

- MDN Internationalization: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Internationalization
- ECMA-402: https://tc39.es/ecma402/
- Unicode CLDR: https://cldr.unicode.org/

### Next.js

- Next.js Internationalization: https://nextjs.org/docs/app/guides/internationalization

### Translation Libraries

- next-intl: https://next-intl.dev/
- i18next: https://www.i18next.com/
- FormatJS: https://formatjs.io/
- Paraglide JS: https://inlang.com/m/gerre34r/library-inlang-paraglideJs

### RTL and Accessibility

- W3C Internationalization: https://www.w3.org/International/
- W3C Directionality: https://www.w3.org/International/questions/qa-html-dir
- W3C Language Tags: https://www.w3.org/International/articles/language-tags/

Always verify current library APIs, framework conventions and browser support before implementation.
