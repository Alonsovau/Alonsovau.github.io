---
author: "Xin Zhou"
date: 2018-10-26
linktitle: 使用dict实现switch类似功能
title: 使用dict实现switch类似功能
weight: 10
tags: [
    "python", "dict"
]
categories: [
    "Python"
]
---

```py
switch_dict = {

    'char': lambda x: 'i am char' + x,

    'double': lambda x: 'i am double' + x,

    'int': lambda x: 'i am int' + x

}



print(switch_dict['char']('999'))

```
