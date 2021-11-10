from django.http import HttpRequest
from django.test import TestCase

from chat.views import home


class HomePageViewTest(TestCase):
    def test_home_returns_200(self):
        request = HttpRequest()

        response = home(request)

        self.assertEqual(response.status_code, 200)
