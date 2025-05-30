from django.contrib import admin
from .models import Product, Variation, ProductVariation, ProductImage, Brand, Category



class VariationInline(admin.TabularInline):
   model = ProductVariation
   extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ['title', 'base_price', 'is_variable', 'get_cover']
   prepopulated_fields = {'slug':('title',)}
   inlines = [VariationInline]



@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
   list_display = ['title']


# @admin.register(ProductVariation)
# class ProductVariationAdmin(admin.ModelAdmin):
#    list_display = ['product',]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
   list_display = ['title', 'created_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ['title', 'category']


# @admin.register(ProductImage)
# class ProductImageAdmin(admin.ModelAdmin):
#    list_display = ['image', 'alt_text']


