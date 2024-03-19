from api.serializers import CitySerializer, LineOfBuisnessSerializer
from orders.models import City, Order, LineOfBuisness
from rest_framework.viewsets import ModelViewSet


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class ProfessionViewSet(ModelViewSet):
    queryset = LineOfBuisness.objects.all()
    serializer_class = LineOfBuisnessSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = LineOfBuisnessSerializer
