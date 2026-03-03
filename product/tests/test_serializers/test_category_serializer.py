from django.test import TestCase
from product.factories import CategoryFactory
from product.serializers import CategorySerializer


class TestCategorySerializer(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory(title="food")
        self.serializer = CategorySerializer(self.category)

    def test_category_serializer(self):
        data = self.serializer.data
        self.assertEqual(data["title"], "food")
