---
author: "Xin Zhou"
date: 2018-11-29
linktitle: 查询RPM包信息
title: 查询RPM包信息
weight: 10
tags: [
    "linux", "shell"
]
categories: [
    "Linux"
]
---

```bash

# 查询文件属于哪个安装包

$ rpm -qf /usr/bin/ldd

# 查询某个目录、文件、模块是由哪个包提供

$ rpm -q --whatprovides /usr/bin

# 查询被哪个包需要

$ rpm -q --whatrequires /usr/bin/lynx 

# 查询包中文件

$ rpm -qpl filename

# 查询已安装文件

$ rpm -ql name

# 查询配置文件

$ rpm -qpc filename

$ rpm -qc name

# 查询所有信息

$ rpm -qpil filename

$ rpm -qil name

```
