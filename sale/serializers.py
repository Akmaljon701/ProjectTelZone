from rest_framework.serializers import ModelSerializer
from client.serializers import ClientSerializerForRelation
from product.serializers import ProductSerializerForRelation
from sale.models import Sale, CreditBase


class CreditBaseCreateSerializer(ModelSerializer):
    class Meta:
        model = CreditBase
        fields = ('name',)


class CreditBaseUpdateSerializer(ModelSerializer):
    class Meta:
        model = CreditBase
        fields = ('name',)


class CreditBaseGetSerializer(ModelSerializer):
    class Meta:
        model = CreditBase
        fields = ('id', 'name',)


class SaleCreateSerializer(ModelSerializer):

    class Meta:
        model = Sale
        fields = ['product', 'client', 'sold_price', 'credit_base', 'info', 'date']
        read_only_fields = ['date']


class SaleUpdateSerializer(ModelSerializer):
    class Meta:
        model = Sale
        fields = ('product', 'client', 'sold_price')


class SaleGetSerializer(ModelSerializer):
    product = ProductSerializerForRelation()
    client = ClientSerializerForRelation()

    class Meta:
        model = Sale
        fields = ('product', 'client', 'sold_price')
