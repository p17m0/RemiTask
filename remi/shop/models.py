from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Catalog(models.Model):
    """
    Каталог (иерархическое дерево категорий).
    """
    category = models.CharField(max_length=25)



class Commodity(models.Model):
    """
    Товар связанный с категорией каталога,
    например с изображением и «спецификацией» (Filefield).
    """
    category = models.ForeignKey(Catalog,
                                 on_delete=models.CASCADE,
                                 related_name='commodities')
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='data/uploads/images')
    specification = models.FileField(upload_to='data/uploads/specifications')
    price = models.FloatField(max_length=4)

class Basket(models.Model):
    """
    Корзина \ заказ набор товаров, изменение статусов заказов, завершение.
    """
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity,
                                  on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'commodity'],
                                    name='unique_commodity')
        ]

class Share(models.Model):
    """
    Промо абстракция для объединения между собой товаров в “акцию”,
    с дополнительными условиями.
    """
    share = models.IntegerField()
    condition = models.CharField(max_length=40)
    good = models.ForeignKey(Commodity,
                             on_delete=models.CASCADE)

