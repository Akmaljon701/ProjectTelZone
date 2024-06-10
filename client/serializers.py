from rest_framework.serializers import ModelSerializer
from client.models import Client


class ClientSerializerForRelation(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientCreateSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'FIO', 'phone_number')


class ClientUpdateSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'FIO', 'phone_number')


class ClientGetSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'FIO', 'phone_number')
