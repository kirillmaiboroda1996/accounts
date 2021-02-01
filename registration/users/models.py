from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=155, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=155, null=True, blank=True)
    last_name = models.CharField(max_length=155, null=True, blank=True)
    date_joined = models.DateField(default=timezone.now())

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_full_name(self):
        if not (self.first_name and self.last_name):
            return self.email
        else:
            return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        if not self.first_name:
            return self.email
        else:
            return self.first_name

    def __str__(self):
        return self.email
