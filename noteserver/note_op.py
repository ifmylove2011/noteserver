# -*- coding: utf-8 -*-

import json

from django.http import HttpResponse
from django.http import StreamingHttpResponse
from NoteModel.models import Note, Category, Attach
from noteserver.tool import *
import os
from django.core import serializers
from django.shortcuts import render

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ROOT_IP = 'liang.hsk.la:50087'
UPLOAD_DIR = os.path.join(ROOT_DIR, "upload")
ROOT_IP = '192.168.191.4:8088'


def add_cate(data):
    print(data, data.__class__)
    category = Category(**data)
    category.save()
    return build_response_data('')


def add_note(data):
    print(data, data.__class__)
    cate = Category.objects.get(_id=data['cate_id'])

    note = Note(cate=cate, **data)
    note.save()

    cate.count += 1
    cate.save()

    return build_response_data("")


def add_attach(data):
    print(data, data.__class__)

    note = Note.objects.get(_id=data['note_id'])

    attach = Attach(note=note, **data)
    attach.save()

    return build_response_data('')


def change_cate(data):
    # category = Category.objects.get(_id=data['id'])
    # category.name = data['name']
    # category.isDelete = data['isDelete']
    # category.isFinish = data['isFinish']
    # category.isUpdate = data['isUpdate']
    # category.count = data['count']
    # category.accessLevel = data['accessLevel']
    # category.save()
    add_cate(data)
    return build_response_data('')


def change_note(data):
    add_note(data)
    return build_response_data('')


def change_attach(data):
    add_attach(data)
    return build_response_data('')


def delete_cate(data):
    category = Category.objects.get(_id=data['id'])
    category.delete()
    return build_response_data('')


def delete_note(data):
    note = Note.objects.get(_id=data['id'])
    note.delete()

    cate = Category.objects.get(_id=note.cate_id)
    cate.count -= 1
    cate.save()

    return build_response_data('')


def delete_attach(data):
    attach = Attach.objects.get(_id=data['id'])
    attach.delete()
    return build_response_data('')


def query_cate(params):
    category = Category.objects.filter(**params).values()
    if category.count() == 0:
        return build_response_error(10003)
    return build_response_data(list(category))


def query_note(params):
    note = Note.objects.filter(**params).values()
    if note.count() == 0:
        return build_response_error(10003)
    return build_response_data(list(note))


def query_attach(params):
    attach = Attach.objects.filter(**params).values()
    if attach.count() == 0:
        return build_response_error(10003)
    return build_response_data(list(attach))


def sync_note_list(data):
    for jo in data:
        add_note(jo)
    return build_response_data('')


def sync_cate_list(data):
    for jo in data:
        add_cate(jo)
    return build_response_data('')


def sync_attach_list(data):
    for jo in data:
        add_attach(jo)
    return build_response_data('')


def query_version(data):
    '''{
      "title": "SlimNote_V1.0.2",
      "apkUrl": "http://ifmylove2011.55555.io:17668/SlimNote_V1.0.2_baidu.apk",
      "version": "1.0.2",
      "updateTime": "2017-12-29 16:26:00",
      "desc": "测试专用",
      "apkSize": 103013300
    }'''
    channel = data['channel']
    version = {}
    version_file_list = os.listdir(os.path.join(ROOT_DIR, 'version'))
    for file in version_file_list:
        print(file)
        if channel in file:
            version['title'] = os.path.splitext(file)[0]
            version['apkUrl'] = 'http://' + ROOT_IP + '/' + 'download' + '/' + file
            version['version'] = '1.0.2'
            version['updateTime'] = '2017-12-29 16:26:00'
            version['desc'] = 'test'
            version['apkSize'] = os.path.getsize(os.path.join(ROOT_DIR, 'version', file))
    print(version)
    return build_response_data(version)


dict_code = {200: '成功', 10001: '无此业务', 10002: '数据异常', 10003: '无此数据', 10004: '无此文件'}


def build_response_data(data):
    response = {'code': 200, 'message': dict_code[200], 'processTime': datetime.datetime.now()}
    if data != '':
        response['data'] = data
    return HttpResponse(json.dumps(response, cls=CJsonEncoder, ensure_ascii=False),
                        content_type="application/json; charset=utf-8")


def build_response_error(code):
    response = {'code': code, 'message': dict_code[code], 'processTime': datetime.datetime.now()}
    return HttpResponse(json.dumps(response, cls=CJsonEncoder, ensure_ascii=False),
                        content_type="application/json; charset=utf-8")


def noteservice(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        return post_request(request_data['code'], request_data['data'])
    else:
        print(request.GET)
        code = request.GET['code']
        params = {}
        for key, value in request.GET.items():
            if key != 'code':
                params[key] = value
        print(params)
        return get_request(code, params)


dict_post_request = {'C101': add_cate, 'C102': change_cate, 'C103': delete_cate, 'C110': sync_cate_list,
                     'C201': add_note, 'C202': change_note, 'C203': delete_note, 'C210': sync_note_list,
                     'C301': add_attach, 'C302': change_attach, 'C303': delete_attach, 'C310': sync_attach_list}

dict_get_request = {'C104': query_cate, 'C204': query_note, 'C304': query_attach, 'C001': query_version}


def post_request(code, data):
    if code in dict_post_request:
        return dict_post_request[code](data)
    else:
        return build_response_error(10001)


def get_request(code, params):
    if code in dict_get_request:
        return dict_get_request[code](params)
    else:
        return build_response_error(10001)


def file_download(request, file_name):
    file_path = os.path.join(ROOT_DIR, 'version', file_name)
    print(file_path)

    def read_file(file, chunk_size=1024):
        with open(file, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    response = StreamingHttpResponse(read_file(file_path))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Length'] = os.path.getsize(file_path)
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)

    return response


def upload(request):
    if request.method == 'POST':
        try:
            user = request.POST.get('byd')
            img = request.FILES.get('attach')
            img_path = os.path.join(UPLOAD_DIR, img.name)
            f = open(img_path, 'wb')
            for chunk in img.chunks():
                f.write(chunk)
                f.close()
            print(img_path)
        except Exception as e:
            print(str(e))
        finally:
            print("")
        return HttpResponse(build_response_data(""))
    else:
        return render(request, 'upload.html')
