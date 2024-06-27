from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from product.models import Product


class ProductSerializerForRelation(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ['status']


class ProductUpdateSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ['status']


class ProductGetSerializer(ModelSerializer):
    purchase_price = SerializerMethodField()
    percent = SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_purchase_price(self, obj):
        user = self.context['request'].user
        if user.role == 'worker':
            return 0
        return obj.purchase_price

    def get_percent(self, obj):
        user = self.context['request'].user
        if user.role == 'worker':
            return 0
        return obj.percent



