# Environment Configuration

## 1. Purpose

Define how frontend applications manage environment-specific configuration safely and consistently.

The agent must ensure that development, staging and production environments behave correctly without leaking secrets or mixing configuration.

This reference applies to:

- Environment variables.
- Configuration files.
- Development, staging and production.
- API URLs.
- Authentication configuration.
- Feature flags.
- Docker.
- CI/CD.
- Hosting platforms.
- Next.js.
- Vite.
- React applications.
- Runtime configuration.
- Build-time configuration.
- Secret management.
- Configuration validation.

The objective is to make configuration predictable, secure, maintainable and environment-aware.

## 2. Core Principles

Follow these principles:

1. Separate development, staging and production configuration.
1. Never expose secrets to browser-side code.
1. Validate required configuration.
1. Avoid hardcoding environment-specific values.
1. Use the framework's supported environment variable conventions.
1. Keep configuration centralized.
1. Use explicit defaults only when safe.
1. Never commit real secrets.
1. Keep local and deployment configuration consistent.
1. Document required variables without documenting secret values.

Do not create a complicated configuration framework when a small configuration module is sufficient.

## 3. Inspect Before Changing Configuration

For existing projects, inspect:

- Framework and version.
- Runtime and package manager.
- Existing `.env` files.
- Environment variable naming.
- Configuration modules.
- Build configuration.
- Hosting platform settings.
- CI/CD workflows.
- Docker configuration.
- API client configuration.
- Authentication configuration.
- Existing secret management.
- Environment-specific scripts.

Understand which variables are:

- Build-time configuration.
- Runtime configuration.
- Server-only secrets.
- Public browser configuration.
- Optional settings.
- Required settings.

Do not assume every framework exposes environment variables in the same way.

## 4. Environment Separation

Maintain distinct environments.

### Development

Used for local development.

Typical characteristics:

- Local API or development backend.
- Development database.
- Debugging tools.
- Development-specific integrations.
- Local environment variables.

### Staging

Used to validate changes before production.

Typical characteristics:

- Staging API.
- Staging database.
- Staging authentication configuration.
- Production-like deployment.
- Integration testing.
- Release verification.

### Production

Used by real users.

Typical characteristics:

- Production API.
- Production database.
- Restricted access.
- Production secrets.
- Monitoring.
- Optimized builds.
- Strict security configuration.

### Example Configuration Matrix

| Setting | Development | Staging | Production |
| ------------- | -------------------- | --------------- | ------------------ |
| API URL | Local API | Staging API | Production API |
| Database | Development DB | Staging DB | Production DB |
| Debugging | Enabled where useful | Restricted | Restricted |
| Test accounts | Allowed | Controlled | Avoid |
| Analytics | Development setup | Staging setup | Production setup |
| Secrets | Local secrets | Staging secrets | Production secrets |

Actual values belong in the appropriate environment, not in shared source code.

## 5. Environment Variable Files

Common environment file patterns include:

```text
.env
.env.local
.env.development
.env.production
.env.example
```

Their behavior depends on the framework and tooling.

Important rules:

- Read the framework's environment loading documentation.
- Understand file precedence.
- Check whether variables are loaded at build time or runtime.
- Do not assume `.env` behavior is identical across tools.
- Avoid maintaining duplicate sources of truth.

### Example `.env.example`

```dotenv
# Application
APP_ENV=development

# Public API configuration
NEXT_PUBLIC_API_URL=http://localhost:4000

# Server-only configuration
DATABASE_URL=
AUTH_SECRET=
```

This file contains variable names and safe placeholders.

It must not contain actual credentials.

Adapt prefixes to the framework.

For example:

- Next.js browser-exposed variables generally use `NEXT_PUBLIC_`.
- Vite browser-exposed variables generally use `VITE_`.

These prefixes are not security mechanisms. Their values are exposed to client-side code.

## 6. Public and Private Variables

Separate public configuration from secrets.

### Public Configuration

Values that are intentionally exposed to browser-side code.

Examples:

- Public API base URL.
- Public analytics identifier.
- Public feature configuration.
- Public application name.

### Private Configuration

Values that must remain server-side.

Examples:

- Database connection strings.
- Authentication secrets.
- Private API keys.
- Payment provider secret keys.
- Private service credentials.
- Signing keys.

Never expose private values through:

- Client Components.
- Browser JavaScript.
- Public environment prefixes.
- HTML.
- API responses.
- Logs.
- Source maps.
- Build artifacts.

A public API key and a private API secret are not interchangeable.

## 7. Next.js Environment Configuration

Next.js provides built-in environment variable support.

Common conventions:

- `.env.local`
- `.env.development`
- `.env.production`
- `.env.example`
- `NEXT_PUBLIC_` for browser-exposed variables.

### Example

```dotenv
# Server-only
DATABASE_URL=postgresql://...
AUTH_SECRET=...

# Browser-exposed
NEXT_PUBLIC_API_URL=https://api.example.com
```

The values above are illustrative. Do not use real credentials in committed examples.

### Important Behavior

