# SEO and Discoverability

## 1. Purpose

Define standards for making frontend applications discoverable, crawlable, understandable and shareable across search engines and other content discovery systems.

The agent must understand how frontend architecture affects SEO and implement appropriate technical and content-level improvements.

This reference covers:

- Technical SEO.
- Search engine crawling and indexing.
- Rendering strategies.
- Metadata.
- Page titles and descriptions.
- Canonical URLs.
- Robots directives.
- Sitemap generation.
- Structured data.
- Open Graph and social previews.
- Semantic HTML.
- Internal linking.
- URL architecture.
- Image SEO.
- International SEO.
- Performance and Core Web Vitals.
- Search engine verification.
- AI search and answer engine discoverability.

SEO must reflect actual page content and application behavior.

Adding metadata alone does not make an application search-engine optimized.

## 2. Inspect Before Making SEO Changes

Before implementing SEO in an existing project:

1. Inspect the framework and version.
1. Understand the routing architecture.
1. Identify public and private routes.
1. Review existing metadata.
1. Inspect canonical URL behavior.
1. Check sitemap and robots configuration.
1. Review rendering strategies.
1. Inspect existing structured data.
1. Identify duplicate or parameterized routes.
1. Review image and font optimization.
1. Check existing SEO packages.
1. Review deployment domain and HTTPS configuration.

For existing applications:

- Preserve correct existing metadata.
- Avoid generating duplicate metadata.
- Reuse existing SEO utilities.
- Respect the current routing architecture.
- Avoid changing URLs without a migration plan.
- Identify pages that should not be indexed.

Do not assume every route should appear in search results.

## 3. SEO Fundamentals

Understand the difference between these concepts.

| Concept | Meaning |
| --------------- | -------------------------------------------------- |
| Crawling | Search engines discover and request URLs |
| Rendering | Search engines process page content and resources |
| Indexing | Search engines consider a page for their index |
| Ranking | Search engines determine where a result may appear |
| Discoverability | Users and systems can find and understand content |

A page being crawlable does not guarantee indexing.

A page being indexed does not guarantee ranking.

The agent must never promise specific ranking positions or indexing outcomes.

## 4. Search-Friendly Rendering

Search engines must be able to access meaningful page content.

Consider the rendering architecture.

### Server-Side Rendering (SSR)

HTML is generated on the server for each request or according to the framework's rendering strategy.

Useful for:

- Dynamic content.
- Frequently changing information.
- Public pages that need accessible initial HTML.

### Static Site Generation (SSG)

HTML is generated during the build process.

Useful for:

- Marketing pages.
- Documentation.
- Blog content.
- Public pages with relatively stable content.

### Incremental Static Regeneration (ISR)

Supports updating generated pages without rebuilding the entire application, depending on framework capabilities and configuration.

Useful for:

- Product catalogs.
- Public content.
- Frequently updated pages.

### Client-Side Rendering (CSR)

Content is rendered primarily in the browser.

It can be appropriate for:

- Internal dashboards.
- Authenticated applications.
- Highly interactive tools.

For important public content, do not rely blindly on client-side JavaScript execution.

Verify that meaningful content is available to crawlers and users.

### Rendering Decision

Choose based on:

- Content freshness.
- User interaction.
- Personalization.
- Caching requirements.
- SEO requirements.
- Backend availability.
- Framework capabilities.

Do not introduce SSR solely for SEO when the current architecture already provides adequate crawlable content.

## 5. URL Architecture

URLs should be understandable, stable and consistent.

Prefer:

```text
/products
/products/wireless-headphones
/blog
/blog/frontend-performance
/about
/contact
```

Avoid unnecessary complexity:

```text
/page?id=123&ref=abc
```

Query parameters are valid when required, such as for search, filters and pagination.

Guidelines:

- Use meaningful path segments.
- Keep URLs reasonably short.
- Use lowercase paths where appropriate.
- Use consistent trailing slash behavior.
- Avoid unnecessary URL parameters.
- Avoid duplicate routes for identical content.
- Use permanent redirects when URLs change.
- Preserve existing URL contracts unless a migration is required.

Do not change public URLs without considering existing links and search indexing.

## 6. Page Titles

Every important public page should have a meaningful title.

Guidelines:

- Make titles unique where practical.
- Describe the actual page content.
- Put the most important topic early.
- Include the brand where appropriate.
- Avoid keyword stuffing.
- Avoid repeating generic titles across all routes.

Example:

```text
Frontend Performance Guide | Brand Name
```

Avoid:

```text
Home | Home | Best Website | Best Website
```

