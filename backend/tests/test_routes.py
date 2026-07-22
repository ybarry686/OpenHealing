import unittest

from backend.app import app


class TestArticleRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_articles_returns_results(self):
        response = self.client.get("/api/articles?query=grief")
        self.assertEqual(response.status_code, 200)

    def test_articles_requires_a_query(self):
        response = self.client.get("/api/articles")
        self.assertEqual(response.status_code, 400)


class TestResourceRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_resources_requires_a_query(self):
        response = self.client.get("/api/resources")
        self.assertEqual(response.status_code, 400)
