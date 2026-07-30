# GitHub Repository Setup

## 1. Create the repository

Recommended temporary repository name:

`open-inspection-data-standard`

Use a public repository only after replacing the contact placeholders and reviewing the licensing and interim IP policy with counsel.

## 2. Upload this package

From the extracted directory:

```bash
git init
git add .
git commit -s -m "Initial OIDS Version 0.1 working draft"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## 3. Replace placeholders

- Replace `@REPOSITORY-OWNER` in `.github/CODEOWNERS`.
- Add a private security contact in `SECURITY.md`.
- Review project naming, domain availability, trademarks, and permanent schema namespace.
- Add repository URLs to `CITATION.cff` after the public URL exists.

## 4. GitHub settings

Recommended settings:

- Enable Issues and Discussions.
- Require pull requests for `main` once additional maintainers join.
- Require the `Validate specification` status check.
- Enable secret scanning and dependency alerts.
- Disable force pushes and branch deletion on `main`.
- Add topics such as `inspection`, `construction`, `openbim`, `json-schema`, `openapi`, and `interoperability`.

## 5. First release

Create a prerelease tag such as `v0.1.0-draft.1`. Mark it as a pre-release and state clearly that it is not a final standard or certification program.

## 6. Before the public founding announcement

- Obtain written permission before listing any organization.
- Collect at least two vendor mappings.
- Replace interim security and legal placeholders.
- Publish meeting and decision procedures.
- Define the first interoperability pilot.
