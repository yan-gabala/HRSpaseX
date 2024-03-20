from rest_framework.viewsets import ModelViewSet

from api.serializers import (CitySerializer, LineOfBusinessSerializer,
                             OrderSerializer)
from orders.models import City, LineOfBusiness, Order


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class LineOfBusinessViewSet(ModelViewSet):
    queryset = LineOfBusiness.objects.all()
    serializer_class = LineOfBusinessSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
