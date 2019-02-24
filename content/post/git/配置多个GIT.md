---
author: "Xin Zhou"
date: 2018-07-09
linktitle: 配置多个GIT
title: 配置多个GIT
weight: 10
tags: [
    "git"
]
categories: [
    "Git"
]
---
1. .ssh文件夹下建立config文件：

    ```conf

    # 84

    Host 172.28.10.84

    HostName 172.28.10.84

    PreferredAuthentications publickey

    IdentityFile ~/.ssh/id_rsa_84

    ```

2. 执行ssh-agent让ssh识别新的私钥

    ```bash

    ssh-add ~/.ssh/id_rsa_84

    该命令如果报错：Could not open a connection to your authentication agent.无法连接到ssh agent，可执行ssh-agent bash命令后再执行ssh-add命令

    ```
