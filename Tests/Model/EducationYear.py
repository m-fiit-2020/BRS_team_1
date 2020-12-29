import unittest
from Tests.Mock.Models import EducationYear
import Model.EducationYear


class EducationTestCase(unittest.TestCase):
    def test_case_0(self):
        # given
        beginYear = 2020
        endYear = 2022
        # when
        educationYear = EducationYear(begin_year=beginYear, end_year=endYear)
        # then
        self.assertEqual((educationYear.begin_year, educationYear.end_year), (beginYear, endYear))
        # after TDD
        developed_education_year = Model.EducationYear.EducationYear(begin_year=beginYear, end_year=endYear)
        self.assertEqual((educationYear.begin_year, educationYear.end_year),
                         (developed_education_year.begin_year, developed_education_year.end_year))

    def test_case_1(self):
        # given
        beginYear = 2020
        endYear = 2022
        # when
        educationYear = Model.EducationYear.EducationYear(begin_year=endYear, end_year=beginYear)
        # then
        self.assertNotEqual((educationYear.begin_year, educationYear.end_year), (beginYear, endYear))
        # after TDD
        developed_education_year = Model.EducationYear.EducationYear(begin_year=endYear, end_year=beginYear)
        self.assertEqual((educationYear.begin_year, educationYear.end_year),
                         (developed_education_year.begin_year, developed_education_year.end_year))
