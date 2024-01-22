from rest_framework.serializers import ModelSerializer
from .models import Otp, ShippingAddress


class OtpSlz(ModelSerializer):
   class Meta:
      model=Otp
      fields= '__all__'


class AddressSlz(ModelSerializer):
   class Meta:
      model= ShippingAddress
      fields= '__all__'