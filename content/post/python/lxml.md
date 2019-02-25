---
author: "Xin Zhou"
date: 2018-02-23
linktitle: lxml
title: lxml
weight: 10
tags: [
    "python", "lxml"
]
categories: [
    "Python"
]
---

```py
from lxml import etree

html = etree.HTML(resHtml, parser=etree.HTMLParser(encoding='utf-8'))

# 处理源文件的时候，由于没有指定编码，所以它使用了一个默认编码，从而导致和UTF-8冲突，产生乱码

# http://lxml.de/api/index.html

```
