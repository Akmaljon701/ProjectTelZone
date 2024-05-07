from rest_framework.fields import ListField, IntegerField
from rest_framework.serializers import ModelSerializer

from sale.models import Sale


class SellProductSerializer(ModelSerializer):
    class Meta:
        model = Sale
        fields = ('product', 'client', 'sold_price')
