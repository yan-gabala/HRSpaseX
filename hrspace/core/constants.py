from enum import IntEnum


class Limits(IntEnum):
    BUSINESS_TRIP_LENGTH = 50
    DESIGNATION = 200
    EDUCATION_LENGTH = 50
    LINE_OF_BUSINESS = 200
    MAX_LEN_EMAIL_FIELD = 256
    MAX_LEN_USERS_CHARFIELD = 150
    MAX_SALARY = 999999
    MIN_AMOUNT_EMPLOYEES = 1
    MIN_SАLARY = 17000
    NAME_MAX_LEN = 100
    PAYMENT_LENGTH = 50
    PORTFOLIO_LENGTH = 50
    WORK_EXPERIENCE_LENGTH = 100
    WORK_FORMAT_LENGTH = 200


BENEFITS_PACKAGE_CHOICES = [
    ('VHI', 'ДМС'),
    ('vocation', 'Отпуск'),
    ('free_education', 'Компенсация обучения'),
    ('free_meals', 'Компенсация питания')
]

BUSINESS_TRIP_CHOICES = [
    ('yes', 'Да'),
    ('no', 'Нет'),
    ('sometimes', 'Иногда')
]

CITY_CHOICES = [
    ('tver', 'Тверь'),
    ('pskov', 'Псков')
]

EDUCATION_CHOICES = [
    ('is_required', 'Требуется'),
    ('not_required', 'Не требуется')
]

EMPLOYMENT_CHOICES = [
    ('full', 'Полная'),
    ('partial', 'Частичная'),
    ('project', 'Проектная'),
    ('internship', 'Стажировка'),
]

SСHEDULE_CHOICES = [
    ('full_day', 'Полный день'),
    ('flexible schedule', 'Гибкий график'),
    ('shift work', 'Сменный график'),
    ('watch', 'Вахтовый метод'),
]

FORMAT_INTERVIEWS_CHOICES = [
    (1, 'Со всеми кандидатами с релевантным резюме'),
    (2, 'Итоговое собеседование с кандидатами, '
        'прошедшими предварительный отбор')
]

HR_RESPONSIBILITY_CHOICES = [
    (1, 'Поиск и предоставление релевантных резюме'),
    (2, 'Проведение первичных интервью'),
    (3, 'Организация собеседований с заказчиком + '
        'присутствие на собеседованиях'),
    (4, 'Запрос рекомендаций с предыдущих мест работы'),
    (5, 'Отправка кандидату тестового задания'),
    (6, 'Отправка кандидату дополнительной анкеты'),
    (7, 'Отправка финалисту приглашения на работу')
]

INFO_CANDIDATES_CHOICES = [
    (1, 'Резюме без предварительного собеседования'),
    (2, 'Резюме кандидатов с проведенными первичными интервью')
]

PAYMENT_CHOICES = [
    ('credit_card', 'Банковская карта'),
    ('instant_payment_system', 'СБП')
]

PAYMENT_HR_CHOICES = [
    (1, '100% за выход сотрудника'),
    (2, '50% за выход и 50% по окончанию гарантийного периода'),
    (3, '100% по окончанию гарантийного периода')
]

PORTFOLIO_CHOICES = [
    ('is_required', 'Требуется'),
    ('not_required', 'Не требуется')
]

PROFESSION_CHOICES = [
    ('analyst', 'Аналитик данных'),
    ('data_scientist', 'Специалист по Data Science'),
    ('python_dev', 'Python-разработчик'),
    ('web_dev', 'Веб-разработчик'),
    ('qa_engineer', 'Инженер по тестированию(QA)'),
]

WORK_EXPERIENCE_CHOICES = [
    ('doesnot_matter', 'Не имеет значение')
    ('up_to_year', 'До года'),
    ('from_one_to_three_years', 'От 1 года до 3 лет'),
    ('from_three_to_six_years', 'От 3 года до 6 лет'),
    ('more_six_years', 'Более 6 лет')
    ('without_experience', 'Без опыта'),
]

WORK_FORMAT_CHOICES = [
    ('remote', 'Удалённая'),
    ('mixed', 'Гибрид'),
    ('office', 'Офис')
]
