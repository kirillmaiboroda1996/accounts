from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, password=None, *args, **kwargs):
        email = kwargs.get('email', None)
        first_name = kwargs.get('first_name', None)
        last_name = kwargs.get('last_name', None)
        user = self.model(email=email, first_name=first_name, last_name=last_name)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
