from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import JsonResponse
from apps.shop.models import Product,ProductType
from apps.cart.models import CartItem, Cart, ShippingAddress, Order, OrderItem
from rest_framework.views import APIView
from rest_framework.response import Response



CART_SESSION_ID = "cart"

class SessionCart:
   def __init__(self, request):
      self.session = request.session
      cart = self.session.get(CART_SESSION_ID)
      if not cart :
         cart= self.session[CART_SESSION_ID]= {}
      self.cart= cart
      
   def __iter__(self):
      cart= self.cart.copy()
      for cartItem in cart.values():
         product= Product.objects.get(id= int(cartItem["id"]) )
         cartItem["product"] = product
         cartItem["total"]= int(cartItem["quantity"]) * int(cartItem["price"])
         cartItem["id"]= self.unique_id_generator(product.id, cartItem['size'])
         yield cartItem


   def total_price(self):
      cart = self.cart.values()
      total = 0
      for item in cart :
         total += item['total']
      return total
         
   def unique_id_generator(self, id, size):
      return f'{id}-{size}'

   
   def add(self, product, quantity, price, size):
      unique= self.unique_id_generator(product.id, size)
      if unique not in self.cart:
         self.cart[unique] = {
            "quantity": 0, 
            "price": str(price), 
            "size": size, 
            "id":product.id
         }
      self.cart[unique]['quantity'] += int(quantity)
      self.save()
      
   def delete(self, id):
      if id in self.cart :
         del self.cart[id]
         self.save()
   
   def save(self):
      self.session.modified = True
   
   def remove_all_items(self):
      del self.session[CART_SESSION_ID]



class CartPageView(View):
   def get(self, request, **kwags):
      if request.user.is_authenticated:
         cart = Cart.objects.filter(user= request.user).first()
         cart = cart.cart_items.all().order_by('-created_at')
      else:
         cart = SessionCart(request)
      
      return render(request, "cart/cart.html", { "cart": cart })


class ThankfullView(View):
   def get(self, request, **kwags):
     
      return render(request, "cart/thankyou.html", context={"cartitem_list": 'cartItems'} )
   
  
class CheckoutShippingView(View):
   def get(self, request, **kwags):
      cart = request.user.cart
      context={'cart': cart } 
      return render(request, "cart/shipping.html", context)
   
   
class CheckoutPaymentView(View):
   def get(self, request, **kwags):
      cart = request.user.cart
      return render(request, "cart/payment.html", { "cart": cart })
 
   
class HandelCart(APIView):
   def post(self, request, pk):
      product_id = request.POST.get("product_id")
      size = request.POST.get("product_size")
      quantity = request.POST.get("product_quantity")
      product = Product.objects.get(id=product_id)
      type = ProductType.objects.filter(product= product, title= size).first()
      price = type.price
      
      if request.user.is_authenticated:
         cartItem = CartItem.objects.filter(
            product__id= product_id, 
            product_type= type, 
            cart= request.user.cart
         ).first()
         if cartItem:
            cartItem.quantity += int(quantity)
            cartItem.save()
         else:
            cartItem= CartItem.objects.create(
               product_type= type,
               product=product,
               cart= request.user.cart,
               quantity= quantity
            )
      else:
         cart = SessionCart(request)
         cart.add(product, quantity, price, size)
 
      return redirect( f"/products/detail/{product_id}/{product.slug}/" )

   def delete(self, request, pk):
      # pk =  request.data['pk']
      if request.user.is_authenticated:
         CartItem.objects.filter(id=pk).delete()
      else:
         cart = SessionCart(request)
         cart.delete(pk)
      
      total_price= request.user.cart.total_price()
      return JsonResponse({ 'pk': pk, 'cart_price': total_price })
 
   def put(self, request, pk):
      qty = int(request.data['qty'])
      pk = request.data['pk']
      
      if qty == 0 :
         cartItem= CartItem.objects.filter(id= pk).delete()
         cart_item_price = 0
      else:
         cartItem = CartItem.objects.filter(id= pk).first()
         cartItem.quantity= qty
         cartItem.save()
         cart_item_price = cartItem.get_price()
         
      total_price= request.user.cart.total_price()
      return JsonResponse({'pk':pk, 'qty': qty, 'cart_price': total_price, 'cart_item_price':cart_item_price})


class ApplyDiscountCode(APIView):
   def post(self, request):
      # print('', request.data)
      
      return Response({}, status= 200)

   
class HandleAddress(APIView):
   def post(self, request):
      print('HandleAddress', request.data)
      try:
         cart = request.user.cart         
         if cart.shipping_address:
            if cart.shipping_address.id ==  int(request.data['pk']):
               cart.shipping_address = None
               cart.save()
               return Response({}, status= 204)
            else:
               cart.shipping_address = ShippingAddress.objects.get(id= int(request.data['pk']))
               cart.save()
         else:
            cart.shipping_address = ShippingAddress.objects.get(id= int(request.data['pk']))
            cart.save()
            
      except:
         return Response({}, status= 400)
      return Response({}, status= 200)


class HandleShippingMethod(APIView):
   def post(self, request):
      try:
         cart = request.user.cart 
         if int(cart.shipping_method) == 30000 :
            if request.data['method'] == 'normal':
               return Response({}, status= 400)
            else:
               cart.shipping_method = cart.SPECIAL
               cart.save()
         else:
            if request.data['method'] ==  'special':
               return Response({}, status= 400)
            else:
               cart.shipping_method = cart.NORMAL
               cart.save()
      except:
         return Response({}, status= 400)
      return Response({}, status= 200)

   
class HandleOrder(APIView):
   def post(self, request):
      if not request.user.is_authenticated:
         return Response({}, status= 403)
      
      try:
         cart = request.user.cart
         cart_items= cart.cart_items.all()

         if len(cart_items) == 0:
            return Response(data={}, status=400)
         new_order= Order.objects.create(
            user= request.user,
            shipping_address= cart.shipping_address,
            shipping_method= 'normal',
            shipping_price= cart.shipping_price(),
            shipping_day= None,
            payment_method= 'local',
            total_items= cart.total_items(),
            total_price= cart.total_price(),
         )
         for cartItem in cart_items:
            product= Product.objects.get(id=cartItem.product.id)
            product_type= ProductType.objects.get(id=cartItem.product_type.id)
            orderItem= OrderItem.objects.create(
               order= new_order,
               product= product,
               product_type= product_type,
               title= product.title,
               quantity= cartItem.quantity,
               price= cartItem.quantity * product_type.price,
            )
            product_type.count_in_stock -= int(cartItem.quantity)
            product_type.save()
            if orderItem :
               print(orderItem.id)
               for cartItem in cart_items:
                  CartItem.objects.filter(id = cartItem.id).delete()           
               
         return Response({}, status=201)
      except:
         return Response({}, status= 400)

   







