
from django.test import TestCase


class MenuPageTest(TestCase):

    def test_menu_page_status_code(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
