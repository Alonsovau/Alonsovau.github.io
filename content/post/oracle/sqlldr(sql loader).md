---
author: "Xin Zhou"
date: 2017-04-12
linktitle: sqlldr(sql loader)
title: sqlldr(sql loader)
weight: 10
tags: [
    "oracle"
]
categories: [
    "Oracle"
]
---

```bash
sqlldr userid=system/oracle@172.31.198.121/orabiz control=d:\student.ctl log=d:\log\student.log bad=d:\bad\student.bad skip=1

```

- control--控制文件名

- log--日志文件名

- bad--错误文件名

- discard--废弃文件名

- discardmax--允许废弃的文件的数目

- skip--要跳过的逻辑记录的数目（默认0）

- load--要加载的逻辑记录的数目（默认全部）

- errors--允许的错误的数目

- rows--常规路径绑定数组中或直接路径保存数据间的行数 (默认:常规路径 64, 所有直接路径)

- bindsize--常规路径绑定数组的大小，以字节计，默认256000

- silent-- 运行过程中隐藏消息 (标题,反馈,错误,废弃,分区)

- direct-- 使用直接路径                     (默认 FALSE)

- parfile-- 参数文件: 包含参数说明的文件的名称

- parallel-- 执行并行加载                    (默认 FALSE)

- file-- 要从以下对象中分配区的文件     

- skip\_unusable_indexes-- 不允许/允许使用无用的索引或索引分区  (默认 FALSE)

- skip\_index_maintenance-- 没有维护索引, 将受到影响的索引标记为无用  (默认 FALSE)

- commit_discontinued-- 提交加载中断时已加载的行(默认 FALSE)

- readsize-- 读取缓冲区的大小(默认 1048576)

- external\_table-- 使用外部表进行加载; NOT\_USED, GENERATE\_ONLY, EXECUTE  (默认 NOT_USED)

- columnarrayrows-- 直接路径列数组的行数  (默认 5000)

- streamsize-- 直接路径流缓冲区的大小 (以字节计)  (默认 256000)

- multithreading-- 在直接路径中使用多线程

- resumable-- 启用或禁用当前的可恢复会话  (默认 FALSE)

- resumable_name -- 有助于标识可恢复语句的文本字符串

- resumable_timeout-- RESUMABLE 的等待时间 (以秒计)  (默认 7200)

- date_cache-- 日期转换高速缓存的大小 (以条目计)  (默认 1000)

- no\_index_errors-- 出现任何索引错误时中止加载  (默认 FALSE)

```bash
OPTIONS (skip=1,load=128) -- sqlldr 命令显示的选项可以写到这里边来,skip=1 用来跳过数据中的第一行

LOAD DATA

INFILE 'users_data.csv' --指定外部数据文件，可以写多个 INFILE "another_data_file.csv" 指定多个数据文件

--这里还可以使用 BADFILE、DISCARDFILE 来指定坏数据和丢弃数据的文件，

truncate 

--truncate

--insert：需要插入的表数据为空，insert为默认选项；

--append：在表中增加数据，此时用户必须拥有对表的select权限；

--replace：删除原有数据导入新数据，表必须在schema下，或者有删除权限

INTO TABLE users -- 要插入记录的表

Fields terminated by ',' -- 数据中每行记录用 ',' 分隔

Optionally enclosed by '"' -- 数据中每个字段用 '"' 框起，比如字段中有 "," 分隔符时

trailing nullcols --表的字段没有对应的值时允许为空

(

  user_id number, --字段可以指定类型，否则认为是 CHARACTER类型, log 文件中有显示

  user_name,

  login_times,

  last_login DATE "YYYY-MM-DD HH24:MI:SS" -- 指定接受日期的格式，相当用 to_date() 函数转换

)

```

[SQL\*Loader Field List Reference](https://docs.oracle.com/cloud/latest/db112/SUTIL/ldr_field_list.htm#SUTIL1152)  

[SQL\*Loader Control File Reference](http://docs.oracle.com/cd/B19306_01/server.102/b14215/ldr_control_file.htm)  

[SQL\*Loader Command-Line Reference](https://docs.oracle.com/cd/B19306_01/server.102/b14215/ldr_params.htm)