Use page-specific metadata rather than one global title for every route.

## 7. Meta Descriptions

Write meaningful descriptions for important public pages.

Guidelines:

- Summarize the page accurately.
- Explain its value.
- Use natural language.
- Avoid keyword stuffing.
- Avoid duplicate descriptions where practical.
- Avoid misleading claims.

Example:

```html
<meta
  name="description"
  content="Learn practical techniques for improving React rendering, reducing bundle size and optimizing frontend performance."
/>
```

Search engines may generate their own snippets instead of using the provided description.

Do not promise that a particular description will appear in search results.

## 8. Metadata Architecture

Centralize shared metadata while allowing individual routes to define their own values.

Possible shared configuration:

```ts
export const siteConfig = {
  name: "Example",
  description: "Example application description",
  url: "https://example.com",
  defaultImage: "/images/social-preview.png",
};
```

Guidelines:

- Use the actual production domain.
- Avoid placeholder URLs in production.
- Provide sensible defaults.
- Support page-specific titles and descriptions.
- Keep social metadata consistent.
- Avoid duplicated metadata definitions.
- Ensure metadata is generated from the correct route data.

Do not invent a production domain or social image path.

## 9. Canonical URLs

Canonical URLs indicate the preferred URL for duplicate or substantially similar content.

Example:

```html
<link rel="canonical" href="https://example.com/products/headphones" />
```

Use canonical URLs when appropriate for:

- Query parameter variations.
- Duplicate URL paths.
- Tracking parameters.
- Content accessible through multiple URLs.

Guidelines:

- Use absolute canonical URLs.
- Ensure canonical destinations are valid.
- Avoid canonical chains.
- Avoid canonicalizing unrelated pages to one URL.
- Keep canonical behavior consistent with redirects and internal links.
- Use self-referencing canonicals when appropriate.

Canonical tags are hints to search engines, not guaranteed directives.

Do not use canonical URLs as a substitute for access control or security.

## 10. Robots Directives

Understand the difference between robots.txt and page-level indexing directives.

### robots.txt

Controls crawler access to URL paths.

Example:

```text
User-agent: *
Allow: /

Sitemap: https://example.com/sitemap.xml
```

### Meta Robots

Controls indexing and link-following behavior when crawlers can access the page.

Example:

```html
<meta name="robots" content="noindex, follow" />
```

### X-Robots-Tag

An HTTP response header that can apply indexing directives to HTML and non-HTML resources.

Important:

- Do not accidentally block important public pages.
- Do not block resources required for rendering without a reason.
- Use `noindex` for pages that should not appear in search results.
- Understand that crawlers generally need to access a page to read its `noindex` directive.
- Avoid exposing private information through public pages.
- Do not treat robots.txt as an access-control mechanism.

Authenticated and sensitive pages must be protected by authentication and authorization.

## 11. Sitemap Generation

A sitemap helps search engines discover important URLs.

Include appropriate public, canonical URLs.

Consider:

- Important public pages.
- Product pages.
- Blog articles.
- Documentation pages.
- Relevant category pages.
- Last modification dates when accurate.

Exclude:

- Authenticated dashboards.
- Internal application pages.
- Private user pages.
- Duplicate URLs.
- Redirected URLs.
- Noindex pages.
- Temporary or irrelevant routes.

Example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset
  xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
>
  <url>
    <loc>https://example.com/</loc>
  </url>
  <url>
    <loc>https://example.com/about</loc>
  </url>
</urlset>
```

Guidelines:

- Use absolute URLs.
- Keep the sitemap synchronized with actual routes.
- Generate dynamic entries from the content source.
- Avoid manually maintaining large dynamic sitemaps.
- Split large sitemaps where necessary.
- Use a sitemap index when appropriate.
- Keep the sitemap valid XML.

A sitemap helps discovery but does not guarantee indexing.

## 12. robots.txt and Sitemap Configuration

Provide robots.txt through the framework's supported mechanism.

For Next.js App Router, supported metadata routes include:

- `app/robots.ts` or `app/robots.txt`.
- `app/sitemap.ts` or `app/sitemap.xml`.

For other frameworks, use their existing routing or static asset conventions.

Do not create multiple conflicting robots or sitemap implementations.

Verify the generated production URLs.

## 13. Structured Data

Structured data helps search engines understand entities and page content.

JSON-LD is a commonly used format.

Possible schema types:

- Organization.
- WebSite.
- Article.
- BlogPosting.
- Product.
- BreadcrumbList.
- LocalBusiness.
- Event.
- SoftwareApplication.
- FAQPage, where applicable and eligible.

Example:

```html
<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Example",
    "url": "https://example.com"
  }
