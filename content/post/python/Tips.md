---
author: "Xin Zhou"
date: 2018-11-06
linktitle: Tips
title: Tips
weight: 10
tags: [
    "python"
]
categories: [
    "Python"
]
---
1. 并不是所有的装饰器都使用了@wraps，因此这里的方案并不全部适用。特别的，内置的装饰器@staticmethod和@classmethod就没有遵循这个约定(它们把原始函数存储在属性__func__中)

2. dis模块反编译