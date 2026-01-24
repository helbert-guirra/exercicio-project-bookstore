from rest_framework import serializers
from order.models.order import Order
from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=True, many=True)
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total

    class Meta:
        model = Order  # ← ERA Product, AGORA É Order!
        fields = ['product', 'total']