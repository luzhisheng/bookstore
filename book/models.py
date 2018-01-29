from db.base_models import *
from utils.get_hash import get_hash
# Create your models here.

#自定义管理器
class PassportManger(models.Manager):
	#添加一个账户
	def add_one_passport(self,username,password,email):
		passport = self.create(username=username,password=get_hash(password),email=email)
		return passport

	#根据用户名和密码查找信息
	def get_one_passport(self,username,password):
		try:
			passport = self.get(username=username,password=get_hash(password))
		except self.model.DoesNotExist:
			passport = None
		return passport

#用户模型类
class Passport(BaseModel):
	username = models.CharField(max_length=20,verbose_name="用户名")
	password = models.CharField(max_length=40,verbose_name="密码")
	email = models.EmailField(verbose_name="邮箱")
	is_active = models.BooleanField(default=False,verbose_name="激活状态")

	#用户表管理器
	objects = PassportManger()

	class Meta:
		verbose_name = '注册用户'
		db_table = "passport"
		
	def __str__(self):
		return self.username

#地址模型管理器类
class AddressManger(models.Manager):
	'''查询指定用户的默认收货地址'''
	def get_default_address(self,passport_id):
		try:
			select_addr = self.get(passport_id=passport_id,is_default=True)
		except self.model.DoesNotExist:#不存在
			select_addr = None
		return select_addr

	#添加收货地址
	def add_one_address(self,recipient_name,recipient_addr,zip_code,recipient_phone,passport_id):
		#判断用户是否有默认收货地址
		addr = self.get_default_address(passport_id)

		if addr:
			is_default = False#存在默认
		else:
			is_default = True#不存在默认

		#添加一个地址
		addr = self.create(
			recipient_name = recipient_name,
			recipient_addr = recipient_addr,
			zip_code = zip_code,
			recipient_phone = recipient_phone,
			is_default = is_default,
			passport_id = passport_id,
		)

		return  addr

#用户中心的实现
class Address(BaseModel):
	recipient_name = models.CharField(max_length=20,verbose_name='收件人')
	recipient_addr = models.CharField(max_length=60,verbose_name='收件地址')
	zip_code = models.CharField(max_length=8,verbose_name='邮编')
	recipient_phone = models.CharField(max_length=11,verbose_name='手机号码')
	is_default = models.BooleanField(default=False,verbose_name='是否默认')
	passport = models.ForeignKey('Passport',verbose_name='账户')

	objects = AddressManger()

	class Meta:
		verbose_name = '用户中心'
		db_table = "address"

	def __str__(self):
		return self.recipient_name

