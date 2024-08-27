import unittest
from src.explanations import get_command_explanations

class TestExplanationsCommand(unittest.TestCase):
    def test_valid_command(self):
        result = get_command_explanations('git ch')
        self.assertIn('git checkout', result)

    def test_invalid_command(self):
        result = get_command_explanations('')
        self.assertEqual(result, "Invalid input: command part cannot be empty.")

    def test_no_match(self):
        result = get_command_explanations('invalidcommand')
        self.assertEqual(result, "No valid command found.")

if __name__ == '__main__':
    unittest.main()