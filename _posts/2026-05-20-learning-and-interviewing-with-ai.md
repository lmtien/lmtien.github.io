---
title: "How I Would Learn and Interview as a Software Engineer Now"
categories:
  - Software-Development
tags:
  - ai
  - interview
  - learning
  - software engineering
---

I spent some time reading about how developers are using AI and how hiring platforms are reacting to it. My simple conclusion is:

```text
AI changes how we practice.
AI changes what interviews should measure.
AI does not remove the need to understand software.
```

That last line is the important one.

The mistake is not using AI. The mistake is letting AI become the part of your brain that should be learning.

![AI-era learning loop](/assets/images/post/2026-05-20-ai-learning-loop.svg){: .align-center}

## What changed

AI tools are normal now.

HackerRank's 2025 Developer Skills Report says 97% of developers use AI assistants, and many developers use more than one tool. CodeSignal launched AI-assisted coding assessments and interviews in 2025, which means some hiring processes are starting to evaluate candidates with AI in the room instead of pretending AI does not exist.

At the same time, trust is still a problem. Stack Overflow's 2025 survey says more developers distrust the accuracy of AI tools than trust it, and only a small fraction highly trust the output.

That is the tension:

```text
Everyone uses AI.
Not everyone trusts AI.
Interviews need to test judgment, not just typing speed.
```

So if I were preparing for interviews now, I would not try to become "the person who never uses AI." That is unrealistic.

I would try to become "the person who can use AI without becoming careless."

## How I would learn now

I would split learning into two modes.

### Mode 1: AI as tutor

This is where AI is useful.

I would ask it to:

- explain a concept in simple words
- compare two approaches
- give small examples
- quiz me
- find edge cases
- review my solution
- suggest what to learn next

For example:

```text
Explain hash maps like I know arrays but not hashing.
Then give me three small exercises.
Do not show the answers until I try.
```

This is a good use of AI because it accelerates feedback.

### Mode 2: no-AI reps

This is where learning becomes real.

After I use AI to understand something, I need to solve a problem without it. No autocomplete. No chat. No hints.

Not forever. Just for the final rep.

If I cannot implement a binary search, explain a SQL index, debug a failing test, or design a small API without the tool, then I have not really learned it.

AI can help me climb the wall. It should not become the legs I stand on.

## What to study

I would not study only LeetCode.

Algorithms still matter, but modern interviews increasingly care about real-world engineering too. HackerRank's report says developers prefer practical coding challenges over theoretical tests, and CodeSignal's move toward AI-assisted interviews points in the same direction: companies want a stronger signal about how candidates work with tools, not only whether they memorized a trick.

My study list would be:

- data structures and algorithms
- debugging and reading existing code
- APIs and data modeling
- databases and indexes
- testing strategy
- system design basics
- security basics
- communication and trade-offs
- responsible AI tool use

That may sound like a lot, but it is just software engineering.

The difference now is that AI can make the shallow version easier. So I need to practice the deeper version on purpose.

## How I would use AI in interview prep

I would use AI like a coach:

```text
Act as an interviewer.
Give me one backend coding problem.
Do not give hints unless I ask.
After I answer, critique correctness, readability, tests, and edge cases.
```

Then I would do the same problem again manually.

I would also ask AI to attack my solution:

```text
Find edge cases that break this code.
Explain what tests I forgot.
Give me one simpler implementation if possible.
```

This helps because interviews are not only about writing the first solution. They are about improving it while someone is watching.

## How interviews should work now

I think interviews should be honest about AI.

Some companies will allow AI in the interview. Some will not. Both are fine if the rule is clear.

If AI is allowed, the interviewer should watch for:

- how the candidate frames the problem
- what the candidate asks the AI
- whether the candidate blindly accepts generated code
- whether the candidate can explain the final solution
- whether the candidate tests and debugs
- whether the candidate notices trade-offs

If AI is not allowed, the candidate should respect that. Using AI secretly is not clever. It is a trust problem.

