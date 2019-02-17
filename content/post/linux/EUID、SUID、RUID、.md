---
author: "Xin Zhou"
date: 2017-03-31
linktitle: EUID、SUID、RUID、
title: EUID、SUID、RUID、
weight: 10
tags: [
    "linux"
]
categories: [
    "Linux"
]
---有效用户ID（Effective UID，即EUID）与有效用户组ID（Effective Group ID，即EGID）在创建与访问文件的时候发挥作用；具体来说，创建文件时，系统内核将根据创建文件的进程的EUID与EGID设定文件的所有者/组属性，而在访问文件时，内核亦根据访问进程的EUID与EGID决定其能否访问文件。



真实用户ID（Real UID,即RUID）与真实用户组ID（Real GID，即RGID）用于辨识进程的真正所有者，且会影响到进程发送信号的权限。没有超级用户权限的进程仅在其RUID与目标进程的RUID相匹配时才能向目标进程发送信号，例如在父子进程间，子进程从父进程处继承了认证信息，使得父子进程间可以互相发送信号。



暂存用户ID（Saved UID，即SUID）于以提升权限运行的进程暂时需要做一些不需特权的操作时使用，这种情况下进程会暂时将自己的有效用户ID从特权用户（常为root）对应的UID变为某个非特权用户对应的UID，而后将原有的特权用户UID复制为SUID暂存；之后当进程完成不需特权的操作后，进程使用SUID的值重置EUID以重新获得特权。在这里需要说明的是，无特权进程的EUID值只能设为与RUID、SUID与EUID（也即不改变）之一相同的值。



文件系统用户ID（File System UID，即FSUID）在Linux中使用，且只用于对文件系统的访问权限控制，在没有明确设定的情况下与EUID相同（若FSUID为root的UID，则SUID、RUID与EUID必至少有一亦为root的UID），且EUID改变也会影响到FSUID。设立FSUID是为了允许程序（如NFS服务器）在不需获取向给定UID账户发送信号的情况下以给定UID的权限来限定自己的文件系统权限。
