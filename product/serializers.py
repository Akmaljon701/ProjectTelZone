from rest_framework.serializers import ModelSerializer, Serializer, ListField, IntegerField
from product.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'status': {'read_only': True},
            'client': {'read_only': True}
        }



