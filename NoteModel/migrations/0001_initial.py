# Generated by Django 2.0.1 on 2018-01-22 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attach',
            fields=[
                ('_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=100, verbose_name='文件名称')),
                ('filepath', models.CharField(max_length=100, verbose_name='文件路径')),
                ('filesize', models.IntegerField(default=0, verbose_name='文件大小')),
                ('filetype', models.IntegerField(default=0, verbose_name='文件类型')),
                ('uploadTime', models.DateTimeField(editable=False, null=True, verbose_name='上传时间')),
                ('isFinish', models.IntegerField(choices=[(0, '已完成'), (1, '未完成')], default=0, verbose_name='是否完成')),
                ('isUpdate', models.IntegerField(choices=[(0, '未更新'), (1, '已更新')], default=0, verbose_name='是否更新')),
                ('isDelete', models.IntegerField(choices=[(0, '未删除'), (1, '已删除')], default=0, verbose_name='是否删除')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='目录名称')),
                ('accessLevel', models.IntegerField(default=0, verbose_name='访问级别')),
                ('count', models.IntegerField(default=0, editable=False, verbose_name='条目数')),
                ('isDelete', models.IntegerField(choices=[(0, '未删除'), (1, '已删除')], default=0, verbose_name='是否删除')),
                ('isFinish', models.IntegerField(choices=[(0, '已完成'), (1, '未完成')], default=0, verbose_name='是否完成')),
                ('isUpdate', models.IntegerField(choices=[(0, '未更新'), (1, '已更新')], default=0, verbose_name='是否更新')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='笔记名称')),
                ('updateTime', models.DateTimeField(editable=False, null=True, verbose_name='更新时间')),
                ('createTime', models.DateTimeField(editable=False, null=True, verbose_name='创建时间')),
                ('sourceUrl', models.CharField(max_length=300, null=True, verbose_name='资源链接')),
                ('isDelete', models.IntegerField(choices=[(0, '未删除'), (1, '已删除')], default=0, verbose_name='是否删除')),
                ('isFinish', models.IntegerField(choices=[(0, '已完成'), (1, '未完成')], default=0, verbose_name='是否完成')),
                ('isUpdate', models.IntegerField(choices=[(0, '未更新'), (1, '已更新')], default=0, verbose_name='是否更新')),
                ('password', models.CharField(max_length=100, null=True, verbose_name='密码')),
                ('passwordHint', models.CharField(max_length=100, null=True, verbose_name='密码提示')),
                ('encrypted', models.IntegerField(choices=[(0, '未加密'), (1, '已加密')], default=0, verbose_name='是否加密')),
                ('content', models.TextField(blank=True, max_length=10485760, verbose_name='内容')),
                ('lastviewtime', models.DateTimeField(editable=False, null=True, verbose_name='最近查看时间')),
                ('cate', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='NoteModel.Category')),
            ],
        ),
        migrations.AddField(
            model_name='attach',
            name='note',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NoteModel.Note'),
        ),
    ]
