---
author: "Xin Zhou"
date: 2018-12-12
linktitle: 常用shell
title: 常用shell
weight: 10
tags: [
    "linux", "shell"
]
categories: [
    "Linux"
]
---

```sh

#得到当前脚本路径

script=`readlink -f $0`

base_dir=`dirname $script`



#循环该目录下所有文件

for exchange in `ls /target/sixreceiver -I mdloader`

do

done



#生成一个uuid

cat /proc/sys/kernel/random/uuid



#查找不区分大小写的name并拷贝指定目录

find . -iname *config.xml -exec cp '{}' ./zx/zx \;



#查看压缩包中文件

tar -vtf package.tar.gz



#shell函数

func() {

    

}





```
