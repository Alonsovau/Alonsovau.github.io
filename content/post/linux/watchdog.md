---
author: "Xin Zhou"
date: 2018-12-13
linktitle: watchdog
title: watchdog
weight: 10
tags: [
    "linux"
]
categories: [
    "Linux"
]
---- The Linux kernel watchdog is used to monitor if a system is running. It is supposed to automatically reboot hanged systems due to unrecoverable software errors. The watchdog module is specific to the hardware or chip being used. Personal computer users don’t need watchdog as they can reset the system manually. However, it is useful for systems that are mission critical and need the ability to reboot themselves without human intervention. For example, servers on a remote location or embedded equipment on a spacecraft that need automatic hardware reset capabilities.

- https://linuxhint.com/linux-kernel-watchdog-explained/

- https://access.redhat.com/documentation/en-us/red_hat_virtualization/4.1/html/virtual_machine_management_guide/sect-configuring_a_watchdog

- http://www.fit-pc.com/wiki/index.php/Linux_Mint:_Watchdog_configuration