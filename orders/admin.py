from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):  
    model = OrderItem  
    extra = 1 
    readonly_fields = ('price_at_purchase',)  
    fields = ('product', 'quantity', 'price_at_purchase') 

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_amount', 'status', 'created_at')  
    list_filter = ('status', 'created_at') 
    search_fields = ('customer__email',)  
    ordering = ('-created_at',)  
    readonly_fields = ('created_at', 'total_amount')  
    inlines = [OrderItemInline] 

admin.site.register(Order, OrderAdmin)
