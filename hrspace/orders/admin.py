from django.contrib import admin

from orders.models import (City, HrRequirements, HrResponsibility, LineOfBusiness,
                           Order, Skill)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'line_of_business', 'city', 'work_format',
        'salary_from', 'salary_to'
    )
    list_filter = ('city', 'line_of_business', 'work_format')


admin.site.register(City)
admin.site.register(HrRequirements)
admin.site.register(HrResponsibility)
admin.site.register(LineOfBusiness)
admin.site.register(Skill)
