from django.urls import path
from .views import *


app_name = 'users'


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('registration/', UserRegistrationView.as_view(), name='user_registration'),
    path('account/', AccountView.as_view(), name='index')
]