from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem, DiscountCode


class CartItemInlines(admin.TabularInline):
   model= CartItem
   extra = 0
   
class CartAdmin(admin.ModelAdmin):
   list_display= ("user",)
   inlines = [CartItemInlines]

class CartItemAdmin(admin.ModelAdmin):
   list_display= ("product","quantity", "created_at")

class OrderAdmin(admin.ModelAdmin):
   list_display= ("user","shipping_day","is_paid","paid_at","is_delivered","delivere_at","get_created_at",)
   
class OrderItemAdmin(admin.ModelAdmin):
   list_display= ("title", "product", "quantity")


class DiscountCodeAdmin(admin.ModelAdmin):
   list_display= ("title", "code", "percent", "expiration_date")






admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(DiscountCode, DiscountCodeAdmin)