import unittest
from Tests.Mock.Factory import CreateBRSPoints
from Model.Student import Student
from datetime import date
from Model.Group import Group
from Model.EducationYear import EducationYear
from Model.Subject import Subject
from Model.CrossSection import CrossSection
from Model.BRSPoints import BRSPoints
import Factory


class CreateBRSPointsTestCase(unittest.TestCase):
    def setUp(self):
        self.student = Student(code=166009,
                               fio="Platonov Simon Vladimirovich",
                               birthdate=date(2001, 3, 27),
                               email="plats2002@gmail.com",
                               phone="+79142247346",
                               group=Group(name="М-ФИИТ", year=2020))
        self.education_year = EducationYear(begin_year=2020, end_year=2022)
        self.subject = Subject(code="Б1.О.03", name="Управление проектами")
        self.cross_section = CrossSection.FinalSection

    def test_case_0(self):
        # given
        points = "100"
        # when
        brs_points = CreateBRSPoints(student=self.student,
                                     subject=self.subject,
                                     year=self.education_year,
                                     cross_section=self.cross_section,
                                     points=points)
        # then
        points_int = 100
        self.assertIsInstance(brs_points, BRSPoints)
        self.assertEqual((brs_points.student,
                          brs_points.subject,
                          brs_points.year,
                          brs_points.cross_section,
                          brs_points.points),
                         (self.student,
                          self.subject,
                          self.education_year,
                          self.cross_section,
                          points_int))
        # after TDD
        developed_brs_points = Factory.create_brs_points(student=self.student,
                                                         subject=self.subject,
                                                         year=self.education_year,
                                                         cross_section=self.cross_section,
                                                         points=points)
        self.assertIsInstance(developed_brs_points, BRSPoints)
        self.assertEqual((brs_points.student,
                          brs_points.subject,
                          brs_points.year,
                          brs_points.cross_section,
                          brs_points.points),
                         (developed_brs_points.student,
                          developed_brs_points.subject,
                          developed_brs_points.year,
                          developed_brs_points.cross_section,
                          developed_brs_points.points))

    def test_case_1(self):
        # given
        points = "ten"
        # then
        with self.assertRaises(Exception):
            # when
            CreateBRSPoints(student=self.student,
                            subject=self.subject,
                            year=self.education_year,
                            cross_section=self.cross_section,
                            points=points)
        # after TDD
        # then
        with self.assertRaises(Exception):
            # when
            Factory.create_brs_points(student=self.student,
                                      subject=self.subject,
                                      year=self.education_year,
                                      cross_section=self.cross_section,
                                      points=points)

    def test_case_2(self):
        # given
        points = "101"
        # then
        with self.assertRaises(Exception):
            # when
            CreateBRSPoints(student=self.student,
                            subject=self.subject,
                            year=self.education_year,
                            cross_section=self.cross_section,
                            points=points)
        # after TDD
        # then
        with self.assertRaises(Exception):
            # when
            Factory.create_brs_points(student=self.student,
                                      subject=self.subject,
                                      year=self.education_year,
                                      cross_section=self.cross_section,
                                      points=points)
