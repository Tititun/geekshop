import json
from django.core.management.base import BaseCommand
from mainapp.models import Product, Product_Category

def load_from_json(filename):
    with open(filename, 'r', encoding='utf8') as f:
        return json.load(f)

class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('mainapp/fixtures/categories.json')

        Product_Category.objects.all().delete()
        for category in categories:
            cat = category.get('fields')
            cat['id'] = category.get('pk')
            new_category = Product_Category(**cat)
            new_category.save()

        products = load_from_json('mainapp/fixtures/products.json')
        Product.objects.all().delete()
        for product in products:
            prod = product.get('fields')
            category = prod.get('category')
            _category = Product_Category.objects.get(id=category)
            prod['category'] = _category
            new_product = Product(**prod)
            new_product.save()