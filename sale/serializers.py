from rest_framework.serializers import ModelSerializer
from client.serializers import ClientSerializerForRelation
from product.serializers import ProductSerializerForRelation
from sale.models import Sale, CreditBase


class SaleCreateSerializer(ModelSerializer):
    class Meta:
        model = Sale
        fields = ('product', 'client', 'sold_price')


class SaleUpdateSerializer(ModelSerializer):
    class Meta:
        model = Sale
        fields = ('product', 'client', 'sold_price')


class SaleGetSerializer(ModelSerializer):
    product = ClientSerializerForRelation()
    client = ProductSerializerForRelation()

    class Meta:
        model = Sale
        fields = ('product', 'client', 'sold_price')


class CreditBaseCreateSerializer(ModelSerializer):
    class Meta:
        model = CreditBase
        fields = ('name',)


class UpdateBaseCreateSerializer(ModelSerializer):
    class Meta:
        model = CreditBase
        fields = ('name',)


class GetBaseCreateSerializer(ModelSerializer):
    class Meta:
        model = CreditBase
        fields = ('id', 'name',)
