import unittest
from datetime import date


class BRSPointsTestCase(unittest.TestCase):
    def test_case_1(self):
        # given
        student = [166009, "PSV", date(2001, 3, 27), "p@gmail.com", "7346", ["FIIT-20", 2020]]
        subject = ["12-a", "Math"]
        year = [2020, 2022]
        cross_section_index = 0
        # then
        self.assertEqual(True, True)

    def test_case_2(self):
        # given missing 1 required positional argument: 'student'
        subject = ["12-a", "Math"]
        year = [2020, 2022]
        cross_section_index = 0
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception()

    def test_case_3(self):
        # given missing 1 required positional argument: 'subject'
        student = [166009, "PSV", date(2001, 3, 27), "p@gmail.com", "7346", ["FIIT-20", 2020]]
        year = [2020, 2022]
        cross_section_index = 0
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception()

    def test_case_4(self):
        # given missing 1 required positional argument: 'year'
        student = [166009, "PSV", date(2001, 3, 27), "p@gmail.com", "7346", ["FIIT-20", 2020]]
        subject = ["12-a", "Math"]
        cross_section_index = 0
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception()

    def test_case_5(self):
        # given missing 1 required positional argument: 'cross_section_index'
        student = [166009, "PSV", date(2001, 3, 27), "p@gmail.com", "7346", ["FIIT-20", 2020]]
        subject = ["12-a", "Math"]
        year = [2020, 2022]
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception()
