#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

# @Project: hello
# @File   : file.py
# @Time   : 2018/11/25 下午4:47
# @Author : Wang xin
"""
from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')


# 打印当前路径下的所有文件
def cwd(filepath):

    for f in os.listdir(filepath):
        fsize = os.path.getsize(f)
        mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
        f_d = os.path.join(filepath, f)
        if os.path.isdir(f_d):
            cwd(f_d)
        else:
            print('%10d  %s  %s' % (fsize, mtime, f_d))

cwd(pwd)
