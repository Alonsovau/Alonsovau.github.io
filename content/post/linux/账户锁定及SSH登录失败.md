---
author: "Xin Zhou"
date: 2018-09-20
linktitle: 账户锁定及SSH登录失败
title: 账户锁定及SSH登录失败
weight: 10
tags: [
    "linux"
]
categories: [
    "Linux"
]
---
#### 1. Pam_Tally2解锁SSH登录失败锁定

```bash

路径: /etc/pam.d/password-auth，/etc/pam.d/system-auth

A pluggable authentication module (PAM) is a mechanism to integrate multiple low-level authentication schemes into a high-level application programming interface (API)

Example: 

auth     required       pam_tally2.so deny=4 even_deny_root unlock_time=1200

```

- deny  指定最大几次认证错误，如果超出此错误，将执行后面的策略。如锁定N秒，如果后面没有其他策略指定时，默认永远锁定，除非手动解锁

- lock_time  锁定多长时间，按秒为单位

- unlock_time 指定认证被锁后，多长时间自动解锁用户

- even_deny_root root用户在认证出错时，一样被锁定


#### 2. 查看状态与解锁

```bash

pam_tally2 --user oracle

pam_tally2 --user oracle --reset

```

#### 3. Linux锁定账号

1. 禁止个别用户登录(su可切换)

    ```bash

    passwd -l test

    passwd -u test

    ```

2. 修改shell类型禁止登录(su切换不可)

    ```bash

    cat /etc/passwd |grep zx

    锁定：

    sed -i 's#/home/zx:/bin/bash#/home/zx:/sbin/nologin#g' /etc/passwd

    等价于：

    usermod zx -s /sbin/nologin

    解锁：

    sed -i 's#/home/zx:/sbin/nologin#/home/zx:/bin/bash#g' /etc/passwd

    等价于：

    usermod zx -s /bin/bash

    ```

3. 禁止其他用户登录(su可切换)

    ```bash

    touch /etc/nologin

    除root以外的用户不能登录，nologin文件中可写入提示信息

    rm -f /etc/nologin

    删除文件即可解锁所有账户

    ```

4. 使用usermod(su可切换)

    ```bash

    usermod -L zx

    usermod -U zx

    ```

#### 4. 参考

1. [Pam参考](http://www.361way.com/pam-tally2/4277.html)

2. [锁定账户参考](https://www.cnblogs.com/kevingrace/p/6109818.html)
