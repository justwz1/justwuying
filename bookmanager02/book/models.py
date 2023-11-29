from django.db import models

# Create your models here.
"""
1 模型类 需要继承自 models.Model
2 定义属性
    
    属性名=models.类型（选项）
    
    2.1 属性名对应 字段名
        不要使用 python mysql等关键字
        不要使用连续的下划线
    2.2 类型 mysql的另外类型
    2.3 选项 是否有默认值 是欧唯一 是否为null
            CharField 必须u设置max_length
            verbose_name 主要是admin站点使用
        
3 改变表的名称
    默认表的名称 子应用名——类名 都是小写
    修改表的名字
            
"""


class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bookinfo'
        verbose_name = '书籍管理'


class PeopleInfo(models.Model):
    # 定义一个有序字典
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )

    name = models.CharField(max_length=10, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)

    # 外键
    # 系统会自动为外健添加 _id

    # 外健的级联操作
    # 主表和从表
    # 1 对多
    # 书籍 对人物
    # set NULL
    # 抛出异常 不让删除
    # 级联删除

    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'

    def __str__(self):
        return self.name


