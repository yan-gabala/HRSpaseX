from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from orders.models import City, Order, Profession
from api.serializers import CitySerializer, ProfessionSerializer


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class ProfessionViewSet(ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = ProfessionSerializer