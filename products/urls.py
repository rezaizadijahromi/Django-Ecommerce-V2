from django.urls import path

app_name = "products"

from .views import (
    ProductListView, ProductDetailView, ProductDetailSlugView
)

urlpatterns = [
    path("", ProductListView.as_view(), name="list"),
    path("<str:slug>/", ProductDetailSlugView.as_view(), name="detail"),
    # path("detail/<int:pk>/", ProductDetailView.as_view(), name="detail"),
]
