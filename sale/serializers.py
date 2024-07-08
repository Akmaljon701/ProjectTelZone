from drf_spectacular.utils import extend_schema_field
from rest_framework.fields import SerializerMethodField, FloatField
from rest_framework.serializers import ModelSerializer
from client.serializers import ClientSerializerForRelation
from product.serializers import ProductSerializerForRelation
from sale.models import Sale, CreditBase
from user.serializers import CustomUserSerializerForRelation


class CreditBaseSerializerForRelation(ModelSerializer):
    class Meta:
        model = CreditBase
        fields = '__all__'


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
        fields = ['product', 'client', 'sold_price', 'credit_base', 'discount', 'info', 'date']
        read_only_fields = ['date']


class SaleUpdateSerializer(ModelSerializer):
    class Meta:
        model = Sale
        fields = ['product', 'client', 'sold_price', 'discount', 'credit_base', 'info']


class SalesGetSerializer(ModelSerializer):
    product = ProductSerializerForRelation(many=True)
    client = ClientSerializerForRelation()
    credit_base = CreditBaseSerializerForRelation(many=True)
    sold_user = CustomUserSerializerForRelation()
    bought_price = SerializerMethodField()

    class Meta:
        model = Sale
        fields = ('id', 'product', 'client', 'bought_price', 'sold_price',
                  'credit_base', 'discount', 'info', 'date', 'sold_user')

    @extend_schema_field(FloatField)
    def get_bought_price(self, obj) -> float:
        if self.context['request'].user.role == 'admin':
            total_bought_price = sum(product.purchase_price for product in obj.product.all())
            return total_bought_price
        else:
            return 0


class SaleGetSerializer(ModelSerializer):
    product = ProductSerializerForRelation(many=True)
    client = ClientSerializerForRelation()
    credit_base = CreditBaseSerializerForRelation(many=True)
    bought_price = SerializerMethodField()

    class Meta:
        model = Sale
        fields = ('id', 'product', 'client', 'bought_price','sold_price',
                  'credit_base', 'discount', 'info', 'date', 'sold_user')

    @extend_schema_field(FloatField)
    def get_bought_price(self, obj) -> float:
        if self.context['request'].user.role == 'admin':
            total_bought_price = sum(product.purchase_price for product in obj.product.all())
            return total_bought_price
        else:
            return 0
