from django.db import models
from db.base_models import BaseModel

#'''订单信息模型类'''
class OrderInfo(BaseModel):
	#支付方法选择
	PAY_METHOD_CHOICES = (
		(1,"货到付款"),
		(2,"微信支付"),
		(3,"支付宝"),
		(4,"银联支付")
	)

	#支付方法
	PAY_METHODS_ENUM = {
		"CASH":1,
		"WEIXIN":2,
		"ALIPAY":3,
		"UNIONPAY":4
	}

	#订购状态选项
	ORDER_STATUS_CHOICES = (
		(1, "待支付"),
		(2, "待发货"),
		(3, "待收货"),
		(4, "待评价"),
		(5, "已完成"),
	)

	order_id = models.CharField(max_length=64,primary_key=True,verbose_name='订单编号')
	passport = models.ForeignKey('book.Passport',verbose_name="下单账户")
	addr = models.ForeignKey('book.Address',verbose_name="收货地址")
	total_count = models.IntegerField(default=1,verbose_name="商品总数")
	total_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="商品总价")
	transit_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="订单运费")
	pay_method = models.SmallIntegerField(choices=PAY_METHOD_CHOICES,default=1,verbose_name="支付方式")#choices=下拉单选框
	status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES,default=1,verbose_name="订单状态")
	#null 如果为True，Django将在数据库中将空值存储为NULL
	#blank 如果为True，则该字段允许为空白
	#unique 如果为 True, 这个字段在表中必须有唯一值.
	trade_id = models.CharField(max_length=100,unique=True,null=True,blank=True,verbose_name="支付编号")

	class Meta:
		verbose_name = '订单信息'
		db_table = 'orderInfo'

	def __str__(self):
		return self.order_id


#订单商品模型类
class OrderGoods(BaseModel):
	order = models.ForeignKey('OrderInfo',verbose_name="所属订单id")
	books = models.ForeignKey('books.Books',verbose_name="订单商品")
	count = models.IntegerField(default=1,verbose_name='商品数量')
	price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='商品价格')

	class Meta:
		verbose_name = "订单商品"
		db_table = 'ordergoods'

	def __str__(self):
		return self.order























