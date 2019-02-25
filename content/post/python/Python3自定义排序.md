---
author: "Xin Zhou"
date: 2018-02-23
linktitle: Python3自定义排序
title: Python3自定义排序
weight: 10
tags: [
    "python"
]
categories: [
    "Python"
]
---
#### 1. 笨方法，不推荐

```py

a = ['星期一', '星期三', '星期二', '星期日']

c = {'星期一': 1, '星期二': 2, '星期三': 3, '星期四': 4, '星期五': 5, '星期六': 6, '星期日': 7}

b = {}

for i in a:

    b[i] = c[i]

b = sorted(b.items(), key=lambda t: t[1])

# b = sorted(zip(b.values(), b.keys()))

# 使用zip下面改为j[1]

a = []

for j in b:

    day = j[0]

    a.append(day)

print(a)

```

#### 2. 自定义大小关系

> python3中取消comparison function，使用key function，cmp_to_key帮助cmp过渡为key

```py

def compare_day(day1, day2):

    c = {'星期一': 1, '星期二': 2, '星期三': 3, '星期四': 4, '星期五': 5, '星期六': 6, '星期日': 7}

    value1 = c[day1]

    value2 = c[day2]

    if value1 > value2:

        return 1

    if value1 < value2:

        return -1

    return 0



a = ['星期一', '星期三', '星期二', '星期日']

from functools import cmp_to_key

a.sort(key=cmp_to_key(compare_day))

print(a)

```

#### 3. key访问外部资源(好)

```py

a = ['星期一', '星期三', '星期二', '星期日']

c = {'星期一': 1, '星期二': 2, '星期三': 3, '星期四': 4, '星期五': 5, '星期六': 6, '星期日': 7}

print(sorted(a, key=c.__getitem__))

```

#### 4. 排序稳定性

> reverse参数保持稳定性，效果可以通过reversed函数2次调用实现

```py

data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]

from operator import itemgetter

standard_way = sorted(data, key=itemgetter(0), reverse=True)

double_resvered = list(reversed(sorted(reversed(data), key=itemgetter(0))))

assert standard_way == double_resvered

print(standard_way)

print(double_resvered)

```

[参考链接](https://docs.python.org/3/howto/sorting.html#sortinghowto)