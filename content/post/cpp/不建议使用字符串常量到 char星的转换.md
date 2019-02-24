---
author: "Xin Zhou"
date: 2018-09-27
linktitle: 不建议使用字符串常量到 char*的转换
title: 不建议使用字符串常量到 char*的转换
weight: 10
tags: [
    "cpp"
]
categories: [
    "CPP"
]
---

```cpp

不建议使用字符串常量到 char*的转换

char* p = "test";

声明了一个指针，而这个指针指向的是全局的const内存区，如果你一定要写这块内存的话，那就是一个非常严重的内存错误

在声明字符串字面量时，应该加上const.

const char *p = "test";

```
