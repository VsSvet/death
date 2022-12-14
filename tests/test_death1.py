from death1 import check_user_input, check_repetitions_user_input, check_presence_letter_in_word
from unittest import TestCase

class TestCheckUserInput(TestCase):
    def test_check_user_input_correct_length(self):
        self.assertTrue(check_user_input("а"))

    def test_check_user_input_correct_value(self):
        self.assertTrue(check_user_input("а"))

    def test_check_user_input_wrong_value_alpha(self):
        self.assertFalse(check_user_input("z"))

    def test_check_user_input_wrong_value_digit(self):
        self.assertFalse(check_user_input("4"))

    def test_check_user_input_wrong_value_symbol(self):
        self.assertFalse(check_user_input("!"))

class TestCheckRepetitionsUserInput(TestCase):
    def test_check_repetitions_user_input_unique_value(self):
        self.assertTrue(check_repetitions_user_input("а", ["б", "с", "е"]))

    def test_check_repetitions_user_input_not_unique_input(self):
        self.assertFalse(check_repetitions_user_input("а", ["б", "с", "а"]))

class TestCheckPresenceLetterInWord(TestCase):
    def test_check_presence_letter_in_word(self):
        self.assertTrue(check_presence_letter_in_word("a", ["a", "b", "c"], ["_", "_", "_"]))

    def test_check_absence_letter_in_word(self):
        self.assertFalse(check_presence_letter_in_word("a", ["a", "b", "c"], ["_", "_", "_"]))




