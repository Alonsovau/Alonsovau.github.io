---
author: "Xin Zhou"
date: 2017-09-14
linktitle: Linux下安装python
title: Linux下安装python
weight: 10
tags: [
    "python"
]
categories: [
    "Python"
]
---
1. 下载tgz包

2. tar -zxvf python-x.x.x.tgz

3. cd Python-x.x.x

4. ./configure

5. make

6. make install

7. cd /usr/bin

8. rm -rf python

9. ln -s /usr/local/bin/python2.7 ./python