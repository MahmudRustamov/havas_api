from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase
from apps.products.models import ProductsModel


class TestProductCreate(APITestCase):
    def setUp(self):
        self.url = reverse_lazy('products:list-create')
        image_path = r"D:\Najot Ta'lim\Django-Rest-Fremwork\havas\media\products\image.jpg"

        with open(image_path, 'rb') as img:
            image_file = SimpleUploadedFile('image.jpg', img.read(), content_type='image/jpeg')

        self.payload = {
            'image': image_file,
            'title': 'Osh',
            'description': 'Mazali milliy taom',
            'discount': 10,
            'price': 25000,
            'category': 'LUNCH',
            'measurement': 'GR',
            'is_active': True
        }

    def test_create_product_success(self):
        response = self.client.post(
            path=self.url,
            data=self.payload,
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = response.json().get('data')

        self.assertIsNotNone(data)
        self.assertEqual(data['title'], 'Osh')
        self.assertEqual(data['category'], 'LUNCH')
        self.assertEqual(data['measurement'], 'GR')
        self.assertIn('image', data)
        self.assertTrue(ProductsModel.objects.filter(title='Osh').exists())
