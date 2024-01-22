from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from apps.users.models import User, Otp
from django.views.generic import TemplateView , View
from .forms import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import OtpSlz, AddressSlz
from django.utils import timezone
from datetime import timedelta


class DashboardView(View):
   def get(self, request, **kwarts):
      form = UserProfileForm(request.GET)
      
      return render(request, 'users/Dashboard.html', context={ })
   

class UserRegisterView(TemplateView):
   def post(self, request):
      if request.user.is_authenticated :
         return redirect("shop:home_page")
      
      form = UserCreationForm(request.POST)
      print("BEFORE is_valid()")
      if form.is_valid():
         print("AFTER is_valid()")
         print("BEFOR form.save()")
         user = form.save()
         login(request, user)
         print("AFTER form.save()")
         return redirect("shop:home_page")
         
      return render(request, 'users/auth-register-basic.html', context={"form": form})
   
   def get(self, request):
      if request.user.is_authenticated :
         return redirect("shop:home_page")
      
      form = UserCreationForm()
      
      return render(request, 'users/auth-register-basic.html', context={"form": form})
      
      
class AdressesView(TemplateView):
   def post(self, request):
      if not request.user.is_authenticated :
         return Response({}, status=403)
      
      return Response({}, status= 200)
   
   def get(self, request):
      if not request.user.is_authenticated :
         return redirect("shop:home_page")

      
      return render(request, 'users/address.html')
      
      
def user_register (request):
   if request.user.is_authenticated :
      return redirect("blog:home-blog")
   
   if request.method == "POST":
      username = request.POST["username"]
      password = request.POST["password"]
      user = User.objects.create( username=username, password=password)
      if user :
         login(request, user)
         return redirect("blog:home-blog")
      else:
         messages.success(request, ("invalid username or password"))
         return redirect("users:user-register")
         
   else:
      return render(request, 'users/register.html', context={})


class UserLogin(TemplateView):
   def get(self, request):
      if request.user.is_authenticated :
            return redirect("shop:home_page")
      
      return render(request, 'users/auth-login-basic.html', context={})
   
   def post(self, request):
      if request.user.is_authenticated :
            return redirect("shop:home_page")
      
      if "submit" in request.POST:
         username = request.POST["username"]
         password = request.POST["password"]
         if not User.objects.filter(username= username).first():
            messages.error(request, ("نام کاربری وجود ندارد"))
            return redirect("users:user_login")
         user = authenticate(request, username=username, password=password)

         if user is not None:
            login(request, user)
            return redirect("shop:home_page")
         else:
            messages.success(request, ("رمز ورود اشتباه است"))
            return redirect("users:user_login")
         
      return render(request, 'users/auth-login-basic.html', context={})


def user_logout (request):
   logout(request)
   return redirect("shop:home_page")


class UserAcount(TemplateView):
   def get(self, request):
         
      return render(request, 'users/dashboard/user-acount.html')
   

class ChangePassword(TemplateView):
   def get(self, request):
      if request.user.is_authenticated :
            return redirect("shop:home_page")
         
      return render(request, 'users/auth-forgot-password-basic.html', context={"form": "form"})
   
   def post(self, request):
      if request.user.is_authenticated :
            return redirect("shop:home_page")


class ChangeEmail(APIView):
   def post(self, request):
      if not request.user.is_authenticated :
         return Response({}, status=403)
      
      email = request.data['email']
      user = User.objects.filter(email= email).first()
      if user :
         return Response({'msg':"ایمیل وجود دارد"}, status=400)
      else:
         user = request.user
         user.email = email
         user.save() 
      
      return Response({}, status=200)


class ChangeFullName(APIView):
   def post(self, request):
      if not request.user.is_authenticated :
         return Response({}, status=403)
      firstName = request.data['firstName']
      lastName = request.data['lastName']
      user = request.user
      user.first_name = firstName
      user.last_name = lastName
      user.save()
      print("ChangeFullName")
      return Response({}, status=200)

  
class ChangePhoneNumber(APIView):
   def post(self, request):
      if not request.user.is_authenticated :
         return Response({}, status=403)
      
      phoneNumber = request.data['phoneNumber']
      if phoneNumber:
         if not len(phoneNumber) == 11:
            return Response({'msg':'تلفن صحیح نیست'}, status=400)
         elif not phoneNumber[0:2] == "09":
            return Response({'msg':'تلفن صحیح نیست'}, status=400)
         elif User.objects.filter(phone_number=phoneNumber).first():
            return Response({'msg':'تلفن موجود است'}, status=400)
      else:
         return Response({'msg':'تلفن صحیح نیست'}, status=400)

      new_otp = Otp()
      new_otp.phone = phoneNumber
      new_otp.generate_password()
      new_otp.save()
      data = OtpSlz( new_otp, many= False ).data
      return Response({'otp_id': data['id']}, status=200)
   
   def put(self, request):
      if not request.user.is_authenticated :
         return Response({}, status=403)
      
      phoneNumber = request.data['phoneNumber']
      otp_id = request.data['otpId']
      code = request.data['otpCode']
      if phoneNumber:
         if not len(phoneNumber) == 11:
            return Response({'msg':'تلفن صحیح نیست'}, status=400)
         elif not phoneNumber[0:2] == "09":
            return Response({'msg':'تلفن صحیح نیست'}, status=400)
         elif User.objects.filter(phone_number=phoneNumber).first():
            return Response({'msg':'تلفن موجود است'}, status=400)
      else:
         return Response({'msg':'تلفن صحیح نیست'}, status=400)
         
      check = Otp.objects.filter(
         id=int(otp_id),
         phone = phoneNumber, 
         password= code,
         valid_until__gte = timezone.now()
      ).first()
      if check:
         user = request.user
         user.phone_number = phoneNumber
         user.save()
      else :
         return Response({'msg':'کد صحیح نیست'}, status=400)
         
      return Response({}, status=200)
   

class HandleAddress(APIView):
   def post(self, request):
      if not request.user.is_authenticated :
         return Response({}, status=403)
      
      data = request.data
      data['user'] = request.user.id
      serializer= AddressSlz(data = data)
      if serializer.is_valid():
         address = serializer.save()
      else:
         print(serializer.errors)
      
      return Response({}, status=200)
   
   def put(self, request):
      if not request.user.is_authenticated :
         return Response({}, status=403)
      
      phoneNumber = request.data['phoneNumber']
      otp_id = request.data['otpId']
      code = request.data['otpCode']
      if phoneNumber:
         if not len(phoneNumber) == 11:
            return Response({'msg':'تلفن صحیح نیست'}, status=400)
         elif not phoneNumber[0:2] == "09":
            return Response({'msg':'تلفن صحیح نیست'}, status=400)
         elif User.objects.filter(phone_number=phoneNumber).first():
            return Response({'msg':'تلفن موجود است'}, status=400)
      else:
         return Response({'msg':'تلفن صحیح نیست'}, status=400)
         
      check = Otp.objects.filter(
         id=int(otp_id),
         phone = phoneNumber, 
         password= code,
         valid_until__gte = timezone.now()
      ).first()
      if check:
         user = request.user
         user.phone_number = phoneNumber
         user.save()
      else :
         return Response({'msg':'کد صحیح نیست'}, status=400)
         
      return Response({}, status=200)
   
   def delete(self, request):
      if not request.user.is_authenticated :
         return Response({}, status=403)
      
      pk = request.data['id']
      check = ShippingAddress.objects.filter(id= pk).delete()
      return Response({}, status=200)
   







