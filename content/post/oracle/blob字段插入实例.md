---
author: "Xin Zhou"
date: 2017-10-12
linktitle: blob字段插入实例
title: blob字段插入实例
weight: 10
tags: [
    "oracle"
]
categories: [
    "Oracle"
]
---
blob字段插入实例

```sql
create table blob_table(

  id number primary key,

  blob_cl blob not null

);

insert into blob_table values(1,to_blob('11111000011111'));

commit;

select * from blob_table;

update blob_table

set blob_cl=to_blob('110010000110011')

where id=1;

delete from blob_table where id=1;

commit;

```