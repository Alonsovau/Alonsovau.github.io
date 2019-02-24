---
author: "Xin Zhou"
date: 2017-04-11
linktitle: truncate,delete,drop
title: truncate,delete,drop
weight: 10
tags: [
    "database"
]
categories: [
    "Database"
]
---
##### 总体

- delete：DML语言、可以回退、可以有条件的删除 

- truncate：DDL语言、无法回退、默认所有的表内容都删除、删除速度比delete快、表结构及其列、约束、索引等均保持不变、truncate不记录在日志中，所以不能激活触发器。

- drop：DDL语言、操作立即生效,原数据不放到rollback segment中,不能回滚. 操作不触发trigger  

##### 对比

1. DELETE语句每删除一行，都在事务日志中为所删除的每行记录一项；TRUNCATE TABLE通过释放存储表数据所用的数据页来删除数据，并且只事务日志中记录页的释放。

2. 对于由 FOREIGN KEY 约束引用的表，不能使用 TRUNCATE TABLE，而应使用不带 Where 子句的 Delete 语句。由于 TRUNCATE TABLE 不记录在日志中，所以它不能激活触发器。 

3. TRUNCATE TABLE 不能用于参与了索引视图的表。  

4. truncate和 delete只删除数据不删除表的结构(定义)，drop语句将删除表的结构被依赖的约束(constrain),触发器(trigger),索引(index);依赖于该表的存储过程/函数将保留,但是变为invalid状态. 

5. delete语句是dml,这个操作会放到rollback segement中,事务提交之后才生效;如果有相应的trigger,执行的时候将被触发. truncate,drop是ddl, 操作立即生效,原数据不放到rollback segment中,不能回滚. 操作不触发trigger. 

6. delete语句不影响表所占用的extent, 高水线(high water mark)保持原位置不动，显然drop语句将表所占用的空间全部释放，truncate语句缺省情况下将空间释放到minextents个extent,除非使用reuse storage;truncate会将高水线复位(回到最开始). 

7. 速度,一般来说: drop> truncate >  delete 

8. 安全性:小心使用drop 和truncate,尤其没有备份的时候.否则哭都来不及 