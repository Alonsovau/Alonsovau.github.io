---
author: "Xin Zhou"
date: 2018-11-07
linktitle: core文件
title: core文件
weight: 10
tags: [
    "linux", "cpp"
]
categories: [
    "Linux"
]
---

```bash

1.ulimit -c unlimited

2./proc/sys/kernel/core_pattern  

2.或者/etc/sysctl.conf中添加kernel.core_pattern=core_%e_%p或sysctl -w kernel.core_pattern=core_%e_%p

3.查看/etc/security/limits.conf

*      soft     core         unlimited //所有用户

<user-login-id>      soft     core         unlimited //设置某个用户

还有hard core需要考虑

```

```bash
$sysctl -a|grep core_pattern
```

kernel.core_pattern = |/usr/libexec/abrt-hook-ccpp /var/cache/abrt %p %s %u %c


“abrtd” creates a sub-directory (named something like “ccpp-1279914365-14618”) in the directory “/var/cache/abrt” as shown in the value of the variable. This also means that the core files will also be stored in that sub-directory in the “/var/cache/abrt” directory (in addition to the current directory where application was run). ABRT daemon also creates other files in addition to the core dump files in the sub-directory to further help users in debugging the crash issue.


By default, “abrtd” created core dump files only for those executable (or packages) that are managed by “rpm” (red hat package manager) utility. To enable “abrtd” for non-rpm application (something you compiled locally and are not managed through rpm), you need to edit the file cat “/etc/abrt/abrt.conf” , and change the value of the field “ProcessUnpackaged” to “yes” as follows:


ProcessUnpackaged = no   #(before editing the file)


ProcessUnpackaged = yes  #(after editing the file)
