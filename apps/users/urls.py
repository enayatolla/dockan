from django.urls import path
from .views import *


app_name= "users"
urlpatterns =[
   path("register/", UserRegisterView.as_view(), name='user_register'),
   path("login/", UserLogin.as_view(), name='user_login'),
   path("logout/", user_logout, name='user_logout'),
   path("dashboard/", DashboardView.as_view(), name='dashboard'),
   path("address/", AdressesView.as_view(), name='address'),
   path("change-password/", ChangePassword.as_view(), name='change_password'),
   path("change-email/", ChangeEmail.as_view(), name='change_email'),
   path("change-fullname/", ChangeFullName.as_view(), name='change_fullname'),
   path("change-phonenumber/", ChangePhoneNumber.as_view(), name='change_phonenumber'),
   path("user-acount/", UserAcount.as_view(), name='user_acount'),
   path("handle-address/", HandleAddress.as_view(), name='handle_address'),
]

