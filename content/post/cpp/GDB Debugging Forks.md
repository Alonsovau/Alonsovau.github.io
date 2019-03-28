---
author: "Xin Zhou"
date: 2019-03-27
linktitle: GDB Debugging Forks
title: GDB Debugging Forks
weight: 10
tags: [
    "linux", "cpp"
]
categories: [
    "CPP"
]
---

```gdb
show follow-fork-mode
Debugger response to a program call of fork or vfork is "parent".
```

```gdb
set follow-fork-mode mode

parent
The original process is debugged after a fork. The child process runs unimpeded. This is the default.

child
The new process is debugged after a fork. The parent process runs unimpeded.

```

```gdb

show detach-on-fork

Whether gdb will detach the child of a fork is on.

```

```gdb
set detach-on-fork mode

on
The child process (or parent process, depending on the value of follow-fork-mode) will be detached and allowed to run independently. This is the default.

off
Both processes will be held under the control of GDB. One process (child or parent, depending on the value of follow-fork-mode) is debugged as usual, while the other is held suspended.

```

follow-fork-mode | detach-on-fork | result
-------- | -------- | --------
parent | on | debug parent process
child | on | debug first child process
parent | off | after fork() all child processes will be blocked, parent |process will continue, the inferior will on parent proces
child | off | after fork() first child process will be created, parent process will be bolcked on fork(), the inferior will on child process, when switch to parent process and continue running fork(), another child process will be created

<br/>

```gdb

info inferiors
  Num   Description     Executable
  1     process 17027   exe1
* 2     process 17028   exe1

inferior 1
[Switching to inferior 1 .......
```

[4.11 Debugging Forks](https://sourceware.org/gdb/onlinedocs/gdb/Forks.html)
