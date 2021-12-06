from django.contrib import admin

from mainapp.models import Product_Category, Product

# Register your models here.
admin.site.register(Product_Category)
# admin.site.register(Product)

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category']
    fields = ['name', 'description', ('price', 'quantity'), 'category']
    readonly_fields = ['category']
    ordering = ['name', 'price']
    search_fields = ['name']
