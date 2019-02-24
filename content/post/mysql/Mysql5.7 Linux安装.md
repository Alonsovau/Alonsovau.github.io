---
author: "Xin Zhou"
date: 2018-05-24
linktitle: Mysql5.7 Linux安装
title: Mysql5.7 Linux安装
weight: 10
tags: [
    "linux", "mysql"
]
categories: [
    "Mysql"
]
---

```bash
rpm -ivh mysql-community-common-5.7.22-1.el7.x86_64.rpm mysql-community-libs-5.7.22-1.el7.x86_64.rpm

rpm -ivh mysql-community-client-5.7.22-1.el7.x86_64.rpm  mysql-community-server-5.7.22-1.el7.x86_64.rpm

mysqld --user=mysql --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data/  --initialize

service mysqld start

grep 'temporary password' /var/log/mysqld.log

mysql -uroot -p

ALTER USER 'root'@'localhost' IDENTIFIED BY 'cffEx2016!';

GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'cffEx2016!' WITH GRANT OPTION;

拷贝my.cnf到/etc/目录下

my.cnf 权限为-rw-r--r--

重启mysql

```
