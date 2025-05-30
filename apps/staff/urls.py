from django.urls import path, re_path
from . import views



app_name= 'staff'
urlpatterns = [
   path('dashboard/', views.Dashboard.as_view(), name="dashboard"),
   path('seller-profile/', views.Dashboard.as_view(), name="seller_profile"),
   path('my-market/', views.Dashboard.as_view(), name="my_market"),
   path('product-list/', views.ProductList.as_view(), name="product_list"),
   # re_path(r'pd/(?P<pk>[-\w]+)/(?P<slug>[-\w]+)/', views.ProductDetail.as_view(), name="product_detail"),
   # path('new-product/', views.NewProduct.as_view(), name="new_product"),
   path('order-list/', views.Dashboard.as_view(), name="order_list"),
   path('settings/', views.Dashboard.as_view(), name="settings"),
]
