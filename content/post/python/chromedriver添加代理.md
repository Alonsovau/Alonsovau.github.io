---
author: "Xin Zhou"
date: 2018-07-10
linktitle: chromedriver添加代理
title: chromedriver添加代理
weight: 10
tags: [
    "python", "chrome", "webdriver"
]
categories: [
    "Python"
]
---
```py

from selenium import webdriver

from selenium.webdriver.chrome.options import Options



chrome_options = Options()

chrome_options.add_argument("--headless")

chrome_options.add_argument("--no-sandbox")

chrome_options.add_argument("--proxy-server=socks5://127.0.0.1:1080")

driver = webdriver.Chrome(executable_path='/opt/chromedriver', chrome_options=chrome_options)

driver.get('http://pythonscraping.com')

```
