import unittest
from Tests.Mock.Factory import CreateEducationYear
from Model.EducationYear import EducationYear
import Factory


class CreateEducationYearTestCase(unittest.TestCase):
    def test_case_0(self):
        # given
        begin_year = "2020"
        end_year = "2022"
        # when
        education_year = CreateEducationYear(begin_year=begin_year, end_year=end_year)
        # then
        begin_year_int = 2020
        end_year_int = 2022
        self.assertIsInstance(education_year, EducationYear)
        self.assertEqual((education_year.begin_year, education_year.end_year), (begin_year_int, end_year_int))
        # after TDD
        developed_education_year = Factory.create_education_year(begin_year=begin_year, end_year=end_year)
        self.assertIsInstance(developed_education_year, EducationYear)
        self.assertEqual((education_year.begin_year, education_year.end_year),
                         (developed_education_year.begin_year, developed_education_year.end_year))

    def test_case_1(self):
        # given
        begin_year = ""
        end_year = "2022"
        # then
        with self.assertRaises(Exception):
            # when
            CreateEducationYear(begin_year=begin_year, end_year=end_year)
        # after TDD
        # then
        with self.assertRaises(Exception):
            # when
            Factory.create_education_year(begin_year=begin_year, end_year=end_year)

    def test_case_2(self):
        # given
        begin_year = "2022"
        end_year = ""
        # then
        with self.assertRaises(Exception):
            # when
            CreateEducationYear(begin_year=begin_year, end_year=end_year)
        # after TDD
        # then
        with self.assertRaises(Exception):
            # when
            Factory.create_education_year(begin_year=begin_year, end_year=end_year)

    def test_case_3(self):
        # given
        begin_year = "s"
        end_year = "two thousand"
        # then
        with self.assertRaises(Exception):
            # when
            CreateEducationYear(begin_year=begin_year, end_year=end_year)
        # after TDD
        # then
        with self.assertRaises(Exception):
            # when
            Factory.create_education_year(begin_year=begin_year, end_year=end_year)