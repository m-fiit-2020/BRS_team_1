import unittest
from Models.EducationYear import EducationYear


class EducationYearTestCase(unittest.TestCase):
    def setUp(self):
        self.begin_education_year_expected = 2020
        self.end_education_year_expected = 2022

    def test_education_year(self):
        result = EducationYear(2020, 2022)
        self.assertEqual(result.begin_year, self.begin_education_year_expected)
        self.assertEqual(result.end_year, self.end_education_year_expected)