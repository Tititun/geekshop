from django.core.management.base import BaseCommand
from mainapp.models import Product_Category, Product
from django.db.models import Q

class Command(BaseCommand):
   def handle(self, *args, **options):
       test_products = Product.objects.filter(
           Q(category__name='Стулья') |
           Q(category__name='Аксессуары')
       )

       print(len(test_products))