from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.password_validation import validate_password
from django import forms
from .models import CustomUser


class SetNewPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control',
                   'placeholder': 'Old Password'}, ),
        label='Old Password'
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'New password'}),
        strip=False,
        label='New password'
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Confirm New Password'}),
        strip=False,
        label='Confirm Password'
    )


class AccountEditForm(forms.ModelForm):
    """Форма правки личных данных"""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(label='Имя', required=False)
    last_name = forms.CharField(label='Фамилия', required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'username']


class CustomUserLoginForm(AuthenticationForm):
    """Форма авторизации пользователя"""
    username = forms.CharField(
        label='email',
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'})
    )
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password', ]


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(
            attrs={'autocomplete': 'email', 'class': 'form-control', 'placeholder': 'Email'}),
    )
    first_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'First Name'}
        ),
        required=False,
        label='First Name'
    )
    last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'First Name'}
        ),
        required=False,
        label='Last Name'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password',
                   'class': 'form-control',
                   'placeholder': 'Password'}
        ),
        label='Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password',
                   'class': 'form-control',
                   'placeholder': 'Confirm password'}
        ),
        label='Confirm password'
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Введенные пароли не совпадают.')
        return validate_password(cd['password2'])

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        if commit:
            user.save()
        return user
