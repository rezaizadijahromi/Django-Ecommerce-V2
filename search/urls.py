from django.urls import path

app_name = "search"

from .views import (
    SearchProductView,
)

urlpatterns = [
    path('search/', SearchProductView.as_view(), name='list')
]
