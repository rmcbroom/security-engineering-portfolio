# ADR 0001 — Clean-Room Evidence Boundary for Professional Work

> **Status:** Accepted
> **Ownership:** Clean-Room Portfolio Artifact
> **Disclosure:** Public
> **Date:** 2026-09-22

## Context

Professional security work can demonstrate architecture, detection, validation, operational judgment, and governance. The supporting employer or client artifacts may also contain:

- proprietary architecture;
- internal telemetry;
- rules or queries;
- implementation details;
- internal identifiers;
- private metrics;
- confidential workflows; and
- intellectual property.

Removing visible identifiers does not necessarily remove sensitive structure or hidden context. Redaction can leave architecture, workflow, metadata, relationships, or implementation behavior recognizable.

The repository therefore needs a consistent boundary that permits meaningful professional evidence without treating possession of an artifact as permission to publish it. [DISCLOSURE.md](../../DISCLOSURE.md) remains the policy authority for what may be published.

## Decision

Professional employer or client artifacts will not be sanitized, redacted, renamed, traced, transformed, or republished as portfolio evidence.

Professional portfolio material will instead be independently reconstructed using:

- generalized methodology;
- synthetic examples;
- fictional entities;
- independently authored diagrams;
- public security concepts and frameworks; and
- disclosure-safe descriptions of personal contribution.

The repository may describe what Robin knows, how she reasons, the kinds of problems she has solved, and the engineering methodologies she has applied. It must not reconstruct how a specific employer's internal system works.

## Alternatives Considered

### 1. Publish sanitized or redacted employer artifacts — Rejected

Redaction can preserve structural, contextual, metadata, or intellectual-property exposure. It also creates an unreliable assumption that removed identifiers make the remaining artifact safe.

### 2. Publish screenshots with identifiers removed — Rejected

Screenshots can expose proprietary interfaces, layouts, workflows, relationships, timestamps, metadata, or contextual details even when obvious identifiers are removed.

### 3. Publish only high-level résumé statements — Rejected

This approach protects confidentiality but provides too little engineering evidence to show architecture, decision-making, validation, failure analysis, or governance depth.

### 4. Independently reconstruct methodology using synthetic and public material — Accepted

This approach provides meaningful engineering evidence while maintaining a clean-room boundary and explicit provenance.

## Tradeoffs

### Benefits

- Stronger confidentiality and intellectual-property protection
- Clear evidence provenance
- Demonstration of engineering judgment rather than artifact possession
- A reusable evidence model across professional case studies

### Costs

- Less visually direct proof of historical employer work
- Additional effort to create independent public representations
- Some implementation depth must remain private
- Readers must distinguish methodology evidence from independently implemented systems

## Consequences

Professional case studies must:

- identify themselves as professional clean-room evidence;
- exclude employer and client artifacts;
- use synthetic or generalized examples;
- distinguish personal contribution from team or system context;
- avoid claiming ownership of systems not independently owned; and
- keep protected implementation details private.

Independent projects follow a different evidence path, but they remain subject to claim verification and disclosure review.

## Validation

Human review evaluates:

- provenance;
- employer or client derivation;
- ownership wording;
- claims;
- diagrams;
- synthetic examples;
- binary assets; and
- metadata where applicable.

Automated checks may assist with secrets, suspicious filenames, repository integrity, links, and formatting. Automated checks cannot establish intellectual-property safety or the truth of professional claims.

## Reassessment Conditions

Reassess this decision if:

- the portfolio begins publishing substantially different evidence types;
- an employer explicitly authorizes publication of material;
- legal or intellectual-property requirements change;
- a disclosure incident exposes a weakness in this model; or
- new tooling materially changes what can be safely verified.

Even when explicit authorization exists, proposed publication must still be reviewed against the portfolio's purpose and minimum-necessary disclosure.

## Disclosure Notes

This decision governs public representation of professional work. It does not authorize publication of any employer or client material and does not replace the repository-wide [disclosure policy](../../DISCLOSURE.md).

The record exercises the repository's [architecture decision record template](../../frameworks/architecture-decision-record.md) without changing that reusable framework.
