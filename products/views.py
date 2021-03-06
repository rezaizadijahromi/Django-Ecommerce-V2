from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView
)
from django.http import Http404

from .models import Product
from carts.models import Cart

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        super(ProductListView, self).get_queryset(*args, **kwargs)
        return Product.objects.all()


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug)

        except Product.DoesNotExist:    
            raise Http404('Not found...')
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("Fucks going on mannn")

        return instance



class ProductFeaturedListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self):
        return Product.objects.all()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/featured-detail.html'    