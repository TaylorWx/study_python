#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

# @Project: hello
# @File   : re1.py
# @Time   : 2018/12/9 上午10:48
# @Author : Wang xin
"""
"""
字符串匹配规则：
1、用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符
2、\s可以匹配一个空格
"""
import re
# print re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
#
# print re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
# a = 'wand,ji?  dj sak'
# print re.split(',|\?|\s\s',a)
#
# b = 'wab<df>fjk<vv><dffd>dfjk'
# print re.split('\<.+\>',b)
# c = 'wangxi<df>sjk<vccv><cc>vv<sdgj>'
# re.findall('\<[^\>]+\>',c)

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')
# 无法识别连续的字符串
print 'a b   c'.split(' ')


str = 'a,b, c  d'

print re.split(r'[\s\,]+', str)

# 分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print m.groups()


# =============
# someone@gmail.com
# bill.gates@microsoft.com

# [a-z0-9A-Z]+[-|a-z0-9A-Z._]+@([a-z0-9A-Z]+(-[a-z0-9A-Z]+)?\\.)+[a-z]{2}$
str = 'bill.gates@microsoft.com'
if re.match(r'^[a-z0-9A-Z]+[-|a-z0-9A-Z._]+@([a-z0-9A-Z]+.)+[a-z]{2,}$', str) is not None:
    print 'OK'
else:
    print 'NO'