from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from ..models import *
from ..serializers import *
from ..views import *


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        Menu.objects.create(title="Water", price=2, inventory=15)
        Menu.objects.create(title="Coke", price=3, inventory=15)
        Menu.objects.create(title="Sprite", price=3, inventory=15)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        response.render()

        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
