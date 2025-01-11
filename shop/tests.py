from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from shop.models import Category, Product, CustomUser


class APITest(APITestCase):
    def setUp(self):
        # Create sample data for testing
        self.category = Category.objects.create(name="Electronics", description="All electronic items")
        self.product = Product.objects.create(
            name="Laptop",
            price="1500.00",
            category=self.category
        )
        self.user = CustomUser.objects.create_user(
            email="Abdusaidov@gmail.com",
            password="123",
            first_name="John",
            last_name="Doe"
        )

        self.category_url = reverse('category-list')
        self.product_url = reverse('product-list')
        self.user_url = reverse('user-list')

    def test_category_list(self):
        response = self.client.get(self.category_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ensure one category exists
        self.assertEqual(response.data[0]['name'], self.category.name)

    def test_category_create(self):
        data = {"name": "Books", "description": "Books and Articles"}
        response = self.client.post(self.category_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)

    def test_product_list(self):
        response = self.client.get(self.product_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_product_create(self):
        data = {"name": "Tablet", "price": "500.00", "category": self.category.id}
        response = self.client.post(self.product_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_user_creation(self):
        data = {
            "email": "tjdefalco@gmail.com",
            "password": "admin123",
            "first_name": "Defalco",
            "last_name": "Tj"
        }
        response = self.client.post(self.user_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 2)


