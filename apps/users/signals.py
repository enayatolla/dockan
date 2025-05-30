from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, User
# from apps.cart.models import Cart

@receiver(post_save, sender=User)
def create_profile_and_shopping_cart(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        # Cart.objects.create(user=instance)






