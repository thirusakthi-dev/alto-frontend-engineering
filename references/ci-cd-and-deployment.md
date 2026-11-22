# CI/CD and Deployment

## 1. Purpose

Define reliable practices for building, testing, integrating, and deploying frontend applications.

The agent should understand both the existing deployment setup and the requirements of a new project.

This reference applies to:

- Git and GitHub workflows.
- Continuous Integration (CI).
- Continuous Delivery and Deployment (CD).
- GitHub Actions.
- Automated quality checks.
- Production builds.
- Docker.
- Frontend hosting.
- Backend hosting.
- Full-stack deployment.
- Preview deployments.
- Environment-specific configuration.
- Release management.
- Rollbacks.
- Deployment troubleshooting.

The objective is to make application delivery repeatable, secure, maintainable, and verifiable.

## 2. Core Principles

Follow these principles:

1. Inspect the existing deployment setup before changing it.
1. Automate repeatable quality checks.
1. Validate code before deployment.
1. Keep development, staging and production environments separate.
1. Protect secrets and deployment credentials.
1. Make builds reproducible.
1. Prefer simple workflows over unnecessary pipeline complexity.
1. Use the project's existing package manager and scripts.
1. Make deployment failures visible.
1. Provide a reliable recovery strategy.

Do not introduce Docker, Kubernetes, or additional deployment infrastructure without a real requirement.

## 3. Inspect Existing Deployment Infrastructure

Before making changes, inspect:

- Repository structure.
- Git branch strategy.
- Package manager and lockfile.
- Runtime and framework versions.
- Build scripts.
- Lint and type-check scripts.
- Test scripts.
- Existing GitHub Actions workflows.
- Hosting platform.
- Build and output configuration.
- Environment variables.
- Domain and DNS configuration where relevant.
- Backend and database dependencies.
- Existing deployment documentation.

Check existing files such as:

```text
.github/workflows/
package.json
package-lock.json
pnpm-lock.yaml
yarn.lock
bun.lock
Dockerfile
.dockerignore
next.config.ts
vite.config.ts
vercel.json
render.yaml
```

These are examples, not mandatory files.

Do not create duplicate workflows or replace existing infrastructure without understanding it.

## 4. Understand CI/CD

### Continuous Integration (CI)

CI automatically validates code changes.

Typical tasks:

- Install dependencies.
- Run formatting checks.
- Run linting.
- Run TypeScript checks.
- Run unit tests.
- Run integration tests.
- Build the application.

### Continuous Delivery

The application is automatically prepared for release, but production deployment may require approval.

### Continuous Deployment

Validated changes are automatically deployed to the target environment.

Choose the appropriate model based on project requirements and release risk.

## 5. Recommended CI Pipeline

A typical frontend CI workflow:

```text
Pull Request / Push
        |
        v
Checkout Repository
        |
        v
Setup Runtime
        |
        v
Install Dependencies
        |
        v
Formatting Check
        |
        v
Lint
        |
        v
Type Check
        |
        v
Run Tests
        |
        v
Production Build
        |
        v
Report Results
```

Not every project needs every stage.

Use existing project scripts rather than inventing new commands.

### Recommended Quality Gates

| Check | Purpose |
| ----------------- | ------------------------------------------------- |
| Formatting | Consistent source formatting |
| Lint | Detect code quality issues |
| Type check | Detect type errors |
| Unit tests | Verify isolated logic |
| Integration tests | Verify connected behavior |
| E2E tests | Verify important user flows |
| Build | Verify production compilation |
| Security checks | Detect relevant dependency or configuration risks |

A project should not deploy when required quality gates fail.

## 6. GitHub Actions

GitHub Actions can automate CI/CD using workflow files stored in:

```text
.github/workflows/
```

Each workflow defines:

- Trigger events.
- Jobs.
- Runner environments.
- Steps.
- Permissions.
- Secrets.
- Artifacts.
- Deployment conditions.

### Example: Frontend CI

The following is an illustrative workflow for a Node.js project using npm.

Adapt the runtime, scripts and package manager to the actual project.

