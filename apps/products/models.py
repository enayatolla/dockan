from django.db import models
from django.utils.html import format_html
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse


User= get_user_model()


class Category (models.Model):
   title = models.CharField(max_length=128)
   category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True,blank=True, related_name='categories')
   cover = models.ImageField(upload_to='images/category_cover/')
   created_at= models.DateTimeField(auto_now_add= True)
      
   def __str__(self):
      return self.title
   
   def get_cover(self):
      if self.cover:
         return format_html(
            f"<img src='{self.cover.url}' style='object-fit:cover width:50px; height:40px'>"
         )
      else:
         return format_html("<h4>no cover</h4>")


class Brand (models.Model):
   title = models.CharField(max_length=128)
   created_at= models.DateTimeField(auto_now_add= True)
   cover = models.FileField(upload_to='images/brand_cover/')
   
   def __str__(self):
      return self.title
   
   def get_cover(self):
      if self.cover:
         return format_html(
            f"<img src='{self.cover.url}' width='50px' height='40px' style='object-fit:cover'>"
         )
      else:
         return format_html("<h4>no cover</h4>")


class Product(models.Model):
   """
   Product, handels all products instances
   """
   user= models.ForeignKey(User, on_delete= models.SET_NULL, null= True, related_name="products")
   brand= models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name='products')
   category= models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
   title= models.CharField(max_length=200, unique=True)
   slug= models.SlugField(max_length=256, null=True, blank=True, allow_unicode=True)
   sku = models.CharField(max_length=100, unique=True, null=True)
   description= models.TextField(blank=True)
   base_price= models.CharField(max_length=16)
   is_variable= models.BooleanField(default=False)  # Indicates if the product has variations
   created_at= models.DateTimeField(auto_now_add= True)
   cover= models.ImageField(upload_to='images/product_cover')

   def save(self, *args, **kwargs):
      if self.sku == "":
         self.sku = None

      if not self.title == "":
         if not self.slug == slugify(self.title, allow_unicode=True):
            self.slug = slugify(self.title, allow_unicode=True)
      return super().save(*args, **kwargs)

   def get_absolute_url(self):
      return reverse("shop:product_detail", kwargs={"pk": self.pk, "slug": self.slug})
   
   def get_cover(self):
      if self.cover:
         return format_html(f"<img src='{self.cover.url}' width='30px' height='30px' style='object-fit:cover'>")
      else:
         return format_html("<p>no cover</p>")
      
   def __str__(self):
      return self.title


class Variation(models.Model):
   """
   Represents a variation type for a product, e.g., Size, Color, Weight.
   """
   title = models.CharField(max_length=100)  # Example: Size, Color

   def __str__(self):
      return f"{self.title}"


# class VariationOption(models.Model):
#    """
#    Represents a specific option for a variation, e.g., Red, Blue for Color.
#    """
#    variation = models.ForeignKey(Variation, on_delete=models.CASCADE, related_name="options")
#    value = models.CharField(max_length=100)

#    def __str__(self):
#       return f"{self.value} ({self.variation.title})"


class ProductVariation(models.Model):
   """
   Represents a specific combination of variation options for a product.
   """
   product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variations")
   variation = models.ForeignKey(Variation, on_delete=models.CASCADE, null=True)
   value = models.CharField(max_length=100, null=True)

   def __str__(self):
      return f"{self.product.title} - {self.value}"


class ProductImage(models.Model):
   """
   Represents images for products or specific product variations.
   """
   image = models.ImageField(upload_to="images/product_images/")
   alt_text = models.CharField(max_length=200, blank=True)

   def __str__(self):
      return self.alt_text if self.alt_text else "Product Image"









