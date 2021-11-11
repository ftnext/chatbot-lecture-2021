from django.test import TestCase
from django.urls import resolve

from chat import views


class HomePageTestCase(TestCase):
    def test_home_returns_200_and_expected_title(self):
        response = self.client.get("/")

        self.assertContains(response, "Talk with chatbot", status_code=200)

    def test_home_page_uses_expected_template(self):
        response = self.client.get("/")

        self.assertTemplateUsed(response, "chat/home.html")


class HomeViewTestCase(TestCase):
    def test_should_resolve_home(self):
        found = resolve("/")

        self.assertEqual(views.home, found.func)
