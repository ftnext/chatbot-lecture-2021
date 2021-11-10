from django.test import TestCase


class HomePageViewTest(TestCase):
    def test_home_returns_200(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
