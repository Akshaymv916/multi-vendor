from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email', 'phone_no', 'is_vendor', 'is_staff', 'is_active')  
    list_filter = ('is_vendor', 'is_staff', 'is_active')  
    search_fields = ('email', 'phone_no')  
    ordering = ('email',)  
    list_editable = ('is_staff', 'is_active')  
    fieldsets = (
        ('User Info', {'fields': ('email', 'phone_no', 'password')}),
        ('Permissions', {'fields': ('is_vendor', 'is_staff', 'is_superuser', 'is_active')}),
        ('Important Dates', {'fields': ('last_login',)}),
    ) 
    add_fieldsets = (
        ('New User', {
            'classes': ('wide',),
            'fields': ('email', 'phone_no', 'password1', 'password2', 'is_vendor', 'is_staff', 'is_active'),
        }),
    )  

admin.site.register(User, CustomUserAdmin)
