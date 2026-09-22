# AI-Assisted Security Engineering

> **Ownership:** Independent / Mixed  
> **Implementation Status:** Experimental; Some Workflows Implemented  
> **Disclosure:** Public Principles / Private Instructions and Configuration  
> **Evidence:** Experimental Evidence Requires Verification; Public Evaluation Planned

## What I Work On

My work includes formal study of agentic AI and independent experimentation with specialized, security-focused agent workflows. Areas explored include separation of analytical responsibilities, reusable security methodologies, collaboration between specialized roles, and boundaries requiring human review.

This page does not claim that a complete, production-ready Security Engineering Agent System has been built.

## Engineering Concerns

- Evidence-grounded output and unsupported claims
- Prompt injection and malicious retrieved content
- Data minimization and sensitive-data exposure
- Tool permissions and unauthorized action attempts
- Missing, conflicting, or partial evidence
- Tool failure and model uncertainty
- Human approval and accountability
- Auditability of requests, context, tool use, recommendations, and actions

## How I Approach the Problem

I separate responsibilities among four layers:

- Deterministic code and tools perform retrieval, calculations, validation, and structured actions.
- AI assists with interpretation, comparison, synthesis, and hypothesis generation.
- Security controls enforce identity, permissions, access, and audit boundaries.
- Humans retain consequential decisions, exceptions, escalation, and accountability.

The model is not the security boundary. Model capability must not silently become system authority.

## Related Portfolio Work

- [Security Automation & Tooling](security-automation-tooling.md)
- A portfolio-grade Security Engineering Agent System is a future independent project and is not part of Phase 1.

## Current Evidence / Status

Some agent workflows and multi-agent learning projects have been implemented experimentally. The exact public boundary, publication rights for coursework artifacts, technical enforcement mechanisms, adversarial test results, and evaluation evidence still require verification. Private prompts, proprietary instructions, employer information, and confidential evaluation data will not be published.

