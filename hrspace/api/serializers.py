from rest_framework import serializers

from orders.models import City, Order, Profession


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class ProfessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profession
        fields = '__all__'
