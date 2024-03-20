from django.contrib import admin
from orders.models import (City, HrResponsibility, LineOfBusiness, Order,
                           Skill)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'get_line_of_business', 'get_city', 'work_format',
        'salary_from', 'salary_to'
    )
    list_filter = ('line_of_business', 'city', 'work_format')

    def get_line_of_business(self, row):
        return ','.join([obj.name for obj in row.line_of_business.all()])

    get_line_of_business.short_description = 'Сфера'

    def get_city(self, row):
        return ','.join([obj.name for obj in row.city.all()])

    get_city.short_description = 'Город'


admin.site.register(City)
admin.site.register(HrResponsibility)
admin.site.register(LineOfBusiness)
admin.site.register(Skill)
