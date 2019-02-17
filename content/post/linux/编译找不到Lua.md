---
author: "Xin Zhou"
date: 2018-12-06
linktitle: 编译找不到Lua
title: 编译找不到Lua
weight: 10
tags: [
    "linux", "lua"
]
categories: [
    "Linux"
]
---

```bash

cmake . -DLUA_INCLUDE_DIR=/usr/local/include/ -DLUA_LIBRARY=/usr/local/lib/liblua.a

```
