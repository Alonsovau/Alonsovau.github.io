---
author: "Xin Zhou"
date: 2019-02-13
linktitle: Linux和Windows换行
title: Linux和Windows换行
weight: 10
tags: [
    "linux"
]
categories: [
    "Linux"
]
---
- CRLF: Windows \r\n

- LF: Unix and OSX \n

- CR: Classic Mac \r

- Linux下查看格式：  

```bash
vi filename
:set ff 或者 :set fileformat
```

- 修改

```bash
- sed -i 's/\r//g' filename

- sed -i 's/^M//g' filename

- vi filename 然后 set ff=unix 保存
```

- PS:  

注意\^M在linux下写法,按^M是回车换行符,输入方法是按住CTRL+v,松开v,按m