```yaml
name: Frontend CI

on:
  pull_request:
    branches:
      - main
  push:
    branches:
      - main

permissions:
  contents: read

concurrency:
  group: ci-${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  quality:
    name: Validate Application
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 24
          cache: npm

      - name: Install dependencies
        run: npm ci

      - name: Run lint
        run: npm run lint --if-present

      - name: Run type check
        run: npm run typecheck --if-present

      - name: Run tests
        run: npm test --if-present

      - name: Build application
        run: npm run build
```

Important:

- Pin action versions according to the repository's security policy.
- Review third-party actions before using them.
- Use the actual supported runtime version.
- Do not assume optional scripts exist.
- Prefer explicit project scripts when quality checks are mandatory.
- Avoid silently skipping required checks with `--if-present`.
- Use the lockfile-based installation command.
- Do not expose secrets in pull request workflows.
- Do not grant unnecessary workflow permissions.

The example is a starting point, not a universal production workflow.

## 7. Package Manager Consistency

Use the package manager already selected by the project.

Examples:

| Package manager | CI installation |
| --------------- | ------------------------------------------------------------- |
| npm | `npm ci` |
| pnpm | `pnpm install --frozen-lockfile` |
| Yarn | `yarn install --immutable` for supported modern Yarn versions |
| Bun | `bun install --frozen-lockfile` |

Verify the exact command for the installed package manager version.

Do not mix package managers or generate competing lockfiles.

## 8. Pull Request Validation

Run automated validation before merging.

Recommended checks:

- Formatting.
- Linting.
- TypeScript.
- Relevant tests.
- Production build.
- Dependency or security checks where appropriate.

Protect important branches with suitable repository rules.

Consider:

- Required status checks.
- Pull request reviews.
- Restricting direct pushes.
- CODEOWNERS where useful.
- Merge requirements.

Do not enforce unnecessary approval requirements on small personal projects.

## 9. Branch and Deployment Strategy

A simple workflow can use:

```text
feature branch
      |
      v
Pull Request
      |
      v
CI Validation
      |
      v
main
      |
      v
Staging / Preview
      |
      v
Production
```

The exact process depends on the hosting platform and project.

### Branch Recommendations

| Branch | Purpose |
| ----------- | ------------------------- |
| `main` | Stable integration branch |
| `feature/*` | New features |
| `fix/*` | Bug fixes |
| `hotfix/*` | Urgent production fixes |

Avoid creating too many long-lived branches without a clear need.

## 10. Preview Deployments

Preview deployments provide a separate environment for reviewing changes.

Useful for:

- Pull request review.
- UI verification.
- Stakeholder feedback.
- Functional testing.
- Responsive testing.
- Early integration testing.

Preview deployments should not automatically receive production secrets or unrestricted production data.

Check whether the hosting platform supports isolated preview environments.

## 11. Deployment Environments

Maintain separate configurations for:

### Development

Used for local development and debugging.

### Staging

Used for integration testing and release validation.

### Production

Used by real users.

Keep environment-specific settings separate:

- API URLs.
- Authentication callbacks.
- Database connections.
- Storage providers.
- Feature flags.
- Monitoring configuration.
- Third-party integration credentials.

Do not use production secrets in development or staging.

See `environment-configuration.md`.

## 12. Frontend Deployment

Choose a hosting platform based on the framework and application requirements.

Common options include:

- Vercel.
- Netlify.
- Cloudflare Pages.
- Static hosting.
- Container-based hosting.
- Traditional VPS infrastructure.

### Static Frontend

Suitable for applications that can be generated as static assets.

Typical output:

```text
dist/
```

or another framework-specific output directory.

Configure:

- Build command.
- Output directory.
- Environment variables.
- SPA fallback routing where required.
- Custom domain.
- HTTPS.
- Cache headers.

Do not assume every React application is a static application.

### Next.js Deployment

Next.js can use different deployment modes.

Consider:

- Managed Next.js hosting.
- Node.js server deployment.
- Docker.
- Static export where compatible.

Before selecting a deployment model, check whether the application requires:

- Server Components.
- Server Actions.
- Route Handlers.
- Middleware or Proxy functionality.
- Image optimization.
- ISR or server-side caching.
- Runtime-specific features.

Static export does not support every server-dependent feature.

Do not force static hosting when the application requires a server runtime.

## 13. Backend and Full-Stack Deployment

For full-stack applications, identify the responsibilities of each service.

Example:

```text
Browser
   |
   v
Frontend Hosting
   |
   v
Backend API
   |
   v
Database
```

