from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product


class SearchProductView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query is not None:
            return Product.objects.filter(title_icontains=query)
        return Product.objects.featured()