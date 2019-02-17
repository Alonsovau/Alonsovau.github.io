---
author: "Xin Zhou"
date: 2018-02-23
linktitle: sed
title: sed
weight: 10
tags: [
    "linux"
]
categories: [
    "Linux"
]
---
#### 语法

```bash

sed [-hnV][-e<script>][-f<script文件>][文本文件]

```

#### 参数

```bash
-e<script>或--expression=<script> 以选项中指定的script来处理输入的文本文件

-f<script文件>或--file=<script文件> 以选项中指定的script文件来处理输入的文本文件

-h或--help 显示帮助

-n或--quiet或--silent 仅显示script处理后的结果

-V或--version 显示版本信息
```


#### 动作

- a: 新增，在匹配的下一行新增一行

- i: 插入，转匹配的上一行新增一行

- c: 取代，c后面是将替换的值

- d: 删除，删除指定行

- p: 打印，通常与sed -n一起使用

- s: 取代，进行搜索

 

#### 例子

- sed -e 4a\zx zx.txt：在第四行后面加zx，输出到标准输出，macOS语法错误

- nl zx.txt |sed '2,5d'：列出内容并列出行号，同时删除2-5行

- nl zx.txt |sed '2,$d'：删除2到最后一行

- nl zx.txt |sed '2a zx'：第二行后增加zx，行前使用2i,macOS不可

- nl zx.txt |sed '2a zx\按enter键xz'：第二行后加zx，xz2行数据，macOS不可

- nl zx.txt |sed '2,3c kol'：2到3行替换为kol

- nl zx.txt |sed -n '1,4p'：列出1-4行

- nl zx.txt |sed '/iu/p'：输出所有行，匹配的行会有2次输出

- nl zx.txt |sed -n '/iu/p'：输出匹配的行

- nl zx.txt |sed '/iu/d'：删除含iu行输出其他行

- nl zx.txt |sed -n '/iu/{s/iu/iuu/;p;q}'：找到对应行，替换后输出再退出，macOS不可

- sed 's/old/new/g'：替换

- ifconfig en0 |grep 'inet ' |sed 's/^.\*inet //g' |sed 's/ netmask.*$//g'：取出IP

- nl zx.txt |sed -e '6,$d' -e 's/iu/iuu/'：多点编辑，删除6到尾，并替换iu为iuu

- sed -i '$a hyojoo' zx.txt：修改文件内容

- sed -i 's/\\.$/\\!/g' zx.txt：每一行结尾为.替换为!

- sed -i 's/\r//'