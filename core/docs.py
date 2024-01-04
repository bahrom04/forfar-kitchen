# receipt_service/docs.py

from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Printer API",
        default_version='v1',
        description="API for check printing service",
        terms_of_service="terms/",
        contact=openapi.Contact(email="raxmatovbahrom7@gmail.com"),
        license=openapi.License(name="Apache"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('order.urls')), 
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
