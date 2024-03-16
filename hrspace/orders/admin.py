from django.contrib import admin

from orders.models import City, Order, Profession


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    pass



