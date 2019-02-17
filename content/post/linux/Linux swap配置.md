---
author: "Xin Zhou"
date: 2018-07-09
linktitle: Linux swap配置
title: Linux swap配置
weight: 10
tags: [
    "linux"
]
categories: [
    "Linux"
]
---
```sh

#查看swap比率

cat /proc/sys/vm/swappiness 

# open /etc/sysctl.conf as root. Then, change or add this line to the file

vm.swappiness = 10

# Reboot for the change to take effect.

# You can also change the value while your system is still running with

sysctl vm.swappiness=10

# You can also clear your swap by running swapoff -a and then swapon -a as root instead of rebooting to achieve the same effect.

swapoff -a

swapon -a

```
