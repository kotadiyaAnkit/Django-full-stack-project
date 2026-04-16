from django.contrib import admin

from .models import Category, Product, Cart, CartItem, Order, PaymentSettings

admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock_quantity', 'is_offer', 'category']
    list_editable = ['stock_quantity', 'is_offer', 'price']
    list_filter = ['is_offer', 'category']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'person_name', 'phone_number', 'pincode', 'total_price', 'payment_method', 'created_at']
    list_filter = ['payment_method', 'created_at']
    readonly_fields = ['created_at']

@admin.register(PaymentSettings)
class PaymentSettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'updated_at']
