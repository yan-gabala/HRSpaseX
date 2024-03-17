from django.contrib import admin
from orders.models import (BenefitsPackage, City, HrResponsibility, Order,
                           Profession, Skill, TypeEmployment)


@admin.register(BenefitsPackage)
class BenefitsPackageAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(HrResponsibility)
class HrResponsibilityAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(TypeEmployment)
class TypeEmploymentAdmin(admin.ModelAdmin):
    pass