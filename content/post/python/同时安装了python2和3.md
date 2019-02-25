---
author: "Xin Zhou"
date: 2017-08-30
linktitle: 同时安装了python2和3
title: 同时安装了python2和3
weight: 10
tags: [
    "python"
]
categories: [
    "Python"
]
---
1. py -2 hello.py (Windows)

2. py -3 hello.py (Windows)

3. 文件开头加入:

    > #! python2
    
    > #! python3

4. pip

    ```bash

    py -2 -m pip install xxx

    py -3 -m pip install xxx

    ```

5. mac:

    ```py

    #!/usr/bin/env python3

    ```