from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.schemas import *
from user.serializers import CustomUserSerializer
from utils.responses import success


@get_current_user_schema
@api_view(['GET'])
def get_current_user(request):
    serializer = CustomUserSerializer(request.user)
    return Response(serializer.data, status=200)


@update_custom_user_schema
@api_view(['PUT'])
def update_custom_user(request):
    serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success