</script>
```

Guidelines:

- Use schema types that accurately describe the content.
- Match structured data with visible page content.
- Include required properties for the selected type.
- Validate generated JSON-LD.
- Avoid duplicate conflicting schema.
- Do not fabricate ratings, reviews or business information.
- Do not add irrelevant schema solely to obtain rich results.
- Keep structured data synchronized with actual content.

Structured data does not guarantee rich search results.

Google may support only specific structured data types and eligibility rules.

Check current search engine documentation before implementing advanced schema.

## 14. Breadcrumbs and Internal Linking

Internal links help users and crawlers discover related content.

Use:

- Descriptive anchor text.
- Logical navigation.
- Breadcrumbs where appropriate.
- Related content links.
- Category and topic relationships.
- Contextual links within content.

Avoid:

- Excessive internal links.
- Generic repeated anchor text.
- Broken links.
- Orphaned important pages.
- Unnecessary nested navigation.
- JavaScript-only navigation without accessible link semantics.

Use real anchor elements for navigation.

For breadcrumb navigation:

- Represent the page hierarchy accurately.
- Use accessible markup.
- Consider matching BreadcrumbList structured data.

## 15. Semantic HTML

Use semantic HTML to communicate document structure.

Prefer:

- `header`.
- `nav`.
- `main`.
- `article`.
- `section`.
- `aside`.
- `footer`.
- Proper heading levels.
- Lists for list content.
- Buttons for actions.
- Anchors for navigation.

Guidelines:

- Use one clear primary page heading where appropriate.
- Maintain logical heading hierarchy.
- Avoid choosing elements solely for their default visual appearance.
- Use accessible labels for controls.
- Keep meaningful content available in the document.

Semantic HTML supports accessibility and helps systems understand content.

See `accessibility-and-wcag.md`.

## 16. Open Graph and Social Sharing

Provide social metadata for public pages where sharing matters.

Common Open Graph properties:

- `og:title`.
- `og:description`.
- `og:image`.
- `og:url`.
- `og:type`.
- `og:site_name`.

Example:

```html
<meta property="og:title" content="Frontend Engineering Guide" />
<meta
  property="og:description"
  content="Practical frontend engineering guidance."
/>
<meta property="og:image" content="https://example.com/social-preview.png" />
<meta property="og:type" content="website" />
```

Consider social platform-specific metadata such as X card metadata where supported.

Guidelines:

- Use absolute image URLs.
- Provide appropriate image dimensions.
- Use meaningful preview images.
- Avoid broken or inaccessible image paths.
- Keep social descriptions consistent with actual content.
- Generate page-specific previews where useful.

Test previews with the relevant platform tools.

## 17. Image SEO

Images should be accessible, performant and understandable.

Guidelines:

- Use descriptive filenames where practical.
- Provide appropriate alternative text.
- Use empty alt text for purely decorative images.
- Optimize image dimensions and formats.
- Avoid unnecessarily large image files.
- Use responsive images where appropriate.
- Provide explicit width and height where practical.
- Use lazy loading for suitable below-the-fold images.
- Do not lazy-load critical above-the-fold images blindly.

Alternative text should describe the image's purpose in context.

Avoid keyword stuffing in alt attributes.

Do not use image filenames or alt text as substitutes for meaningful page content.

## 18. Pagination and Filtering

Search, category and filtering systems can create large numbers of URL variations.

Consider:

- Query parameter consistency.
- Duplicate content.
- Canonical behavior.
- Crawlable pagination links.
- Empty filter results.
- Sort parameters.
- Search result pages.
- Faceted navigation.

Guidelines:

- Use stable URLs for meaningful content states.
- Avoid generating unlimited crawlable URL combinations.
- Avoid blocking important content accidentally.
- Do not canonicalize distinct content to unrelated pages.
- Use clear navigation between pages.
- Preserve useful query state where appropriate.

Follow current search engine guidance for pagination and faceted navigation.

Do not rely on outdated pagination-specific indexing assumptions.

## 19. International SEO

For multilingual applications, implement language and regional targeting carefully.

Consider:

- Localized URLs.
- Language metadata.
- `hreflang`.
- Canonical relationships.
- Language-specific sitemaps.
- Translated metadata.
- Correct language content.
- Locale-aware navigation.

Example:

```html
<link rel="alternate" hreflang="en" href="https://example.com/en" />

