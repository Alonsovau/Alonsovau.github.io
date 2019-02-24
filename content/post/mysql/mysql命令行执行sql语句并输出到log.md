---
author: "Xin Zhou"
date: 2018-07-24
linktitle: mysql命令行执行sql语句并输出到log
title: mysql命令行执行sql语句并输出到log
weight: 10
tags: [
    "linux", "mysql"
]
categories: [
    "Mysql"
]
---

```bash
mysql -uroot -p -f -h172.28.10.83 -P3382 pms_db < Log.sql_2018-07-24_08-59.sql > t.log 2>&1

```
