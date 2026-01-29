
from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    """
    ViewSet responsável por gerenciar as operações
    de CRUD do modelo Order.
    """

    # Serializer que converte Model <-> JSON
    serializer_class = OrderSerializer

    # Queryset base usado pelo ViewSet
    queryset = Order.objects.all()
