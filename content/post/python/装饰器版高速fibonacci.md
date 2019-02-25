---
author: "Xin Zhou"
date: 2018-11-12
linktitle: 装饰器版高速fibonacci
title: 装饰器版高速fibonacci
weight: 10
tags: [
    "python", "wrapper"
]
categories: [
    "Python"
]
---
##### @functools.lru_cache()此行为关键

```py

import time

from functools import wraps

import functools





def clock(func):

    @wraps(func)

    def clocked(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        elapsed = time.time() - start

        name = func.__name__

        args_list = []

        if args:

            args_list.append(','.join(repr(arg) for arg in args))

        if kwargs:

            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]

            args_list.append(','.join(pairs))

        args_str = ','.join(args_list)

        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, args_str, result))

        return result



    return clocked





@functools.lru_cache()

@clock

def fibonacci(n):

    if n < 2:

        return n

    return fibonacci(n-1) + fibonacci(n-2)





fibonacci(30)

```
