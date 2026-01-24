import pytest
from django.contrib.auth.models import User
from order.models import Order
from product.models import Product, Category


@pytest.mark.django_db
class TestOrderModel:

    def test_create_order(self):
        """Testa criação básica de um pedido"""
        user = User.objects.create_user(
            username="testuser",
            email="test@test.com",
            password="testpass123"
        )

        order = Order.objects.create(user=user)

        assert order.id is not None
        assert order.user == user
        assert order.product.count() == 0

    def test_order_with_products(self):
        """Testa pedido com produtos associados"""
        user = User.objects.create_user(
            username="testuser2",
            email="test2@test.com",
            password="testpass123"
        )

        category = Category.objects.create(
            title="Livros",
            slug="livros",
            active=True
        )

        product1 = Product.objects.create(
            title="Python Book",
            price=50,
            active=True
        )
        product1.category.add(category)

        product2 = Product.objects.create(
            title="Django Book",
            price=75,
            active=True
        )
        product2.category.add(category)

        order = Order.objects.create(user=user)
        order.product.add(product1, product2)

        assert order.product.count() == 2
        assert product1 in order.product.all()
        assert product2 in order.product.all()

    def test_order_str_representation(self):
        """Testa representação padrão em string"""
        user = User.objects.create_user(
            username="testuser3",
            email="test3@test.com",
            password="testpass123"
        )

        order = Order.objects.create(user=user)

        assert "Order object" in str(order)

    def test_order_requires_user(self):
        """Testa que pedido exige usuário"""
        with pytest.raises(Exception):
            Order.objects.create(user=None)

    def test_delete_user_cascades_to_orders(self):
        """Testa cascade ao deletar usuário"""
        user = User.objects.create_user(
            username="testuser4",
            email="test4@test.com",
            password="testpass123"
        )

        order = Order.objects.create(user=user)
        order_id = order.id

        user.delete()

        assert not Order.objects.filter(id=order_id).exists()