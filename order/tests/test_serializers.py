import pytest
from django.contrib.auth.models import User
from order.serializers import OrderSerializer
from order.models import Order
from product.models import Product, Category


@pytest.mark.django_db
class TestOrderSerializer:
    def test_order_serializer(self):
        # Criar usuário
        user = User.objects.create_user(
            username="testuser",
            email="test@test.com",
            password="testpass123"
        )

        # Criar categoria e produto
        category = Category.objects.create(
            title="Livros",
            slug="livros",
            active=True
        )

        product = Product.objects.create(
            title="Python Book",
            price=50,
            active=True
        )
        product.category.add(category)

        # Criar pedido
        order = Order.objects.create(user=user)
        order.product.add(product)

        # Testando serialização
        serializer = OrderSerializer(order)
        serialized_data = serializer.data

        assert "product" in serialized_data
        assert "total" in serialized_data
        assert serialized_data["total"] == 50