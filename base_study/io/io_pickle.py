#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

# @Project: hello
# @File   : pickle.py
# @Time   : 2018/11/25 下午5:12
# @Author : Wang xin
"""
import pickle

d = dict(name='Bob', age=20, score=88)

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
f = open('dump.txt', 'rb')
d = pickle.load(f)
print d
f.close()
