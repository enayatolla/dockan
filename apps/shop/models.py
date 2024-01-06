from collections.abc import Iterable
from django.db import models
from apps.users.models import User
from django.utils.text import slugify
from django.utils.html import format_html
from django.urls import reverse

def validate_file_extension(value):
   import os
   from django.core.exceptions import ValidationError
   ext = os.path.splitext(value.name)[1]
   valid_extensions = ['.jpeg', '.jpg', '.png', '.webp', ".mp4"] 
   if not ext.lower() in valid_extensions:
      raise ValidationError('Unsupported file extension.')


class Category (models.Model):
   id= models.BigAutoField(primary_key= True, editable=False)
   title = models.CharField(max_length=128, null=False, blank=False)
   category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True,blank=True, related_name='categories')
   created_at= models.DateTimeField(auto_now_add= True, null=True)
   cover = models.FileField(
      upload_to='images/category_cover/', 
      validators= [validate_file_extension],
      null=True
   )
   def __str__(self):
      return self.title


class Brand (models.Model):
   id= models.BigAutoField(primary_key= True, editable=False)
   title = models.CharField(max_length=128, null=True, blank=True)
   created_at= models.DateTimeField(auto_now_add= True, null=True)
   cover = models.FileField(
      upload_to='images/brand_cover/', 
      validators= [validate_file_extension] ,
      null=True
   )
   def __str__(self):
      return self.title


class ProductImage(models.Model):
   id= models.BigAutoField(primary_key= True, editable=False)
   product= models.ForeignKey(to='Product', on_delete=models.CASCADE , null= True, blank=True, related_name="images")
   created_at= models.DateTimeField(auto_now_add= True, null=True)
   image = models.FileField(
      upload_to='images/product_images/',
      validators= [validate_file_extension],
      null=True
   )


class Product(models.Model):
   id= models.BigAutoField(primary_key= True, editable=False)
   brand= models.ForeignKey(to=Brand, on_delete=models.SET_NULL, null=True)
   category= models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True)
   user= models.ForeignKey(User, on_delete= models.SET_NULL, null=True)

   title= models.TextField(max_length=256, null=True)
   slug= models.SlugField(max_length=256, null=True , blank=True, allow_unicode=True)
   color=models.CharField(max_length=256, null=True, blank=True)
   size=models.CharField(max_length=256, null=True, blank=True)
   weight=models.CharField(max_length=256, null=True, blank=True)
   description= models.TextField(null=True, blank= True)
   price= models.IntegerField(default= 0, null=True, blank=True)
   count_in_stock= models.IntegerField(null=False, blank=True, default= 0)
   created_at= models.DateTimeField(auto_now_add= True, null=True)
   cover= models.ImageField(upload_to='images/product_cover',null=False)
   
   def __str__(self):
      return self.title
   
   def get_absolute_url(self):
      return reverse("shop:product_detail", kwargs={"pk": self.id, "slug": self.slug})
   
   def save(self) -> None:
      self.slug = slugify(self.title, allow_unicode= True)
      return super(Product, self).save()
   
   def get_cover(self):
      if self.cover:
         return format_html(
            f"<img src='{self.cover.url}' width='50px' height='40px' style='object-fit:cover'>"
         )
      else:
         return format_html("<h4>no cover</h4>")
   
   



class Review (models .Model):
   id = models.BigAutoField(primary_key=True, editable=False)
   product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='reviews')
   user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

   rate = models.IntegerField(null=True, blank=True, default=0)
   comment = models.TextField(null=True, blank=True)
   created_at = models.DateTimeField(auto_now_add=True, null=True)
   def __str__(self) -> str:
      return str(self.product.title)