`NEXT_PUBLIC_` variables are inlined into browser bundles during the build.

Changing the hosting environment variable after the build does not automatically change a value already embedded in the client bundle.

Understand this distinction when promoting the same build artifact between environments.

Server-side environment variables can have different runtime behavior depending on how and where the application is deployed.

### Server-Only Configuration Module

Example:

```ts
// src/config/server.ts

import "server-only";

function getRequiredEnv(name: string): string {
  const value = process.env[name];

  if (!value) {
    throw new Error(`Missing required environment variable: ${name}`);
  }

  return value;
}

export const serverConfig = {
  databaseUrl: getRequiredEnv("DATABASE_URL"),
  authSecret: getRequiredEnv("AUTH_SECRET"),
};
```

Use this module only from server-side code.

Do not import it into Client Components.

Avoid validating optional configuration as mandatory.

## 8. Vite Environment Configuration

Vite exposes variables through `import.meta.env`.

Common conventions:

```dotenv
VITE_API_URL=http://localhost:4000
```

Example:

```ts
// src/config/env.ts

const apiUrl = import.meta.env.VITE_API_URL;

if (!apiUrl) {
  throw new Error("Missing VITE_API_URL");
}

export const env = {
  apiUrl,
};
```

Only variables with the configured public prefix are exposed to browser code.

Do not place secrets in `VITE_` variables.

Check the project's actual Vite configuration before assuming the default prefix.

## 9. Centralized Configuration

Avoid accessing environment variables throughout unrelated application files.

Prefer a small configuration layer.

Example:

```text
src/
├── config/
│   ├── env.ts
│   ├── api.ts
│   └── constants.ts
├── services/
└── features/
```

The exact structure should follow the existing architecture.

Benefits:

- Centralized validation.
- Easier environment changes.
- Fewer hardcoded values.
- Consistent API configuration.
- Easier testing.
- Better maintainability.

Do not create multiple configuration abstractions that provide no additional value.

## 10. Validate Required Variables

Required configuration should fail clearly when missing.

Avoid allowing an application to start with an invalid API URL or missing authentication configuration.

A validation strategy should distinguish:

- Required variables.
- Optional variables.
- Public variables.
- Server-only variables.
- Environment-specific variables.

Example:

```ts
function getOptionalEnv(name: string): string | undefined {
  return process.env[name] || undefined;
}
```

For larger configuration schemas, a runtime validation library may be appropriate.

Possible tools:

- Zod.
- Valibot.
- ArkType.

Do not add a validation dependency for a handful of simple variables without justification.

Never log secret values during validation.

## 11. API Base URLs

Avoid hardcoding API endpoints in individual components.

Use a centralized API client.

Example:

```ts
// src/config/api.ts

export const API_BASE_URL = env.apiUrl;
```

Then:

```ts
// src/lib/api-client.ts

import { API_BASE_URL } from "@/config/api";

export async function apiRequest<T>(
  path: string,
  init?: RequestInit,
): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, init);

  if (!response.ok) {
    throw new Error(`API request failed: ${response.status}`);
  }

  return response.json() as Promise<T>;
}
```

This is a simplified example.

Add appropriate response validation, error handling, authentication and cancellation according to the API architecture.

Do not assume that TypeScript generics validate external JSON responses.

## 12. Feature Flags and Environment-Specific Behavior

Feature flags can control functionality across environments.

Examples:

- New dashboard experience.
- Experimental UI.
- Beta functionality.
- Gradual rollout.
- Emergency feature disablement.

Use a suitable strategy:

- Static environment configuration.
- Server-managed flags.
- Feature flag providers.
- User or organization-specific configuration.

Important:

- Keep security authorization independent of feature flags.
- Do not use frontend feature flags as access control.
- Avoid scattering environment checks across components.
- Remove temporary flags when they are no longer needed.

## 13. Configuration in Docker

Docker configuration must respect environment boundaries.

Do not bake production secrets into images.

Avoid:

```dockerfile
ENV DATABASE_URL=production-secret
```

Prefer injecting required values through the deployment platform or container runtime.

Example:

```bash
docker run \
  --env-file .env.production \
  -p 3000:3000 \
  my-frontend-app
```

This is an illustrative command.

Do not commit `.env.production`.

### Docker Build Arguments

Understand the difference between:

- Build arguments.
- Image environment variables.
- Runtime environment variables.
- Framework build-time public variables.

A value passed during a Docker build may become part of the image or generated frontend assets.

Do not pass secrets as build arguments unless the build process uses an appropriate secret mechanism.

See `ci-cd-and-deployment.md`.

## 14. Configuration in CI/CD

Configure environment variables through the appropriate platform.

Examples:

- GitHub Actions secrets and variables.
- Vercel environment variables.
- Render environment settings.
- Cloud provider secret managers.

Keep separate values for:

- Development.
- Staging.
- Production.

Use restricted permissions for production secrets.

Do not print secrets in workflow logs.

Do not expose deployment credentials to untrusted pull request workflows.

CI should validate that required configuration is present without displaying its values.

