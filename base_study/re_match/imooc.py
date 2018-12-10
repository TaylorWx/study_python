#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

# @Project: hello
# @File   : imooc.py
# @Time   : 2018/12/10 下午12:32
# @Author : Wang xin
"""

import re
str = "[nn]"

# 匹配有效的python变量名，以下划线打头或者是字母大头
print re.match(r'[_a-zA-Z]+[_\w]*',str)
# 匹配0-99
print re.match(r'[1-9]?[\d]','09').group()
# 匹配以imooc开头
print re.match(r'\Aimmoc[\w]+','immoc')

print re.match(r'\[[\w]\]',str)