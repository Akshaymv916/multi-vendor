from django.contrib import admin
from products.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'vendor', 'price', 'stock', 'created_at')  
    list_filter = ('vendor', 'price', 'stock') 
    search_fields = ('name', 'description') 
    ordering = ('-created_at',)  
    list_editable = ('price', 'stock')  
    readonly_fields = ('created_at',)  
    fieldsets = (
        ('Basic Information', {'fields': ('name', 'vendor', 'description')}),
        ('Pricing & Stock', {'fields': ('price', 'stock')}),
        ('Metadata', {'fields': ('created_at',)}),
    )  

admin.site.register(Product, ProductAdmin)
