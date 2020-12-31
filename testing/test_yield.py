#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/29 15:58
# @Author : xurq
# @Site : 
# @File : test_yield.py
# @Software: PyCharm

# yield 生成器 暂停并记住上次执行的位置
def fun():
    for i in range(3):
        print('i=%d'%i)
        yield
        print('end')

f = fun()
next(f)





