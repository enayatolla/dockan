from django.contrib import admin
from .models import Brand, Category, Product, ProductImage, Review, ProductType, ProductGroup,Banner



class ReviewAdmin(admin.ModelAdmin):
   list_display= ("user", "product", "comment")
   list_filter= ("user", "product")

class PhotoInline(admin.TabularInline):
   model = ProductImage
   extra = 0
   
class TypeInline(admin.TabularInline):
   model = ProductType
   extra = 0
   
class ProductAdmin(admin.ModelAdmin):
   list_display = ( "title", "group", "user", "get_cover")
   list_filter = ( "category", "brand")
   prepopulated_fields = {'slug':('title',)}
   inlines = ( PhotoInline, TypeInline )
   
class ProductInline(admin.TabularInline):
   model= Product
   extra= 0
   
class ProductGroupAdmin(admin.ModelAdmin):
   list_display= ("title", "id")
   list_filter= ("title",)
   prepopulated_fields = {'slug':("title",)}
   inlines = ( ProductInline, )
   
class BrandAdmin(admin.ModelAdmin):
   list_display= ("title", "id", "get_cover")
   list_filter= ("title",)
   
class CategoryAdmin(admin.ModelAdmin):
   list_display= ("title", "id", "category", "get_cover")
   list_filter= ("title", "category")

   
class ProductImageAdmin(admin.ModelAdmin):
   list_display= ("product", "id", "get_image")
   list_filter= ("product",)
   
class BannerAdmin(admin.ModelAdmin):
   list_display= ("title", "id", "get_cover")


     

admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Banner, BannerAdmin)







