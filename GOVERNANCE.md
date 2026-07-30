# Governance

## 1. Purpose

This document establishes interim governance for the Open Inspection Data Standard (OIDS) during its public working-draft phase. The objective is to move from founding stewardship by T2D2 to durable, vendor-neutral, multi-stakeholder governance.

## 2. Founding stewardship

T2D2 is the founding steward for Version 0.1. Its responsibilities are to maintain the initial repository, organize meetings, publish drafts, document decisions, and recruit a representative founding group.

Founding stewardship does **not** grant T2D2 permanent unilateral control over the standard. T2D2 may not represent that the project is an independent consensus standard until the governance transition described below has occurred.

## 3. Participants

Participation is open to software vendors, inspection firms, engineers, contractors, asset owners, regulators, researchers, standards organizations, and other materially affected stakeholders.

Initial roles are:

- **Contributor:** participates in issues, discussions, mappings, examples, or pull requests.
- **Maintainer:** performs repository review, release administration, and editorial work.
- **Technical Steering Committee (TSC) member:** participates in major technical and governance decisions.
- **Observer or advisor:** provides domain or regulatory input without implementation commitments.

## 4. Interim maintainers

Until a TSC is established, T2D2 may designate interim maintainers. Maintainers must apply the published contribution and decision procedures consistently and disclose material conflicts of interest.

## 5. Technical Steering Committee transition

The project should establish an initial TSC when at least five independent organizations are actively participating, including:

1. at least two independent software vendors;
2. at least one inspection, engineering, or contractor organization; and
3. at least one asset-owner, regulator, academic, or standards-community representative.

No single organization may control more than one-third of TSC voting seats. T2D2 is expected to retain at least one founding seat during the initial term but may not hold a majority.

The TSC will adopt its first permanent charter, maintainers, voting rules, and intellectual-property policy. It may choose to place the project under an established neutral standards or open-source host.

## 6. Decision process

The project prefers documented consensus:

1. material changes begin as an issue or request for comments (RFC);
2. affected implementers have a reasonable review period;
3. objections and proposed alternatives are recorded publicly;
4. maintainers summarize the apparent consensus; and
5. accepted decisions are recorded in `decisions/`.

During interim governance, if consensus cannot be achieved, interim maintainers may accept a reversible working-draft decision after documenting the competing positions. A final Version 1.0 decision may not rely solely on T2D2's unilateral vote.

After a TSC is formed, its charter should require a supermajority for breaking technical changes, governance changes, certification rules, or final-standard approval.

## 7. Releases

- Patch releases correct errors without intended data-model breakage.
- Minor `0.x` releases may add or change working-draft behavior.
- Release candidates require published conformance results.
- Version 1.0 should require at least two independent implementations and one end-to-end interoperability demonstration.

## 8. Working groups

The TSC or interim maintainers may establish working groups for areas such as core model, API and events, taxonomies, openBIM alignment, inspection profiles, or regulatory filing. Working-group outputs remain subject to the repository's review process.

## 9. Transparency

Meeting notes, material decisions, releases, conformance criteria, and known conflicts should be public unless confidentiality is necessary for security, privacy, or third-party legal obligations.

## 10. Neutrality and branding

Participation does not constitute endorsement of another participant's products. The project name and marks may not be used to imply certification or regulator authorization without an approved program.

## 11. Amendments

Interim amendments require a public RFC and at least 30 days for comment. Once the TSC is formed, its permanent charter will supersede this interim document.
