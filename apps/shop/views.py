from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db.models import Q, QuerySet, Sum, Avg , F
from .models import Product , Brand, Review, Category
from .tasks import *
from django.views.decorators.cache import cache_page

class HomePageView(View):
   def get(self, request, **kwags):
      categories = Category.objects.all()[0:4]
      featured = Product.objects.all()[0:6]
      
      banner_list = [
         {
            "id": "1",
            "title": "Tiny and Perfect eCommerce Template",
            "description": "Zay Shop is an eCommerce HTML5 CSS template withlatest version of Bootstrap 5 (beta 1). This template is 100 free provided by",
            "cover": "/static/images/18.jpg",
         },
         {
            "id": "2",
            "title": "Tiny and Perfect eCommerce Template",
            "description": "Zay Shop is an eCommerce HTML5 CSS template withlatest version of Bootstrap 5 (beta 1). This template is 100 free provided by",
            "cover": "/static/images/18.jpg",
         },
         {
            "id": "2",
            "title": "Tiny and Perfect eCommerce Template",
            "description": "Zay Shop is an eCommerce HTML5 CSS template withlatest version of Bootstrap 5 (beta 1). This template is 100 free provided by",
            "cover": "/static/images/18.jpg",
         },
      ]

      context = { "categories": categories, "featured_list": featured, "banner_list":banner_list }
      return render(request, "shop/Home.html", context)
   

class ProductListView(View):
   def get(self, request, **kwags):
      
      colors= request.GET.getlist("colors")
      sizes= request.GET.getlist("sizes")
      min, max= request.GET.get("min_price"), request.GET.get("max_price")
      print(colors, sizes, min, max)
      
      test_query = Product.objects.filter(Q(title= "book") | Q(category=2))
      test_query = Product.objects.filter(title= F("description") + "" )
      
      
      brand_list = Brand.objects.all().order_by('-created_at')
      product_list = Product.objects.all().order_by("-created_at")
      colors = ["red", "black", "blue", "green", "white"]
      sizes = ["s", "m", "l", "xl", "xxl", "xxxl"]
      
      context={"object_list": product_list, "brand_list": brand_list, "colors": colors, "sizes": sizes}
      
      return render(request, "shop/product_list.html", context )
   

class ProductDetailView(View):
   def get(self, request, pk, slug ):
      from django.core.cache import cache
      cache.clear()
      
      colors = [ "black", "white" ]
 
      product = Product.objects.get(id = pk)
      product_list = Product.objects.all()
      context={"related": product_list, "product": product, "colors": colors} 
      return render(request, "shop/product_detail.html", context )
   
   def post(self, request, pk, slug):
 
      product = Product.objects.get(id = pk)
      product_list = Product.objects.all()
      context={"related": product_list, "product": product} 
      return render(request, "shop/product_detail.html", context )
   

class SearchView(View):
   def get(self, request, **kwags):
   
      taskCelery.delay()
   
      brand_list = Brand.objects.all().order_by('-created_at')
      product_list = Product.objects.all().order_by("-created_at")
      context={"object_list": product_list, "brand_list": brand_list}
      
      return render(request, "shop/product_list.html", context)







