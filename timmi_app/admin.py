from django.contrib import admin
from . models import Offer, Products

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class OffersAdmin(admin.ModelAdmin):
    list_display = ('code','discount','description')

admin.site.register(Products, ProductAdmin)
admin.site.register(Offer, OffersAdmin)

