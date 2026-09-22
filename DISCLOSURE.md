# Portfolio Disclosure Policy

This portfolio communicates engineering judgment without publishing employer or client intellectual property, confidential information, security-sensitive implementation details, or independently owned material that should remain private.

## Clean-Room Rule

Professional experience is represented through independently authored methodologies, generic explanations, and newly created synthetic demonstrations.

- Employer and client artifacts are never published.
- Employer artifacts are not sanitized, redacted, renamed, traced, or otherwise reused.
- Public diagrams, examples, datasets, scenarios, interfaces, and documents are created from first principles.
- No employer name is required to understand a technical case study.
- If material cannot be safely substantiated, it is omitted.
- If disclosure is uncertain, the material remains private.

Professional experience may inform general engineering principles, skills, lessons, and classes of problems. It does not authorize reconstruction of a particular employer's implementation.

## Independent Work

Independent projects may contain greater technical depth because I own the underlying architecture and implementation. Ownership does not require complete disclosure.

Source code, strategies, security controls, private prompts, formulas, thresholds, credentials, configurations, and other implementation details may remain private when publication would expose intellectual property, weaken security, or allow reproduction of protected behavior.

## Classification Labels

### Ownership

| Label | Meaning |
| --- | --- |
| **Professional Experience** | Work performed in a professional context. Public material is independently authored and clean-room. |
| **Independent** | Work I independently designed or built and have authority to discuss. |
| **Mixed** | Work combines more than one context; the boundary must be explained. |

### Implementation Status

| Label | Meaning |
| --- | --- |
| **Implemented** | Built or put into use within the stated scope. |
| **Designed** | Architected or specified but not represented as fully implemented. |
| **Experimental** | Built or tested for exploration; results and maturity are limited to the stated experiment. |
| **Conceptual / Planned** | Proposed to explain an idea or future direction; not yet implemented. |

Modifiers such as **Actively Developed** may be added when they clarify current state without obscuring the primary status.

### Disclosure

| Label | Meaning |
| --- | --- |
| **Public** | Safe to publish directly within the stated scope. |
| **Showcase** | Architecture, methodology, decisions, or sanitized evidence may be shown; protected implementation remains private. |
| **Private** | Must not appear in the public portfolio. |

### Evidence

Evidence labels are descriptive rather than maturity claims:

| Label | Meaning |
| --- | --- |
| **Verified** | Checked against the current independently owned implementation or reproducible result. |
| **Independently Recreated** | Newly authored from first principles to demonstrate professional methodology. |
| **Synthetic** | Uses fictional scenarios, identities, infrastructure, or data created for the portfolio. |
| **Planned** | Proposed evidence that does not yet exist. |

## Standard Project Header

Use only the fields relevant to the page. Do not use a header to imply evidence or maturity that has not been established.

Independent project example:

```text
Ownership: Independent
Implementation Status: Implemented / Actively Developed
Disclosure: Public Architecture / Private Implementation
Evidence: Verified / Planned
Last Verified: YYYY-MM-DD
```

Professional methodology example:

```text
Ownership: Professional Experience
Implementation Status: Implemented
Disclosure: Clean-Room Methodology
Evidence: Independently Recreated / Synthetic
```

## Claim and Evidence Rules

- Describe personal responsibility precisely; do not convert team outcomes into individual ownership.
- Separate implemented, designed, experimental, and conceptual work.
- Verify changing facts and metrics immediately before publication.
- Explain the scope and measurement method for any published metric.
- Do not imply production use, scale, effectiveness, profitability, or business impact without support.
- Do not use employer artifacts as evidence, even if names and identifiers are removed.
- Keep private material out of the repository and its Git history; do not commit it temporarily for later redaction.
- Review every artifact with the [disclosure checklist](frameworks/disclosure-review.md) before publication.

## Never Publish

- Credentials, secrets, tokens, account identifiers, or private keys
- Internal URLs, hostnames, repositories, resource identifiers, or network topology
- Employer or client source code, queries, configurations, schemas, prompts, screenshots, documents, or data
- Customer, employee, or incident information
- Production detection logic, thresholds, scoring weights, or feature calculations
- Sensitive attack paths or unremediated weaknesses
- Proprietary trading strategy, signals, formulas, indicators, thresholds, account data, or history
- Private AI prompts, agent instructions, model configurations, or confidential evaluation data

