from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db.models import Q, QuerySet, Sum, Avg , F
from apps.products.models import Product , Brand, Category
from .tasks import *
from django.views.decorators.cache import cache_page

class HomePageView(View):
   def get(self, request, **kwags):
      categories = Category.objects.all()[0:4]
      special_products = Product.objects.all().order_by('-created_at')[0:6]
      # banner_list = Banner.objects.all().order_by('-created_at')

      context = { 
         "categories": categories,
         "special_products": special_products,
         "banner_list":"banner_list",
         'title': 'فروشگاه اینترنتی پوشاک',
      }
      return render(request, "shop/home/index.html", context)
   

# class ProductListView(View):
#    def get(self, request, **kwags):
      
#       colors= request.GET.getlist("colors")
#       sizes= request.GET.getlist("sizes")
#       min, max= request.GET.get("min_price"), request.GET.get("max_price")
#       print(colors, sizes, min, max)
      
#       test_query = Product.objects.filter(Q(title= "book") | Q(category=2))
#       test_query = Product.objects.filter(title= F("description") + "" )
      
      
#       brand_list = Brand.objects.all().order_by('-created_at')
#       product_list = Product.objects.all().order_by("-created_at")
#       colors = ["red", "black", "blue", "green", "white"]
#       sizes = ["s", "m", "l", "xl", "xxl", "xxxl"]
      
#       context={"object_list": product_list, "brand_list": brand_list, "colors": colors, "sizes": sizes}
      
#       return render(request, "shop/product_list.html", context )
   

class ProductDetailView(View):
   def get(self, request, pk, slug ):
      product = Product.objects.get(id = pk)
      # prefetch_related: catch reverse query
      # select_related: catch ForeignKey fields query
      product_list = Product.objects \
         .prefetch_related('variations') \
         .select_related('brand', 'category')
      
      product_list = Product.objects.prefetch_related('variations').select_related('brand', 'category')

      context={"related": product_list, "product": product} 
      return render(request, "shop/product_detail/index.html", context )
   
   









