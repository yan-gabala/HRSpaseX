from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models

from core.constants import (ACTIVITY_FORMAT_HR, AMOUNT_HR_CHOICES,
                            AWARD_OPTION_CHOICES,
                            BUSINESS_TRIP_CHOICES, CITY_CHOICES,
                            EDUCATION_CHOICES, EMPLOYMENT_CHOICES,
                            FORMAT_INTERVIEWS_CHOICES,
<<<<<<< HEAD
                            HR_RESPONSIBILITY_CHOICES, INFO_CANDIDATES_CHOICES,
                            PAYMENT_CHOICES, PAYMENT_HR_CHOICES,
                            PORTFOLIO_CHOICES, LINE_OF_BUISNESS_CHOICES,
                            SСHEDULE_CHOICES, WORK_EXPERIENCE_CHOICES,
=======
                            HR_RESPONSIBILITY_CHOICES,
                            LINE_OF_BUSINESS_CHOICES,
                            PORTFOLIO_CHOICES, SCHEDULE_CHOICES,
                            WORK_EXPERIENCE_CHOICES,
>>>>>>> 3495f3d (Chore: редактирование модели заявки)
                            WORK_FORMAT_CHOICES, Limits)


<<<<<<< HEAD
class LineOfBuisness(models.Model):
    """Модель Сфера деятельности"""
    name = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        # поменять на скрипт загрузки из файла в БД #
        choices=LINE_OF_BUISNESS_CHOICES,
        verbose_name='Сфера деятельности'
=======
class LineOfBusiness(models.Model):
    """Модель Сфера"""
    name = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        # поменять на скрипт загрузки из файла в БД #
        choices=LINE_OF_BUSINESS_CHOICES,
        verbose_name='Сфера'  # У дизайнеров в макете поле названо сфера
>>>>>>> 3495f3d (Chore: редактирование модели заявки)
    )

    class Meta:
        ordering = ('name',)
<<<<<<< HEAD
        verbose_name = 'Сфера деятельности'
        verbose_name_plural = 'Сферы деятельности'
=======
        verbose_name = 'Сфера'
        verbose_name_plural = 'Сферы'
>>>>>>> 3495f3d (Chore: редактирование модели заявки)

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


<<<<<<< HEAD
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


=======
>>>>>>> 3495f3d (Chore: редактирование модели заявки)
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
<<<<<<< HEAD
    name = models.CharField(
=======
    name = models.CharField(  # Поменять на PositiveIntegerField ?
        max_length=Limits.NAME_MAX_LEN.value,
>>>>>>> 3495f3d (Chore: редактирование модели заявки)
        choices=HR_RESPONSIBILITY_CHOICES,
        max_length=Limits.NAME_MAX_LEN.value,
        verbose_name='Обязанности рекрутера'
    )

    class Meta:
        verbose_name = 'Обязанность рекрутера'
        verbose_name_plural = 'Обязанности рекрутера'

    def __str__(self):
        return f'{self.name}'


class HrRequirements(models.Model):
    """Модель Требования к рекрутеру"""
    name = models.CharField(
        choices=ACTIVITY_FORMAT_HR,
        verbose_name='Форма деятельности',
        max_length=Limits.ACTIVITY_MAX_LEN.value
    )

    class Meta:
        verbose_name = 'Форма деятельности'
        verbose_name_plural = 'Формы деятельности'

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    """Модель Заявка"""

    """1 поле"""
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
<<<<<<< HEAD
    """2 поле"""
    line_of_buisness = models.ForeignKey(
        LineOfBuisness,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Сфера деятельности'
=======
    line_of_business = models.ForeignKey(
        LineOfBusiness,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Сфера'
>>>>>>> 3495f3d (Chore: редактирование модели заявки)
    )
    """3 поле"""
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='cities',
        verbose_name='Город'
    )
    """4 поле"""
    work_format = models.CharField(
        verbose_name='Формат работы',
        choices=WORK_FORMAT_CHOICES,
        max_length=Limits.WORK_FORMAT_LENGTH.value
    )
    """5 поле"""
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
    """6 поле"""
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
<<<<<<< HEAD
    """7 поле"""
=======
>>>>>>> 3495f3d (Chore: редактирование модели заявки)
    start_work_day = models.TimeField(
        verbose_name='Начало рабочего дня',
        null=True,
        blank=True
    )
<<<<<<< HEAD
    """8 поле"""
    end_work_day = models.TimeField(
        verbose_name='Окончание рабочего дня',
=======
    end_work_day = models.TimeField(
        verbose_name='Конец рабочего дня',
>>>>>>> 3495f3d (Chore: редактирование модели заявки)
        null=True,
        blank=True
    )
    """9 поле"""
    schedule = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        choices=SCHEDULE_CHOICES,
        verbose_name='График работы'
    )
<<<<<<< HEAD
    """10 поле"""
    type_employment = models.ForeignKey(
        TypeEmployment,
        on_delete=models.CASCADE,
        related_name='employments',
        verbose_name='Тип занятости'
    )
    ###########################################
    #
    ###########################################
    amount_of_subordinate = models.PositiveIntegerField(
        verbose_name='Количество подчинённых в управлении',
        default=0
    )
    benefits_package = models.ManyToManyField(
        BenefitsPackage,
        related_name='packages',
        verbose_name='Социальный пакет',
    )
=======
    amount_of_subordinate = models.PositiveIntegerField(
        verbose_name='Количество подчинённых в управлении',
        default=0
    )
    type_employment = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        choices=EMPLOYMENT_CHOICES,
        verbose_name='Тип занятости'
    )
