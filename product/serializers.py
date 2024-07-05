from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, FloatField
from product.models import Product
from user.models import CustomUserPermission
from drf_spectacular.utils import extend_schema_field


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

    @extend_schema_field(FloatField)
    def get_purchase_price(self, obj) -> float:
        user = self.context['request'].user
        if user.role == 'worker':
            permission = CustomUserPermission.objects.get(user=user)
            if not permission.product_can_update:
                return 0
        return obj.purchase_price

    @extend_schema_field(FloatField)
    def get_percent(self, obj) -> float:
        user = self.context['request'].user
        if user.role == 'worker':
            permission = CustomUserPermission.objects.get(user=user)
            if not permission.product_can_update:
                return 0
        return obj.percent



