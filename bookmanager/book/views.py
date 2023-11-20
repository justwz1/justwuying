from django.shortcuts import render

# Create your views here.
"""
视图
视图就是python函数
 两个要求
    1. 试图函数的第一个参数就是接受请求
    2. 必须返回一个响应
"""
from django.http import HttpRequest
from django.http import HttpResponse


# 我们期望用户输入 http://127.0.0.1:8000/index/
# 来访问视图函数

def index(request):
    # return HttpResponse('ok')

    # render 渲染模板
    # request, template_name, context = None,
    # request,         请求
    # template_name,   模板名字
    # context = None

    # 模拟数据查询
    context = {
        'name': '马上双11, 点击有惊喜'
    }
    
    return render(request, 'book/index.html', context=context)
