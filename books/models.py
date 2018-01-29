from django.db import models
from db.base_models import BaseModel
from tinymce.models import HTMLField
from books.enums import *#导入常量

# 商品模型管理器
class BooksManager(models.Manager):
	def get_books_by_type(self, type_id, limit=None, sort='default'):
		if sort == 'new':
			order_by = ('-create_time')# sort='new' 按照创建时间进行排序
		elif sort == 'hot':
			order_by = ('-sales')# sort='hot' 按照商品销量进行排序
		elif sort == 'price':
			order_by = ('-price')# sort='price' 按照商品的价格进行排序
		else:
			order_by = ('-pk')  # sort= 按照默认顺序排序

		# 查询语句
		books_li = self.filter(type_id=type_id, ).order_by(order_by)

		# 查询结果集的限制
		if limit:
			books_li = books_li[:limit]

		return books_li

	# 根据商品的id获取商品信息
	def get_books_by_id(self, books_id):
		try:
			books = self.get(id=books_id)
		except self.model.DoesNotExist:  # 如果根据给出的参数匹配不到对象的话，get() 将触发DoesNotExist 异常
			# 不存在商品
			books = None

		return books

#商品模型类
class Books(BaseModel):
	books_type_choices = ((k,v) for k,v in BOOKS_TYRE.items())#items() 函数以列表返回可遍历的(键, 值) 元组数组。
	status_choices = ((k,v) for k,v in STATUS_CHOICE.items())
	#SmallIntegerField 和 IntegerField 类似，但是只允许在一个数据库相关的范围内的数值（通常是-32,768到+32,767）
	type_id = models.SmallIntegerField(default=PYTHON,choices=books_type_choices,verbose_name='商品种类')
	name = models.CharField(max_length=20,verbose_name='商品名称')
	desc = models.CharField(max_length=128,verbose_name='商品简介')
	price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='商品价格')
	unite = models.CharField(max_length=20,verbose_name='商品单位')
	stock = models.IntegerField(default=1,verbose_name='商品库存')
	sales = models.IntegerField(default=0,verbose_name='商品销量')
	detail = HTMLField(verbose_name='商品详情')
	image = models.ImageField(upload_to='book',verbose_name='商品图片')
	status = models.SmallIntegerField(default=ONLINE,choices=status_choices,verbose_name='商品状态')

	objects = BooksManager()

	class Meta:
		verbose_name = '商品'
		db_table = 'books'

	def __str__(self):
		return self.name


