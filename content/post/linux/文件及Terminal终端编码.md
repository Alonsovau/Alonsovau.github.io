---
author: "Xin Zhou"
date: 2018-06-16
linktitle: 文件及Terminal终端编码
title: 文件及Terminal终端编码
weight: 10
tags: [
    "linux"
]
categories: [
    "Linux"
]
---

```bash

1. set fileencoding 查看文件编码

2. set fileencdding=utf-8 设置文件编码 按wq保存

3. :e ++enc=cp936 

# vim打开文档后，encoding=utf-8（locale决定的），fileencoding=latin1（自动编码判断机制不准导致的），termencoding=空（默认无需转换term编码），显示文件为乱码

```
