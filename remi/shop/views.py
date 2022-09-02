import re
from django.shortcuts import render
from django.views import generic, View
from .models import *

class CatalogView(generic.ListView):
    model = Catalog
    template_name = 'catalog.html'

# class BasketView(generic.ListView):
#     model = Basket
class CategoryView(View):
    def get(self, request, id):
        category = Catalog.objects.get(id=id)
        commodities = Commodity.objects.filter(category=category)
        context = {
            'commodities': commodities,
        }
        return render(request, 'category.html', context)

class CommodityView(generic.DetailView):
    model = Commodity
    template_name = 'commodity.html'

