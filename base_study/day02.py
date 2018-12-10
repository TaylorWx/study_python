#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum
import pdb

"""

# @Project: hello
# @File   : day02.py
# @Time   : 2018/11/25 上午9:54
# @Author : Wang xin
"""
class People(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):

        return 'People Object (name :^=%s)' % self.name


print (People("wangxin"))

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值


Month = Enum('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
print Month.Jan