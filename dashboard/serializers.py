from rest_framework.serializers import ModelSerializer
from dashboard.models import Expense


class ExpenseCreateSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class ExpenseUpdateSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class ExpenseGetSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

