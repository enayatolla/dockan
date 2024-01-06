from django.shortcuts import render
from django.views import View
from .models import Product , Brand, Review


class HomePageView(View):
   def get(self, request, **kwags):
      

      return render(request, "shop/index.html", context={} )
   

class ProductListView(View):
   def get(self, request, **kwags):
      
      brand_list = Brand.objects.all().order_by('-created_at')
      product_list = Product.objects.all().order_by("-created_at")
      context={"object_list": product_list, "brand_list": brand_list}
      
      return render(request, "shop/product_list.html", context )
   

class ProductDetailView(View):
   def get(self, request, pk, slug ):
      images =[
         "/static/shop/img/product_single_01.jpg",
         "/static/shop/img/product_single_02.jpg",
         "/static/shop/img/product_single_03.jpg",
         "/static/shop/img/product_single_04.jpg",
         "/static/shop/img/product_single_05.jpg",
         "/static/shop/img/product_single_06.jpg",
         "/static/shop/img/product_single_07.jpg",
         "/static/shop/img/product_single_08.jpg",
         "/static/shop/img/product_single_09.jpg",
         "/static/shop/img/product_single_09.jpg",
      ]
      related =[
         '/static/shop/img/shop_01.jpg',
         '/static/shop/img/shop_02.jpg',
         '/static/shop/img/shop_03.jpg',
         '/static/shop/img/shop_04.jpg',
         '/static/shop/img/shop_05.jpg',
         '/static/shop/img/shop_06.jpg',
         '/static/shop/img/shop_07.jpg',
         '/static/shop/img/shop_08.jpg',
         '/static/shop/img/shop_09.jpg',
         '/static/shop/img/shop_10.jpg',
         '/static/shop/img/shop_11.jpg',
         '/static/shop/img/shop_10.jpg',
      ]
      
      product = Product.objects.get(id = pk)
      product_list = Product.objects.all()
      images = product.images
      print(images)
      context={"related": product_list, "product": product} 
      return render(request, "shop/product_detail.html", context )
   
   
class SearchView(View):
   def get(self, request, **kwags):
   
      brand_list = Brand.objects.all().order_by('-created_at')
      product_list = Product.objects.all().order_by("-created_at")
      context={"object_list": product_list, "brand_list": brand_list}
      
      return render(request, "shop/product_list.html", context)
   
   
   