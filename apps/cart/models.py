from django.db import models
from apps.users.models import User
from apps.shop.models import Product


class ShippingAddress (models.Model):
   id = models.BigAutoField(primary_key=True, editable=False)
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="addresses")
   created_at= models.DateTimeField(auto_now_add= True, null=True, blank=True)

   address = models.CharField(max_length=256, null=True, blank=True)
   address_compact= models.CharField(max_length=128, null=True, blank=True)
   country = models.CharField(max_length=32, null=True, blank=True)
   city= models.CharField(max_length=32, null=True, blank=True)
   district= models.CharField(max_length=128, null=True, blank=True)
   last= models.CharField(max_length=64, null=True, blank=True)
   latitude=models.CharField(max_length=32, null=True, blank=True)
   longitude=models.CharField(max_length=32, null=True, blank=True)
   neighbourhood= models.CharField(max_length=32, null=True, blank=True)
   phone=models.CharField(max_length=16, null=True, blank=True)
   plaque= models.CharField(max_length=16, null=True, blank=True)
   postal_address= models.CharField(max_length=64, null=True, blank=True)
   postal_code= models.CharField(max_length=32, null=True, blank=True)
   primary= models.CharField(max_length=64, null=True, blank=True)
   province= models.CharField(max_length=32, null=True, blank=True)
   region= models.CharField(max_length=32, null=True, blank=True)
   rural_district= models.CharField(max_length=64, null=True, blank=True)
   stairs=models.CharField(max_length=32, null=True, blank=True)
   village= models.CharField(max_length=64, null=True, blank=True)

   def __str__(self):
      return str(self.user)


class Order(models.Model):
   id = models.BigAutoField(primary_key=True, editable=False)
   user = models.ForeignKey (User, on_delete=models.SET_NULL, null=True,related_name='orders',)
   shipping_address = models.ForeignKey (ShippingAddress, on_delete=models.SET_NULL, null=True,related_name='shipping_address')
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


class OrderItem(models.Model):
   id = models.BigAutoField(primary_key=True, editable=False)
   title= models.TextField(max_length=256, null=True)
   product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
   order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,related_name='order_items')
   quantity = models.IntegerField( default=1, null=True, blank=True)
   price = models.IntegerField(default=0, null=True, blank=True)


class Cart(models.Model):
   id= models.BigAutoField(primary_key= True, editable=False)
   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

   def __str__(self) -> str:
      return str(self.user.username)


class CartItem(models.Model):
   id= models.BigAutoField(primary_key= True, editable=False)
   cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   quantity = models.IntegerField(default=1, null=True, blank=True)
   created_at= models.DateTimeField(auto_now_add= True, null=True, blank=True)

   def __str__(self) -> str:
      return str(self.product.title)




