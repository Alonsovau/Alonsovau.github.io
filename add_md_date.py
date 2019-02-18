import os
import time
import shutil


target_path = './target/'
if os.path.exists(target_path):
    shutil.rmtree(target_path)
os.mkdir(target_path)

for i in os.listdir('./resource'):
    md_header = '''---
author: "Xin Zhou"
date: $$DATE
linktitle: $$TITLE
title: $$TITLE
weight: 10
tags: [
    "linux"
]
categories: [
    "Linux"
]
---'''

    md_file = os.path.join('./resource', i)
    md_time = os.path.getmtime(md_file)
    md_time = time.localtime(md_time)
    md_time = time.strftime('%Y-%m-%d', md_time)

    md_header = md_header.replace('$$DATE', md_time)\
        .replace('$$TITLE', i.replace('.md', ''))
    # print(md_header)

    with open(md_file) as f:
        with open(target_path+i, 'w') as fw:
            fw.write(md_header+'\n'.join(f.readlines()))

