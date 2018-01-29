from django.contrib import admin
from .models import Passport,Address
# Register your models here.
admin.site.register(Passport)

@admin.register(Address)
class RegisterAddress(admin.ModelAdmin):
	list_display = ('recipient_name', 'recipient_addr', 'recipient_phone','passport')