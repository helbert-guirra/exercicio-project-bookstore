import json

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from order.factories import OrderFactory, UserFactory
from order.models import Order
from product.factories import CategoryFactory, ProductFactory


class TestOrderViewSet(APITestCase):

    client = APIClient()

    def setUp(self):
        self.user = UserFactory()
        self.token = Token.objects.create(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token.key
        )

        self.category = CategoryFactory(title="technology")
        self.product = ProductFactory(
            title="mouse",
            price=100,
            category=[self.category]
        )

        self.order = OrderFactory(
            product=[self.product],
            user=self.user
        )

    def test_get_all_orders(self):
        response = self.client.get(
            reverse("order-list", kwargs={"version": "v1"})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        order_data = json.loads(response.content)

        self.assertEqual(
            order_data["results"][0]["product"][0]["title"],
            self.product.title
        )

    def test_create_order(self):
        new_product = ProductFactory()

        data = json.dumps({
            "products_id": [new_product.id],
            "user": self.user.id
        })

        response = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(
            Order.objects.filter(user=self.user).exists()
        )
