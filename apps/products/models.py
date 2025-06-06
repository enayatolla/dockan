from django.db import models
from django.utils.html import format_html
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey



User= get_user_model()


class Category (MPTTModel):
   title = models.CharField(_("عنوان"), max_length=128)
   parent = TreeForeignKey(
      'self',
      on_delete=models.CASCADE,
      null=True,
      blank=True,
      related_name='children',
      verbose_name=_("دسته بندی والد")
   )
   cover = models.ImageField(_("تصویر"), upload_to='images/category_cover/', null=True, blank=True)
   created_at= models.DateTimeField(auto_now_add= True)

   class Meta:
      unique_together = (('title', 'parent'),)
      verbose_name = "دسته بندی"
      verbose_name_plural = "دسته بندی ها"

   class MPTTMeta:
      order_insertion_by = ('title',)

   def get_object_cover(self):
      if self.cover:
         return format_html(
            f"""<img src='{self.cover.url}' height='120px' style='object-fit:cover'>"""
         )
      else:
         return "No cover found"
      
   def __str__(self):
      return self.title

class Brand (models.Model):
   title = models.CharField(max_length=128)
   created_at= models.DateTimeField(auto_now_add= True)
   cover = models.FileField(_("تصویر"), upload_to='images/brand_cover/', null=True, blank=True)

   class Meta:
      verbose_name = "نام تجاری"
      verbose_name_plural = "نام های تجاری"

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
   user= models.ForeignKey(User, on_delete= models.SET_NULL, null= True, related_name="products", verbose_name=_("کاربر"))
   brand= models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name='products', verbose_name=_("نام تجاری"))
   category= models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products', verbose_name=_("دسته بندی"))
   title= models.CharField(_("عنوان"), max_length=200, unique=True)
   slug= models.SlugField(_("کلمات کلیدی"), max_length=256, null=True, blank=True, allow_unicode=True)
   sku = models.CharField(_("شناسه یکتا"), max_length=100, unique=True, null=True, blank=True)
   description= models.TextField(_("توضیحات"),max_length=800, null=True, blank=True)
   base_price= models.CharField(_("قیمت پایه"), max_length=16)
   is_variable= models.BooleanField(_("آیا متغیر است؟"), default=False)  # Indicates if the product has variations
   created_at= models.DateTimeField(auto_now_add= True)
   cover= models.ImageField(_("تصویر نمایش"), upload_to='images/product_cover')

   class Meta:
      verbose_name = "محصول"
      verbose_name_plural = "محصولات"

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
   title = models.CharField(_('عنوان'), max_length=100)  # Example: Size, Color
   fa_title = models.CharField(_('عنوان به فارسی'), max_length=100)  # Example: Size, Color

   class Meta:
      verbose_name = "نوع متغیر"
      verbose_name_plural = "انواع متغیر"

   def __str__(self):
      return f"{self.title}"


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
   variation = models.ForeignKey(ProductVariation, on_delete=models.CASCADE, related_name="images", null=True, blank=True)

   def __str__(self):
      return self.alt_text if self.alt_text else "Product Image"


class ProductFeature(models.Model):
   """
   Represents a feature or attribute of a product.
   """
   product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="features")
   title = models.CharField(max_length=200)
   description = models.CharField(max_length=400, blank=True)

   def __str__(self):
      return self.title


class ProductDescription(models.Model):
   """
   Represents a detailed description of a product.
   """
   product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="descriptions")
   content = models.TextField()
   image = models.ImageField(upload_to="images/product_descriptions/", blank=True, null=True)

   def __str__(self):
      return f"Description for {self.product.title}"




