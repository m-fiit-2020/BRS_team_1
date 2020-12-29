import unittest
from datetime import date
from Tests.Mock.Models import BRSPoints
from Model.CrossSection import CrossSection
from Model.Student import Student
from Model.Group import Group
from Model.EducationYear import EducationYear
from Model.Subject import Subject
import Model.BRSPoints


class BRSPointsTestCase(unittest.TestCase):
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
        points = 100
        # when
        brs_points = BRSPoints(student=self.student,
                               subject=self.subject,
                               year=self.education_year,
                               cross_section=self.cross_section,
                               points=points)
        # then
        self.assertEqual((brs_points.subject, brs_points.year, brs_points.cross_section, brs_points.points),
                         (self.subject, self.education_year, self.cross_section, points))
        # after TDD
        developed_brs_points = Model.BRSPoints.BRSPoints(student=self.student,
                                                         subject=self.subject,
                                                         year=self.education_year,
                                                         cross_section=self.cross_section,
                                                         points=points)
        self.assertEqual((developed_brs_points.subject, developed_brs_points.year,
                          developed_brs_points.cross_section, developed_brs_points.points),
                         (brs_points.subject, brs_points.year, brs_points.cross_section, brs_points.points))
