---
author: "Xin Zhou"
date: 2017-08-04
linktitle: root账户远程登录
title: root账户远程登录
weight: 10
tags: [
    "mysql"
]
categories: [
    "Mysql"
]
---

1. 关闭windows防火墙或者在入站规则添加3306端口

2. 执行

    ```sql

    GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'root' WITH GRANT OPTION;

    ```

3. 修改root@%此用户的密码
