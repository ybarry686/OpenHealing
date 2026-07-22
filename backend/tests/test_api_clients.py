import unittest

from backend.services.gemini_client import build_prompt
from backend.services.google_maps_client import search_resources


class TestBuildPrompt(unittest.TestCase):

    def test_all_resources_are_included(self):
        resources = [
            {"name": "First Place", "address": "1 Main St", "category": "Clinic"},
            {"name": "Second Place", "address": "2 Main St", "category": "Clinic"},
        ]
        prompt = build_prompt("I need help", resources, [])
        self.assertIn("First Place", prompt)
        self.assertIn("Second Place", prompt)

    def test_prompt_is_built_with_no_resources(self):
        prompt = build_prompt("I need help", [], [])
        self.assertIsNotNone(prompt)

    def test_articles_are_included(self):
        articles = [{"title": "Coping With Grief", "summary": "A short summary"}]
        prompt = build_prompt("I need help", [], articles)
        self.assertIn("Coping With Grief", prompt)

    def test_user_message_is_included(self):
        prompt = build_prompt("I lost my mother", [], [])
        self.assertIn("I lost my mother", prompt)

    def test_prompt_includes_safety_instruction(self):
        prompt = build_prompt("I need help", [], [])
        self.assertIn("emergency services", prompt)


class TestSearchResources(unittest.TestCase):

    def test_no_location_returns_empty_list(self):
        results = search_resources("food bank")
        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.main()
