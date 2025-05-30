from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.apps import apps
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.utils.html import format_html
from datetime import timedelta
import random, string


class UserManager(BaseUserManager):
   def _create_user(self, username, email, password, **extra_fields):
      if not username:
         raise ValueError("The given username must be set")
      email = self.normalize_email(email)
      GlobalUserModel = apps.get_model(
         self.model._meta.app_label, self.model._meta.object_name
      )
      username = GlobalUserModel.normalize_username(username)
      user = self.model(username=username, email=email, **extra_fields)
      user.password = make_password(password)
      user.save(using=self._db)
      return user

   def create_user(self, username, email=None, password=None, **extra_fields):
      extra_fields.setdefault("is_staff", False)
      extra_fields.setdefault("is_superuser", False)
      return self._create_user(username, email, password, **extra_fields)

   def create_superuser(self, username, email=None, password=None, **extra_fields):
      extra_fields.setdefault("is_staff", True)
      extra_fields.setdefault("is_superuser", True)

      if extra_fields.get("is_staff") is not True:
         raise ValueError("Superuser must have is_staff=True.")
      if extra_fields.get("is_superuser") is not True:
         raise ValueError("Superuser must have is_superuser=True.")

      return self._create_user(username, email, password, **extra_fields)

   def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
      if backend is None:
         backends = auth._get_backends(return_tuples=True)
         if len(backends) == 1:
            backend, _ = backends[0]
         else:
            raise ValueError(
               "You have multiple authentication backends configured and "
               "therefore must provide the `backend` argument."
            )
      elif not isinstance(backend, str):
         raise TypeError(
            "backend must be a dotted import path string (got %r)." % backend
         )
      else:
         backend = auth.load_backend(backend)
      if hasattr(backend, "with_perm"):
         return backend.with_perm(
            perm,
            is_active=is_active,
            include_superusers=include_superusers,
            obj=obj,
         )
      return self.none()


class User(AbstractBaseUser, PermissionsMixin):
   username_validator = UnicodeUsernameValidator()
   username = models.CharField(
      _("username"),
      max_length=150,
      unique=True,
      help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
      validators=[username_validator],
      error_messages={"unique": _("A user with that username already exists.")},
   )
   email = models.EmailField(_("email address"),max_length=256, null=True, blank=True)
   phone_number = models.CharField(_("phone number"),max_length=14, null=True, blank=True)
   is_staff = models.BooleanField(_("staff status"), default=False)
   is_active = models.BooleanField(_("active"), default=True)
   date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
   is_seller = models.BooleanField(_("is seller"), default=False)
   objects = UserManager()
   EMAIL_FIELD = "email"
   USERNAME_FIELD = "username"
   REQUIRED_FIELDS = []
   
   class Meta:
      verbose_name = _("user")
      verbose_name_plural = _("users")
      abstract = False
      swappable = "AUTH_USER_MODEL"
      
   def __str__(self):
      return str(self.username)

   def clean(self):
      super().clean()
      self.email = self.__class__.objects.normalize_email(self.email)

   def email_user(self, subject, message, from_email=None, **kwargs):
      """Send an email to this user."""
      send_mail(subject, message, from_email, [self.email], **kwargs)


class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", editable=False)
   avatar = models.ImageField(upload_to='images/profile_avatar', null=True, blank=True)
   description= models.TextField( max_length=512, null=True, blank=True )
   birth_date = models.DateTimeField( default=None, null=True, blank=True )

   def get_avatar(self):
      if self.avatar:
         return format_html(
            f"<img src= '{self.avatar.url}' style='object-fit:cover;width:40px; height:30px' />"
         )
      else:
         return format_html("<h2 >no avatar</h2>")


class Otp(models.Model):
   id= models.BigAutoField(primary_key=True, editable= False)
   phone= models.CharField(max_length= 13)
   password=  models.CharField(max_length= 6, null=True)
   valid_until= models.DateTimeField(default= timezone.now)
   created_at= models.DateTimeField(default= timezone.now)

   def generate_password(self):
      self.valid_until= timezone.now() + timedelta(minutes=2)
      code = self._random_password()
      self.password= code
      self.send_otp(code)

   def _random_password(self):
      rand = random.SystemRandom()
      digits = rand.choices(string.digits, k= 4)
      return ''.join(digits)
   
   def send_otp(self, code) -> None:
      print( code )
   
   class Meta:
      verbose_name= _('One Time Password')
      verbose_name_plural= _('One Time Passwords')


class ShippingAddress (models.Model):
   id = models.BigAutoField(primary_key=True, editable=False)
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
   created_at= models.DateTimeField(auto_now_add= True, null=True, blank=True)

   province= models.CharField(max_length=64, null=True, blank=True)
   city= models.CharField(max_length=64, null=True, blank=True)
   address = models.CharField(max_length=512, null=True, blank=True)
   region= models.CharField(max_length=32, null=True, blank=True)
   last= models.CharField(max_length=64, null=True, blank=True)
   plaque= models.CharField(max_length=16, null=True, blank=True)
   postal_code= models.CharField(max_length=32, null=True, blank=True)
   stairs=models.CharField(max_length=32, null=True, blank=True)
   phone=models.CharField(max_length=16, null=True, blank=True)
   
   def __str__(self):
      return str(self.province + ', ' + self.city + ', ' + self.address)


# latitude=models.CharField(max_length=32, null=True, blank=True)
# longitude=models.CharField(max_length=32, null=True, blank=True)
# primary= models.CharField(max_length=64, null=True, blank=True)
# neighbourhood= models.CharField(max_length=32, null=True, blank=True)
# village= models.CharField(max_length=64, null=True, blank=True)
# rural_district= models.CharField(max_length=64, null=True, blank=True)
# district= models.CharField(max_length=128, null=True, blank=True)
# address_compact= models.CharField(max_length=128, null=True, blank=True)
# country = models.CharField(max_length=32, null=True, blank=True)
# postal_address= models.CharField(max_length=64, null=True, blank=True)
