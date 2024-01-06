from django.urls import path
from . import views


app_name = "cart"

urlpatterns =[
   path("cart/", views.CartPageView.as_view(), name="cart"),
   path("checkout/shipping/", views.CheckoutShippingView.as_view(), name="checkout_shipping"),
   path("checkout/payment/", views.CheckoutPaymentView.as_view(), name="checkout_payment"),
   path("thank-you/", views.ThankfullView.as_view(), name="thankyou"),
]