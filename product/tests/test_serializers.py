import pytest
from product.serializers import CategorySerializer, ProductSerializer
from product.models import Category, Product


@pytest.mark.django_db
class TestCategorySerializer:
    def test_category_serializer(self):
        # Dados de teste
        data = {
            "title": "Livros",
            "slug": "livros",
            "description": "Categoria de livros",
            "active": True
        }

        # Testando a desserialização
        serializer = CategorySerializer(data=data)

        # Verificando se os dados são válidos
        assert serializer.is_valid(), f"Erros: {serializer.errors}"

        # Salvando no banco
        category = serializer.save()

        # Verificando os dados salvos
        assert category.title == data["title"]
        assert category.slug == data["slug"]
        assert category.description == data["description"]
        assert category.active == data["active"]


@pytest.mark.django_db
class TestProductSerializer:
    def test_product_serializer(self):
        # Primeiro cria uma categoria
        category = Category.objects.create(
            title="Eletrônicos",
            slug="eletronicos",
            description="Produtos eletrônicos",
            active=True
        )

        # Cria um produto manualmente
        product = Product.objects.create(
            title="Notebook",
            description="Notebook Dell",
            price=3000,
            active=True
        )
        product.category.add(category)

        # Testa a SERIALIZAÇÃO (converter objeto em JSON)
        serializer = ProductSerializer(product)
        serialized_data = serializer.data

        # Verificando dados serializados
        assert serialized_data["title"] == "Notebook"
        assert serialized_data["description"] == "Notebook Dell"
        assert serialized_data["price"] == 3000
        assert serialized_data["active"] is True
        assert "category" in serialized_data
        assert len(serialized_data["category"]) == 1
        assert serialized_data["category"][0]["title"] == "Eletrônicos"