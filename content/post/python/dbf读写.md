---
author: "Xin Zhou"
date: 2018-02-23
linktitle: dbf读写
title: dbf读写
weight: 10
tags: [
    "python", "dbf"
]
categories: [
    "Linux"
]
---
1. 新建一个dbf并写入数据

    ```py
    import dbf

    table = dbf.Table('temptable', 'name C(30); age N(3,0); birth D')

    print(table.field_names)

    table.open()

    for datum in (('John Doe', 31, dbf.Date(1979, 9, 13)), ('Ethan Furman', 102, dbf.Date(1909, 4, 1)), 

                  ('Jane Smith', 57, dbf.Date(1954, 7, 2)), ('John Adams', 44, dbf.Date(1967, 1, 9)),):

        table.append(datum)

    for record in table:

        print(record)

    table.close()

    ```

2. 读取一个dbf并写入数据

    ```py
    table = dbf.Table('1.DBF')

    print(table.field_names)

    table.open()

    for data in (('1000', '10000001', '1', '1', '1', '1', '2', '1'), ):

        table.append(data)

    table.close()

    ```