from django.db import models

# blank and null True only in textfield

# Create your models here.
class Product_Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True, db_index=True)

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='product_image', blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Product_Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name} | {self.category}'
