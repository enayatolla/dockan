from rest_framework.serializers import ModelSerializer, Serializer
from .models import CartItem


class CartItemSeralizer(ModelSerializer):
   class Meta:
      model= CartItem
      fields= '__all__'














