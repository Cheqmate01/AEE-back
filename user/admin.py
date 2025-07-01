from django.contrib import admin
from .models import UserInfo

# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'd_o_b')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('d_o_b',)

admin.site.register(UserInfo, UserInfoAdmin)