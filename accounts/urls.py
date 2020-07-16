from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    login_page,
    register_page
)

app_name = 'accounts'

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
]
