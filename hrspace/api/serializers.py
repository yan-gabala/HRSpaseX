from rest_framework import serializers

from orders.models import City, LineOfBusiness, Order


class CitySerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = City
        fields = ('id', 'name')

    def validate_name(self, name):
        ...


class LineOfBusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model = LineOfBusiness
        fields = ('__all__')


class OrderSerializer(serializers.ModelSerializer):

    line_of_business = serializers.StringRelatedField(many=False)
    city = serializers.StringRelatedField(many=False)
    skill = serializers.StringRelatedField(many=True)
    salary_from = serializers.StringRelatedField()
    salary_to = serializers.StringRelatedField()
    amount_of_subordinate = serializers.StringRelatedField()
    amount_of_employees = serializers.StringRelatedField()
    award_option = serializers.StringRelatedField()
    award = serializers.StringRelatedField()
    format_interview = serializers.StringRelatedField()
    amount_of_hr = serializers.StringRelatedField()
    start_work_day = serializers.TimeField(format='%#H.%M')
    end_work_day = serializers.TimeField(format='%#H.%M')
    start_work = serializers.DateField(format='%d.%m.%Y')
    start_interview = serializers.DateField(format='%d.%m.%Y')

    class Meta:
        model = Order
        fields = ('id', 'name', 'line_of_business', 'city', 'work_format',
                  'salary_from', 'salary_to', 'start_work_day', 'end_work_day',
                  'schedule', 'type_employment', 'business_trip', 'amount_of_subordinate',
                  'features_vacancy',
                  'work_experience', 'skill', 'education', 'portfolio',
                  'amount_of_employees', 'award_option', 'award', 'start_work',
                  'format_interview', 'start_interview', 'amount_of_hr',
                  'hr_responsibility1', 'hr_responsibility2', 'hr_responsibility3',
                  'hr_responsibility4', 'hr_responsibility5', 'hr_requirements',
                  'hr_requirements1', 'hr_requirements2')
