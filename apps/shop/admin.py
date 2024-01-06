from django.contrib import admin
from .models import Brand, Category, Product, ProductImage, Review


class PhotoInline(admin.TabularInline):
   model = ProductImage
   extra = 5
   
class ProductAdmin(admin.ModelAdmin):
   list_display = ( "title", "user", "slug", "get_cover")
   list_filter = ( "category", "brand")
   inlines = (PhotoInline,)
   
class BrandAdmin(admin.ModelAdmin):
   list_display= ("title", "id", "cover")
   list_filter= ("title",)
   
class CategoryAdmin(admin.ModelAdmin):
   list_display= ("title", "id", "category", "cover")
   list_filter= ("title", "category")
   
class ProductImageAdmin(admin.ModelAdmin):
   list_display= ("product", "id", "image")
   list_filter= ("product",)
   list
   
class ReviewAdmin(admin.ModelAdmin):
   list_display= ("user", "product", "comment")
   list_filter= ("user", "product")


     

admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Review, ReviewAdmin)







