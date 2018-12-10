#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

# @Project: hello
# @File   : fucntion_programming.py
# @Time   : 2018/11/20 上午9:27
# @Author : Wang xin
"""
import functools


# 函数式编程，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！


def firstUpper(s):
    return s.title()


L = ['Adam', 'Lisa', 'Bart']
print map(firstUpper, L)
print sorted((1, 2, 4, 6, 8, 3, 2, 0))






def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wapper(*args, **kwargs):
            print("hello:%s", text, func.__name__)
            return func(*args, **kwargs)

        return wapper

    return decorator

@log('wangxin')
def now():
    print 'kk'

now()


class A:
    pass

class B:
    pass

class C(A, B):
    pass
