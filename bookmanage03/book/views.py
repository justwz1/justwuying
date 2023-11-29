from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo


# Create your views here.

def create_book(request):
    book = BookInfo.objects.create(
        name='abc',
        pub_date='2000-1-1',
        readcount=10
    )

    return HttpResponse("create")


def shop(request, city_id, mobile):
    print(city_id, mobile)

    import re
    # if not re.match('\d{5}',shop_id):
    #     return HttpResponse('没有此商品')

    query_params = request.GET
    print(query_params)
    # order=query_params.get('order')
    # order = query_params['order']
    # print(order)

    ###############################
    # <QueryDict: {'order': ['readcount']}>
    # QueryDict 具有字典的特性
    # 还具有 一键多值
    # <QueryDict: {'order': ['readcount', 'commentcount'], 'page': ['1']}>
    order = query_params.getlist('order')
    print(order)

    return HttpResponse('吴振')


def register(request):
    data = request.POST
    print(data)
    return HttpResponse('ok')


def json(request):
    body = request.body
    # print(body)

    body_str = body.decode()
    # print(body_str)

    import json
    body_dict = json.loads(body_str)
    # print(body_dict)

    # print(request.META)
    print(request.META['SERVER_PORT'])

    return HttpResponse('json')

def method(request):

    print(request.method)

    return HttpResponse('method')
