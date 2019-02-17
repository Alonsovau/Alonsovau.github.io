---
author: "Xin Zhou"
date: 2018-07-20
linktitle: 查询Linux进程启动和运行时间
title: 查询Linux进程启动和运行时间
weight: 10
tags: [
    "linux", "shell"
]
categories: [
    "Linux"
]
---

```bash

ps -eo pid,start,etime,cmd |grep -v grep | grep ss

```
