from rest_framework.fields import ListField, IntegerField
from rest_framework.serializers import ModelSerializer

from client.serializers import ClientSerializer
from product.serializers import ProductSerializer
from sale.models import Sale


class SaleSerializer(ModelSerializer):
    product = ProductSerializer()
    client = ClientSerializer()

    class Meta:
        model = Sale
        fields = ('product', 'client', 'sold_price')


class CreateAndUpdateSaleSerializer(ModelSerializer):
    class Meta:
        model = Sale
        fields = ('product', 'client', 'sold_price')