>>>>>>> 3495f3d (Chore: редактирование модели заявки)
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
        verbose_name='Особенности вакансии',
    )
    work_experience = models.CharField(
        verbose_name='Опыт работы',
        choices=WORK_EXPERIENCE_CHOICES,
        max_length=Limits.WORK_EXPERIENCE_LENGTH.value
    )
    skill = models.ManyToManyField(
        Skill,
        related_name='skills',
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
<<<<<<< HEAD
    employee_responsibility = models.TextField(
        verbose_name='Обязанности сотрудника'
    )
    skill = models.ManyToManyField(
        Skill,
        related_name='skills',
        verbose_name='Ключевые навыки'
    )
=======
>>>>>>> 3495f3d (Chore: редактирование модели заявки)
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
<<<<<<< HEAD
    payment_hr = models.CharField(
        verbose_name='Выплата рекрутеру',
        choices=PAYMENT_HR_CHOICES,
        max_length=100
=======
    award_option = models.PositiveIntegerField(
        verbose_name='Варианты вознаграждения',
        choices=AWARD_OPTION_CHOICES
>>>>>>> 3495f3d (Chore: редактирование модели заявки)
    )
    award = models.PositiveIntegerField(
        verbose_name='Размер вознаграждения',
        default=0
    )
    start_work = models.DateField(
        verbose_name='Дата вступления в должность'
    )
    format_interview = models.CharField(
        verbose_name='Формат собеседований',
        choices=FORMAT_INTERVIEWS_CHOICES,
        max_length=Limits.INTERVIEW_MAX_LEN.value
    )
<<<<<<< HEAD
=======
    start_interview = models.DateField(
        verbose_name='Старт собеседований'
    )
    amount_of_hr = models.PositiveIntegerField(
        verbose_name='Количество рекрутеров',
        choices=AMOUNT_HR_CHOICES,
        default=1
    )
>>>>>>> 3495f3d (Chore: редактирование модели заявки)
    hr_responsibility = models.ManyToManyField(
        HrResponsibility,
        related_name='responsobilities',
        verbose_name='Обязанности рекрутера',
    )
    hr_requirements = models.ManyToManyField(
        HrRequirements,
        related_name='requirements',
        verbose_name='Требования к рекрутеру'
    )

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.name
