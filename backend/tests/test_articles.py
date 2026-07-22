import unittest

from backend.services.articles_client import search_articles


class TestArticleSearch(unittest.TestCase):

    def test_search_returns_results(self):
        articles = search_articles("grief")
        self.assertTrue(len(articles) > 0)

    def test_article_has_expected_keys(self):
        articles = search_articles("grief")
        self.assertIn("title", articles[0])
        self.assertIn("summary", articles[0])
        self.assertIn("url", articles[0])
