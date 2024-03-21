from rest_framework import serializers

from orders.models import City, LineOfBusiness, Order


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class LineOfBusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model = LineOfBusiness
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
