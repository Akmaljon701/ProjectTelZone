from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer
from user.models import CustomUser, CustomUserPermission


class CustomUserPermissionSerializerForRelation(ModelSerializer):

    class Meta:
        model = CustomUserPermission
        exclude = ['id', 'user']


class CustomUserPermissionSerializer(ModelSerializer):

    class Meta:
        model = CustomUserPermission
        exclude = ['user']


class CustomUserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'role')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        instance = super().update(instance, validated_data)
        return instance


class CurrentUserUpdateSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'username', 'password')

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        instance = super().update(instance, validated_data)
        return instance


class CustomUserGetSerializer(ModelSerializer):
    permission_fields = CustomUserPermissionSerializerForRelation()

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'username', 'role', 'permission_fields')


class CurrentUserGetSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'username', 'role')
