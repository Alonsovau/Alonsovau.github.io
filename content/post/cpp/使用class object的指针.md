---
author: "Xin Zhou"
date: 2018-02-23
linktitle: 使用class object的指针
title: 使用class object的指针
weight: 10
tags: [
    "cpp"
]
categories: [
    "CPP"
]
---
使用class object的指针略有不同，这是因为class object链接到一组我们可以调用(invoke)的操作行为(operations)，举例来说检查fibnacci vector的第二个元素是否为1，我们可能会这么写：

```cpp

if (!fibonacci.empty() && (fibonacci[1] == 1))

```

上例中的fibonacci和empty()两字之间的逗号，称为dot成员选择运算符(member selection operator)，用来选择想要施行的操作，如果要通过指针来指针来选择操作行为，必须改用arrow成员选择运算符：  

由于指针可能未指向任何对象，所以先校验pv是否为非零值

```cpp

if (pv && pv->empty() && ((*pv)[1] == 1))

```
