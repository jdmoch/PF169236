import unittest
from pesel_validator import PeselValidator


class TestPeselValidator(unittest.TestCase):
    def test_validate_format(self):
        self.assertTrue(PeselValidator.validate_format('02251904321'))
        self.assertFalse(PeselValidator.validate_format('123'))
        self.assertFalse(PeselValidator.validate_format('123456789012'))

    def test_validate_check_digit(self):
        self.assertTrue(PeselValidator.validate_check_digit('02051401458'))
        self.assertFalse(PeselValidator.validate_check_digit('44051401459'))

    def test_validate_birth_date(self):
        self.assertTrue(PeselValidator.validate_birth_date('02051401458'))
        self.assertFalse(PeselValidator.validate_birth_date('10131401458'))

    def test_get_gender(self):
        self.assertEqual(PeselValidator.get_gender('50051401458'), 'male')
        self.assertEqual(PeselValidator.get_gender('02051401468'), 'female')

    def test_is_valid(self):
        self.assertTrue(PeselValidator.is_valid('02051401458'))
        self.assertFalse(PeselValidator.is_valid('02051401459'))

if __name__ == '__main__':
    unittest.main()