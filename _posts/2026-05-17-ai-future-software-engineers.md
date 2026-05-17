---
title: "What AI Changes About Being a Software Engineer"
categories:
  - Software-Development
tags:
  - ai
  - software engineering
  - future of work
  - engineering
---

I spent some time reading reports and studies about AI in software engineering, because the internet answer is usually too loud in both directions.

One side says software engineers are basically finished. The other side says nothing important will change. I do not believe either one.

My current view is simpler: AI will probably write a lot more code in the next 5-10 years, but that does not mean software engineering disappears. It means the center of the job moves. Less time typing obvious code. More time deciding what should exist, checking whether it is correct, and keeping systems understandable after the speed goes up.

![AI-assisted software engineering loop](/assets/images/post/2026-05-17-ai-engineer-loop.svg){: .align-center}

## The evidence is mixed, which is the point

The strongest optimistic data is real.

Microsoft Research published a controlled GitHub Copilot experiment in 2023 where developers using Copilot completed a JavaScript task 55.8% faster than the control group. GitHub's Octoverse 2025 report also shows software activity growing quickly: more than 180 million developers on GitHub, more than 36 million new developers in one year, and nearly 1 billion commits in 2025.

Stanford's 2026 AI Index makes the capability curve look even steeper. It says performance on SWE-bench Verified, a coding benchmark, rose from around 60% to near 100% in a single year. It also notes that agents improved sharply on real-computer task benchmarks, while still failing often enough that we should not confuse benchmark progress with dependable autonomy.

So yes, AI is getting better.

But the cautious data is also real.

Stack Overflow's 2025 Developer Survey says positive sentiment toward AI tools fell to about 60%, and more developers distrust AI output accuracy than trust it. Their survey also says 52% of developers report a positive productivity effect, but most respondents are not "vibe coding" as part of professional work.

The most useful cold shower for me was METR's 2025 study on experienced open-source developers. In that randomized trial, developers working on mature codebases they already knew took 19% longer when using early-2025 AI tools. That does not prove AI is bad. It proves the context matters. On familiar, complex systems, reviewing and correcting almost-right output can cost more time than writing the change yourself.

DORA's 2025 report has the cleanest framing: AI is an amplifier. It magnifies the system around it. Good engineering habits get stronger. Weak process, weak tests, unclear ownership, and poor documentation get exposed faster.

That feels right.

## My 5-10 year guess

I do not think the next decade is "AI replaces engineers." I think it is "AI changes the shape of engineering teams."

Small tasks will become increasingly automated. A well-described bug, a migration with clear rules, a test suite expansion, a simple UI state, a documentation update, a mechanical refactor: these are exactly the kinds of work agents will keep eating.

The engineer's job moves toward the edges of the task:

- choosing the right problem
- giving the agent enough context
- reading the diff like a maintainer
- checking behavior with tests and production signals
- deciding when the generated solution is too clever, too fragile, or simply wrong

That is not glamorous, but it is engineering.

![How software engineering work shifts over time](/assets/images/post/2026-05-17-ai-engineer-shift.svg){: .align-center}

## Code gets cheaper; judgment gets more expensive

Software teams used to be constrained by code production. A feature took time because someone had to write every branch, type every model, and wire every screen.

AI changes that. Code becomes cheaper.

But when code is cheap, the bottleneck moves somewhere else. The expensive parts become:

- knowing what users actually need
- understanding old systems
- designing stable interfaces
- protecting data
- proving correctness
- keeping latency, cost, and reliability under control
- explaining trade-offs to other humans

I think this is where many people get the future wrong. They look at code generation and conclude that engineering skill is less valuable. I think the opposite may happen. When code generation becomes abundant, the person who can say "this is the right code" becomes more valuable.

## The trust gap

AI can produce code faster than most teams can review it.

That creates what I think of as verification debt. The code exists, the pull request looks plausible, the tests maybe pass, but nobody really understands the consequences yet.

![AI productivity and trust gap](/assets/images/post/2026-05-17-ai-engineer-trust-gap.svg){: .align-center}

This is why I do not trust simple productivity metrics like "lines of code generated" or "number of pull requests opened." More code is not always more progress. Sometimes it is just more surface area for bugs.

