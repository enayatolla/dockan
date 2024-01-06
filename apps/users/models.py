from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.apps import apps
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
import uuid, random, string
from datetime import timedelta


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
   first_name = models.CharField(_("first name"), max_length=150, blank=True)
   last_name = models.CharField(_("last name"), max_length=150, blank=True)
   email = models.EmailField(_("email address"),max_length=256, null=True, blank=True)
   phone_number = models.CharField(_("phone number"),max_length=14, null=True, blank=True)
   is_staff = models.BooleanField(_("staff status"), default=False)
   is_active = models.BooleanField(_("active"), default=True)
   date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
   date_of_birth = models.DateField(_("date of birth"), null=True, blank=True)
   objects = UserManager()
   EMAIL_FIELD = "email"
   USERNAME_FIELD = "username"
   REQUIRED_FIELDS = []
   
   class Meta:
      verbose_name = _("user")
      verbose_name_plural = _("users")
      abstract = False
      swappable = "AUTH_USER_MODEL"

   def clean(self):
      super().clean()
      self.email = self.__class__.objects.normalize_email(self.email)

   def email_user(self, subject, message, from_email=None, **kwargs):
      """Send an email to this user."""
      send_mail(subject, message, from_email, [self.email], **kwargs)


class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   avatar = models.ImageField(
      upload_to='images/profile_avatar',
      default="avatar/DefaultAvatar.jpg",
      null=True,
      blank=True,
   )
   description= models.TextField( max_length=512, null=True, blank=True )
   birth_date = models.DateTimeField( default=None, null=True, blank=True )


class Otp(models.Model):
   request_id= models.BigAutoField(primary_key=True, editable= False)
   phone= models.CharField( max_length= 12, null=False, blank=False )
   password=  models.CharField(max_length= 6, null=True)
   valid_until= models.DateTimeField(default= timezone.now)

   def generate_password(self):
      self.password= self._random_password()
      self.valid_until= timezone.now() + timedelta(minutes=2)

   def _random_password(self):
      rand = random.SystemRandom()
      digits = rand.choices(string.digits, k= 4)
      print(''.join(digits))
      return ''.join(digits)
   
   class Meta:
      verbose_name= _('One Time Password')
      verbose_name_plural= _('One Time Passwords')



