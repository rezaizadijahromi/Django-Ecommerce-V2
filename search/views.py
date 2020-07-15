from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

from django.db.models import Q

class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        q = Product.objects.all()
        request = self.request
        query = request.GET.get('q', None) # method_dict['q']
        if query is not None:
            q = q.filter(
                Q(title__icontains=query)|
                Q(description__icontains=query)|
                Q(price__icontains=query)
            ).distinct()

            return q
        return Product.objects.featured()
     