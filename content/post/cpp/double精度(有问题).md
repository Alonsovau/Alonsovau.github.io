---
author: "Xin Zhou"
date: 2018-10-29
linktitle: double精度(有问题)
title: double精度(有问题)
weight: 10
tags: [
    "cpp"
]
categories: [
    "CPP"
]
---

> double小数前后加起来的有效数字只有16位，当给定的double有效数在16位以内转换为字符串不会丢失精度

Code:

```cpp

char precisionStr[100] = {0};

double precisionTest = 11.437565871234012;

sprintf(precisionStr, "%.20f", precisionTest);

cout << "precision----" << precisionStr << endl;

precisionTest = 119.437565871234012;

sprintf(precisionStr, "%.20f", precisionTest);

cout << "precision----" << precisionStr << endl;

```

Output:

```cpp

precision----11.43756587123401224915

precision----119.43756587123401402550

```
