from django.urls import path
from .views import (
    account_login,
    account_logout,
    account_register)

app_name = 'accounts'

urlpatterns = [
    path('login/', account_login, name="login"),
    path('logout/', account_logout, name="logout"),
    path('register/', account_register, name="register"),

]
