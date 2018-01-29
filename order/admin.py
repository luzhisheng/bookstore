from django.contrib import admin
from order.models import *

# Register your models here.
@admin.register(OrderGoods)
class RegisterBooks(admin.ModelAdmin):
	list_display = ('order', 'books', 'count','price')


@admin.register(OrderInfo)
class RegisterBooks(admin.ModelAdmin):
	list_display = ('order_id', 'addr', 'total_count','total_price')