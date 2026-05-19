---
title: "From PRD to SDD: Who Writes the Spec?"
categories:
  - Software-Development
tags:
  - sdd
  - prd
  - product management
  - software engineering
---

I have been thinking about SDD again, but this time from a more practical angle:

```text
If we already have PRDs, how do we turn them into SDD?
Do we still need a BA role?
Can PMs write SDD directly instead of writing PRDs?
```

After reading more about Spec-Driven Development, PRDs, and business analysis work, my short answer is:

```text
PRD explains why and what.
SDD makes it buildable and testable.
BA may disappear as a title in some teams, but the BA work does not disappear.
PM can start the SDD, but engineering should co-own it before implementation.
```

That sounds simple, but the boundary matters.

![PRD to SDD map](/assets/images/post/2026-05-19-prd-to-sdd-map.svg){: .align-center}

## First, define the words

A PRD, or Product Requirements Document, is usually a product artifact. It describes the problem, target users, goals, scope, requirements, constraints, and success metrics. In a good PRD, requirements are measurable enough that designers, engineers, and QA can build and verify against them.

An SDD, in the current AI-assisted engineering sense, means Spec-Driven Development. It puts specifications at the center of the development workflow. GitHub Spec Kit describes the flow as specification, plan, tasks, and implementation. Kiro describes a similar structure with `requirements.md`, `design.md`, and `tasks.md`.

So I see them like this:

```text
PRD = product intent
SDD = product intent + technical plan + task breakdown + verification
```

The PRD should not decide everything about implementation. The SDD should not forget the product reason.

## Why PRD alone is not enough

A PRD can say:

```text
Users should be able to export their invoices.
```

That is useful, but an engineer still has questions:

- Export as PDF, CSV, or both?
- Which invoices are included?
- Is the export generated instantly or emailed later?
- What happens if there are 50,000 invoices?
- Who is allowed to export?
- Should we log the export for audit?
- What data must not appear in the file?

If these questions are answered inside chat messages, meetings, or someone's memory, the code will eventually become the real spec. That is dangerous. Code is a bad place to negotiate product meaning.

The SDD step forces us to turn the PRD into something explicit before we build.

## How I would convert PRD to SDD

For a small feature, I would use six steps.

### 1. Extract product intent

From the PRD, copy only the things that explain the product reason:

```text
Problem:
Users need invoice exports for accounting.

User:
Company admin.

Goal:
Admin can download invoices for a selected month.

Success metric:
80% of invoice export requests complete without support contact.
```

This keeps the SDD tied to the real user problem.

### 2. Turn requirements into testable statements

Rewrite vague product language into requirements that can be checked.

Instead of:

```text
Export should be fast and easy.
```

write:

```text
WHEN an admin selects a month with fewer than 1,000 invoices,
THE SYSTEM SHALL generate a CSV export within 10 seconds.
```

I like this style because it exposes weak thinking. If I cannot write the requirement clearly, I probably do not understand it yet.

### 3. Add non-goals

Non-goals are where many projects save time.

```text
Non-goals:
- No PDF export in this release.
- No scheduled exports.
- No export for non-admin users.
```

This is especially important when using AI agents. If we do not set boundaries, the agent may build a bigger feature than the team actually needs.

### 4. Add acceptance scenarios

Acceptance scenarios are the bridge between product and testing:

```text
Scenario: Admin exports invoices for March
Given the admin has 120 invoices in March
When the admin clicks Export CSV
Then the downloaded file contains those 120 invoices
And the file includes invoice number, date, customer, amount, and status
```

This gives QA something concrete. It also gives engineers a target.

### 5. Let engineering write the design

This is where I do not think PM should work alone.

The design section should answer:

- What API changes are needed?
- What database query or model change is needed?
- What background job is needed?
- What permissions are checked?
- What are the failure modes?
- What is the testing strategy?

PM can understand and challenge the design, but engineering should own the technical trade-offs.

### 6. Break it into tasks

The task list should be small and reviewable:

```text
Tasks:
- Add backend permission check for invoice export.
- Add CSV export endpoint.
- Add frontend export button for admins.
- Add tests for permission, empty result, and large result.
- Add manual QA checklist for CSV contents.
```

This is where SDD becomes useful for AI coding agents. The agent does not need to guess the whole project. It can work task by task.

![Simple PRD to SDD template](/assets/images/post/2026-05-19-prd-sdd-template.svg){: .align-center}

## Do we still need BA?

I do not think the right question is "do we need a BA?"

The better question is:

```text
Who is doing the business analysis work?
```

