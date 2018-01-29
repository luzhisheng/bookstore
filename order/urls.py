from django.conf.urls import url
from order import views

urlpatterns = [
	url(r'^$',views.order_place,name="place"),
	url(r'^commit/$',views.order_commit,name='commit'),
	url(r'^pay/$', views.order_pay, name='pay'),# 订单支付
	url(r'^check_pay/$',views.check_pay,name='check_pay'),# 查询支付结果
]