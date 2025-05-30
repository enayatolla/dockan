from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.users.models import User, UserProfile, Otp
from apps.users.forms import UserCreationForm, UserChangeForm
from .models import ShippingAddress

class UserAdmin(BaseUserAdmin):
   # The forms to add and change user instances
   form = UserChangeForm
   add_form = UserCreationForm

   # The fields to be used in displaying the User model.
   # These override the definations on the base UserAdmin
   # that reference specific fields on auth.User.
   list_display = ["username","phone_number", "email", "is_staff", "id"]
   list_filter = ["is_staff"]
   fieldsets = [
      (None, {"fields": [ "email", "password", "username", "phone_number"]}),
      ("Permissions", {"fields": ["is_staff", "is_superuser", "is_active", "is_seller"]}),
   ]
   # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
   # overrides get_fieldsets to use this attribute when creating a user.
   add_fieldsets = [
      (
         None,
         {
            "classes": ["wide"],
            "fields": ["username", "email", "password1", "password2"],
         },
      ),
   ]
   search_fields = ["username"]
   ordering = ["username"]
   filter_horizontal = []


class UserProfileAdmin(admin.ModelAdmin):
   list_display = ("user", "description", "birth_date", "get_avatar")


class OtpAdmin(admin.ModelAdmin):
   list_display = ( "id", "phone", "password", "valid_until", "created_at")
   
class AddressAdmin(admin.ModelAdmin):
   list_display= ("user", "province", "city")
      

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Otp, OtpAdmin)
admin.site.register(ShippingAddress, AddressAdmin)

# admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions, unregister the Group model from admin.
admin.site.unregister(Group)






