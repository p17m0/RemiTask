from django.shortcuts import render, redirect
from django.views import generic, View
from .models import (
    Catalog,
    BasketItem,
    Commodity,
)
from .forms import OrderForm


class CatalogView(generic.ListView):
    model = Catalog
    template_name = 'shop/catalog.html'

class BasketView(View):
    def get(self, request):
        basket = BasketItem.objects.filter(user=request.user.id)
        context = {
            'basket': basket,
        }
        return render(request, 'shop/basket.html', context)

    def post(self, request, pk):
        commodity = Commodity.objects.get(id=pk)
        BasketItem.objects.get(user=request.user, commodity=commodity).delete()
        return redirect('shop:basket')

class CategoryView(View):
    def get(self, request, pk):
        category = Catalog.objects.get(id=pk)
        commodities = Commodity.objects.filter(category=category)
        context = {
            'commodities': commodities,
        }
        return render(request, 'shop/category.html', context)

class CommodityView(View):
    def get(self, request, pk):
        commodity = Commodity.objects.get(id=pk)
        in_basket = bool(BasketItem.objects.filter(user=request.user, commodity=commodity))
        context = {
            'commodity': commodity,
            'in_basket': in_basket,
        }
        return render(request, 'shop/commodity.html', context)

    def post(self, request, pk):
        commodity = Commodity.objects.get(id=pk)
        BasketItem.objects.create(user=request.user, commodity=commodity)
        return redirect('shop:commodity', pk=pk)

class OrderView(View):
    def get(self, request):
        basketitems = BasketItem.objects.filter(user=request.user)
        form = OrderForm
        context = {
            'form': form,
            'basketitems': basketitems,
        }
        return render(request, 'shop/order.html', context)
    
    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            return redirect('shop:order')
        return redirect('shop:order')