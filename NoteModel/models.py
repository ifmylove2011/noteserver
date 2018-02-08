# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible
class Category(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, verbose_name='目录名称')
    accessLevel = models.IntegerField(default=0, verbose_name='访问级别')
    count = models.IntegerField(default=0, verbose_name='条目数', editable=False)
    isDelete = models.IntegerField(choices=((0, u'未删除'), (1, u'已删除')), default=0, verbose_name='是否删除')
    isFinish = models.IntegerField(choices=((0, u'已完成'), (1, u'未完成')), default=0, verbose_name='是否完成')
    isUpdate = models.IntegerField(choices=((0, u'未更新'), (1, u'已更新')), default=0, verbose_name='是否更新')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Note(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=200, verbose_name='笔记名称')
    updateTime = models.DateTimeField(null=True, verbose_name='更新时间', editable=False)
    createTime = models.DateTimeField(null=True, verbose_name='创建时间', editable=False)
    sourceUrl = models.CharField(max_length=300, null=True, verbose_name='资源链接')
    isDelete = models.IntegerField(choices=((0, u'未删除'), (1, u'已删除')), default=0, verbose_name='是否删除')
    isFinish = models.IntegerField(choices=((0, u'已完成'), (1, u'未完成')), default=0, verbose_name='是否完成')
    isUpdate = models.IntegerField(choices=((0, u'未更新'), (1, u'已更新')), default=0, verbose_name='是否更新')
    password = models.CharField(null=True, max_length=100, verbose_name='密码')
    passwordHint = models.CharField(null=True, max_length=100, verbose_name='密码提示')
    encrypted = models.IntegerField(choices=((0, u'未加密'), (1, u'已加密')), default=0, verbose_name='是否加密')
    content = models.TextField(verbose_name='内容', blank=True, max_length=1024 * 1024 * 10)
    lastviewtime = models.DateTimeField(null=True, verbose_name='最近查看时间', editable=False)
    cate = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Attach(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    filename = models.CharField(max_length=100, verbose_name='文件名称')
    filepath = models.CharField(max_length=100, verbose_name='文件路径')
    filesize = models.IntegerField(default=0, verbose_name='文件大小')
    filetype = models.IntegerField(default=0, verbose_name='文件类型')
    uploadTime = models.DateTimeField(null=True, verbose_name='上传时间', editable=False)
    isFinish = models.IntegerField(choices=((0, u'已完成'), (1, u'未完成')), default=0, verbose_name='是否完成')
    isUpdate = models.IntegerField(choices=((0, u'未更新'), (1, u'已更新')), default=0, verbose_name='是否更新')
    isDelete = models.IntegerField(choices=((0, u'未删除'), (1, u'已删除')), default=0, verbose_name='是否删除')
    note = models.ForeignKey(Note, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.filename
