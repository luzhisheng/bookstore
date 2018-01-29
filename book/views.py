from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from book.models import *
from django.http import JsonResponse
import re
from utils.decorators import login_required
from order.models import *
from django_redis import get_redis_connection
from books.models import *
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from django.conf import settings
from django.core.mail import send_mail
from book.tasks import send_active_email
from django.http import HttpResponse

# Create your views here.
def register(request):
	return render(request, 'users/register.html')

def register_handle(request):
	username = request.POST.get('user_name')
	password = request.POST.get('pwd')
	email = request.POST.get('email')

	# 判断数据是否为空
	if not all([username, password, email]):
		return render(request, 'users/register.html', {'errmsg': "参数不能为空"})

	# 判断邮箱是否合法
	if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
		return render(request, 'users/register.html', {'errmsg': "邮箱格式不对"})

	# 进行业务处理:注册，向账户系统中添加账户
	passport = Passport.objects.add_one_passport(username=username, password=password, email=email)

	# 生成激活的token itsdangerous
	serializer = Serializer(settings.SECRET_KEY, 3600)
	token = serializer.dumps({'confirm': passport.id}) # 返回bytes
	token = token.decode()

	#给用户的邮箱发激活邮件
	#send_mail('尚硅谷书城用户激活', '', settings.EMAIL_FROM, [email],html_message='<a href="http://127.0.0.1:8000/user/active/%s/">http://127.0.0.1:8000/user/active/</a>' % token)
	send_active_email.delay(token,username,email)

	return redirect(reverse('books:index'))

def login(request):
	'''显示登录页面'''
	username = request.COOKIES.get('username', '')

	checked = ''

	context = {
		'username': username,  #
		'checked': checked,  # 让单选框默认选中
	}

	return render(request, 'users/login.html', context)


# 登录页面
def login_check(request):
	# 获取数据
	username = request.POST.get('username')
	password = request.POST.get('password')
	remember = request.POST.get('remember')
	print(username, password, remember)
	# 数据校验
	if not all([username, password, remember]):
		# 有数据为空
		next_url = reverse('books:index')  # 重定向首页
		return JsonResponse({'res': 2, 'next_url': next_url})

	passport = Passport.objects.get_one_passport(username=username, password=password)  # 根据用户名和密码查找信息
	print(passport)

	if passport:
		# 用户名密码正确
		# next_url = request.session.get('url_path', reverse('books:index')) # /user/
		# 我们先从session中取数据，如果没有，那就拿重定向的 reverse('books:index')
		next_url = reverse('books:index')  # 重定向首页
		jres = JsonResponse({'res': 1, 'next_url': next_url})

		# 判断是否需要记住用户名
		if remember == 'true':
			# 记住用户名
			jres.set_cookie('username', username, max_age=7 * 24 * 3600)  # 一周时间
		else:
			jres.delete_cookie('username')  #

		# 记住用户登录状态
		request.session['islogin'] = True
		request.session['username'] = username
		request.session['passport.id'] = passport.id
		return jres
	else:
		return JsonResponse({'res': 0})


def logout(request):
	request.session.flush()
	return redirect(reverse('books:index'))


@login_required
def user_info(request):
	passport_id = request.session.get('passport.id')
	# 获取用户信息
	select_addr = Address.objects.get_default_address(passport_id=passport_id)

	# 获取用户的最近浏览信息
	con = get_redis_connection('default')
	key = 'history_%d' % passport_id

	# 取出用户最近浏览的5个商品的id
	history_li = con.lrange(key, 0, 4)
	# history_li = [21,20,11]
	# print(history_li)

	# 查询数据库，获取用户最近浏览的商品信息
	books_li = Books.objects.filter(id__in=history_li)

	# books_li = []

	context = {
		'select_addr': select_addr,  # 用户收货信息
		'page': 'user_info',  # 路径
		'books_li': books_li  # 最近浏览
	}
	# print(select_addr)
	return render(request, 'users/user_center_info.html', context)


@login_required
def address(request):
	# 获取登录用户的id
	passport_id = request.session.get('passport.id')

	if request.method == 'GET':
		# 显示地址页面
		# 查询用户的默认地址
		addr = Address.objects.get_default_address(passport_id=passport_id)
		return render(request, 'users/user_center_site.html', {'addr': addr, 'page': 'address'})
	else:
		# 添加收货地址
		# 1.接收数据
		recipient_name = request.POST.get('username')
		recipient_addr = request.POST.get('addr')
		zip_code = request.POST.get('zip_code')
		recipient_phone = request.POST.get('phone')

		# 进行校验
		if not all([recipient_addr, recipient_name, zip_code]):
			return render(request, 'users/user_center_site.html', ({'errmsg': '参数不能为空'}))

		# 3.添加收货地址
		Address.objects.add_one_address(recipient_name=recipient_name,
										recipient_addr=recipient_addr,
										zip_code=zip_code,
										recipient_phone=recipient_phone,
										passport_id=passport_id
										)

		# 4.返回应答
		return redirect(reverse('user:address'))


# 用户中心-定单页面
@login_required
def order(request):
	# 查询用户的订单信息
	passport_id = request.session.get('passport.id')

	# 获取订单信息
	order_li = OrderInfo.objects.filter(passport_id=passport_id)

	# 遍历获取订单的商品信息
	# order->OrderInfo实例对象
	for order in order_li:
		# 根据订单id查询订单商品信息
		order_id = order.order_id
		order_books_li = OrderGoods.objects.filter(order_id=order_id)

		# 计算商品的小计
		# order_books ->OrderBooks实例对象
		for order_books in order_books_li:
			count = order_books.count
			price = order_books.price
			amount = count * price

			# 保存订单中每一个商品的小计
			order_books.amount = amount

		# 给order对象动态增加一个属性order_books_li,保存订单中商品的信息
		order.order_books_li = order_books_li

	context = {
		'order_li': order_li,
		'page': 'order',
	}

	return render(request, 'users/user_center_order.html', context)

def register_active(request,token):
	'''用户账户激活'''
	serializer = Serializer(settings.SECRET_KEY,3600)
	try:
		info = serializer.loads(token)
		passport_id = info['confirm']
		# 进行用户激活
		passport = Passport.objects.get(id=passport_id)
		passport.is_active = True
		passport.save()
		# 跳转的登录页
		return redirect(reverse('books:index'))
	except SignatureExpired:
		# 链接过期
		return HttpResponse('激活链接已过期')