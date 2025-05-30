from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('' , include("apps.shop.urls", namespace= 'shop')),
    path('checkout/' , include("apps.cart.urls"), name='checkout'),
    path('users/' , include("apps.users.urls"), name='users'),
    path('staff/' , include("apps.staff.urls"), name='staff'),
]
urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)




