#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/30 11:08
# @Author : xurq
# @Site : 
# @File : conftest.py
# @Software: PyCharm


import pytest

# scope参数有function级别，class级别，module级别（整个模块只执行一次，也就是每人.py文件，跟setup_module和teardown_module一样）,
# session级别(整个执行过程的session域里可用，整个测试目录不管有多少个测试文件只执行一次)，如果不传默认是function级别
# autouse=True 在每个function级别自动调用
# fixtrue传参
@pytest.fixture(scope='module',params=['user1','user2','user3'])
def login(request):
    print("登录方法")
    print(request.param)
    # yield激活fixture的teardown方法
    yield ['username','password']
    print('teardown')




