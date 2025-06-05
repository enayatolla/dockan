from django.contrib import admin
from .models import Product, Variation, ProductVariation, ProductImage, Brand, Category, ProductFeature, ProductDescription


class VariationInline(admin.TabularInline):
   model = ProductVariation
   extra = 1
class FeatureInline(admin.TabularInline):
   model = ProductFeature
   extra = 1
class DescriptionInline(admin.TabularInline):
   model = ProductDescription
   extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ['title', 'base_price', 'is_variable', 'get_cover']
   inlines = [VariationInline, FeatureInline, DescriptionInline]
   search_fields = ['title', 'brand__title', 'category__title']
   list_filter = ['brand', 'category']


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
   list_display = ['title']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
   list_display = ['title', 'created_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ['title', 'created_at']



