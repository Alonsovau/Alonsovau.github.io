---
author: "Xin Zhou"
date: 2018-10-15
linktitle: netbeans修改默认编码
title: netbeans修改默认编码
weight: 10
tags: [
    "ide"
]
categories: [
    "CPP"
]
---
1. 项目级别，修改项目属性

2. 整体IDE,修改etc/netbeans.conf,-J-Dfile.encoding=UTF-8

```conf
netbeans_default_options="-J-client -J-Xss2m -J-Xms32m -J-XX:PermSize=32m -J-XX:MaxPermSize=200m -J-Dapple.laf.useScreenMenuBar=true -J-Dapple.awt.graphics.UseQuartz=true -J-Dsun.java2d.noddraw=true -J-Dfile.encoding=UTF-8"
```
