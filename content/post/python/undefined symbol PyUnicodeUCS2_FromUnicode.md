---
author: "Xin Zhou"
date: 2018-02-23
linktitle: undefined symbol PyUnicodeUCS2_FromUnicode
title: undefined symbol PyUnicodeUCS2_FromUnicode
weight: 10
tags: [
    "python"
]
categories: [
    "Python"
]
---
```py
import sys

print(sys.maxunicode)

# 大于65535为UCS4，否则为UCS2

```

- python2.6.6 -- 1114111

- python2.7.10 -- 65535

- python2.7.13 -- 65535

- python3.5.2 -- 1114111

- UCS4为使用4字节Unicode编译扩展模块，UCS2为2字节Unicode，解决方法是使用对应的python版本编译