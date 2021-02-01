from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from .models import CustomUser
from .forms import UserRegistrationForm, CustomUserLoginForm


class AccountView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'users/index.html'

    def get_object(self, queryset=None):
        user_email = self.request.user.email
        currant_user = CustomUser.objects.get(email=user_email)
        return currant_user


class UserRegistrationView(SuccessMessageMixin, CreateView):
    model = CustomUser
    template_name = 'users/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    success_message = 'Account Created'


class UserLoginView(LoginView):
    redirect_authenticated_user = True
    form_class = CustomUserLoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('users:index')


class UserLogoutView(LogoutView):
    next_page = 'users:login'
