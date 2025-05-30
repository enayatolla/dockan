from django.db.models.signals import post_save
from django.dispatch import receiver
# from .models import Product, ProductGroup

# @receiver(post_save, sender=Product)
# def create_group(sender, instance, created, **kwargs):
#     if created:
#         group =  ProductGroup.objects.filter(slug= instance.slug).first()
#         if group :
#             # instance in not the first product
#             instance.group = group
#             instance.save()
#         else:
#             group = ProductGroup.objects.create(title=instance.title)
#             instance.group = group
#             instance.save()
        
        






