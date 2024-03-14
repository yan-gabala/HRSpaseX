from django.db import models


from .constants import (NAME_MAX_LEN, CITY_CHOICES,
                        PROFESSION_CHOICES)
from .validators import SALARY_VALIDATOR

class ApplicationForm(models.Model):
    profession = models.CharField(
        max_length=NAME_MAX_LEN,
        choices=PROFESSION_CHOICES,
        verbose_name='Профессия'
    )
    city = models.CharField(
        max_length=NAME_MAX_LEN,
        choices=CITY_CHOICES,
        verbose_name='Город'
    )
    salary = models.PositiveIntegerField(
        verbose_name='Зарплата gross(до вычета НДФЛ)',
        validators=SALARY_VALIDATOR
    )
    what_do = models.TextField(
        verbose_name='Обязанности сотрудника',
    )