The teams that benefit most from AI will probably be the teams that make verification scale:

- fast tests
- strong type systems
- small pull requests
- clear ownership
- observability
- good rollback paths
- secure development practices
- readable architecture notes

Without those, AI can make the mess arrive faster.

## What happens to junior engineers?

This is the part I worry about most.

Junior engineers traditionally learn by doing small tasks: fixing bugs, adding simple endpoints, writing tests, reading code reviews, and slowly building taste. If AI absorbs too much of that work, teams might accidentally remove the training path.

The mistake would be treating junior engineers as slower versions of AI agents.

They are not. They are future senior engineers.

Companies will need to design better learning loops: pairing juniors with AI but still requiring them to explain the code, trace failures, write tests, and review generated diffs. If we skip that, we may get short-term speed and long-term weakness.

I think the best junior engineers in the next decade will be the ones who learn to use AI without outsourcing their thinking to it.

## What skills become stronger moats?

If I were planning my next 5 years as a software engineer, I would still write code. But I would deliberately invest in the things AI is bad at or cannot own.

First: codebase literacy. The ability to walk into a large system and understand where behavior lives, why the ugly parts are ugly, and what will break if we touch them.

Second: testing and verification. Not just writing tests, but knowing what should be tested, what can be mocked, what must run end-to-end, and what production signal tells us the truth.

Third: system design. Interfaces, data models, failure modes, queues, migrations, rollbacks, security boundaries. These decisions age slowly and hurt for a long time when they are wrong.

Fourth: product judgment. AI can generate options. It does not know which trade-off fits the business, the user, the team, and the timeline unless a human frames the problem well.

Fifth: communication. More generated code means more need for clear design docs, concise review comments, and shared context. A confusing engineer with powerful AI tools can still create confusing systems.

## My practical workflow

For real work, I would use AI more like a fast teammate than an oracle.

I would ask it to:

- explore unfamiliar APIs
- draft tests
- explain code paths
- propose refactors
- generate boring glue code
- compare implementation options
- find edge cases I missed

But I would keep ownership of:

- final architecture
- security-sensitive code
- data migrations
- production behavior
- public APIs
- anything that changes money, privacy, permissions, or availability

The boundary is not "AI writes, human reviews." That is too shallow.

The better boundary is: AI can help create candidates, but humans stay responsible for intent and consequence.

## So, will AI replace software engineers?

Some tasks, yes.

Some roles, probably.

The whole profession, I doubt it.

The U.S. Bureau of Labor Statistics still projects software developers, QA analysts, and testers to grow 15% from 2024 to 2034, which is much faster than average. Forecasts can be wrong, but it is a useful reminder: society is not running out of software demand. If anything, AI may create more software ideas than teams can safely maintain.

What changes is the bar.

The engineer who only knows how to translate tickets into code will feel more pressure. The engineer who can understand systems, guide agents, verify output, and make product-aware technical decisions will still matter.

Maybe more than before.

## Final thought

AI makes software feel more fluid. Ideas can become prototypes quickly. Refactors that once felt too boring to start can become possible. Learning a new codebase can be less lonely.

But software is still a promise we make to users. It should keep working after the demo. It should protect data. It should fail safely. It should be understandable enough for the next engineer to change it.

In the next 5-10 years, I think the best software engineers will not be the ones who avoid AI. They also will not be the ones who blindly trust it.

They will be the ones who can make AI useful without letting it lower their standards.

## Sources

- [Stanford HAI: The 2026 AI Index Report](https://hai.stanford.edu/ai-index/2026-ai-index-report)
- [DORA: State of AI-assisted Software Development 2025](https://dora.dev/research/2025/dora-report/)
- [Stack Overflow: 2025 Developer Survey, AI](https://survey.stackoverflow.co/2025/ai)
- [GitHub Octoverse 2025](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/)
- [Microsoft Research: The Impact of AI on Developer Productivity](https://www.microsoft.com/en-us/research/publication/the-impact-of-ai-on-developer-productivity-evidence-from-github-copilot/)
- [METR: Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
- [U.S. Bureau of Labor Statistics: Software Developers, Quality Assurance Analysts, and Testers](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm)