Possible hosting arrangements:

- Frontend on Vercel and backend on Render.
- Frontend and backend in separate containers.
- A single Node.js application serving both frontend and API.
- Cloud infrastructure with independent services.

Verify:

- API connectivity.
- CORS configuration.
- Authentication cookie domains.
- HTTPS.
- Database access.
- Network restrictions.
- Health checks.
- Deployment ordering.
- Environment-specific URLs.

Do not expose internal service addresses or credentials to the browser.

## 14. Docker

Docker provides a consistent environment for building and running applications.

It can be useful when:

- Deployment requires a container.
- Local and production environments need consistency.
- The application has multiple services.
- A hosting platform expects container images.
- Runtime dependencies must be controlled.

Do not introduce Docker simply because it is common in production projects.

### Example: Next.js Dockerfile

This is a simplified example using a multi-stage build.

It assumes the project is configured with Next.js standalone output.

```dockerfile
FROM node:24-alpine AS base

WORKDIR /app

FROM base AS dependencies

COPY package.json package-lock.json ./

RUN npm ci

FROM base AS builder

COPY --from=dependencies /app/node_modules ./node_modules
COPY . .

RUN npm run build

FROM base AS runner

ENV NODE_ENV=production

WORKDIR /app

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs

EXPOSE 3000

ENV PORT=3000

CMD ["node", "server.js"]
```

The application must configure:

```ts
// next.config.ts

const nextConfig = {
  output: "standalone",
};

export default nextConfig;
```

Adapt the Dockerfile to the actual project.

Important considerations:

- Use a compatible Node.js version.
- Keep dependencies reproducible.
- Run as a non-root user.
- Use `.dockerignore`.
- Avoid copying local secrets.
- Avoid unnecessary build tools in the runtime image.
- Verify native dependencies and platform compatibility.
- Use a supported base image.
- Review image size and vulnerabilities.

### Example `.dockerignore`

```text
node_modules
.next
.git
.env
.env.*
!.env.example
coverage
dist
build
npm-debug.log
.DS_Store
```

Adapt the rules to the project's build requirements.

Never include credentials in container images.

## 15. Container Orchestration

Use container orchestration only when operational requirements justify it.

Possible technologies:

- Docker Compose.
- Kubernetes.
- Managed container platforms.

Docker Compose can be useful for local development involving multiple services.

Kubernetes is not a default requirement for a small frontend application.

Prefer managed infrastructure when it reduces operational complexity.

## 16. Deployment Security

Apply these practices:

- Store deployment credentials in platform secrets.
- Use least-privilege permissions.
- Protect production environments.
- Avoid exposing secrets in logs.
- Avoid deploying untrusted pull request code with privileged credentials.
- Review third-party GitHub Actions.
- Use secure dependency installation.
- Enable HTTPS.
- Protect deployment tokens.
- Keep environment-specific credentials separate.
- Restrict access to production resources.

Never hardcode secrets in:

- Source code.
- Workflow YAML.
- Dockerfiles.
- Public environment variables.
- Build artifacts.
- Commit history.

A variable exposed to browser-side code is not a secret.

## 17. Deployment Verification

A successful build does not guarantee a successful deployment.

After deployment, verify:

- Application loads.
- Important routes work.
- API calls succeed.
- Authentication works.
- Assets load.
- No unexpected console errors.
- No broken navigation.
- Responsive layouts remain correct.
- SEO metadata is present where required.
- Monitoring receives events.
- Health checks pass where configured.

Use smoke tests for critical functionality.

Avoid testing production by performing destructive actions or using real customer data.

## 18. Rollbacks and Recovery

A deployment process should have a recovery strategy.

Possible approaches:

- Revert a Git commit.
- Redeploy a known-good release.
- Restore a previous deployment.
- Roll back a container image.
- Disable a problematic feature flag.
- Apply a database migration recovery procedure.

Consider:

- Database compatibility.
- API compatibility.
- Cached assets.
- Session compatibility.
- Environment changes.
- Data migrations.

A frontend rollback may not reverse a database migration.

Plan data changes separately.

Never claim a rollback is successful without checking the application afterward.

## 19. Deployment Troubleshooting

### Build Failure

Inspect:

- Build logs.
- Runtime version.
- Package manager.
- Missing environment variables.
- TypeScript errors.
- Dependency compatibility.
- Build configuration.

