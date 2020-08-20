---
title: "Solution for git modifying unintended files"
categories:
  - Software-Development
tags:
  - backend
---

I'm using MacOS and when I need to work with a project in my company (a very big repo). After cloned it to my laptop, I checked out the develop branch. Immediately, I saw some files were being modified even though I haven't touched to them yet.

It showed some `ttf` files, and even a `java` file were modified. I have tried many different ways to “reset” those files
```
git reset --hard
```
or
```
git checkout -- .
```
but these command didn’t work.

![image-center](/assets/images/post/2020-08-20-git-modified-files.png){: .align-center}

Git automatically modified files unexpectedly after checking out. And I can’t discard these files from the commit.

## Initial Trying
Initially, I thought the issue was something with having a `core.autocrlf` that it can change EOL (end of lines) characters even for (binary) documents that should not be touched.

Thus, I tried
```
git config --global core.autocrlf false
```
and then cloned again the repo.
I also tried to add `.gitattributes` file for that.
However the problem was still insisted.

## Solution
After investigating, I found out the problem was because of the file system of MacOS, and we need to store the repo in a case sensitive disk format.

1. Open Disk Utilities
2. Click on + sign
3. Choose APFS (Case Sensitive)
4. Type any <<name>>
5. Click on size option
6. Put maybe 50 GB or even 10 GB is enough for both
7. Copy the repo or clone it again to /Volumes/<<name>>
8. Then you can `git stash` there (if needed)

This solution worked for me, I hope it will solve your similar issue as well.
