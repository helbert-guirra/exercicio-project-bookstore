import pytest
from product.models import Category, Product
from decimal import Decimal


@pytest.mark.django_db
class TestCategoryModel:

    def test_create_category(self):
        category = Category.objects.create(
            title="Eletrônicos",
            slug="eletronicos",
            description="Produtos eletrônicos",
            active=True
        )

        assert category.id is not None
        assert category.title == "Eletrônicos"
        assert category.slug == "eletronicos"
        assert category.active is True

    def test_category_slug_unique(self):
        Category.objects.create(
            title="Categoria 1",
            slug="categoria",
            active=True
        )

        with pytest.raises(Exception):
            Category.objects.create(
                title="Categoria 2",
                slug="categoria",
                active=True
            )

    def test_category_str_representation(self):
        category = Category.objects.create(
            title="Livros",
            slug="livros",
            active=True
        )

        assert "Category object" in str(category)

    def test_category_can_be_inactive(self):
        category = Category.objects.create(
            title="Descontinuados",
            slug="descontinuados",
            active=False
        )

        assert category.active is False

    def test_category_default_values(self):
        category = Category.objects.create(
            title="Teste",
            slug="teste"
        )

        assert category.active is True
        assert category.description == "" or category.description is None


@pytest.mark.django_db
class TestProductModel:

    def test_create_product(self):
        category = Category.objects.create(
            title="Livros",
            slug="livros",
            active=True
        )

        product = Product.objects.create(
            title="Python Programming",
            description="Learn Python",
            price=99.99,
            active=True
        )
        product.category.add(category)

        assert product.id is not None
        assert product.title == "Python Programming"
        assert product.price == 99.99
        assert product.active is True
        assert category in product.category.all()

    def test_product_with_multiple_categories(self):
        cat1 = Category.objects.create(title="Livros", slug="livros", active=True)
        cat2 = Category.objects.create(title="Programação", slug="programacao", active=True)

        product = Product.objects.create(
            title="Python Book",
            price=50,
            active=True
        )
        product.category.add(cat1, cat2)

        assert product.category.count() == 2

    def test_product_price_positive(self):
        category = Category.objects.create(title="Livros", slug="livros", active=True)

        with pytest.raises(Exception):
            product = Product.objects.create(
                title="Produto Inválido",
                price=-10,
                active=True
            )
            product.full_clean()

    def test_product_str_representation(self):
        product = Product.objects.create(
            title="Django Book",
            price=75,
            active=True
        )

        assert "Product object" in str(product)

    def test_delete_category_effect_on_product(self):
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

        category.delete()

        product.refresh_from_db()
        assert product.category.count() == 0

    def test_product_can_be_inactive(self):
        product = Product.objects.create(
            title="Discontinued Product",
            price=10,
            active=False
        )

        assert product.active is False

    def test_product_price_decimal(self):
        product = Product.objects.create(
            title="Test Product",
            price=Decimal("29.99"),
            active=True
        )

        assert product.price == Decimal("29.99")