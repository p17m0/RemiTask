from unicodedata import category
from django.contrib import admin
from .models import Catalog, Subcategory, Commodity, Basket

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

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'commodity')
    list_filter = ('user', )
    search_fields = ('user', )