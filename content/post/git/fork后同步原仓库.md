---
author: "Xin Zhou"
date: 2018-11-20
linktitle: fork后同步原仓库
title: fork后同步原仓库
weight: 10
tags: [
    "git"
]
categories: [
    "Git"
]
---
#### configuring a remote for a fork

- 查看远程状态

```bash

git remote -v

# origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)

# origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)

```

- 添加一个将被同步给 fork 远程的上游仓库

```bash

git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git

```

- 再次查看远程状态

```bash

git remote -v

# origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)

# origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)

# upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (fetch)

# upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (push)

```

#### syncing a fork

- 从原仓库fetch数据到本地，并会被存储在本地分支upstream/master

```bash

git fetch upstream

# remote: Counting objects: 75, done.

# remote: Compressing objects: 100% (53/53), done.

# remote: Total 62 (delta 27), reused 44 (delta 9)

# Unpacking objects: 100% (62/62), done.

# From https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY

#  * [new branch]      master     -> upstream/master

```

- 切换本地分支（如果不存在的话）

```bash

git checkout master

```

- 把upstream/master分支合并到本地分支上

```bash
git merge upstream/master

# Updating a422352..5fdff0f

# Fast-forward

#  README                    |    9 -------

#  README.md                 |    7 ++++++

#  2 files changed, 7 insertions(+), 9 deletions(-)

#  delete mode 100644 README

#  create mode 100644 README.md

```

- 更新到自己fork的仓库上

```bash

git push origin master

```