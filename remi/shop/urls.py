from django.urls import path
from .views import CatalogView, CommodityView, CategoryView

app_name = 'shop'

urlpatterns = [
    path('catalog/', CatalogView.as_view()),
    path('catalog/<int:id>/', CategoryView.as_view(), name='category'),
]