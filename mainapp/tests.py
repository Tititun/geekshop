from django.test import TestCase
from mainapp.models import Product_Category, Product


class TestMainSmokeTest(TestCase):

    def setUp(self) -> None:
        Product_Category.objects.create(
            name='TestCell'
        )

    def tearDown(self) -> None:
        pass

    def test_products_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_category(self):
        for category in Product_Category.objects.all():
            response = self.client.get(f'/products/category/{category.pk}')
            self.assertEqual(response.status_code, 200)
