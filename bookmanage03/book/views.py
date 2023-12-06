from django.http import HttpResponse
from django.shortcuts import render, redirect
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


from django.http import HttpResponse, JsonResponse


def response(repuest):
    # response = HttpResponse('res',status=200)
    #
    # response['name']='itcase'
    #
    # return response
    info = {
        'name': 'itcast',
        'address': 'shunyi'
    }
    girl_firends = [
        {
            'name': 'rose',
            'address': 'shunyi'
        },
        {
            'name': 'jack',
            'address': 'changping'
        }
    ]

    # response = JsonResponse(data=girl_firends,safe=False)
    #
    # return response

    return redirect('http://www.itcast.cn')

    #  import json
    #  data = json.dumps(girl_firends)
    #
    #  response = HttpResponse(data)
    #  return response


"""
第一次请求，携带 查询字符串
http://127.0.0.1:8000/set_cookie/?username=itcast&password=123
服务器接收到请求之后，获取username.服务器设置cookie信息，cookie信息包括 username
浏览器接收到服务器的响应之后，应该把cookie保存起来


第二次及其之后的请求，我们访问http://127.0.0.1:8000 都会携带cookie信息。 服务器就可以读取cookie信息，来判断用户身份

"""


def set_cookie(request):
    # 1. 获取查询字符串数据
    username = request.GET.get("username")
    password = request.GET.get("password")
    # 2. 服务器设置cookie信息
    # 通过响应对象 set_cookie 方法
    response = HttpResponse('set_cookie')
    # key,value=''
    response.set_cookie('name', username, max_age=3600)
    response.set_cookie('pwd', password)

    # response.delete_cookie('name')

    return response


def get_cookie(request):
    # 获取cookie
    print(request.COOKIES)
    name = request.COOKIES.get('name')
    return HttpResponse(name)


##############################################################################

# session 是保存在服务器端
# session 需要依赖于cookie

"""

第一次请求 http://127.0.0.1:8000/set_session/?username=itheima 。我们在服务器端设置sesison信息
服务器同时会生成一个sessionid的cookie信息。
浏览器接收到这个信息之后，会把cookie数据保存起来


第二次及其之后的请求 都会携带这个sessionid. 服务器会验证这个sessionid. 验证没有问题会读取相关数据。实现业务逻辑

"""


def set_session(request):
    # 1. 模拟 获取用户信息
    username = request.GET.get('username')

    # 2. 设置session信息
    user_id = 1

    request.session['user_id'] = user_id
    request.session['username'] = username

    # clear 删除session里的数据，但是key有保留
    # request.session.clear()
    # flush 是删除所有的数据 包括key
    # request.session.flush()

    request.session.set_expiry(3600)

    return HttpResponse('set_session')


def get_session(request):
    user_id = request.session.get('user_id')
    username = request.session.get('username')

    content = '{} , {}'.format(user_id, username)

    return HttpResponse(content)


######################类视图############################


def login(request):
    print(request.method)

    if request.method == 'GET':
        return HttpResponse('get 逻辑')
    else:

        return HttpResponse('post 逻辑')


"""
类视图的定义

class 类视图名字 （view）:

    def get(self,request):
    
        :return HttpResponse('xxx')
        
    def http_method_lower(self,request):
    
        ret HttpResponse('xxx')
        
1. 继承自View
2. 类视图中的方法 是采用 http方法小写来区分不同的请求方式
"""
from django.views import View


class loginView(View):

    # def get(self, request):

        # return HttpResponse('get get get ')


    def post(self, request):

        return HttpResponse('post post post')



"""
我的订单。个人中心页面
如果登陆用户 可以访问 
如果未登陆用户 不应该访问 应该跳转到登陆页面

定义一个订单 个人中心 类视图

如果定义我没有登陆呢？？？ 我们以登陆 后台站点为例
"""

from django.contrib.auth.mixins import LoginRequiredMixin

# LoginRequiredMixin 作用 判断 只有登陆用户才可以访问页面
class OrderView(LoginRequiredMixin,View):

    def get(self,request):

        # 模拟一个标记位
        # islogin=False
        # if not islogin:
        #     return HttpResponse('你没有登陆，跳转到登陆页面中')

        return HttpResponse('get我的订单页面，这个页面必须登陆')

    def post(self,request):
        return HttpResponse('post我的订单页面，这个页面必须登陆')

    """
    多继承
    python，c++
    
    """