### Application Starts but Returns Errors

Inspect:

- Runtime logs.
- API URLs.
- Environment configuration.
- Server-side dependencies.
- Database connections.
- Runtime permissions.

### Application Works Locally but Fails in Production

Investigate:

- Environment differences.
- Case-sensitive file paths.
- Build-time versus runtime variables.
- Missing static assets.
- Server/client execution boundaries.
- CORS.
- Authentication domains.
- Hosting platform limitations.

Do not assume that a successful local run proves production readiness.

## 20. Existing Project Deployment Changes

When modifying an existing deployment pipeline:

1. Inspect current workflows.
1. Understand deployment triggers.
1. Identify existing quality gates.
1. Review secrets and permissions.
1. Understand the hosting provider.
1. Identify affected environments.
1. Make the smallest required change.
1. Validate workflow syntax and configuration.
1. Run available checks.
1. Review the final diff.

Preserve existing deployment behavior unless the user requests a change.

Do not replace a working deployment architecture with a preferred stack without justification.

## 21. Common CI/CD Anti-Patterns

Avoid:

- Deploying without required checks.
- Using floating or unreviewed dependencies in workflows.
- Exposing production secrets to pull requests.
- Running every expensive test on every event without reason.
- Ignoring failed pipeline steps.
- Using inconsistent runtime versions.
- Mixing package managers.
- Committing generated secrets.
- Using production databases for test runs.
- Building Docker images unnecessarily.
- Using Kubernetes for simple applications.
- Deploying without a recovery plan.
- Assuming build success means runtime success.
- Making deployment configuration changes without validation.

## 22. Recommended Delivery Workflow

For a typical application:

1. Developer creates a feature branch.
1. Developer implements and tests the change.
1. Pull request is opened.
1. CI runs quality checks.
1. Review and approval happen where required.
1. Change is merged.
1. Preview or staging deployment is created.
1. Critical flows are verified.
1. Production deployment is approved or triggered.
1. Smoke checks and monitoring are reviewed.
1. A rollback path remains available.

Adapt this workflow to the project's size and risk.

## 23. Review Checklist

### Repository and Workflow

- [ ] Existing infrastructure inspected.
- [ ] Correct package manager used.
- [ ] Runtime version specified.
- [ ] CI workflows are understandable.
- [ ] Required quality checks run.

### Security

- [ ] Secrets are stored securely.
- [ ] Workflow permissions are restricted.
- [ ] Untrusted code cannot access privileged credentials.
- [ ] Dependencies and actions are reviewed.
- [ ] Production access is protected.

### Deployment

- [ ] Environment configuration is correct.
- [ ] Build and runtime requirements are supported.
- [ ] Deployment platform matches application requirements.
- [ ] HTTPS is enabled.
- [ ] Critical application flows are verified.

### Recovery

- [ ] Rollback strategy exists.
- [ ] Database changes are considered.
- [ ] Monitoring and deployment logs are available.

### Communication

- [ ] Actual workflow changes are reported.
- [ ] Checks are reported accurately.
- [ ] Deployment success is not claimed without verification.

## 24. Related References

- anti-ai-slop-and-engineering-quality.md
- architecture-and-project-structure.md
- package-selection-and-ecosystem.md
- frontend-security.md
- testing-strategy.md
- performance-and-core-web-vitals.md
- observability-and-monitoring.md
- debugging-and-self-correction.md
- environment-configuration.md
- production-readiness.md

## 25. Official Resources

### GitHub Actions

- GitHub Actions: https://docs.github.com/en/actions
- Workflow syntax: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
- Security hardening: https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions

### Docker

- Docker Documentation: https://docs.docker.com/
- Dockerfile Reference: https://docs.docker.com/reference/dockerfile/
- Docker Build: https://docs.docker.com/build/

### Next.js

- Next.js Deployment: https://nextjs.org/docs/app/getting-started/deploying
- Next.js Standalone Output: https://nextjs.org/docs/app/api-reference/config/next-config-js/output

### Hosting

- Vercel: https://vercel.com/docs
- Render: https://render.com/docs
- Cloudflare: https://developers.cloudflare.com/

Always verify current platform features, supported runtime versions, workflow syntax and deployment requirements before implementation.
