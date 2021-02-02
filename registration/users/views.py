from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView, RedirectView,
)

from .models import CustomUser

from .forms import (
    UserRegistrationForm,
    CustomUserLoginForm,
    AccountEditForm,
    SetNewPasswordForm,
)


class AccountView(LoginRequiredMixin, DetailView):
    """Returns account page after log in."""
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
    success_message = 'Account Created.'


class UserLoginView(LoginView):
    redirect_authenticated_user = True
    form_class = CustomUserLoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('users:account')


class UserLogoutView(LogoutView):
    next_page = 'users:login'


class EditAccount(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'users/change_user_info.html'
    form_class = AccountEditForm
    success_url = reverse_lazy('users:index')
    success_message = 'Personal data have been updated.'

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class UserPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    """Class for setting new password."""
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:index')
    form_class = SetNewPasswordForm
    success_message = 'Password changed.'


class AccountEditRedirectView(LoginRequiredMixin, RedirectView):
    """Redirect on visit root site uri."""
    url = reverse_lazy('users:edit_account')

