from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static
from sale.views import create_credit_base, update_credit_base, get_credit_bases, get_credit_base

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('credit_base/create/', create_credit_base, name='create_credit_base'),
    path('credit_base/update/', update_credit_base, name='update_credit_base'),
    path('credit_base/all/', get_credit_bases, name='get_credit_bases'),
    path('credit_base/', get_credit_base, name='get_credit_base'),

    path('user/', include('user.urls')),
    path('client/', include('client.urls')),
    path('product/', include('product.urls')),
    path('sale/', include('sale.urls')),
    path('dashboard/', include('dashboard.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
