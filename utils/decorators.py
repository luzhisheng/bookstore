from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http import HttpResponse

#登录判断装饰器
def login_required(view_func):
	def wrapper(request,*view_args,**view_kwargs):
		if request.session.has_key('islogin'):#判断session是否有has_key键
			#用户登录
			return view_func(request,*view_args,**view_kwargs)
		else:
			# 跳转到登录页面
			return redirect(reverse('user:login'))
	return wrapper