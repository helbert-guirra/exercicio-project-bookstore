from rest_framework import serializers
from product.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    categories_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        many=True,
        write_only=True
    )

    class Meta:
        model = Product
        fields = ["id", "title", "price", "active", "categories_id"]

    def create(self, validated_data):
        categories = validated_data.pop("category")
        product = Product.objects.create(**validated_data)
        product.category.set(categories)
        return product