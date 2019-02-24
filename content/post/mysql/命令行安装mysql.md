---
author: "Xin Zhou"
date: 2017-08-04
linktitle: 命令行安装mysql
title: 命令行安装mysql
weight: 10
tags: [
    "mysql"
]
categories: [
    "Mysql"
]
---
1. C:\Program Files\mysql目录下新建my.ini

    ```ini

    [mysql]

    default-character-set=utf8

    [mysqld]

    sql_mode='NO_AUTO_VALUE_ON_ZERO,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION,PIPES_AS_CONCAT,ANSI_QUOTES'

    port = 3306

    basedir=C:\Program Files\mysql

    datadir=C:\Program Files\mysql\data

    max_connections=200

    character-set-server=utf8

    default-storage-engine=INNODB

    ```

2. 进入C:\Program Files\mysql\bin

3. 执行mysqld --initialize-insecure （不设置root密码，建议使用）

4. 执行mysqld -install

5. 执行net start mysql

6. 执行mysql -u root -p，回车不输入密码即可进入

7. update mysql.user set authentication_string=PASSWORD('wasd123') whereUser='root';

8. 卸载：net stop mysql,执行mysqld --remove,删除data文件夹