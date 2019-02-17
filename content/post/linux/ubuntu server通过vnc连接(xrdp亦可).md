---
author: "Xin Zhou"
date: 2017-04-09
linktitle: ubuntu server通过vnc连接(xrdp亦可)
title: ubuntu server通过vnc连接(xrdp亦可)
weight: 10
tags: [
    "linux"
]
categories: [
    "Linux"
]
---
1.安装

```bash
apt-get install vnc4server
```

2.设置密码

```bash
vncpasswd
```

或者

```bash
vncserver
```

创建一个

3.启动vnc

```bash
vncserver:1
```

4.启动vnc客户端

输入IP地址加:1,例如192.168.1.104:1

5.配置文件

进入/root/.vnc

```bash
vi xstartup

#!/bin/sh


# Uncomment the following two lines for normal desktop:

# unset SESSION_MANAGER

# exec /etc/X11/xinit/xinitrc


[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup   

[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources   

xsetroot -solid grey

vncconfig -iconic &

#x-terminal-emulator -geometry 80x24+10+10 -ls -title "$VNCDESKTOP Desktop" &

#x-window-manager &


sesion-manager & xfdesktop & xfce4-panel &

xfce4-menu-plugin &

xfsettingsd &

xfconfd &

xfwm4 &  

```

6.重新启动vnc

```bash

vncserver -kill :1   

Killing Xvnc4 process ID 1844   

vncserver :1   

```

7.调整vnc分辨率



```bash

vncserver :1 -geometry 1280*720

```


