---
author: "Xin Zhou"
date: 2017-03-31
linktitle: find -print -print0
title: find -print -print0
weight: 10
tags: [
    "linux"
]
categories: [
    "Linux"
]
---
#### -print

> True;  print the full file name on the standard output, followed by a newline.   If you are

              piping the output of find into another program and there is the faintest  possibility  that

              the  files  which  you are searching for might contain a newline, then you should seriously

              consider using the -print0 option instead of -print.  See the UNUSUAL FILENAMES section for

              information about how unusual characters in filenames are handled.

#### print0

>True;  print  the  full  file  name  on  the  standard output, followed by a null character

              (instead of the newline character that -print uses).  This allows file names  that  contain

              newlines or other types of white space to be correctly interpreted by programs that process

              the find output.  This option corresponds to the -0 option of xargs.
