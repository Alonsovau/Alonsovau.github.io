---
author: "Xin Zhou"
date: 2017-05-08
linktitle: 杂项
title: 杂项
weight: 10
tags: [
    "oracle"
]
categories: [
    "Oracle"
]
---
select text from all_source where type='TRIGGER' AND name='TR_XXX';

关键字： 

:NEW 和:OLD使用方法和意义，new 只出现在insert和update时，old只出现在update和delete时。在insert时new表示新插入的行数据，update时new表示要替换的新数据、old表示要被更改的原来的数据行，delete时old表示要被删除的数据。 

ORA-08002: 序列 sequence226 尚未在此会话中定义创建Sequence后直接查询它的当前值（CURRVAL）会出错，要先调用Sequence对象.NEXTVAL，才能查询当前值