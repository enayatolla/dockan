from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.auth import get_user_model
from apps.products.models import Product, Variation, ProductVariation
from django.core.validators import MaxValueValidator, MinValueValidator

User= get_user_model()


# class SellerProfileForm(forms.ModelForm):
#    class Meta:
#       model = SellerProfile
#       fields = ['business_name', 'description', 'phone_number', 'address', 'city', 'state', 'country', 'postal_code', 'website', 'logo', 'payment_info']
#       widgets = {
#          'business_name': forms.TextInput(
#             attrs={
#                'class': 'w-full border border-gray-400 rounded', 'placeholder':'نام فروشگاه'
#             }
#          ),
#          'description': forms.Textarea(
#             attrs={
#                'class': 'w-full border border-gray-400 rounded',
#                'placeholder':'توضیحات', 
#                'rows': 4
#             }
#          ),
#          'phone_number': forms.TextInput(
#             attrs={'class': 'w-full border border-gray-400 rounded', 'placeholder':'تلفن همراه'}
#          ),
#          'address': forms.Textarea(
#             attrs={'class': 'w-full border border-gray-400 rounded', 'placeholder':'آدرس', 'rows': 4}
#          ),
#          'city': forms.TextInput(attrs={'class': 'w-full border border-gray-400 rounded', 'placeholder':'شهر'}),
#          'state': forms.TextInput(attrs={'class': 'w-full border border-gray-400 rounded', 'placeholder':'استان'}),
#          'country': forms.TextInput(attrs={'class': 'w-full border border-gray-400 rounded', 'placeholder':'کشور'}),
#          'postal_code': forms.TextInput(attrs={'class': 'w-full border border-gray-400 rounded', 'placeholder':'کدپستی'}),
#          'website': forms.TextInput(attrs={'class': 'w-full border border-gray-400 rounded', 'placeholder':'نشانی اینترنتی فروشگاه'}),
#          'logo': forms.ClearableFileInput(attrs={'class': 'cursor-pointer', 'placeholder':''}),
#          'payment_info': forms.TextInput(attrs={'class': 'w-full border border-gray-400 rounded', 'placeholder':'اطلاعات پرداخت'}),
#       }


# class EditProfileForm(forms.ModelForm):
#    birth_date = forms.CharField(widget=forms.TextInput(attrs={'class': 'jalali-datepicker rounded w-full', 'autocomplete': 'off'}))
   
#    def clean_birth_date(self): 
#       birth_date = self.cleaned_data['birth_date'] 
#       # Convert Jalali date to Gregorian date 
#       try:
#          birthday_gregorian = jdatetime.datetime.strptime(birth_date, '%Y/%m/%d').togregorian() 
#          return birthday_gregorian 
#       except ValueError: 
#          raise forms.ValidationError("Enter a valid date.")
   
#    class Meta:
#       model = UserProfile
#       fields = ['first_name', 'last_name', 'avatar', 'bio', 'birth_date', 'national_code']
#       widgets={
#          'first_name': forms.TextInput(
#             attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}
#          ),
#          'last_name': forms.TextInput(
#             attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}
#          ),
#          'avatar': forms.FileInput(
#             attrs={
#                'id': 'user_avatar_change_btn',
#                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 
#                'hidden':''
#             }
#          ),
#          'birth_date': forms.TextInput(
#             attrs={'type': 'date', 'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'autocomplete': 'off'}
#          ),
#          'bio': forms.Textarea(
#             attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'rows': 4}
#          ),
#          'national_code': forms.TextInput(
#             attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}
#          )
#       }


# class EditOrderForm(forms.ModelForm):
#    class Meta:
#       model= Order
#       fields= ['is_paid', 'is_ready', 'is_delivered', "is_sending"]


class AddProductForm(forms.ModelForm):
   class Meta:
      model= Product
      fields= [ 'user', 'brand', 'category', 'title', 'slug', 'description', 'base_price', 'is_variable', 'cover']
      widgets= {
         'cover': forms.FileInput(attrs={ 'id': 'cover_image_tag', 'class': 'hidden' }),
      }


# class VariationOptionForm(forms.ModelForm):
#    class Meta:
#       model = VariationOption
#       fields = ['value', ]
#       widgets={
#          'value': {}
#       }


class ProductVariationForm(forms.ModelForm):
   class Meta:
      model = ProductVariation
      fields = ['variation', 'value']
      widgets={
         'variation': {},
         'value': {},
      }




# VariationOptionFormSet = inlineformset_factory(
#    Variation, 
#    VariationOption, 
#    form=VariationOptionForm,
#    extra=1,  # Number of empty forms to display
#    can_delete=True,
# )


ProductVariationFormSet = inlineformset_factory(
   Product, 
   ProductVariation, 
   form=ProductVariationForm,
   extra=1,  # Number of empty forms to display
   can_delete=True,
)




