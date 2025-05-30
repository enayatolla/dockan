from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from apps.products.models import Product
from apps.products.forms import AddProductForm, ProductVariationFormSet


class Dashboard(View):
   def get(self, request):

      context= {}
      return render(request, 'staff/dashboard.html', context)
   



# class OrderList(View):
#    def get(self, request):
#       order_list= Order.objects.all().order_by('-created_at')
#       return render(request, 'sellers/order_list.html', {'order_list': order_list})

#    def post(self, request):
#       form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
#       if 'submit' in request.POST:
#          if form.is_valid():
#             profile = form.save(commit=False) 
#             profile.birth_date = form.cleaned_data['birth_date'] 
#             profile.save()
#             messages.success(request, "تغییرات با موفقیت زخیره شد")
#             return redirect("sellers:seller_profile")
#       return render(request, "sellers/seller_profile.html", {"form": form})


# class OrderDetail(View):
#    def get(self, request, pk):
#       order= Order.objects.filter(id= pk).first()
#       from .forms import EditOrderForm
#       form= EditOrderForm(instance= order)
#       context= {
#          'order': order,
#          'form': form
#       }
#       return render(request, 'sellers/order_detail.html', context)

#    def post(self, request, pk):
#       from .forms import EditOrderForm
#       order= Order.objects.filter(id= pk).first()
#       form = EditOrderForm(request.POST, request.FILES, instance= order)
#       if 'submit' in request.POST:
#          if form.is_valid():
#             profile = form.save(commit=False) 
#             profile.save()
#             messages.success(request, "تغییرات با موفقیت زخیره شد")
#             return redirect("sellers:order_detail", pk=pk)
#       context= {
#          'form': form,
#          'order': order
#       }
#       return render(request, "sellers/order_detail.html", context)


class ProductList(View):
   def get(self, request):
      product_list= Product.objects.filter(user= request.user).order_by('-created_at')
      return render(request, 'staff/product_list.html', {'product_list':product_list})


class ProductDetail(View):
   def get(self, request, pk, slug):
      product= Product.objects.filter(id= pk).first()
      form= AddProductForm(instance= product)
      context= {'product': product, 'form':form }
      return render(request, 'staff/product_detail.html', context)

   # def post(self, request):
   #    form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
   #    if 'submit' in request.POST:
   #       if form.is_valid():
   #          profile = form.save(commit=False) 
   #          profile.birth_date = form.cleaned_data['birth_date'] 
   #          profile.save()
   #          messages.success(request, "تغییرات با موفقیت زخیره شد")
   #          return redirect("sellers:seller_profile")
   #    return render(request, "sellers/seller_profile.html", {"form": form})
   

class NewProduct(View):
   def get(self, request):
      form= "AddProductForm()"
      formset = ""
      formset = ProductVariationFormSet()

      context= {'product_form': form, 'formset': formset }   
      return render(request, 'staff/new_product.html', context)

   def post(self, request):
      form = "AddProductForm(request.POST, request.FILES, instance=request.user.profile)"
      if 'submit' in request.POST:
         if form.is_valid():
            new_form = form.save(commit=False) 
            new_form.user = request.user
            new_form.save()
            messages.success(request, "jkbaxBKJCSJBCSKCSABJBKCJSAKBJSA")
            return redirect("staff:new_product")
      return render(request, "staff/new_product.html", {"form": form})


# class Settings(View):
#    def get(self, request):
#       return render(request, 'sellers/settings.html', {})

#    def post(self, request):
#       form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
#       if 'submit' in request.POST:
#          if form.is_valid():
#             profile = form.save(commit=False) 
#             profile.birth_date = form.cleaned_data['birth_date'] 
#             profile.save()
#             messages.success(request, "تغییرات با موفقیت زخیره شد")
#             return redirect("sellers:seller_profile")
#       return render(request, "sellers/seller_profile.html", {"form": form})
