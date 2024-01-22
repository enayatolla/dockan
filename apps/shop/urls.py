from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from . import views


app_name = "shop"
urlpatterns =[
   path("", cache_page(0)(views.HomePageView.as_view()), name="home_page"),
   path("products/", (views.ProductListView.as_view()), name="product_list"),
   re_path(
      r"products/detail/(?P<pk>[-\w]+)/(?P<slug>[-\w]+)/", 
      (views.ProductDetailView.as_view()),
      name="product_detail"
   ),
   path("search/", views.SearchView.as_view(), name="search"),
]







