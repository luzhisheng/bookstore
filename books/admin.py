from django.contrib import admin
from books.models import Books

# Register your models here.
@admin.register(Books)
class RegisterBooks(admin.ModelAdmin):
	list_display = ('name', 'price', 'sales','type_id')