That is the same as using any unauthorized help in an exam.

![Interview signals in the AI era](/assets/images/post/2026-05-20-ai-interview-map.svg){: .align-center}

## What I would show in an AI-allowed interview

If the interview allows AI, I would be very transparent.

I would say:

```text
I am going to ask the AI for edge cases, not for the full answer.
I will explain which suggestions I accept and reject.
```

Then I would keep ownership of the solution.

For example, if the AI gives me code, I would not just paste it. I would read it and say:

```text
This part handles the happy path.
But it misses empty input.
It also uses O(n^2), which may be too slow.
I will rewrite it with a map.
```

That is the signal I want to show: I can use the tool, but I am still the engineer.

## What I would show in a no-AI interview

If AI is not allowed, I would prepare the old way, but with a modern focus.

I would practice:

- explaining my thinking out loud
- writing clean code without autocomplete
- testing with examples
- finding edge cases
- simplifying after the first solution
- discussing time and space complexity
- asking clarifying questions

I would not try to memorize 300 problems.

I would rather deeply understand 50 patterns and be able to explain them under pressure.

## A simple 4-week plan

If I had one month to prepare, I would do this:

![Four-week AI-era practice plan](/assets/images/post/2026-05-20-ai-practice-plan.svg){: .align-center}

### Week 1: fundamentals

Review arrays, hash maps, stacks, queues, trees, graphs, sorting, and Big-O.

Use AI to explain weak spots. Then solve one problem per day without AI.

### Week 2: debugging and tests

Take small buggy programs and fix them.

Ask AI for edge cases after you write your own tests. The order matters. Your tests first, AI second.

### Week 3: system design basics

Practice designing small systems:

- URL shortener
- notification service
- file upload service
- search autocomplete
- order checkout flow

For each one, explain APIs, data model, bottlenecks, failure modes, and what you would monitor.

### Week 4: mock interviews

Use AI as the interviewer, then do a manual retry.

Record yourself explaining the solution. This feels awkward, but it works. Many interview failures are not knowledge failures. They are explanation failures.

## My interview rules

These are the rules I would follow:

```text
Ask whether AI is allowed.
If AI is allowed, use it openly.
If AI is not allowed, do not use it.
Do not paste code you cannot explain.
Always test generated code.
Always mention trade-offs.
Practice some reps without AI.
```

This is simple, but it builds trust.

## What I think interviewers should change

Interviewers should stop pretending AI does not exist.

They should ask questions like:

- How would you verify AI-generated code?
- What would make you reject this generated solution?
- Can you improve this code for readability?
- Can you write tests for this code?
- Can you debug this failing test?
- Can you explain the trade-off between these two designs?

These questions are better than "can you type a memorized solution quickly?"

Typing speed is less valuable now. Judgment is more valuable.

## Final thought

AI makes learning easier to start and easier to fake.

That is the danger.

If I use AI to explain, quiz, review, and challenge me, I learn faster. If I use AI to skip the struggle, I become weaker while feeling productive.

For interviews, I think the future belongs to engineers who can do both:

```text
Use AI well.
Think without it.
```

That is the balance I would train for.

## Sources

- [HackerRank 2025 Developer Skills Report](https://www.hackerrank.com/reports/developer-skills-report-2025)
- [Stack Overflow 2025 Developer Survey: AI](https://survey.stackoverflow.co/2025/ai)
- [CodeSignal launches AI-assisted coding assessments and interviews](https://codesignal.com/newsroom/press-releases/codesignal-launches-ai-assisted-coding-assessments-and-interviews-redefining-technical-hiring-in-the-ai-era/)
- [CodeSignal: Developers and AI Coding Assistant Trends](https://codesignal.com/report-developers-and-ai-coding-assistant-trends/)
- [Stack Overflow Blog: Closing the developer AI trust gap](https://stackoverflow.blog/2026/02/18/closing-the-developer-ai-trust-gap/)
