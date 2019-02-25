---
author: "Xin Zhou"
date: 2017-08-16
linktitle: failed with error code 1
title: failed with error code 1
weight: 10
tags: [
    "python"
]
categories: [
    "Python"
]
---
command "python setup.py egg_info" failed with error code 1 in ...  

解决方法：

```bash
pip install distribute

```