---
author: "Xin Zhou"
date: 2018-02-23
linktitle: Decode HTML entities
title: Decode HTML entities
weight: 10
tags: [
    "python", "html"
]
categories: [
    "Python"
]
---
#### Python3.4+

```py
import html

print(html.unescape('&pound;682m'))

```

#### Python2.6-3.3

```py
from html.parser import HTMLParser

h = HTMLParser()

print(h.unescape('&pound;682m'))

```

[link](https://stackoverflow.com/questions/2087370/decode-html-entities-in-python-string)