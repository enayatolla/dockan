from datetime import datetime, timedelta
from typing import Any
from django.db import models
from apps.users.models import User, ShippingAddress
from apps.products.models import Product, ProductVariation



class DiscountCode(models.Model):
   title= models.CharField(max_length= 128, null=True)
   code = models.CharField(max_length= 32, null=True)
   percent = models.IntegerField(default = 100,null=True)
   expiration_date = models.DateTimeField(default= None, null=True, blank=True)
   def __init__(self, *args, **kwargs) -> None:
      super(DiscountCode, self).__init__(*args, **kwargs)
      if self.expiration_date == None :
         self.expiration_date = datetime.now() + timedelta(days= 1)


class Order(models.Model):
   id = models.BigAutoField(primary_key=True, editable=False)
   user = models.ForeignKey (User, on_delete=models.SET_NULL, null=True,related_name='orders',)
   shipping_address = models.ForeignKey (ShippingAddress, on_delete=models.SET_NULL, null=True, related_name='addresses')
   shipping_method = models.CharField (max_length=64, null=True,blank=True)
   shipping_day = models.CharField (max_length=64, null=True, blank=True)
   shipping_price = models.IntegerField(default=25000, null=True, blank=True)
   payment_method = models.CharField(max_length=32, null=True, blank=True)
   total_items = models.IntegerField(default=0, null=True, blank= True)
   total_price = models.IntegerField(default=0, null=True, blank= True)
   is_paid = models. BooleanField(default=False)
   paid_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
   is_delivered = models.BooleanField(default=False)
   delivere_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   def __str__(self):
      return str(self.user.username)
   
   def get_created_at(self):
      return self.created_at +  timedelta(minutes=210)


class OrderItem(models.Model):
   id = models.BigAutoField(primary_key=True, editable=False)
   order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,related_name='order_items')
   product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
   product_variation = models.ForeignKey(ProductVariation, on_delete=models.SET_NULL, null=True)
   title= models.TextField(max_length=256, null=True)
   quantity = models.IntegerField( default=1, null=True, blank=True)
   price = models.IntegerField(default=0, null=True, blank=True)


class Cart(models.Model):
   id= models.BigAutoField(primary_key= True, editable=False)
   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
   discount = models.ForeignKey(DiscountCode, on_delete=models.SET_NULL, null=True, blank= True)
   shipping_address = models.OneToOneField(ShippingAddress, on_delete=models.SET_NULL, null=True, blank= True)
   NORMAL = 30000
   SPECIAL = 80000
   shipping_method = models.IntegerField( default= NORMAL)

   def __str__(self) -> str:
      return str(self.user.username)
   
   def total_price(self):
      totalPrice = 0
      cart_items= self.cart_items.all()
      for item in cart_items:
         totalPrice += item.get_price()
      return totalPrice
   
   def discounted_total_price(self):
      amount = int(self.total_price()) - int(self.discount_amount())
      return amount
   
   def total_items(self):
      total = 0
      for item in self.cart_items.all() :
         total += item.quantity
      return total
   
   def shipping_price(self):
      return (self.shipping_method)
         
   def discount_amount(self):
      if self.discount :
         coefficient = self.discount.percent / 100
         amount = self.total_price() * coefficient
      else:
         amount = 0
      return amount
   
   def payment_amount(self):
      amount = int(self.total_price()) - int(self.discount_amount()) + int(self.shipping_price())
      return amount
         
         
class CartItem(models.Model):
   id= models.BigAutoField(primary_key= True, editable=False)
   cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   product_variation = models.ForeignKey(ProductVariation, on_delete=models.CASCADE , null=True)
   quantity = models.IntegerField(default=1, null=True, blank=True)
   created_at= models.DateTimeField(auto_now_add= True, null=True, blank=True)

   def __str__(self) -> str:
      return str(self.product.title)
   
   def get_price(self):
      return int(self.quantity) * int(self.product_type.price)

   def range_qty(self):
      return list(range(0, self.product_type.count_in_stock))


