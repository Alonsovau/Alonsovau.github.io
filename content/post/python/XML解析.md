---
author: "Xin Zhou"
date: 2018-02-23
linktitle: XML解析
title: XML解析
weight: 10
tags: [
    "python", "xml", "lxml"
]
categories: [
    "Python"
]
---
### XML

```py

# document.xml为docx文件中的

from xml.etree.ElementTree import parse

from xml.etree.ElementTree import XMLParser

f = open('document.xml')

doc = parse(f, XMLParser(encoding="utf-8"))

# 1

t_elems = doc.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')

# 2

ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

t_elems = doc.findall('.//w:t', ns)

# 3

t_elems = doc.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')

for elem in t_elems:

    print(elem.text)

```

### LXML

```py

from lxml import etree

f = open('document.xml')

doc_lxml = etree.parse(f, etree.XMLParser(encoding="utf-8"))

# 1

p_lxml = doc_lxml.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')

# 2

ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

find_results = doc_lxml.findall('//w:t', ns)

# Namespace prefix->URI mapping known in the context of this Element. This includes all namespace declarations of the parents.

# Note that changing the returned dict has no effect on the Element.

print(doc_lxml.getroot().nsmap)

```
