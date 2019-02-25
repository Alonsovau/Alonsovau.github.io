---
author: "Xin Zhou"
date: 2018-12-21
linktitle: csv文件操作
title: csv文件操作
weight: 10
tags: [
    "python"
]
categories: [
    "Python"
]
---

```py
    with open('./old/zce_l1.csv') as f:

        f_csv = csv.reader(f)

        headers = next(f_csv)

        print(headers)

        Row = namedtuple('Row', headers)

        for r in f_csv:

            row = Row(*r)

            print(row.TradingDay)

```
