from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from user.serializers import CustomUserSerializer


@extend_schema(summary="Get current user", responses=CustomUserSerializer)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def get_current_user(request):
    serializer = CustomUserSerializer(request.user)
    return Response(serializer.data, status=200)


@extend_schema(
    summary="Get current user",
    request=CustomUserSerializer,
    responses={
        200: CustomUserSerializer
    },
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def update_custom_user(request):
    serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=200)
