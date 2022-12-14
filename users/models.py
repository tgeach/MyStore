from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomAccountManager(BaseUserManager):
    
    # Since we've created a custom user model with additional fields, we also need to create a custom manager for it

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(gettext_lazy('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assingedto is_superuser=True')

        return self.create_user(email, user_name, first_name, password, **other_fields)
        

class CustomUser(AbstractBaseUser, PermissionsMixin):

    # gettext_lazy allows for translation of some text
    # PermissionMixins is needed when creating custom user classes to link this new model to the Django Permission system/framework.

    email = models.EmailField(gettext_lazy('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(gettext_lazy('about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    # This is set to default not active in order to implement an email validation step later on
    is_active = models.BooleanField(default=False)

    # Tells this model to use the CustomAccountManager defined above
    objects = CustomAccountManager()

    # changes unique identifying field from user_name to email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name

