---
author: "Xin Zhou"
date: 2018-02-23
linktitle: crontab
title: crontab
weight: 10
tags: [
    "linux"
]
categories: [
    "Linux"
]
---
### 1. 用法：

```bash

1.cat /etc/crontab 系统级

2./etc/cron.deny 所列用户不允许使用

3./etc/cron.allow 所列用户允许使用

4./var/spool/cron/ 下存储以用户名存储的文件

5.minute hour day month week command

6.crontab [-u user] -l 显示当前用户任务

7.crontab -l > z 备份当前用户的任务到z文件

8.crontab [-u user] -e 编辑当前用户的任务

9.crontab [-u user] -r 删除

10.crontab <filename> 从文件恢复

11.service crond start/stop/restart/reload

```

### 2. 例子：

```bash

* * * * * command

每分钟执行

3,15 * * * * command

每小时第3，15分钟执行

3,15 8-11 */2 * * command

每2天的8-11点的第3，15分钟执行

30 21 * * 0,6 command

每周日、周六21:30分执行

* */2 * * * command

每2小时执行

```


