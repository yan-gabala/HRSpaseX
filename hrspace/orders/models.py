from core.constants import (BENEFITS_PACKAGE_CHOICES, BUSINESS_TRIP_CHOICES,
                            CITY_CHOICES, EDUCATION_CHOICES,
                            EMPLOYMENT_CHOICES, HR_RESPONSIBILITY_CHOICES,
                            INFO_CANDIDATES_CHOICES, PAYMENT_CHOICES,
                            PAYMENT_HR_CHOICES, PORTFOLIO_CHOICES,
                            PROFESSION_CHOICES, WORK_EXPERIENCE_CHOICES,
                            WORK_FORMAT_CHOICES, Limits)
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models


class Profession(models.Model):
    """Модель Профессия"""
    name = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        # поменять на скрипт загрузки из файла в БД #
        choices=PROFESSION_CHOICES,
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
        # добавить скрипт загрузки данных из файла в БД #
        choices=CITY_CHOICES,
        verbose_name='Город'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f'{self.name}'


class TypeEmployment(models.Model):
    """Модель Тип занятости"""
    name = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        choices=EMPLOYMENT_CHOICES,
        verbose_name='Тип занятости'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тип занятости'
        verbose_name_plural = 'Типы занятости'

    def __str__(self):
        return f'{self.name}'


class Skill(models.Model):
    """Модель Ключевые навыки"""
    name = models.CharField(
        max_length=Limits.DESIGNATION.value,
        # добавить скрипт загрузки данных из файла в БД #
        verbose_name='Ключевые навыки'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ключевой навык'
        verbose_name_plural = 'Ключевые навыки'

    def __str__(self):
        return f'{self.name}'


class HrResponsibility(models.Model):
    """Модель Обязанности рекрутера"""
    name = models.PositiveIntegerField(
        choices=HR_RESPONSIBILITY_CHOICES,
        verbose_name='Обязанности рекрутера'
    )

    class Meta:
        verbose_name = 'Обязанность рекрутера'
        verbose_name_plural = 'Обязанности рекрутера'

    def __str__(self):
        return f'{self.name}'


class BenefitsPackage(models.Model):
    """Модель Социальный пакет"""
    name = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        choices=BENEFITS_PACKAGE_CHOICES,
        verbose_name='Социальный пакет'
    )

    class Meta:
        verbose_name = 'Социальный пакет'
        verbose_name_plural = 'Социальные пакеты'

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
    work_format = models.CharField(
        verbose_name='Формат работы',
        choices=WORK_FORMAT_CHOICES,
        max_length=Limits.WORK_FORMAT_LENGTH.value
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
    amount_of_subordinate = models.PositiveIntegerField(
        verbose_name='Количество подчинённых в управлении',
        default=0
    )
    type_employment = models.ManyToManyField(
        TypeEmployment,
        related_name='employments',
        verbose_name='Тип занятости'
    )
    start_work_day = models.TimeField(
        verbose_name='Начало рабочего дня',
        null=True,
        blank=True
    )
    end_work_day = models.TimeField(
        verbose_name='Окончание рабочего дня',
        null=True,
        blank=True
    )
    benefits_package = models.ManyToManyField(
        BenefitsPackage,
        related_name='packages',
        verbose_name='Социальный пакет',
    )
    business_trip = models.CharField(
        verbose_name='Командировка',
        choices=BUSINESS_TRIP_CHOICES,
        max_length=Limits.BUSINESS_TRIP_LENGTH.value
    )
    work_experience = models.CharField(
        verbose_name='Опыт работы',
        choices=WORK_EXPERIENCE_CHOICES,
        max_length=Limits.WORK_EXPERIENCE_LENGTH.value
    )
    education = models.CharField(
        verbose_name='Образование',
        choices=EDUCATION_CHOICES,
        max_length=Limits.EDUCATION_LENGTH.value
    )
    portfolio = models.CharField(
        verbose_name='Портфолио',
        choices=PORTFOLIO_CHOICES,
        max_length=Limits.PORTFOLIO_LENGTH.value
    )
    employee_responsibility = models.TextField(
        verbose_name='Обязанности сотрудника'
    )
    skill = models.ManyToManyField(
        Skill,
        related_name='skills',
        verbose_name='Ключевые навыки'
    )

    amount_of_employees = models.PositiveIntegerField(
        verbose_name='Количество сотрудников',
        default=0,
        validators=[
            MinValueValidator(
                Limits.MIN_AMOUNT_EMPLOYEES.value,
                'Количество сотрудников должно быть выше 0'
            )
        ]
    )
    payment_hr = models.PositiveIntegerField(
        verbose_name='Выплата рекрутеру',
        choices=PAYMENT_HR_CHOICES
    )
    award = models.PositiveIntegerField(
        verbose_name='Вознаграждение за сотрудника',
        default=0
    )
    start_interview = models.DateField(
        verbose_name='Старт собеседований с кандидатом'
    )
    start_work = models.DateField(
        verbose_name='Дата вступления сотрудника в должность'
    )
    hr_responsibility = models.ManyToManyField(
        HrResponsibility,
        related_name='responsobilities',
        verbose_name='Обязанности рекрутера',
    )
    info_candidates = models.PositiveIntegerField(
        verbose_name='Предоставление данных о кандидатах',
        choices=INFO_CANDIDATES_CHOICES
    )
    payment = models.CharField(
        verbose_name='Тип оплаты',
        choices=PAYMENT_CHOICES,
        max_length=Limits.PAYMENT_LENGTH.value
    )

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.name
