from rest_framework.test import APITestCase
from django.urls import reverse
from fruit.models import Fruit
from fruit.serializers import FruitSerializer
from rest_framework import status


class FruitApiTestCase(APITestCase):
    def test_get_list(self):
        fruit_1 = Fruit.objects.create(name='Апельсин', price=15)
        fruit_2 = Fruit.objects.create(name='Яблоко', price=21)

        response = self.client.get(reverse('fruit_api_list'))

        serial_data = FruitSerializer([fruit_1, fruit_2], many=True).data
        serial_data = {'fruit_list': serial_data}

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serial_data, response.data)