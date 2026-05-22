---
title: "Superpowers and Spec Kit: Can They Work Together?"
categories:
  - Software-Development
tags:
  - ai
  - superpowers
  - spec-kit
  - software engineering
---

I spent some time reading [obra/superpowers](https://github.com/obra/superpowers) and comparing it with [github/spec-kit](https://github.com/github/spec-kit). At first they look similar because both are about making AI coding agents more disciplined.

But after reading the docs, I think they sit at different layers.

```text
Spec Kit helps define the work.
Superpowers helps the agent do the work.
```

That is the simplest way I can explain it.

![Superpowers and Spec Kit layers](/assets/images/post/2026-05-22-superpowers-vs-spec-kit-layers.svg){: .align-center}

## What Superpowers is

Superpowers describes itself as an agentic skills framework and software development methodology for coding agents. It works across several agent harnesses, including Claude Code, Codex CLI, Codex App, Factory Droid, Gemini CLI, OpenCode, Cursor, and GitHub Copilot CLI.

The interesting part is not only installation. The interesting part is the behavior it tries to enforce.

Instead of letting the agent jump straight into code, Superpowers gives it skills such as:

- brainstorming
- using git worktrees
- writing plans
- executing plans
- subagent-driven development
- test-driven development
- requesting code review
- finishing a development branch
- systematic debugging
- verification before completion

The README says the basic workflow starts with brainstorming, moves to a design, then to an implementation plan, then to task execution with TDD and review.

That feels more like a coding discipline than a single tool.

![Superpowers workflow](/assets/images/post/2026-05-22-superpowers-workflow.svg){: .align-center}

## What Spec Kit is

Spec Kit is different.

Spec Kit is a toolkit for Spec-Driven Development. It helps turn an idea into artifacts:

- specification
- clarification
- checklist
- plan
- tasks
- analysis
- implementation

The commands look like:

```text
/speckit.specify
/speckit.clarify
/speckit.checklist
/speckit.plan
/speckit.tasks
/speckit.analyze
/speckit.implement
```

Spec Kit is strongest before implementation. It helps me make the problem explicit before asking an agent to code.

## The difference

Here is my mental model:

| Question | Spec Kit | Superpowers |
| --- | --- | --- |
| What problem does it solve? | Turns intent into spec, plan, and tasks | Makes the coding agent follow disciplined engineering habits |
| Main output | Markdown artifacts | Agent behavior and workflow |
| Best moment | Before implementation | During planning, implementation, review, and finishing |
| Strongest habit | Specification before coding | TDD, worktrees, subagents, code review |
| Risk if misused | Too many stale docs | Too much process for small changes |

So I would not say one replaces the other.

Spec Kit is more like the product and engineering contract.

Superpowers is more like the operating system for how the coding agent behaves.

## Can they be used together?

Yes, I think they can be used together.

But I would be careful.

The danger is duplicate planning. If Spec Kit creates a plan and tasks, and then Superpowers creates another independent plan and another task list, the agent may have two sources of truth.

That is where confusion starts.

My rule would be:

```text
Use Spec Kit to clarify the feature.
Use Superpowers to execute the approved plan.
Do not let both tools own the task list at the same time.
```

![Superpowers and Spec Kit together](/assets/images/post/2026-05-22-superpowers-spec-kit-together.svg){: .align-center}

## The simplest combined workflow

If I were trying them together, I would start small.

### 1. Use Spec Kit to define the feature

For example:

```text
/speckit.specify
Add a reading progress bar to blog posts.
It should show how far the reader is through the article.
It should work on mobile and desktop.
It should not track users or require backend changes.
```

Then I would run clarification, checklist, plan, tasks, and analyze.

The goal is to end up with a clear spec and one approved task list.

### 2. Read the artifacts myself

This is not optional.

Before implementation, I would read:

```text
spec.md
plan.md
tasks.md
```

I would check:

- are requirements testable?
- are non-goals written down?
- does the plan match the existing codebase?
- are tasks small enough?
- do tasks trace back to requirements?

If something feels vague, I would fix it before coding.

### 3. Use Superpowers for implementation discipline

After the Spec Kit artifacts are approved, I would let Superpowers help with:

- using a git worktree
- turning tasks into very small steps if needed
- enforcing TDD
- using subagents for independent tasks
- reviewing for spec compliance
- reviewing for code quality
- finishing the branch cleanly

This is where Superpowers shines. Its TDD skill is strict about red-green-refactor. Its subagent-driven development skill uses a fresh subagent per task and a two-stage review: spec compliance first, code quality second.

That maps nicely to a Spec Kit plan.

### 4. Update the spec if implementation changes reality

This is the boring part people skip.

If the implementation discovers something new, update the spec or plan. Otherwise the documents become decoration.

## When I would use only Spec Kit

I would use only Spec Kit when:

- I mainly need clearer requirements
- the implementation is small enough to do manually
- I want a lightweight spec and task list
- the team already has its own TDD and review habits

For example, a small blog feature may not need a full Superpowers workflow. Spec Kit alone might be enough.

## When I would use only Superpowers

I would use only Superpowers when:

- the requirement is already clear
- I want the agent to follow TDD
- I want worktree isolation
- I want stricter code review behavior
- the work is implementation-heavy

For example, if I already have a good issue or technical design, Superpowers can help the agent execute without drifting.

## When I would use both

I would use both when:

- the feature has unclear requirements
- implementation has several steps
- I want AI help but need more guardrails
- mistakes would be expensive
- the team wants reviewable artifacts and disciplined execution

The combined flow is useful for medium-sized features, not tiny edits.

## A practical example

Suppose I want to add a reading progress bar to this blog.

I would use Spec Kit to create:

```text
spec.md:
- show progress while reading
- no tracking
- mobile and desktop
- no backend changes

plan.md:
- add markup to post layout
- add CSS
- add small JavaScript scroll calculation
- no dependencies

tasks.md:
- add markup
- add styles
- add behavior
- test long and short posts
```

Then I would use Superpowers to implement:

```text
Create a worktree.
Write failing tests or verification steps first.
Implement one task at a time.
Review against the spec.
Review code quality.
Finish the branch only after verification.
```

That is a good split.

Spec Kit says what we are building.

Superpowers keeps the agent honest while building it.

## My warning

Both tools add process.

That process is valuable only if it removes confusion. If the process becomes bigger than the feature, I would stop.

For a typo, I need neither tool.

For a small refactor, maybe Superpowers TDD is enough.

For a new product feature, maybe Spec Kit is enough.

For a medium feature with real behavior and risk, both together make sense.

## My conclusion

I like both tools, but for different reasons.

Spec Kit is good at turning vague intent into explicit artifacts.

Superpowers is good at making the agent behave more like a disciplined engineering team: design first, plan carefully, test first, review, verify, and finish cleanly.

If I combine them, I would keep the rule simple:

```text
Spec Kit owns the feature definition.
Superpowers owns the implementation discipline.
Human review owns the final judgment.
```

That balance feels practical.

## Sources

- [obra/superpowers repository](https://github.com/obra/superpowers)
- [Superpowers skills directory](https://github.com/obra/superpowers/tree/main/skills)
- [Superpowers brainstorming skill](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md)
- [Superpowers writing-plans skill](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md)
- [Superpowers test-driven-development skill](https://github.com/obra/superpowers/blob/main/skills/test-driven-development/SKILL.md)
- [Superpowers subagent-driven-development skill](https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md)
- [GitHub Spec Kit repository](https://github.com/github/spec-kit)
- [GitHub Spec Kit documentation](https://github.github.io/spec-kit/)
