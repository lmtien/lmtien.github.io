---
title: "Good Git commit message"
categories:
  - Software-Development
tags:
  - backend
---

As a developer, I believe most of us used to make commits in git. Sometime you may be wondering on how to write a good git commit message? This is an important topic for most of us, but nobody teaches us in the school.

In fact, there is no right or wrong answer for this question. However, in 1 project, each developer write the commit message in their own way, the git history will not be beautiful anymore. Moreover, it will be very difficult and time consuming if we need to find a commit few months ago, and it doesn't follow any standard or format.
![image-center](/assets/images/post/2019-04-11-git-commit.png){: .align-center}

These are few issues that I can think of:
- You read the commit message, but still don't know its purposes.
- You need to summarize code changes when releasing after development (Changelog).
- Pick the correct version v1.0.0, v1.0.1, v1.1.0 or v2.0.0…? avoid headache when seeing lots of commits.
- Search easier by using regex.

You may have been using some personal rules for your project to solve those problems. But what if you need to work on other project? Are there any common rules that we can follow?

## Conventional Commits

The [Conventional Commits](https://www.conventionalcommits.org/) specification is a lightweight convention on top of commit messages. It provides an easy set of rules for creating an explicit commit history; which makes it easier to write automated tools on top of. This convention dovetails with [SemVer](http://semver.org/), by describing the features, fixes, and breaking changes made in commit messages.

Git Conventional Commits is being used in many repository, especially open source projects where thousand developers contribute together. You can check out some project on github, for example [Electron](https://github.com/electron/electron/commits/master) or [Athens](https://github.com/athensresearch/athens/commits/master)
![image-center](/assets/images/post/2019-04-11-electron-commit.png){: .align-center}

## Commit Message structure
The commit message should be structured as follows:
```
<type>[optional scope]: <description>

[optional body]

[optional footer]
```

- `type` and `description` are mandatory in commit message.
- `type` for categorizing a commit such as feature, fix bug, refactor, etc.
- `scope` also for categorizing a commit, but to answer the question: *"what does this commit refactor/fix?"*. For example: `feat(authentication):`, `fix(parser):`, etc.
- `description` is a short summary on what will be changed in the commit.
- `body` is a longer explanation and details of the commit, in case the short description can describe the purpose clearly.
- `BREAKING CHANGE` at the beginning of its optional body or footer section introduces a breaking API change (correlating with MAJOR in semantic versioning). A BREAKING CHANGE can be part of commits of any type.
- `footer` other information such as ticket-id, link to other pull request, issue-id, etc. and you need to follow the conventional rule as well.

### Common `type`

| Type     | Meaning                                                                        |
|----------|--------------------------------------------------------------------------------|
| feat     | Add a new feature                                                              |
| fix      | Fix bug for the system                                                         |
| refactor | Changing code, but not adding new feature or fixing bug                        |
| chore    | Some minor changes                                                             |
| docs     | Add / Modify document                                                          |
| style    | Changing the code format, style or appearance, but not changing the code logic |
| perf     | Improving / optimizing the performance                                         |
| vendor   | Update version for dependencies or packages                                    |

### Examples

Commit message with description and breaking change in body
```
feat: allow provided config object to extend other configs

BREAKING CHANGE: `extends` key in config file is now used for extending other config files
```

Commit message with optional ! to draw attention to breaking change
```
chore!: drop Node 6 from testing matrix

BREAKING CHANGE: dropping Node 6 which hits end of life in April
```

Commit message with no body
```
docs: correct spelling of CHANGELOG
```

Commit message with scope
```
feat(lang): add polish language
```
```
fix(player): uiza player can not initialize
```

Commit message for a fix using an (optional) issue number.
```
fix: correct minor typos in code

see the issue for details on the typos fixed

closes issue #12
```

## The seven rules of a great Git commit message
1. Separate subject from body with a blank line
2. Limit the subject line to 50 characters
3. Capitalize the subject line
4. Do not end the subject line with a period
5. Use the imperative mood in the subject line
6. Wrap the body at 72 characters
7. Use the body to explain what and why vs. how

For example:
```
Summarize changes in around 50 characters or less

More detailed explanatory text, if necessary. Wrap it to about 72
characters or so. In some contexts, the first line is treated as the
subject of the commit and the rest of the text as the body. The
blank line separating the summary from the body is critical (unless
you omit the body entirely); various tools like `log`, `shortlog`
and `rebase` can get confused if you run the two together.

Explain the problem that this commit is solving. Focus on why you
are making this change as opposed to how (the code explains that).
Are there side effects or other unintuitive consequences of this
change? Here's the place to explain them.

Further paragraphs come after blank lines.

 - Bullet points are okay, too

 - Typically a hyphen or asterisk is used for the bullet, preceded
   by a single space, with blank lines in between, but conventions
   vary here

If you use an issue tracker, put references to them at the bottom,
like this:

Resolves: #123
See also: #456, #789
```

> Inspirations, sources and further reading
>
> - [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
> - [Pro Git Book - Commit guidelines](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project#_commit_guidelines)
> - [A Note About Git Commit Messages](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
> - [Pro Git Book - Rewriting History](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History)