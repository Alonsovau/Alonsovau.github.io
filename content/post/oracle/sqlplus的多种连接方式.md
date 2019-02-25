---
author: "Xin Zhou"
date: 2018-02-23
linktitle: sqlplus的多种连接方式
title: sqlplus的多种连接方式
weight: 10
tags: [
    "oracle"
]
categories: [
    "Oracle"
]
---
1. sqlplus / as sysdba

    > 操作系统认证，不需要数据库服务器启动listener，也不需要数据库服务器处于可用状态。比如我们想要启动数据库就可以用这种方式进入

2. sqlplus username/password

    > 连接本机数据库，不需要数据库服务器的listener进程，但是由于需要用户名密码的认证，因此需要数据库服务器处于可用状态才行

3. sqlplus username/password@orcl

    > 通过网络连接，这是需要数据库服务器的listener处于监听状态。此时建立一个连接的大致步骤如下

    a. 查询sqlnet.ora，看看名称的解析方式，默认是TNSNAME；

    b. 查询tnsnames.ora文件，从里边找orcl的记录，并且找到数据库服务器的主机名或者IP，端口和service_name；

    c. 如果服务器listener进程没有问题的话，建立与listener进程的连接；

    d. 根据不同的服务器模式如专用服务器模式或者共享服务器模式，listener采取接下去的动作。默认是专用服务器模式，没有问题的话客户端就连接上了数据库的server process。

4. sqlplus username/password@//host:port/sid

    > sqlplus system/oracle@//192.168.130.99:1521/orabiz