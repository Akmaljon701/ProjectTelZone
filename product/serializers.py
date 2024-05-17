from rest_framework.serializers import ModelSerializer
from product.models import Product


class ProductSerializerForRelation(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = 'status'


class ProductUpdateSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = 'status'


class ProductGetSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



