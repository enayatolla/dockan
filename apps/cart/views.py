from django.shortcuts import render
from django.views import View

cartItems = [
   {
      "id": 7889873547459497 ,
      "title": "Product Name",
      "cover": "https://via.placeholder.com/250x250/5fa9f8/ffffff",
      "brand": "brand",
      "category": "category",
      "price": "300000",
      "quantity": 2,
   },
   {
      "id": 7889873547459497 ,
      "title": "Product Name",
      "cover": "https://via.placeholder.com/250x250/5fa9f8/ffffff",
      "brand": "brand",
      "category": "category",
      "price": "300000",
      "quantity": 2,
   },
   {
      "id": 7889873547459497 ,
      "title": "Product Name",
      "cover": "https://via.placeholder.com/250x250/5fa9f8/ffffff",
      "brand": "brand",
      "category": "category",
      "price": "300000",
      "quantity": 2,
   },
   {
      "id": 7889873547459497 ,
      "title": "Product Name",
      "cover": "https://via.placeholder.com/250x250/5fa9f8/ffffff",
      "brand": "brand",
      "category": "category",
      "price": "300000",
      "quantity": 2,
   },

]
      

class CartPageView(View):
   def get(self, request, **kwags):
     
      return render(request, "cart/cart.html", context={"cartitem_list": cartItems} )
   
   
class CheckoutShippingView(View):
   def get(self, request, **kwags):
     
      return render(request, "cart/shipping.html", context={"cartitem_list": cartItems} )
   
   
class CheckoutPaymentView(View):
   def get(self, request, **kwags):
     
      return render(request, "cart/payment.html", context={"cartitem_list": cartItems} )
   
   
class ThankfullView(View):
   def get(self, request, **kwags):
     
      return render(request, "cart/thankyou.html", context={"cartitem_list": cartItems} )
   
   
   