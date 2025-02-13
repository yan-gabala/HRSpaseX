from enum import IntEnum


class Limits(IntEnum):
    ACTIVITY_MAX_LEN = 50
    BUSINESS_TRIP_LENGTH = 50
    DESIGNATION = 200
    EDUCATION_LENGTH = 50
    MAX_LEN_EMAIL_FIELD = 256
    MAX_LEN_USERS_CHARFIELD = 150
    MAX_SALARY = 999999
    MIN_AMOUNT_EMPLOYEES = 1
    MIN_SALARY = 17000
    NAME_MAX_LEN = 100
    PORTFOLIO_LENGTH = 50
    WORK_EXPERIENCE_LENGTH = 100
    WORK_FORMAT_LENGTH = 200
    INTERVIEW_MAX_LEN = 100


AMOUNT_HR_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3')
)

AWARD_OPTION_CHOICES = (
    (1, '100% за выход сотрудника'),
    (2, '50% за выход + 50% по окончании гарантийного периода'),
    (3, '100% по окончании гарантийного периода (1 месяц)')
)

BUSINESS_TRIP_CHOICES = (
    ('yes', 'Да'),
    ('no', 'Нет'),
    ('sometimes', 'Иногда')
)

EDUCATION_CHOICES = (
    ('higher', 'Высшее'),
    ('secondary_special', 'Среднее специальное'),
    ('courses', 'Курсы')
)

EMPLOYMENT_CHOICES = (
    ('full', 'Полная'),
    ('partial', 'Частичная'),
    ('project', 'Проектная'),
    ('internship', 'Стажировка'),
)

FORMAT_INTERVIEWS_CHOICES = (
    (1, 'Со всеми кандидатами, чьё резюме будет релевантным'),
    (2, 'С кандидатами, прошедшими предварительный отбор')
)

INFO_CANDIDATES_CHOICES = (
    (1, 'Резюме без предварительного собеседования'),
    (2, 'Резюме кандидатов с проведенными первичными интервью')
)

LINE_OF_BUSINESS_CHOICES = (
    ('analyst', 'Аналитик данных'),
    ('data_scientist', 'Специалист по Data Science'),
    ('python_dev', 'Python-разработчик'),
    ('web_dev', 'Веб-разработчик'),
    ('qa_engineer', 'Инженер по тестированию(QA)'),
)

PORTFOLIO_CHOICES = (
    ('is_required', 'Необходимо предоставить'),
    ('not_required', 'Не требуется')
)

SCHEDULE_CHOICES = (
    ('full_day', 'Полный день'),
    ('flexible schedule', 'Гибкий график'),
    ('shift work', 'Сменный график'),
    ('watch', 'Вахтовый метод'),
)

SKILL_CHOICES = (
    ('django', 'Django'),
    ('python', 'Python'),
    ('api', 'API'),
    ('tax_reporting', 'Налоговая отчетность'),
    ('financial_accounting', 'Бухгалтерский учёт')
)

WORK_EXPERIENCE_CHOICES = (
    ('doesnot_matter', 'Не имеет значение'),
    ('from_one_to_three_years', 'От 1 года до 3 лет'),
    ('from_three_to_six_years', 'От 3 до 6 лет'),
    ('more_six_years', 'Более 6 лет'),
    ('without_experience', 'Нет опыта'),
)

WORK_FORMAT_CHOICES = (
    ('remote', 'Удалённая'),
    ('mixed', 'Гибрид'),
    ('office', 'Офис')
)
