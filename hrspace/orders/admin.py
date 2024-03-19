from django.contrib import admin
from orders.models import (BenefitsPackage, City, HrResponsibility, Order,
                           Profession, Skill, TypeEmployment)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'get_profession', 'get_city', 'work_format',
        'salary_from', 'salary_to'
    )
    list_filter = ('profession', 'city', 'work_format')

    def get_profession(self, row):
        return ','.join([obj.name for obj in row.profession.all()])

    get_profession.short_description = 'Профессия'

    def get_city(self, row):
        return ','.join([obj.name for obj in row.city.all()])

    get_city.short_description = 'Город'


admin.site.register(BenefitsPackage)
admin.site.register(City)
admin.site.register(HrResponsibility)
admin.site.register(Profession)
admin.site.register(Skill)
admin.site.register(TypeEmployment)
