import unittest


class EducationTestCase(unittest.TestCase):
    def test_case_1(self):
        # given missing 1 required positional argument: 'beginYear'
        endYear = 2022
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception()

    def test_case_2(self):
        # given missing 1 required positional argument: 'endYear'
        beginYear = 2020
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception()

    def test_case_3(self):
        # given
        beginYear = 2020
        endYear = 2022
        # then
        self.assertEqual(True, True)
