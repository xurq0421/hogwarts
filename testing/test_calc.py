#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/27 14:35
# @Author : xurq
# @Site : 
# @File : test_calc.py
# @Software: PyCharm
import sys

import pytest

print(sys.path.append('..'))

from pythoncode.calc import Calculator

@pytest.mark.add
def test_add():
    cal = Calculator()
    assert 2 == cal.add(1,1)

@pytest.mark.add
def test_add1():
    cal = Calculator()
    assert 3 == cal.add(1,2)

@pytest.mark.div
def test_div():
    cal = Calculator()
    assert 1 == cal.div(2,2)