The International Institute of Business Analysis describes business analysis tasks as iterative work that can be performed by anyone in any role. That matches what I see in real teams.

In a small startup, the PM may do most of it. In a technical product team, the engineering lead may do a lot of it. In an enterprise, regulated industry, or complex domain, a dedicated BA can be extremely valuable.

The BA role is especially useful when:

- there are many stakeholders
- requirements need traceability
- business rules are complex
- compliance or audit matters
- process changes are bigger than the software change
- users and buyers are different people
- the team needs someone to model current and future state

So no, SDD does not remove BA work.

It just makes the work more visible.

![Roles in PRD to SDD](/assets/images/post/2026-05-19-prd-sdd-roles.svg){: .align-center}

## Can PM write SDD directly?

Sometimes, yes.

For small features, I think a PM can write the first version of the SDD directly:

```text
requirements.md
acceptance criteria
non-goals
open questions
```

That may even be better than writing a separate PRD first. If the PRD is only one page and the SDD captures the same product intent more clearly, duplicating both documents is waste.

But I would draw a line:

```text
PM can own the "what" and "why."
Engineer should co-own the "how."
QA should co-own the "how we verify."
BA, when present, should help with clarity, traceability, and business rules.
```

If a PM writes API design, database schema, and task breakdown alone, that is risky. Not because PMs cannot be technical, but because the SDD becomes real implementation pressure. Technical decisions need technical review.

## My simple team workflow

If I were applying this tomorrow, I would not introduce a big process. I would use one folder per feature:

```text
specs/
  invoice-export/
    prd.md
    requirements.md
    design.md
    tasks.md
```

For a very small team, I might merge `prd.md` and `requirements.md`:

```text
specs/
  invoice-export/
    spec.md
    design.md
    tasks.md
```

Then I would use this workflow:

1. PM writes the first product spec.
2. BA or PM clarifies business rules and edge cases.
3. Engineer adds design options and risks.
4. QA adds acceptance checks.
5. Team reviews open questions before implementation.
6. AI agent or engineer implements task by task.
7. Any behavior change updates the spec, not only the code.

This is simple enough to use without special tools.

Tools like GitHub Spec Kit or Kiro can help, but the habit matters more than the tool.

## A small checklist

Before engineering starts, I would check:

```text
Can we explain the user problem in one paragraph?
Are requirements testable?
Are non-goals listed?
Are edge cases visible?
Are open questions assigned to someone?
Does design explain the main technical trade-offs?
Does every task trace back to a requirement?
Do we know how to verify the feature?
```

If the answer is no, I would slow down.

Not for bureaucracy. For speed.

Going slower before implementation often makes the implementation faster.

## What AI changes

AI makes this more important, not less.

Without SDD, an AI agent can produce a lot of code from a vague PRD. That feels fast until the team needs to review, debug, and align it with real product behavior.

With SDD, the agent gets better context:

```text
Here are the requirements.
Here are the non-goals.
Here is the design.
Here is the task.
Implement only this task.
Explain which requirement your change satisfies.
```

That is much safer than:

```text
Build invoice export.
```

The first prompt gives the agent a contract. The second gives it room to invent.

## My conclusion

PRD and SDD do not need to fight each other.

The PRD is useful when product discovery is still happening: who is the user, what problem matters, why now, what does success mean?

The SDD is useful when the team is getting ready to build: what exactly must happen, how will it fit the system, what are the risks, what tasks should be done, and how will we verify it?

BA is still valuable when the domain is complex. PM can write the first spec when the feature is small. Engineers should co-own the SDD before implementation.

The real goal is not more documents.

The goal is fewer hidden assumptions.

## Sources

- [GitHub Spec Kit documentation](https://github.github.io/spec-kit/)
- [GitHub Spec Kit: Specification-Driven Development](https://github.com/github/spec-kit/blob/main/spec-driven.md)
- [Microsoft for Developers: Diving Into Spec-Driven Development With GitHub Spec Kit](https://developer.microsoft.com/blog/spec-driven-development-spec-kit)
- [Kiro docs: Specs](https://kiro.dev/docs/specs/)
- [IIBA: Introducing Business Analysis Tasks](https://www.iiba.org/knowledgehub/business-analysis-standard/4-tasks-and-knowledge-areas/introducing-business-analysis-tasks/)
- [Jama Software: Product Requirements Document Guide](https://www.jamasoftware.com/requirements-management-guide/writing-requirements/product-requirements-document/)
- [Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants](https://arxiv.org/abs/2602.00180)
