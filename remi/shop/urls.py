from django.urls import path

from .views import (BasketView, CatalogView, CategoryView, CommodityView,
                    OrderView)

app_name = 'shop'

urlpatterns = [
    path('catalog/', CatalogView.as_view()),
    path('catalog/<int:pk>/', CategoryView.as_view(), name='category'),
    path('commodity/<int:pk>/', CommodityView.as_view(),
         name='commodity'),
    path('commodity/<int:pk>/add', CommodityView.as_view(),
         name='add_commodity'),
    path('basket/', BasketView.as_view(), name='basket'),
    path('basket/<int:pk>/del', BasketView.as_view(),
         name='del_commodity'),
    path('order/', OrderView.as_view(), name='order')]
