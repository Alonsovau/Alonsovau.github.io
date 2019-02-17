---
author: "Xin Zhou"
date: 2018-11-29
linktitle: 查询缺少的so由什么提供
title: 查询缺少的so由什么提供
weight: 10
tags: [
    "linux", "shell"
]
categories: [
    "Linux"
]
---

```bash

$ yum list name 可以看包版本

$ yum provides libselinux.so.1

libselinux-2.0.94-5.3.el6.i686 : SELinux library and simple utilities

Repo        : local

Matched from:

Other       : libselinux.so.1

```