## 15. Runtime Configuration vs Build-Time Configuration

Understand when values are read.

### Build-Time Configuration

Resolved during the build process.

Common examples:

- Public frontend environment variables.
- Static generation inputs.
- Build-time feature configuration.

### Runtime Configuration

Resolved while the application is running.

Common examples:

- Server-only configuration.
- Runtime service credentials.
- Server-side API endpoints.

Do not assume that every deployment platform supports runtime changes for every variable.

When promoting a built artifact between environments, verify whether environment-specific values are embedded during compilation.

Avoid rebuilding unnecessarily when the architecture supports safe runtime configuration.

## 16. Configuration Security

Apply these rules:

- Never commit real secrets.
- Keep `.env*` files out of version control where appropriate.
- Commit a safe `.env.example`.
- Restrict secret access.
- Rotate exposed credentials.
- Use separate credentials per environment.
- Avoid secrets in browser bundles.
- Avoid secrets in logs and error messages.
- Use server-only modules for sensitive configuration.
- Restrict production environment access.
- Validate redirect URLs and external endpoints where relevant.

If a secret is exposed, treat it as compromised.

Removing it from the latest commit does not invalidate the exposed credential.

Rotate it using the provider's supported process.

## 17. Configuration Testing

Verify configuration behavior across environments.

Test:

- Missing required variables.
- Invalid URLs.
- Invalid configuration formats.
- Development defaults.
- Staging endpoints.
- Production endpoints.
- Public/private separation.
- Build-time configuration.
- Runtime configuration.
- Feature flag defaults.

Avoid tests that depend on real production secrets.

Use isolated test configuration.

## 18. Existing Project Configuration Changes

When modifying an existing project:

1. Inspect current environment conventions.
1. Identify the actual runtime.
1. Inspect all relevant configuration sources.
1. Identify public and private values.
1. Trace where variables are consumed.
1. Check deployment platform configuration.
1. Preserve existing environment behavior.
1. Make targeted changes.
1. Update `.env.example` and documentation.
1. Validate each affected environment where possible.

Do not rename existing environment variables without checking all references and deployment settings.

Do not assume a variable can be removed just because it is not referenced in the first file inspected.

## 19. Common Configuration Anti-Patterns

Avoid:

- One configuration for every environment.
- Hardcoded API URLs.
- Hardcoded secrets.
- Exposing private keys through public prefixes.
- Duplicating configuration in many files.
- Logging environment values.
- Committing production `.env` files.
- Using production credentials locally.
- Mixing staging and production databases.
- Assuming build-time variables update at runtime.
- Adding unnecessary configuration libraries.
- Silently falling back when required configuration is missing.
- Using frontend feature flags for authorization.
- Putting secrets in Docker images.

## 20. Recommended Configuration Workflow

1. Inspect the current environment setup.
1. Identify the framework's variable conventions.
1. Classify each variable.
1. Define environment-specific values.
1. Centralize access where useful.
1. Validate required configuration.
1. Protect secrets.
1. Update example files and documentation.
1. Configure CI/CD and hosting platforms.
1. Verify development, staging and production behavior.

## 21. Review Checklist

### Environment Separation

- [ ] Development configuration exists.
- [ ] Staging configuration is separate.
- [ ] Production configuration is separate.
- [ ] Environment-specific API URLs are correct.
- [ ] Database connections are isolated.

### Security

- [ ] No real secrets are committed.
- [ ] Public variables contain no private credentials.
- [ ] Server-only configuration stays on the server.
- [ ] Secret access is restricted.
- [ ] Logs do not expose sensitive values.

### Reliability

- [ ] Required variables are validated.
- [ ] Invalid configuration fails clearly.
- [ ] Build-time and runtime behavior are understood.
- [ ] Docker and CI/CD use the correct configuration.
- [ ] Environment documentation is accurate.

### Existing Project Safety

- [ ] Existing conventions inspected.
- [ ] Existing variable references checked.
- [ ] Deployment settings considered.
- [ ] Unrelated behavior preserved.

## 22. Related References

- anti-ai-slop-and-engineering-quality.md
- architecture-and-project-structure.md
- nextjs-engineering.md
- api-integration.md
- authentication-and-authorization.md
- frontend-security.md
- package-selection-and-ecosystem.md
- debugging-and-self-correction.md
- ci-cd-and-deployment.md
- observability-and-monitoring.md
- production-readiness.md

## 23. Official Resources

### Next.js

- Environment Variables: https://nextjs.org/docs/app/guides/environment-variables

### Vite

- Environment Variables and Modes: https://vite.dev/guide/env-and-mode

### Node.js

- Environment Variables: https://nodejs.org/en/learn/command-line/how-to-read-environment-variables-from-nodejs

### Docker

- Docker Build Secrets: https://docs.docker.com/build/building/secrets/
- Environment Variables: https://docs.docker.com/compose/how-tos/environment-variables/

### GitHub Actions

- Variables: https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-variables
- Secrets: https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets

Always verify environment variable behavior against the installed framework version and deployment platform.
