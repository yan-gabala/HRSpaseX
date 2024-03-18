from django.urls import include, path
from rest_framework import routers

from api.views import CityViewSet, OrderViewSet, ProfessionViewSet

router = routers.DefaultRouter()
router.register('cities', CityViewSet)
router.register('orders', OrderViewSet)
router.register('professions', ProfessionViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),

]
