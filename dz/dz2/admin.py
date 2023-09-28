from django.contrib import admin
from .models import Client, Product, Order, OrderItem


# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'registration_date')
    list_filter = ('name', 'email', 'phone_number', 'address')
    search_fields = ('name', 'email', 'phone_number')
    date_hierarchy = 'registration_date'
    ordering = ['name', 'phone_number']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity')
    list_filter = ('name', 'description', 'price', 'quantity')
    search_fields = ('name', 'description')
    date_hierarchy = 'added_date'
    ordering = ['name']

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'order_date','total_cost','paid')
    fieldsets = (
        (None, {
            'fields': ('id','client', 'order_date')
        }),
        ('Информация об оплате:', {
            'fields': ('total_cost', 'paid')
        }),
    )
    readonly_fields = ['id','order_date','total_cost']
    inlines = [OrderItemInline]

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'price', 'quantity')
    search_fields = ('order', 'product', 'price', 'quantity')
    ordering = ['order', 'id']
    fieldsets = (
        (None, {
            'fields': ('id', 'order', 'product')
        }),
        ('Информация о позиции заказа:', {
            'fields': ('price', 'quantity','get_cost')
        }),
    )
    readonly_fields = ['id', 'get_cost']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity')
    list_filter = ('name', 'description', 'price', 'quantity')
    search_fields = ('name', 'description')
    date_hierarchy = 'added_date'
    ordering = ['name']



admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)


