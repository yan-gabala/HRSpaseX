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
        fields = ('id', 'name', 'line_of_business', 'city', 'work_format',
                  'salary_from', 'salary_to', 'start_work_day', 'end_work_day',
                  'schedule', 'type_employment','business_trip', 'amount_of_subordinate',
                  'features_vacancy',
                  'work_experience','skill', 'education', 'portfolio',
                  'amount_of_employees', 'award_option', 'award', 'start_work',
                  'format_interview', 'start_interview', 'amount_of_hr',
                  'hr_responsibility', 'hr_requirements')
