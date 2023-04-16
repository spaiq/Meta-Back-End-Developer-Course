from django.test import TestCase
from ..models import *


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Chicken", price=10.00, inventory=10)
        self.assertEqual(item.__str__(), "Chicken 10.0")
