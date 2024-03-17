from rest_framework import routers
from django.urls import path, include

from api.views import (CityViewSet, OrderViewSet,
                       ProfessionViewSet)

router = routers.DefaultRouter()
router.register('cities', CityViewSet)
router.register('orders', OrderViewSet)
router.register('professions', ProfessionViewSet)


urlpatterns = [
    path('', include(router.urls)),

]
