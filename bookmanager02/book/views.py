from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from book.models import BookInfo


def index(request):
    books = BookInfo.objects.all()


    print(books)

    return HttpResponse('index')


# name='abc'

############################增加数据#############################
from book.models import BookInfo

# 方式1
book = BookInfo(
    name='Django',
    pub_date='2000-1-1',
    readcount=10
)
# 必须要调用 对象的save方法才能将数据保存到数据库中
book.save()

# 方式2
# objects  相当于一个代增删改查
BookInfo.objects.create(
    name='wuzhen',
    pub_date='2000-1-1',
    readcount=100
)

############################修改数据#############################

# 方式1
# select * from bookinfo where id=6;
book = BookInfo.objects.get(id=6)
book.name = '运维开发入'

# 方式2
BookInfo.objects.filter(id=6).update(name='爬虫入门', commentcount=666)
# 错误的
BookInfo.objects.get(id=5).update(name='555', commentcount=699)

############################删除数据#############################

# 方式1
book = BookInfo.objects.get(id=6)
# 删除分2种 物理删除（这条记录删除） 逻辑删除（修改标记位 例如 is_delete=False）

book.delete()

# 方式2
BookInfo.objects.get(id=6).delete()

BookInfo.objects.filter(id=5).delete()

############################查询数据#############################

# get查询单一结果，如果不存在会抛出模型类.DoesNotExist异常。
try:
    book = BookInfo.objects.get(id=1)
except BookInfo.DoesNotExist:
    print('查询结果不存在')

# all查询多个结果。
BookInfo.objects.all()
from book.models import PeopleInfo

PeopleInfo.objects.all()

# count查询结果数量。
BookInfo.objects.all().count()
BookInfo.objects.count()

############################过滤查询数据#############################
# 实现SQL中的where功能，包括
#
# filter过滤出多个结果
# exclude排除掉符合条件剩下的结果
# get过滤单一结果

# 语法格式 模型类名。objects.filter(属性名——运算符=值);  获取n个结果
# 语法格式 模型类名。objects.exclude(属性名——运算符=值);  获取n个结果
# 语法格式 模型类名。objects.get(属性名——运算符=值);  获取1个结果 或者 异常


# 查询编号为1的图书
book = BookInfo.objects.get(id=1)

BookInfo.objects.get(pk=1)

BookInfo.objects.filter(id=1)

# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')

# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')

# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)

# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1, 3, 5])

# 大于 gt         great 大
# 大于等于 gte     e  equal
# 小于 lt         less then  litte
# 小于等与lte


# 查询编号大于3的图书
BookInfo.objects.filter(id__gt=3)

# 查询编号不等于3的图书
BookInfo.objects.exclude(id=3)

# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)

# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')

########################################################################

from django.db.models import F

# 使用 2个属性的比较
# 语法形式：
# 查询阅读量大于等于评论量的图书
BookInfo.objects.filter(readcount__gte=F('commentcount'))

##############################################################################

# 并且查询
# 查询阅读量大于20，并且编号小于3的图书
BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)

BookInfo.objects.filter(readcount__gt=20, id__lt=3)

# 或者查询
# 查询阅读量大于20，或编号小于3的图书
from django.db.models import Q

# 或者语法：

BookInfo.objects.filter(Q(readcount__gt=20) | Q(id__lt=3))

##########################################################

from django.db.models import Sum, Max, Min, Avg, Count

#

BookInfo.objects.aggregate(Sum('readcount'))

############################################################
BookInfo.objects.all().order_by('readcount')

###########################2个表的级联操作############################

# 查询书籍为1的所有人物信息
book = BookInfo.objects.get(id=1)

book.peopleinfo_set.all()

# PeopleInfo.objects.filter(book=1)


# 查询人物为1的书籍信息
from book.models import PeopleInfo

person = PeopleInfo.objects.get(id=1)

person.book.name
person.book.readcount

##########################关联过滤查询#######################


# 查询图书，要求图书人物为"郭靖"

BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
BookInfo.objects.filter(peopleinfo__name='郭靖')

# 查询图书，要求图书中人物的描述包含"八"

BookInfo.objects.filter(peopleinfo__description__contains="八")

# 查询书名为“天龙八部”的所有人物

PeopleInfo.objects.filter(book__name='天龙八部')
PeopleInfo.objects.filter(book__commentcount__exact="天龙八部")

# 查询图书阅读量大于30的所有人物
PeopleInfo.objects.filter(book__readcount__gt=30)
