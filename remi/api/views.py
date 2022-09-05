from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from shop.models import BasketItem, Catalog, Commodity, Order

from .serializers import (BasketItemSerializer, CatalogSerializer,
                          CommoditySerializer, OrderSerializer)


class CatalogListViewSet(ReadOnlyModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer

    def retrieve(self, request, id):
        catalog = Catalog.objects.get(id=id)
        queryset = catalog.subcategories.all()
        return queryset


class CommodityListViewSet(ReadOnlyModelViewSet):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer


class BasketItemViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.DestroyModelMixin,
                        GenericViewSet):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer


class OrderViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