<link rel="alternate" hreflang="ta" href="https://example.com/ta" />
```

Guidelines:

- Use valid language and region codes.
- Ensure alternate pages actually exist.
- Maintain reciprocal alternate relationships.
- Avoid pointing every locale to one generic page.
- Do not automatically redirect all visitors based only on browser language.
- Provide a user-controlled language option where appropriate.

See `internationalization-and-rtl.md`.

## 20. SEO for Next.js

Use the official Metadata API for App Router projects.

Common capabilities include:

- `metadata`.
- `generateMetadata`.
- `generateStaticParams`.
- Metadata file conventions.
- `sitemap.ts`.
- `robots.ts`.
- `opengraph-image`.
- `twitter-image`.

### Static Metadata

Example:

```tsx
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "About | Example",
  description: "Learn about Example.",
};
```

### Dynamic Metadata

Use `generateMetadata` when page metadata depends on route parameters or fetched content.

Example:

```tsx
import type { Metadata } from "next";

type Props = {
  params: Promise<{
    slug: string;
  }>;
};

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params;

  return {
    title: `${slug} | Example`,
    description: `Learn more about ${slug}.`,
  };
}
```

This is an illustrative pattern.

Use the installed Next.js version's actual route and parameter types.

### Guidelines

- Define shared metadata in the appropriate root layout.
- Override metadata at the page or nested layout level.
- Avoid duplicating inherited metadata unnecessarily.
- Generate dynamic metadata from actual content.
- Use absolute metadata base URLs in production.
- Handle missing content and invalid slugs.
- Avoid unnecessary duplicate data fetching.
- Keep metadata consistent with canonical URLs.

Do not place private information into public metadata.

## 21. SEO for React Applications

For React applications without built-in metadata support:

- Use the router's established metadata approach.
- Use a suitable document head library if needed.
- Avoid adding multiple competing head-management libraries.
- Ensure route changes update metadata.
- Ensure public content is accessible to crawlers.
- Consider prerendering or SSR when justified.

For client-rendered applications, inspect actual crawler behavior rather than assuming JavaScript rendering always works perfectly.

Verify:

- Page title.
- Description.
- Canonical URL.
- Open Graph metadata.
- Rendered content.
- Internal links.

## 22. Performance and SEO

Performance contributes to user experience and can affect search visibility.

Consider:

- Largest Contentful Paint (LCP).
- Interaction to Next Paint (INP).
- Cumulative Layout Shift (CLS).
- Image loading.
- Font loading.
- JavaScript size.
- Server response time.
- Caching.
- Rendering strategy.

Do not optimize only for a Lighthouse score.

Measure real user experience where possible.

See `performance-and-core-web-vitals.md`.

## 23. AI Search and Answer Engine Discoverability

Modern content discovery includes search engines, AI-powered search experiences and answer engines.

Focus on making content understandable, accurate and useful.

Guidelines:

- Use clear page titles.
- Explain important topics directly.
- Organize content with meaningful headings.
- Provide accurate definitions.
- Use descriptive internal links.
- Identify authors and organizations where relevant.
- Keep important facts consistent.
- Use structured data where appropriate.
- Cite trustworthy sources in editorial content.
- Keep documentation and product information current.
- Avoid misleading or mass-generated low-value content.

Do not:

- Invent special AI crawler tags.
- Promise inclusion in AI-generated answers.
- Add schema that does not represent the content.
- Create large amounts of repetitive pages for search traffic.
- Assume a special file or markup guarantees AI citations.

AI search systems differ in how they discover, retrieve and cite content.

Verify platform-specific requirements against official documentation.

## 24. SEO for Authenticated Applications

Not every application page should be indexed.

Typical public pages:

- Landing pages.
- Product information.
- Documentation.
- Public articles.
- Public company information.

Typical private pages:

- Dashboards.
- User profiles containing private data.
- Internal reports.
- Account settings.
- Administrative pages.
- Private CRM records.

Guidelines:

- Protect private pages through authentication and authorization.
- Do not expose private data through metadata.
- Do not expose private data in sitemaps.
- Use appropriate noindex behavior for pages that should not appear in search.
- Avoid leaking sensitive information through server-rendered HTML.

Remember: `noindex` is not a security mechanism.

## 25. Search Engine Verification

After implementation, verify the actual production output.

Check:

- Page title.
- Meta description.
- Canonical URL.
- Robots directives.
- Sitemap.
- robots.txt.
- Structured data.
- Open Graph metadata.
- Social preview images.
- HTTP response status.
- Rendered HTML.
- Internal links.
- Redirect behavior.

Useful tools:

- Google Search Console.
- Google Rich Results Test.
- Schema.org Validator.
- Lighthouse.
- PageSpeed Insights.
- Bing Webmaster Tools.
- Browser developer tools.

Do not claim indexing has occurred simply because metadata exists.

Search engine indexing is controlled by the search engine.

## 26. Existing Project SEO Improvements

When improving an existing project:

1. Inspect route structure.
1. Identify important public pages.
1. Audit current metadata.
1. Check rendering behavior.
1. Identify duplicate URLs.
1. Inspect canonical configuration.
1. Review sitemap and robots output.
1. Check structured data.
1. Review image and social metadata.
1. Fix the most important issues first.
1. Test generated output.
1. Verify production behavior.

Avoid changing every route when only a few pages have problems.

Do not change existing URL structures without considering redirects and external links.

## 27. Common SEO Anti-Patterns

Avoid:

- Duplicate page titles.
- Generic descriptions across all routes.
- Missing canonical URLs where needed.
- Invalid structured data.
- Fabricated reviews or ratings.
- Keyword stuffing.
- Hidden keyword content.
- Broken internal links.
- Unnecessary URL parameters.
- Indexing private dashboards.
- Exposing sensitive metadata.
- Blocking important resources accidentally.
- Empty public pages that rely entirely on client-side data loading.
- Huge unoptimized images.
- Incorrect hreflang relationships.
- Misleading social previews.
- Assuming a sitemap guarantees indexing.
- Promising specific search rankings.

## 28. SEO Decision Workflow

Before implementing SEO:

1. Identify the page's purpose.
1. Determine whether it should be public and indexable.
1. Understand the rendering architecture.
1. Identify the correct URL.
1. Define page-specific metadata.
1. Set canonical behavior where appropriate.
1. Add sitemap and robots configuration.
1. Add structured data only when applicable.
1. Improve semantic content and internal links.
1. Optimize relevant images and performance.
1. Verify generated output.
1. Report limitations honestly.

Prioritize actual user value and correct technical behavior over SEO tricks.

## 29. Review Checklist

### Technical SEO

- [ ] Important pages are crawlable.
- [ ] Rendering strategy supports public content discovery.
- [ ] URLs are stable and meaningful.
- [ ] Canonical URLs are correct.
- [ ] Robots directives are intentional.
- [ ] Sitemap contains appropriate public URLs.
- [ ] Redirects are correct.

### Metadata

- [ ] Important pages have meaningful titles.
- [ ] Descriptions are accurate.
- [ ] Metadata is not unnecessarily duplicated.
- [ ] Open Graph metadata is correct.
- [ ] Social preview images are valid.

### Content and Structure

- [ ] Semantic HTML is used.
- [ ] Heading hierarchy is logical.
- [ ] Internal links are meaningful.
- [ ] Images have appropriate alt text.
- [ ] Structured data matches visible content.
- [ ] International metadata is correct where applicable.

### Reliability

- [ ] Private pages are not exposed.
- [ ] No sensitive data appears in metadata.
- [ ] No unnecessary duplicate URLs exist.
- [ ] Performance issues are considered.
- [ ] Production output is verified.
- [ ] No unsupported ranking or indexing claims are made.

## 30. Related References

- anti-ai-slop-and-engineering-quality.md
- architecture-and-project-structure.md
- react-engineering.md
- nextjs-engineering.md
- rendering-and-caching-strategies.md
- global-styles-and-design-tokens.md
- accessibility-and-wcag.md
- frontend-security.md
- performance-and-core-web-vitals.md
- internationalization-and-rtl.md
- environment-configuration.md
- production-readiness.md

## 31. Official Resources

### Google Search

- SEO Starter Guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Search Essentials: https://developers.google.com/search/docs/essentials
- JavaScript SEO: https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics
- Robots meta tags: https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag
- Sitemaps: https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview
- Canonical URLs: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- Structured data: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- International SEO: https://developers.google.com/search/docs/specialty/international/localized-versions

### Next.js

- Metadata: https://nextjs.org/docs/app/getting-started/metadata-and-og-images
- Metadata API: https://nextjs.org/docs/app/api-reference/functions/generate-metadata
- Sitemap: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap
- robots.txt: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots

### Other Resources

- Schema.org: https://schema.org/
- Schema Markup Validator: https://validator.schema.org/
- Google Rich Results Test: https://search.google.com/test/rich-results
- Google Search Console: https://search.google.com/search-console
- Bing Webmaster Tools: https://www.bing.com/webmasters/

Always verify current official documentation and search engine guidelines before implementation.
