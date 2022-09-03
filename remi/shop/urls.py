from django.urls import path
from .views import BasketAddView, CatalogView, CommodityView, CategoryView, BasketView, BasketDelView

app_name = 'shop'

urlpatterns = [
    path('catalog/', CatalogView.as_view()),
    path('catalog/<int:pk>/', CategoryView.as_view(), name='category'),
    path('commodity/<int:pk>/', CommodityView.as_view(), name='commodity'),
    path('commodity/<int:pk>/del', BasketDelView.as_view(),name='del_commodity'),
    path('commodity/<int:pk>/add', BasketAddView.as_view(),name='add_commodity'),
    path('basket/', BasketView.as_view(), name='basket'),
    ]