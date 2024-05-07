from rest_framework.serializers import ModelSerializer
from client.models import Client
from product.serializers import ProductSerializer


class ClientSerializer(ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ('id', 'FIO', 'phone_number', 'products')

