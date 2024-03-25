from django.test import TestCase

from orders.models import (City, Order, LineOfBusiness, Skill)


class OrderTests(TestCase):

    def setUp(self):
        self.city = City.objects.create(name='tver')
        self.line_of_business = LineOfBusiness.objects.create(name='python_dev')
        self.skill = Skill.objects.create(name='тестовый навык')

        self.order = Order.objects.create(
            name='Тестовое название вакансии',
            line_of_business=self.line_of_business,
            city=self.city,
            work_format='office',
            salary_from='40000',
            salary_to='50000',
            start_work_day='09:00:00',
            end_work_day='18:00:00',
            schedule='shift work',
            type_employment='partial',
            business_trip='no',
            amount_of_subordinate='0',
            features_vacancy='тест особенности вакансии',
            work_experience='from_one_to_three_years',
            education='higher',
            portfolio='not_required',
            amount_of_employees='1',
            award_option='1',
            award='20000',
            start_work='2024-03-31',
            format_interview='1',
            start_interview='2024-03-25',
            amount_of_hr='1',
            hr_responsibility1=True,
            hr_responsibility2=True,
            hr_responsibility3=False,
            hr_responsibility4=True,
            hr_responsibility5=False,
            hr_requirements='Требования к рекрутеру',
            hr_requirements1=True,
            hr_requirements2=False,
        )

    def test_order(self):
        """Проверка полей модели Заявка"""
        self.assertEqual(self.order.name, 'Тестовое название вакансии')
        self.assertEqual(self.order.line_of_business, self.line_of_business)
        self.assertEqual(self.order.city, self.city)
        self.assertEqual(self.order.work_format, 'office')
        self.assertEqual(self.order.salary_from, '40000')
        self.assertEqual(self.order.salary_to, '50000')
        self.assertEqual(self.order.start_work_day, '09:00:00')
        self.assertEqual(self.order.end_work_day, '18:00:00')
        self.assertEqual(self.order.schedule, 'shift work')
        self.assertEqual(self.order.type_employment, 'partial')
        self.assertEqual(self.order.business_trip, 'no')
        self.assertEqual(self.order.amount_of_subordinate, '0')
        self.assertEqual(self.order.features_vacancy, 'тест особенности вакансии')
        self.assertEqual(self.order.work_experience, 'from_one_to_three_years')
        self.assertEqual(self.order.education, 'higher')
        self.assertEqual(self.order.portfolio, 'not_required')
        self.assertEqual(self.order.amount_of_employees, '1')
        self.assertEqual(self.order.award_option, '1')
        self.assertEqual(self.order.award, '20000')
        self.assertEqual(self.order.start_work, '2024-03-31')
        self.assertEqual(self.order.format_interview, '1')
        self.assertEqual(self.order.start_interview, '2024-03-25')
        self.assertEqual(self.order.amount_of_hr, '1')
        self.assertEqual(self.order.hr_responsibility1, True),
        self.assertEqual(self.order.hr_responsibility2, True),
        self.assertEqual(self.order.hr_responsibility3, False),
        self.assertEqual(self.order.hr_responsibility4, True),
        self.assertEqual(self.order.hr_responsibility5, False),
        self.assertEqual(
            self.order.hr_requirements,
            'Требования к рекрутеру'
        ),
        self.assertEqual(self.order.hr_requirements1, True),
        self.assertEqual(self.order.hr_requirements2, False),

    def test_city(self):
        """Проверка поля модели Город"""
        self.assertEqual(self.city.name, 'tver')

    def test_line_of_business(self):
        """Проверка поля модели Сфера"""
        self.assertEqual(self.line_of_business.name, 'python_dev')

    def test_skill(self):
        """Проверка поля модели Ключевые навыки"""
        self.assertEqual(self.skill.name, 'тестовый навык')

    def test_models_have_correct_object_names(self):
        """Проверка корректности строкового метода моделей"""
        model_str = {
            self.city: self.city.name,
            self.line_of_business: self.line_of_business.name,
            self.skill: self.skill.name,
            self.order: self.order.name
        }
        for model, expected_value in model_str.items():
            with self.subTest(model=model):
                self.assertEqual(expected_value, str(model))
