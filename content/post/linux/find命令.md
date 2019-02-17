---
author: "Xin Zhou"
date: 2017-03-31
linktitle: find命令
title: find命令
weight: 10
tags: [
    "linux"
]
categories: [
    "Linux"
]
---##### find命令

1. find (路径) -name 文件名

2. find -name '\*ora*' 查找包含ora的文件目录

3. find -perm 755 查找权限为755的文件

4. find -user root 查找owner为root的文件

5. find -group root 查找组为root的文件

6. find -mtime -5 更改时间5天内 +5 5天以前

7. find -newer myfile2 查找新于myfile2的文件

8. find -type d  查找类型为文件夹的文件

9. find -size +1k 查找大于1k的文件

10. find -type f -exec ls {} \\;  **注意{}后有空格**

11. find -ipath <范本样式>     此参数的效果和指定“-path”参数类似，但忽略字符大小写的差别,指定字符串作为寻找目录的范本样式

12. find -maxdepth 2 -type f  最大深度为2的文件

13. find -minddepth 2 -type f 最小深度

14. find -type f -name "*.txt" -delete 删除.txt文件

15. find -type f -name ".php" ! -perm 644  权限不是644的php文件

16. find -type f -user root -exec chown zx {} \\;

17. find -name "*.txt" -ok rm {} \\;  -ok和-exec行为一样，不过会给出提示，是否执行相应的操作

18. find -type f -name "*.txt" -exec cat {} \\;> all.txt  当前目录下所有.txt文件把他们拼接起来写入all.txt文件中

19. find -type f -mtime +30 -name ".log" -exec cp {} \\ old\\;  将30天前的log移动到old目录中



- -type类型参数列表

    - f 普通文件

    - l 符号链接

    - d 目录

    - c 字符设备

    - b 块设备

    - s 套接字

    - p fifo



[参考链接](http://man.linuxde.net/find)