from django.db import models

#基类
class BaseModel(models.Model):
	is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')
	create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
	update_time = models.DateTimeField(auto_now=True,verbose_name='修改时间')

	class Meta:
		abstract = True