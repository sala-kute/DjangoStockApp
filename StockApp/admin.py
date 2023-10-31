from django.contrib import admin
from .models import Product, Supplier, Stock

admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Stock)