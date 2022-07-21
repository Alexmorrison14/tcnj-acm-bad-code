from unittest import TestCase
import string
import better as test_code
from hamcrest import assert_that, equal_to


class TestAlphabetGenerator(TestCase):
    def test_all_letters_present(self):
        output = test_code.generate_random_alphabet()
        assert_that(set(output) >= set(string.ascii_lowercase))

    def test_only_26_letters_present(self):
        output = test_code.generate_random_alphabet()
        assert_that(len(output) == 26)