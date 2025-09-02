from django.contrib import admin
from .models import Product, Stock, Brand, Category

admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Brand)
admin.site.register(Category)
