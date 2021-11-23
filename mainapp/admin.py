from django.contrib import admin

from mainapp.models import Product_Category, Product

# Register your models here.
admin.site.register(Product_Category)
admin.site.register(Product)
