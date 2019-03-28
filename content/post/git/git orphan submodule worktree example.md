---
author: "Xin Zhou"
date: 2019-02-18
linktitle: git orphan submodule worktree example
title: git orphan submodule worktree example
weight: 10
tags: [
    "git"
]
categories: [
    "Git"
]
---
### Example 1
##### directories

```bash

$ ll -a

total 22

drwxr-xr-x 1 alons 197609    0 2月  18 19:56 ./

drwxr-xr-x 1 alons 197609    0 2月  18 19:53 ../

drwxr-xr-x 1 alons 197609    0 2月  18 20:04 .git/

-rw-r--r-- 1 alons 197609    7 2月  18 19:53 .gitignore

-rw-r--r-- 1 alons 197609  116 2月  18 19:53 .gitmodules

drwxr-xr-x 1 alons 197609    0 2月  18 19:53 archetypes/

-rw-r--r-- 1 alons 197609 2381 2月  18 19:53 config.toml

drwxr-xr-x 1 alons 197609    0 2月  18 20:03 content/

drwxr-xr-x 1 alons 197609    0 2月  18 19:56 public/

drwxr-xr-x 1 alons 197609    0 2月  18 19:56 resources/

drwxr-xr-x 1 alons 197609    0 2月  18 19:53 themes/

```



##### first init

```bash

echo "public" >> .gitignore

cd public

git init

echo "ss" > readme.txt

git add .

git commit -m "master init"

git remote add origin git@github.com:Alonsovau/tt.git

git push origin master -u



cd ..

git init

git checkout --orphan source

git add .

git commit -m "source init"

git remote add origin git@github.com:Alonsovau/tt.git

git push origin source

git submodule add https://github.com/Xzya/hugo-bootstrap.git themes/hugo-bootstrap

git commit -m "add theme"

git push origin source

```



##### others clone

```bash

git clone git@github.com:Alonsovau/tt.git

cd tt

git checkout source

git worktree add -B master public origin/master

cd themes/

git submodule init

git submodule update

```



### Example 2

```bash

git init

echo "public" >> .gitignore

git remote add origin git@github.com:Alonsovau/ttt.git

git add .

git commit -m "master init"

git push orgin master -u

git checkout --orphan source

git reset --hard

git commit --allow-empty -m "source init"

git push origin source

git checkout master

git worktree add -B source public origin/source

echo "ss" > public/readme.txt

cd public

git add .

git commit -m "readme"

git push origin source

```
