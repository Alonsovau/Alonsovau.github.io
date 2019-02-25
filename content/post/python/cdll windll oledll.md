---
author: "Xin Zhou"
date: 2018-03-16
linktitle: cdll windll oledll
title: cdll windll oledll
weight: 10
tags: [
    "python", "dll"
]
categories: [
    "Python"
]
---
cdll

windll

oledll

它们的不同之处在于：动态链接库中的函数所遵守的函数调用方式（calling convention）以及返回方式有所不同。

cdll用于加载遵循cdecl调用约定的动态链接库，windll用于加载遵循stdcall调用约定的动态链接库，oledll与windll完全相同，只是会默认其载入的函数统一返回一个Windows HRESULT错误编码。