#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

# @Project: hello
# @File   : day01.py
# @Time   : 2018/11/19 下午4:08
# @Author : Wang xin
"""
# python可以处理任意大小的整数、浮点数、字符串、布尔、空值
"""
列表、字段、元组
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数

"""
import os
from collections import Iterable

# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# name = raw_input()
print ord('A')
print chr(75)
print 'wangxin,%s' % 'mei'
print dir(abs)
print isinstance(90, Iterable)

print [x * x for x in range(1, 21)]
L = [1, 2, 3, 4, 5, 6, 7]
for i, j in enumerate(L):
    print i, j

print [i for i in os.listdir('../')]


# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while (n < max):
        yield b
        a, b = b, a + b
        n += 1


for i in fib(1):
    print i
"""
就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，
在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
"""
