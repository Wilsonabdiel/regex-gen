import unittest
from click.testing import CliRunner
import email_in_validate  # replace with your actual module name

class TestEmailValidator(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_validate_valid_email(self):
        result = self.runner.invoke(email_in_validate.validate, ['test@example.com'])
        self.assertEqual(result.output, 'test@example.com is a valid email address.\n')
        self.assertEqual(result.exit_code, 0)

    def test_validate_invalid_email(self):
        result = self.runner.invoke(email_in_validate.validate, ['invalid_email'])
        self.assertEqual(result.output, 'invalid_email is not a valid email address.\n')
        self.assertEqual(result.exit_code, 0)

if __name__ == '__main__':
    unittest.main()
