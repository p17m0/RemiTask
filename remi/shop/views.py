from django.shortcuts import render, redirect
from django.views import generic, View
from .models import *
from .forms import *


class CatalogView(generic.ListView):
    model = Catalog
    template_name = 'catalog.html'

class BasketView(View):
    def get(self, request):
        basket = Basket.objects.filter(user=request.user)
        context = {
            'basket': basket,
        }
        return render(request, 'basket.html', context)

class BasketAddView(View):
    def get(self, request, pk):
        commodity = Commodity.objects.get(id=pk)
        Basket.objects.create(user=request.user, commodity=commodity)
        return redirect('shop:commodity', pk=pk)

class CategoryView(View):
    def get(self, request, pk):
        category = Catalog.objects.get(id=pk)
        commodities = Commodity.objects.filter(category=category)
        context = {
            'commodities': commodities,
        }
        return render(request, 'category.html', context)

class CommodityView(generic.DetailView):
    model = Commodity
    template_name = 'commodity.html'

