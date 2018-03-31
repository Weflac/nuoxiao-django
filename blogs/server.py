# -*- coding: utf-8 -*-
from django.http import HttpResponse
from blogs.models import Users, Garden, Blogs, Theme, Discuss


# 添加用户
def AddUser(request):
    user = Users()
    user.name = 'nuoxiao'
    user.dateTime = '2018-03-31'
    user.save()

    return  HttpResponse('<p>用户添加成功！</p>')

# 添加园子
def AddGarden(request):
    garden = Garden(name='神经园子')
    garden.name = '神经园子'
    garden.introduce = '测试数据'
    garden.description = '添加数据是否通过'
    garden.author = Users.objects.filter('nuoxiao')
    garden.dateTime = '2018-03-31'
    garden.save()

    return HttpResponse('OK!')