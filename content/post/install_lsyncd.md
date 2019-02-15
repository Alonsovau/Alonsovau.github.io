---
author: "Xin Zhou"
date: 2019-02-14
linktitle: 安装lsyncd
title: 安装lsyncd
weight: 10
---

### 1. install Lua5.2  

### 2. install rsync-3.1  

### 3. install lsyncd-2.1.6 2.2.3版本在readhat7.1编译失败  

```bash
cmake -DCMAKE_C_FLAGS=-ldl .
make
make install
```

[参考github](https://github.com/axkibe/lsyncd/issues/511)

PS: example文件夹下有配置文件

```lua
setting{
    statusFile="/tmp/lsyncd.stat",
    statusInterval = 1,
    logfile="/var/log/lsyncd-status.log",
}

sync{
    default.rsyncssh,
    source="/root/zx",
    targetdir="/root/zx",
    exclude={'*.csv', '*.log', 'build', 'nbproject'},
    host="172.30.241.210",
    delay=2,
    rsync = {
        archive=true,
        compress=false,
        whole_file=false,
    },
    ssh = {
        port=22,
        --identityFile="/root/.ssh/id_rsa.pub",
        binary="/usr/bin/ssh",
    },
}

sync{
    default.rsyncssh,
    source="/root/zx",
    targetdir="/cffex/zx",
    exclude={'*.swx', '*.swp', '*.csv', '*.log', 'build', 'nbproject'},
    host="zhx@172.31.197.10",
    delay=2,
    rsync = {
        --rsh="/usr/bin/ssh -l zhx -i /root/.ssh/id_rsa",
        archive=true,
        compress=false,
        whole_file=false,
    },
    ssh = {
        port=22,
        --identityFile="/root/.ssh/id_rsa.pub",
        binary="/usr/bin/ssh",
    },
}

```

### 4. 配置ssh使用公钥登录

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub user@server
```

### 5. 启动

```bash
lsyncd zx.lua -nodaemon
# -nodaemon输出log在控制台
```
