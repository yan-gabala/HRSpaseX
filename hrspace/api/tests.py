from django.test import Client, TestCase


class ApiOrderTests(TestCase):

    def setUp(self):
        self.guest_client = Client()

    def test_static_page(self):
        """Проверка доступа к страницам по URL"""
        pages = ('/api/v1/orders/',
                 '/api/v1/cities/',
                 '/api/v1/line_of_business/')
        for page in pages:
            response = self.guest_client.get(page)
            error_name = f'Ошибка: нет доступа до страницы {page}'
            self.assertEqual(response.status_code, 200, error_name)
