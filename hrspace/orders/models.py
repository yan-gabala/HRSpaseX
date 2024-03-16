from core.constants import (CITY_CHOICES, EMPLOYMENT_CHOICES,
                            PROFESSION_CHOICES, TYPE_EMPLOYMENT_LENGTH, Limits)
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models


class Profession(models.Model):
    """Модель Профессия"""
    name = models.CharField(
        max_length=Limits.DESIGNATION.value,
        # поменять на скрипт загрузки из файла в БД #
        choices=PROFESSION_CHOICES,
        # ------------------------------------------#
        verbose_name='Профессия'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    """Модель Город"""
    name = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        choices=CITY_CHOICES,
        verbose_name='Город'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    """Модель Заявка"""
    name = models.CharField(
        max_length=Limits.DESIGNATION.value,
        verbose_name='Название вакансии',
        validators=[
            RegexValidator(
                regex='[a-zа-я]+',
                message='Принимаются слова из букв'
            )
        ]
    )
    profession = models.ManyToManyField(
        Profession,
        related_name='professions',
        verbose_name='Профессия'
    )
    city = models.ManyToManyField(
        City,
        related_name='cities',
        verbose_name='Город'
    )
    type_employment = models.CharField(
        verbose_name='Тип занятости',
        choices=EMPLOYMENT_CHOICES,
        max_length=TYPE_EMPLOYMENT_LENGTH
    )
    salary_from = models.PositiveIntegerField(
        verbose_name='Минимальная зарплата gross(до вычета НДФЛ)',
        default=0,
        validators=[
            MinValueValidator(
                Limits.MIN_SАLARY.value,
                'Заработная плата по ТК не менее 17 000'
            )
        ]
    )
    salary_to = models.PositiveIntegerField(
        verbose_name='Максимальная зарплата gross(до вычета НДФЛ)',
        default=0,
        validators=[
            MaxValueValidator(
                Limits.MAX_SALARY.value,
                'Проверьте предлагаемую з/п'
            )
        ]
    )

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.name
