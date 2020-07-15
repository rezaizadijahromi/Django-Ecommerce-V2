from django.urls import path
from .views import (
    cart_home
)

app_name = 'carts'

urlpatterns = [
    path('', cart_home, name='cart')
]
