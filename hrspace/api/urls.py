from django.urls import include, path
from rest_framework import routers

from api.views import CityViewSet, LineOfBusinessViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register('cities', CityViewSet)
router.register('line_of_business', LineOfBusinessViewSet)
router.register('orders', OrderViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),

]
