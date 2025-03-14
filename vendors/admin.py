from django.contrib import admin
from .models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'user', 'created_at')  
    list_filter = ('created_at',)
    search_fields = ('business_name', 'user__email') 
    ordering = ('-created_at',)  
    readonly_fields = ('created_at',) 
    fieldsets = (
        ('Vendor Information', {'fields': ('user', 'business_name')}),
        ('Timestamps', {'fields': ('created_at',)}),
    )  

admin.site.register(Vendor, VendorAdmin)
