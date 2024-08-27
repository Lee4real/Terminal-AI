import unittest
from src.autocomplete import autocomplete_command

class TestAutocompleteCommand(unittest.TestCase):
    def test_valid_command(self):
        result = autocomplete_command('git ch')
        self.assertIn('git checkout', result)

    def test_invalid_command(self):
        result = autocomplete_command('')
        self.assertEqual(result, "Invalid input: command part cannot be empty.")

    def test_no_match(self):
        result = autocomplete_command('invalidcommand')
        self.assertEqual(result, "No valid command found.")

if __name__ == '__main__':
    unittest.main()