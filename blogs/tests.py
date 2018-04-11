# -*- coding: utf-8 -*-

from django.http import HttpResponse
from blogs.models import Users, Garden
from django.test import TestCase

import unittest


# 添加用户
def AddUser():
    user = Users('nuoxiao')
    # user.name = 'nuoxiao'
    user.dateTime = '2018-03-31'
    user.save()

    return  True  # HttpResponse('<p>用户添加成功！</p>')

# 添加园子
def AddGarden():
    garden = Garden(name='神经园子')
    # garden.name = '神经园子'
    garden.introduce = '测试数据'
    garden.description = '添加数据是否通过'
    garden.author = Users.objects.get(name='nuoxiao')
    garden.dateTime = '2018-03-31'
    garden.save()

    return False  # HttpResponse('OK!')

class TestAdd(unittest.TestCase):
    def test_int(self):
        self.assertTrue(AddGarden())
    def test_add(self):
        self.assertFalse(AddUser())

if __name__ == '__main__':
    unittest.main()

