---
author: "Xin Zhou"
date: 2018-11-20
linktitle: 根据进程名kill
title: 根据进程名kill
weight: 10
tags: [
    "linux"
]
categories: [
    "Linux"
]
---

```shell

#!/bin/sh

if [ $# -lt 1 ]

then

    echo Usage:xx

    exit 1

fi

NAME=$1

echo $1

PID=`ps -ef|grep $NAME$ |grep -v $0 |awk '{print $2}'`

echo $PID

kill -9 $PID

echo killed

```
