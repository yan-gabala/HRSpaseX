from orders.models import City, Order, LineOfBuisness
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class LineOfBuisnessSerializer(serializers.ModelSerializer):

    class Meta:
        model = LineOfBuisness
        fields = '__all__'
