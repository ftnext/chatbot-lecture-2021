from django.test import TestCase
from django.urls import resolve

from chat import views


class HomePageViewTest(TestCase):
    def test_home_returns_200(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

    def test_should_resolve_home(self):
        found = resolve("/")

        self.assertEqual(views.home, found.func)
