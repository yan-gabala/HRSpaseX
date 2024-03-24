from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models

from core.constants import (AMOUNT_HR_CHOICES,
                            AWARD_OPTION_CHOICES,
                            BUSINESS_TRIP_CHOICES,
                            EDUCATION_CHOICES, EMPLOYMENT_CHOICES,
                            FORMAT_INTERVIEWS_CHOICES,
                            LINE_OF_BUSINESS_CHOICES,
                            PORTFOLIO_CHOICES, SCHEDULE_CHOICES,
                            SKILL_CHOICES, WORK_EXPERIENCE_CHOICES,
                            WORK_FORMAT_CHOICES, Limits)


class LineOfBusiness(models.Model):
    """Модель Сфера"""
    name = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        choices=LINE_OF_BUSINESS_CHOICES,
        verbose_name='Сфера'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Сфера'
        verbose_name_plural = 'Сферы'

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    """Модель Город"""
    name = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        blank=False,
        unique=True,
        verbose_name='Город'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f'{self.name}'


class Skill(models.Model):
    """Модель Ключевые навыки"""
    name = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        choices=SKILL_CHOICES,
        # добавить скрипт загрузки данных из файла в БД #
        verbose_name='Ключевые навыки'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ключевой навык'
        verbose_name_plural = 'Ключевые навыки'

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
    line_of_business = models.ForeignKey(
        LineOfBusiness,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Сфера'
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='cities',
        verbose_name='Город'
    )
    work_format = models.CharField(
        verbose_name='Формат работы',
        choices=WORK_FORMAT_CHOICES,
        max_length=Limits.WORK_FORMAT_LENGTH.value
    )
    salary_from = models.PositiveIntegerField(
        verbose_name='Минимальная зарплата до вычета НДФЛ',
        default=0,
        validators=[
            MinValueValidator(
                Limits.MIN_SALARY.value,
                'Заработная плата по ТК не менее 17 000'
            )
        ]
    )
    salary_to = models.PositiveIntegerField(
        verbose_name='Максимальная зарплата до вычета НДФЛ',
        default=0,
        validators=[
            MaxValueValidator(
                Limits.MAX_SALARY.value,
                'Проверьте предлагаемую з/п'
            )
        ]
    )
    start_work_day = models.TimeField(
        verbose_name='Начало рабочего дня',
        null=True,
        blank=True
    )
    end_work_day = models.TimeField(
        verbose_name='Конец рабочего дня',
        null=True,
        blank=True
    )
    schedule = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        choices=SCHEDULE_CHOICES,
        verbose_name='График работы'
    )
    type_employment = models.CharField(
        verbose_name='Тип занятости',
        max_length=Limits.NAME_MAX_LEN.value,
        choices=EMPLOYMENT_CHOICES
    )
    business_trip = models.CharField(
        verbose_name='Командировки',
        choices=BUSINESS_TRIP_CHOICES,
        max_length=Limits.BUSINESS_TRIP_LENGTH.value
    )
    amount_of_subordinate = models.PositiveIntegerField(
        verbose_name='Сотрудников в подчинении',
        default=0
    )
    features_vacancy = models.TextField(
        verbose_name='Особенности вакансии'
    )
    work_experience = models.CharField(
        verbose_name='Опыт работы',
        choices=WORK_EXPERIENCE_CHOICES,
        max_length=Limits.WORK_EXPERIENCE_LENGTH.value
    )
    skill = models.ManyToManyField(
        Skill,
        related_name='orders',
        verbose_name='Ключевые навыки'
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
    amount_of_employees = models.PositiveIntegerField(
        verbose_name='Количество сотрудников для поиска',
        default=0,
        validators=[
            MinValueValidator(
                Limits.MIN_AMOUNT_EMPLOYEES.value,
                'Количество сотрудников должно быть выше 0'
            )
        ]
    )
    award_option = models.PositiveIntegerField(
        verbose_name='Варианты вознаграждения',
        choices=AWARD_OPTION_CHOICES,
        default=1
    )
    award = models.PositiveIntegerField(
        verbose_name='Размер вознаграждения',
        default=0
    )
    start_work = models.DateField(
        verbose_name='Дата вступления в должность'
    )
    format_interview = models.PositiveIntegerField(
        verbose_name='Формат собеседований',
        choices=FORMAT_INTERVIEWS_CHOICES,
        default=1
    )
    start_interview = models.DateField(
        verbose_name='Старт собеседований'
    )
    amount_of_hr = models.PositiveIntegerField(
        verbose_name='Количество рекрутеров',
        choices=AMOUNT_HR_CHOICES,
        default=1
    )
    hr_responsibility1 = models.BooleanField(
        verbose_name='Подбор кандидатов',
        default=False
    )
    hr_responsibility2 = models.BooleanField(
        verbose_name='Организация собеседований',
        default=False
    )
    hr_responsibility3 = models.BooleanField(
        verbose_name='Проведение собеседований',
        default=False
    )
    hr_responsibility4 = models.BooleanField(
        verbose_name='Запрос рекомендаций',
        default=False
    )
    hr_responsibility5 = models.BooleanField(
        verbose_name='Отправка тестового задания',
        default=False
    )
    hr_requirements = models.TextField(
        verbose_name='Требования к рекрутеру'
    )
    hr_requirements1 = models.BooleanField(
        verbose_name='Только для юридических лиц и ИП',
        default=False
    )
    hr_requirements2 = models.BooleanField(
        verbose_name='Только для самозанятых и фрилансеров',
        default=False
    )

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.name
