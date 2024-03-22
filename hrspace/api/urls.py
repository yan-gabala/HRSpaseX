from django.urls import include, path
from rest_framework import routers
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

from api.views import CityViewSet, LineOfBusinessViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register('cities', CityViewSet)
router.register('line_of_business', LineOfBusinessViewSet)
router.register('orders', OrderViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'v1/schema/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger'
    ),
    path(
        'v1/schema/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
]
