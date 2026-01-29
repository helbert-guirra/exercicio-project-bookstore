from rest_framework import serializers
from product.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title"]


class ProductSerializer(serializers.ModelSerializer):
    categories_id = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True
    )

    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "price",
            "active",
            "category",
            "categories_id",
        ]

    def create(self, validated_data):
        categories_id = validated_data.pop("categories_id")
        product = Product.objects.create(**validated_data)
        product.category.set(categories_id)
        return product