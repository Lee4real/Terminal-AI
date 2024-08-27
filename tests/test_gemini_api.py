import unittest
from src.gemini_api import generate_text

class TestGeminiAPI(unittest.TestCase):
    def test_generate_text_success(self):
        prompt = "Complete the command: git ch"
        result = generate_text(prompt)
        self.assertIn('git checkout', result)

    def test_generate_text_failure(self):
        prompt = ""
        result = generate_text(prompt)
        self.assertEqual(result, "Error: contents must not be empty")

if __name__ == '__main__':
    unittest.main()