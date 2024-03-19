from django.contrib import admin

from orders.models import (BenefitsPackage, City, HrRequirements,
                           HrResponsibility, LineOfBuisness, Order, Skill,
                           TypeEmployment)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'get_line_of_buisness', 'get_city', 'work_format',
        'salary_from', 'salary_to'
    )
    list_filter = ('line_of_buisness', 'city', 'work_format')

    def get_line_of_buisness(self, row):
        return ','.join([obj.name for obj in row.line_of_buisness.all()])

    get_line_of_buisness.short_description = 'Профессия'

    def get_city(self, row):
        return ','.join([obj.name for obj in row.city.all()])

    get_city.short_description = 'Город'


admin.site.register(BenefitsPackage)
admin.site.register(City)
admin.site.register(HrResponsibility)
admin.site.register(LineOfBuisness)
admin.site.register(Skill)
admin.site.register(TypeEmployment)
admin.site.register(HrRequirements)
