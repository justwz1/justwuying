from django.urls import path
from book.views import create_book, shop, register, json, method, response
from book.views import set_cookie, get_cookie, set_session, get_session
from book.views import login
from book.views import loginView, OrderView

from django.urls import converters
from django.urls.converters import register_converter


class MobileConverter:
    # 验证数据的关键是：正则
    regex = '1[3-9]\d{9}'

    # 验证没有问题的数据 给视图函数
    def to_python(self, value):
        return value


register_converter(MobileConverter, 'phone')

urlpatterns = [
    path('create/', create_book),
    path('<int:city_id>/<phone:mobile>/', shop),
    path('register/', register),
    path('json/', json),
    path('method/', method),
    path('res/', response),
    path('set_cookie/', set_cookie),
    path('get_cookie/', get_cookie),
    path('set_session/', set_session),
    path('get_session/', get_session),
    path('login/', login),

    ###############类视图################
    path('163login/', loginView.as_view()),
    path('order/', OrderView.as_view()),

]
