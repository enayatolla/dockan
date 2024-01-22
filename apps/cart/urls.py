from django.urls import path
from . import views


app_name = "cart"

urlpatterns =[
   path("cart/", views.CartPageView.as_view(), name="cart"),
   path("handle-cart/<int:pk>/", views.HandelCart.as_view(), name="handle_cart"),
   path("apply-discount-code/", views.ApplyDiscountCode.as_view(), name="apply_discount_code"),
   path("handle-address/", views.HandleAddress.as_view(), name="handle_address"),
   path("handle-shipping-method/", views.HandleShippingMethod.as_view(), name="handle_shipping_method"),
   path("handle-order/", views.HandleOrder.as_view(), name="handle_order"),
   path("shipping/", views.CheckoutShippingView.as_view(), name="checkout_shipping"),
   path("payment/", views.CheckoutPaymentView.as_view(), name="checkout_payment"),
   path("thank-you/", views.ThankfullView.as_view(), name="thankyou"),
]