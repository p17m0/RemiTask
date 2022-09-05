from ast import Sub
from unicodedata import category
from wsgiref.simple_server import demo_app
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Catalog(models.Model):
    """
    Каталог (иерархическое дерево категорий).
    """
    category = models.CharField(max_length=25)

    def __str__(self):
        return self.category

class Subcategory(models.Model):
    """
    Подкатегория в каталоге.
    """
    category = models.ForeignKey(Catalog, on_delete=models.CASCADE,
                                 related_name='subcategories')
    subcategory_name = models.CharField(max_length=30)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['category',
                                            'subcategory_name'],
                                            name='unique_subcategory')
        ]
    
    def __str__(self):
        return self.subcategory_name

class Commodity(models.Model):
    """
    Товар связанный с категорией каталога,
    например с изображением и «спецификацией» (Filefield).
    """
    category = models.ForeignKey(Catalog,
                                 on_delete=models.CASCADE,
                                 related_name='commodities')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE,
                                    related_name='commodities')
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='data/uploads/images')
    specification = models.FileField(upload_to='data/uploads/specifications')
    price = models.FloatField(max_length=4)

    def __str__(self):
        return self.name

class BasketItem(models.Model):
    """
    Корзина \ заказ набор товаров, изменение статусов заказов, завершение.
    """
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity,
                                  on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    is_ordered = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'commodity'],
                                    name='unique_commodity')
        ]

    def __str__(self):
        return self.commodity.name

class Share(models.Model):
    """
    Промо абстракция для объединения между собой товаров в “акцию”,
    с дополнительными условиями.
    """
    share = models.IntegerField()
    condition = models.CharField(max_length=40)
    commodity = models.ForeignKey(Commodity,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.share

class Order(models.Model):
    basketitem = models.ForeignKey(BasketItem,
                                   on_delete=models.CASCADE,
                                   related_name='items')
    address = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address

