# -*- coding: utf-8 -*-
from django.db import models

# 用户
class Users(models.Model):
    name = models.CharField(max_length=50)  # 用户名
    dateTime = models.DateField() # 时间

    def __str__(self):
        return self.name

# 园子
class Garden(models.Model):
    name = models.CharField(max_length=50)  # 名称
    introduce = models.CharField(max_length=140) # 介绍
    description = models.CharField(max_length=8000) # 描述
    dateTime = models.DateField() # 时间
    author = models.ForeignKey(Users) # 作者

    def __str__(self):
        return self.name

# 博客
class Blogs(models.Model):
    title = models.CharField(max_length=20) # 标题
    subtitle = models.CharField(max_length=50)  # 副标题
    introduction = models.CharField(max_length=140) # 简介
    description = models.CharField(max_length=8000)  # 描述
    imgurl = models.CharField(max_length=500)   # 图片
    dateTime = models.DateField()   # 日期
    author = models.ForeignKey(Users) # 作者
    links = models.IntegerField()   # 点赞数
    reads = models.IntegerField()    # 阅读数
    garden = models.ForeignKey(Garden)  # 园子主键

    def __str__(self):
        return self.title

# 评论
class Commons(models.Model):
    parentId = models.IntegerField() # 引用ID
    contnet = models.CharField(max_length=500)  # 内容
    references = models.IntegerField()   # 引用数
    replys = models.IntegerField()  # 回复数/评论数
    dateTime = models.DateField()   # 日期
    author = models.ForeignKey(Users) # 作者
    links = models.IntegerField()   # 点赞数
    blogs = models.ForeignKey(Blogs)  # 博客

    def __str__(self):
        return self.contnet

# 主题
class Theme(models.Model):
    themeName = models.CharField(max_length=50)  # 主题名
    introduce = models.CharField(max_length=140)  # 介绍
    description = models.CharField(max_length=8000)  # 规则描述
    author = models.ForeignKey(Users) # 作者
    datetime = models.DateField()  # 时间
    members = models.IntegerField() # 成员数

    def __str__(self):
        return self.themeName


# 讨论主题
class DiscussTopic(models.Model):
    title = models.CharField(max_length=50)  # 讨论标题
    links = models.IntegerField()   # 点赞数
    dateTime = models.DateField()  # 时间
    author = models.ForeignKey(Users) # 作者
    theme = models.ForeignKey(Theme) # 主题主键ID

    def __str__(self):
        return self.title


# 主题和讨论关联表 （1：n ）
class Discuss(models.Model):
    parentId = models.IntegerField()  # 引用ID
    contnet = models.CharField(max_length=500)  # 内容
    references = models.IntegerField()  # 引用数
    links = models.IntegerField()   # 点赞数
    dateTime = models.DateField()  # 时间
    author = models.ForeignKey(Users) # 作者
    topic = models.ForeignKey(DiscussTopic) # 讨论主题

    def __str__(self):
        return self.contnet
