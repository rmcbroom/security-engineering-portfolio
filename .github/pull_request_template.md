# Change Review

Use the sections that are applicable to the change. Review depth should be proportional to consequence; formatting-only changes do not require empty claim or limitation narratives.

## Change tier

- [ ] **Low impact** — typo, formatting, navigation wording, or non-substantive presentation adjustment. Review the diff and validate links or formatting as applicable.
- [ ] **Material** — substantive claim, new diagram, case-study content, binary or media asset, or evidence/status change. Complete claim, disclosure, and validation review.
- [ ] **Architecture / governance** — evidence-path or disclosure-policy change, new control, or change to the trusted-public-state model. Review architecture and controls, and consider whether an ADR must be created or reassessed.

## What changed?

<!-- Short description of the change. -->

## Why?

<!-- Why does this belong in the public portfolio? -->

## Evidence path

- [ ] Professional — clean-room
- [ ] Independent
- [ ] Mixed
- [ ] Governance / repository-only
- [ ] Presentation / formatting-only

For mixed evidence, explain which claims belong to which provenance path.

<!-- Evidence-path notes, when needed. -->

## Claim review

- [ ] No substantive claims were added or changed.
- [ ] Claims were added or changed, and their evidence was reviewed.

If claims changed, identify the supporting evidence and any remaining limitations. No additional explanation is required for a formatting-only change with no claim impact.

<!-- Supporting evidence and limitations, when applicable. -->

## Disclosure review

Confirm as applicable:

- [ ] No employer or client artifact is included.
- [ ] No proprietary implementation detail is exposed.
- [ ] No credential, secret, private identifier, or private URL is included.
- [ ] Ownership and contribution wording is accurate.
- [ ] Synthetic or generalized material is clearly represented as such.
- [ ] Binary or media provenance and metadata were reviewed where applicable.

Policy and review references:

- [Portfolio disclosure policy](../DISCLOSURE.md)
- [Full disclosure-review framework](../frameworks/disclosure-review.md)

## Validation

These checks are currently manual. Automated validation is a future control and must not be assumed to exist.

- [ ] Relative links and images were validated.
- [ ] Mermaid was validated where applicable.
- [ ] Markdown structure was reviewed.
- [ ] Sensitive filenames and content were reviewed.
- [ ] Binary size and metadata were reviewed where applicable.

Automation can validate deterministic properties such as links, Markdown structure, Mermaid syntax, forbidden filenames, credential patterns, and selected repository hygiene. Human review must determine whether professional material is disclosure-safe, claims are truthful and properly scoped, ownership wording is accurate, diagrams avoid reconstructing protected implementation, and publication is appropriate.

## Architecture / governance impact

Does this change alter evidence paths, disclosure boundaries, repository architecture, governance or control behavior, or public-state assumptions?

- [ ] No
- [ ] Yes — described below

If yes, explain what changed and whether an ADR should be created or reassessed. An ADR is not required for every change.

<!-- Architecture or governance impact, when applicable. -->

## Limitations / reassessment

<!-- Material limitations, accepted risks, or conditions that should trigger future review. Omit when none apply. -->

## Human review

- [ ] I reviewed the final diff as the portfolio owner.
- [ ] I reviewed the change for disclosure, claim accuracy, and intended public exposure.

Checklist completion is not evidence by itself. Review the actual diff and supporting evidence.
