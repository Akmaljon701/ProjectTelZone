from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from user.models import CustomUser


@extend_schema(responses={
    200: {"description": "The operation was completed successfully", "example": dict(CustomUser.ROLE_CHOICES)},
})
@api_view(['GET'])
@permission_classes([AllowAny])
def user_role_choices(request):
    choices = dict(CustomUser.ROLE_CHOICES)
    return JsonResponse(choices)
