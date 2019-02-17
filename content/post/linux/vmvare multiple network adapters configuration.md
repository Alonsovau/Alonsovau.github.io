---
author: "Xin Zhou"
date: 2019-02-13
linktitle: vmvare multiple network adapters configuration
title: vmvare multiple network adapters configuration
weight: 10
tags: [
    "linux"
]
categories: [
    "Linux"
]
---
#### 1. add second adapter to virtual machine

#### 2. find out network device name, here is ens33 and ens38

```bash
ip a

2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000

    link/ether 00:0c:29:53:2f:a9 brd ff:ff:ff:ff:ff:ff

    inet 192.168.1.150/24 brd 192.168.1.255 scope global dynamic ens33

       valid_lft 27719sec preferred_lft 27719sec

    inet6 fe80::20c:29ff:fe53:2fa9/64 scope link 

       valid_lft forever preferred_lft forever

3: ens38: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000

    link/ether 00:0c:29:53:2f:b3 brd ff:ff:ff:ff:ff:ff

```

#### 3. configure for ens38

My server is Ubuntu 18.04

```yaml

sudo vim /etc/netplan/50-cloud-init.yaml

network:

    ethernets:

        ens33:

            addresses: []

            dhcp4: true

            optional: true

        ens38:

            addresses: []

            dhcp4: true

            optional: true

    version: 2

```



#### 4. apply the new configuration



```bash

sudo netplan apply

```


