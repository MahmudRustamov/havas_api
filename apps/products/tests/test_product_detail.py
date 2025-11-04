from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase
from apps.products.models import ProductsModel


class TestProductDetail(APITestCase):
    def setUp(self):
        image_path = r"D:\Najot Ta'lim\Django-Rest-Fremwork\havas\media\products\image.jpg"
        with open(image_path, 'rb') as img:
            image_file = SimpleUploadedFile('image.jpg', img.read(), content_type='image/jpeg')

        self.product = ProductsModel.objects.create(
            image=image_file,
            title="Osh",
            description="Mazali milliy taom",
            discount=10,
            price=25000,
            category="LUNCH",
            measurement="GR",
            is_active=True
        )
        self.url = reverse_lazy('products:detail', kwargs={'pk': self.product.pk})

    def test_retrieve_product(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('data').get('title'), "Osh")

    def test_update_product(self):
        payload = {
            'title': 'Palov',
            'description': 'Yangi milliy taom',
            'discount': 5,
            'price': 30000,
            'category': 'LUNCH',
            'measurement': 'GR',
            'is_active': True
        }
        response = self.client.put(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('data').get('title'), "Palov")

    def test_partial_update_product(self):
        payload = {'title': 'Somsa'}
        response = self.client.patch(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('data').get('title'), "Somsa")

    def test_delete_product(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ProductsModel.objects.filter(pk=self.product.pk).exists())
