#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

# @Project: hello
# @File   : picture.py
# @Time   : 2018/12/10 下午2:20
# @Author : Wang xin
"""
# 抓取网页信息，并且将图片信息保存在本地

import urllib2
import re

req = urllib2.urlopen('http://www.imooc.com/course/list')
buf = req.read()


info = re.findall(r'src=.+\.jpg', buf)
pic_urls=[]
for i in info:
    pic_url = "http:" + i[5:]
    pic_urls.append(pic_url)

# 得到所有的图片地址，然后进行下载和本地保存
i = 1
print len(pic_urls)
for url in pic_urls:
    f = open(str(i)+'.jpg', 'w')
    req = urllib2.urlopen(url)
    buf = req.read()
    f.write(buf)
    i += 1