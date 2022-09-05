from django.contrib import admin

from .models import BasketItem, Catalog, Commodity, Order, Subcategory


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('category', 'id')
    list_filter = ('category',)
    search_fields = ('category',)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'subcategory_name', 'id')
    list_filter = ('category',)
    search_fields = ('subcategory',)


@admin.register(Commodity)
class CommodityAdmin(admin.ModelAdmin):
    list_display = ('category', 'price', 'name', 'image', 'specification')
    list_filter = ('category', 'price', 'name')
    search_fields = ('name',)


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'commodity', 'quantity')
    list_filter = ('user', )
    search_fields = ('user', )


@admin.register(Order)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('commodity', 'created', 'address')
    list_filter = ('created', )
    search_fields = ('created', )
