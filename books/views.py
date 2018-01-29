from django.shortcuts import render,redirect
from books.models import Books
from books.enums import *
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator #Paginator对象分页
from utils.time import *
from django_redis import get_redis_connection
# Create your views here.

#显示首页
@functime
def index(request):
	# 查询每个种类的3个新品信息和4个销量最好的商品信息
	python_new = Books.objects.get_books_by_type(PYTHON,3,sort='new')
	python_hot = Books.objects.get_books_by_type(PYTHON,4,sort='hot')
	javascript_new = Books.objects.get_books_by_type(JAVASCRIPT,3,sort='new')
	javascript_hot = Books.objects.get_books_by_type(JAVASCRIPT,4, sort='hot')
	algorithms_new = Books.objects.get_books_by_type(ALGORITHMS, 3, sort='new')
	algorithms_hot = Books.objects.get_books_by_type(ALGORITHMS, 4, sort='hot')
	machinelearning_new = Books.objects.get_books_by_type(MACHINELEARNING, 3, sort='new')
	machinelearning_hot = Books.objects.get_books_by_type(MACHINELEARNING, 4, sort='hot')
	operatingsystem_new = Books.objects.get_books_by_type(OPERATINGSYSTEM, 3, sort='new')
	operatingsystem_hot = Books.objects.get_books_by_type(OPERATINGSYSTEM, 4, sort='hot')
	database_new = Books.objects.get_books_by_type(DATABASE, 3, sort='new')
	database_hot = Books.objects.get_books_by_type(DATABASE, 4, sort='hot')

	# \定义模板上下文
	centent = {
		"python_new" : python_new,
		"python_hot": python_hot,
		"javascript_new": javascript_new,
		"javascript_hot": javascript_hot,
		"algorithms_new": algorithms_new,
		"algorithms_hot": algorithms_hot,
		"machinelearning_new": machinelearning_new,
		"machinelearning_hot": machinelearning_hot,
		"operatingsystem_new": operatingsystem_new,
		"operatingsystem_hot": operatingsystem_hot,
		"database_new": database_new,
		"database_hot": database_hot,
	}
	return render(request, 'users/index.html',centent)

#显示商品详细页面
def detail(request,books_id):
	books = Books.objects.get_books_by_id(books_id=books_id)
	# 商品不存在，跳转到首页
	if books is None:
		return  redirect(reverse('books:index'))

	#陈接上，找到本类商品的最新品推荐
	books_li = Books.objects.get_books_by_type(books.type_id,2,'new')

	# 用户登录之后，才能浏览记录
	# 每个用户浏览记录对应redis中的一条信息 格式:'history_用户id':[10,9,2,3,4]
	# [9, 10, 2, 3, 4]
	if request.session.has_key('islogin'):
		# 用户已登录，记录浏览记录
		con = get_redis_connection('default')
		key = 'history_%d' % request.session.get('passport.id')
		#redis列表操作
		#先从redis列表中移除books.id
		con.lrem(key,0,books.id)#？？？
		con.lpush(key,books.id)#从头部插入
		#保存用户最近浏览的5个商品
		con.ltrim(key,0,4)#截取数据

	#定义上下文
	context = {'books':books,'books_li':books_li}
	return render(request,'users/detail.html',context)

# 商品种类 页码 排序方式
# /list/(种类id)/(页码)/?sort=排序方式
def list(request,type_id,page):

	#獲取排序方式
	sort = request.GET.get('sort','default')

	#判断type_id是否合法
	if int(type_id) not in BOOKS_TYRE.keys():#如果type不再常量BOOKS_TYRE.key中直接返回首页
		return redirect(reverse('books:index'))

	# 根据商品种类id和排序方式查询数据
	books_li = Books.objects.get_books_by_type(type_id=type_id,sort=sort)#默认是-pk排序
	print(books_li)

	#分頁
	paginator = Paginator(books_li,1)#books_li是列表，每页显示1条数据

	#獲取分頁之後的总页数
	num_pages = paginator.num_pages#num_pages：页面总数，由 paginator对象.num_pages

	#取第page页数据
	if page == '' or int(page) > num_pages:#如果 page 为空或者 page 大于总页数
		page = 1#那么page==1
	else:
		page = int(page)#如果不是那么强转为int类型

	#返回值是一个page类的实例对象
	books_li = paginator.page(page)#由于查找的books_li阻塞，通过page对象取出第一页的数据

	# 进行页码控制
	if num_pages < 5:# 总页数<5, 显示所有页码
		pages = range(1,num_pages)#pages = [1,2,3,4]
	elif page <= 3:# 当前页是前3页，显示1-5页
		pages = range(1,6)# pages = [1,2,3,4,5]
	elif num_pages - page <= 2:# 当前页是后3页，显示后5页 10 9 8 7
		pages = range(num_pages-4,num_pages+1)# pages = [2,3,4,5,6]
	else:
		pages = range(page-2,page+3)# 其他情况，显示当前页前2页，后2页，当前页

	#新品推荐
	books_new = Books.objects.get_books_by_type(type_id=type_id,limit=2,sort="new")

	#定义山下文
	type_title = BOOKS_TYRE[int(type_id)]#找到商品种类
	context = {
		'books_li':books_li,#分类中书对象集合
		'books_new':books_new,#新品推荐
		'type_id':type_id,#分类id
		'sort':sort,#排序方式
		'type_title':type_title,#分类名称
		'pages':pages#显示的数字
	}
	return render(request, 'users/list.html', context)