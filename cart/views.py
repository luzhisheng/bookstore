from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from books.models import Books
from django_redis import get_redis_connection
from utils.decorators import login_required

#显示购物车页面
@login_required
def cart_show(request):
	passport_id = request.session.get('passport.id')
	#获取用户购物车记录
	conn = get_redis_connection('default')
	cart_key = 'cart_%d' % passport_id
	res_dict = conn.hgetall(cart_key)

	books_li = []
	#保存所有商品的总数
	total_count = 0
	#保存所有商品的总价格
	total_price = 0

	#遍历 res_dict 获取商品的数据
	for id,count in res_dict.items():
		# 根据id获取商品的信息
		books  = Books.objects.get_books_by_id(books_id=id)
		#保存商品的数目
		books.count = count
		#保存商品的价格
		books.amount = int(count) * books.price
		books_li.append(books)

		total_count += int(count)
		total_price += int(count) * books.price

	context = {
		'book_li':books_li,
		'total_count':total_count,
		'total_price':total_price,
	}

	return render(request,'users/cart.html',context)

# 向购物车中添加商品的功能
# 前端发过来的数据：商品id 商品数目 books_id books_count
# 涉及到数据的修改，使用post方式
def cart_add(request):
	#判断用户是否登录
	if not request.session.has_key('islogin'):#has_key是判断是否存在islogin这个键，存在返回true
		return JsonResponse({'res': 0, 'errmsg': '请先登录'})

	#接收数据
	books_id = request.POST.get('books_id') # axjs 传过来的数据
	books_count = request.POST.get('books_count')#axjs 传过来的数据

	#进行数据校验
	if not all([books_id,books_count]):
		return JsonResponse({'res':1,'errmsg':'数据不完整'})

	books = Books.objects.get_books_by_id(books_id=books_id)

	if books is None:
		#商品存在
		return JsonResponse({'res':2,'errmsg':'商品不存在'})

	try:
		count = int(books_count)
	except Exception as e:
		#商品数目不合法
		return JsonResponse({'res': 3, 'errmsg': '商品数量必须是数字'})

	# 添加商品到购物车
	# 每个用户的购物车记录用一条hash数据保存，格式:cart_用户id: 商品id 商品数量
	conn = get_redis_connection('default')#创建redis链接,default是配置文件中的默认数据库

	cart_key = 'cart_%d' % request.session.get('passport.id')#根据每个用户确定购物车的标识

	res = conn.hget(cart_key,books_id)# redis写法

	if res is None:
		# 如果用户的购车中没有添加过该商品，则添加数据
		res = count
	else:
		# 如果用户的购车中已经添加过该商品，则累计商品数目
		res = int(res) + count

	# 判断商品的库存
	if res > books.stock:
		# 库存不足
		return JsonResponse({'res':4,'errmsg':'商品库存不足'})
	else:
		conn.hset(cart_key,books_id,res)#redis写法

	#返回结果
	return JsonResponse({'res': 5})

#获取购物车的商品数量
def cart_count(request):
	if not request.session.get('islogin'):
		return JsonResponse({'res':0})

	# 计算用户购物车商品的数量
	conn = get_redis_connection('default')
	cart_key = 'cart_%d' % request.session.get('passport.id')

	res = 0
	res_list = conn.hvals(cart_key)

	for i in res_list:
		res += int(i)

	return JsonResponse({'res':res})

# cart/views.py
# 前端传过来的参数:商品id books_id
# post
# /cart/del/
#删除商品信息
def cart_del(request):
	#判断用户是否登录
	if not request.session.has_key('islogin'):
		return JsonResponse({'res':0,'errmsg':'请先登录'})

	#接收数据
	books_id = request.POST.get('books_id')

	#校验商品是否存在
	if not all([books_id]):
		return JsonResponse({'res': 1, 'errmsg': '数据不完整'})

	books = Books.objects.get_books_by_id(books_id=books_id)#根据商品的id获取商品信息

	if books is None:
		return JsonResponse({'res': 2, 'errmsg': '商品不存在'})

	# 删除购物车商品信息
	conn = get_redis_connection('default')
	cart_key = 'cart_%d' % request.session.get('passport.id')
	conn.hdel(cart_key,books_id)#删除car_key类中books_id的键值

	return JsonResponse({"res":3})

#实现购物车页面编辑商品数量的功能。
def cart_update(request):
	# 判断用户是否登录
	if not request.session.has_key('islogin'):
		return JsonResponse({'res':0,'errmsg':'请先登录'})

	# 接收数据
	books_id = request.POST.get('books_id')
	books_count = request.POST.get('books_count')

	#数据的效验
	if not all([books_id,books_count]):
		return JsonResponse({'res': 1, 'errmsg': '数据不完整'})

	books = Books.objects.get_books_by_id(books_id=books_id)

	if books is None:
		return JsonResponse({'res': 2, 'errmsg': '商品不存在'})

	try:
		books_count = int(books_count)
	except Exception:
		return JsonResponse({'res': 3, 'errmsg': '商品数目必须为数字'})

	# 更新操作
	conn = get_redis_connection('default')
	cart_key = 'cart_%d'% request.session.get('passport.id')

	# 判断商品库存
	if books_count > books.stock:
		return JsonResponse({'res': 4, 'errmsg': '商品库存不足'})

	conn.hset(cart_key,books_id,books_count)

	return JsonResponse({'res': 5})
