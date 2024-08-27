import unittest
from src.suggestions import suggest_commands

class TestSuggestionsCommand(unittest.TestCase):
    def test_valid_command(self):
        result = suggest_commands('git ch')
        self.assertIn('git checkout', result)

    def test_invalid_command(self):
        result = suggest_commands('')
        self.assertEqual(result, "Invalid input: command part cannot be empty.")

    def test_no_match(self):
        result = suggest_commands('invalidcommand')
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()