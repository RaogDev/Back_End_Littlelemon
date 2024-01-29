from django.test import TestCase
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.response import Response

class MenuTest(TestCase):
    def instance(self):
        return Menu.objects.create(Title='IceCream', Price=80, Inventory=20)

    def test_get_item(self):
        item = self.instance()
        self.assertEqual(str(item), "IceCream : 80")


class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(Title="Rice", Price=1, Inventory=10)
        Menu.objects.create(Title="Pasta", Price=2, Inventory=20)
        Menu.objects.create(Title="Cake", Price=3, Inventory=30)
        Menu.objects.create(Title="Baked Rice", Price=4, Inventory=40)
        Menu.objects.create(Title="Ice Cream", Price=5, Inventory=50)

    def test_getall(self):
        self.setup()
        items = Menu.objects.all()

        for item in items:
            serial = MenuSerializer(item)
            response = Response(serial.data)
            self.assertEqual(serial.data, response.data)