# # -*- coding: utf-8 -*-
#
# from django.http import HttpResponse
#
# from FirstModel.models import First
#
#
# # 数据库操作
# def testadd(request):
#     test1 = First(name='runoob')
#     test1.save()
#     return HttpResponse("<p>数据添加成功！</p>")
#
#
# def testquery(request):
#     # 初始化
#     response = ""
#     response1 = ""
#
#     # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
#     list = First.objects.all()
#
#     # filter相当于SQL中的WHERE，可设置条件过滤结果
#     response2 = First.objects.filter(id=1)
#
#     # 获取单个对象
#     response3 = First.objects.get(id=1)
#
#     # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
#     First.objects.order_by('name')[0:2]
#
#     # 数据排序
#     First.objects.order_by("id")
#
#     # 上面的方法可以连锁使用
#     First.objects.filter(name="runoob").order_by("id")
#
#     # 输出所有数据
#     for var in list:
#         response1 += var.name + " "
#     response = response1
#     return HttpResponse("<p>" + response + "</p>")
#
#
# def testupdate(request):
#     one = First.objects.get(id=1);
#     one.name = 'one'
#     one.save()
#     # 另外一种方式
#     # First.objects.filter(id=1).update(name='Google')
#
#     # 修改所有的列
#     # First.objects.all().update(name='Google')
#
#     return HttpResponse("<p>修改成功</p>")
#
#
# def testdelete(request):
#     # 删除id=1的数据
#     test1 = First.objects.get(id=1)
#     test1.delete()
#
#     # 另外一种方式
#     # First.objects.filter(id=1).delete()
#
#     # 删除所有数据
#     # First.objects.all().delete()
#
#     return HttpResponse("<p>删除成功</p>")
