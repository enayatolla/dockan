from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^i18n/', include('django.conf.urls.i18n')), #Adds Persian language support

    path('' , include("apps.shop.urls", namespace= 'shop')),
    path('checkout/' , include("apps.cart.urls"), name='checkout'),
    path('users/' , include("apps.users.urls"), name='users'),
    path('staff/' , include("apps.staff.urls"), name='staff'),
]


if settings.DEBUG:
    urlpatterns= [
        path("__reload__/", include("django_browser_reload.urls")),
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    ] + urlpatterns





