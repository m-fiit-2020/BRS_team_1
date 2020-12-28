import unittest
from Controller import Checker
from Models.Student import Student
from Models.BRSPoints import BRSPoints
from Models.EducationYear import EducationYear
from Models.CrossSection import CrossSection
from Models.Group import Group
from Models.Subject import Subject


class CheckPointsTestCase(unittest.TestCase):
    def test_check_points(self):
        group1 = Group("М-ФИИТ-20", 2020)
        group2 = Group("М-ФИИТ-19", 2019)

        year1 = EducationYear(2020, 2021)

        subject1 = Subject("321", "Психология")
        subject3 = Subject("323", "Английский")

        cross_section1 = CrossSection.FirstSection
        cross_section2 = CrossSection.SecondSection
        cross_section3 = CrossSection.FinalSection

        student1 = Student(code=123, fio="Егоров Алексей Васильевич", birthdate="01. 04. 1996",
                           email="eavamga@gmail.com", phone="+79244669579", group=group1)
        student2 = Student(code=124, fio="Иванов Иван Иванович", birthdate="30. 12. 2000", email="example@gmail.com",
                           phone="+79991112233", group=group2)

        EgorovAV_cs1 = BRSPoints(subject=subject1, year=year1, cross_section=cross_section1, points=33,
                                 student=student1)
        EgorovAV_cs2 = BRSPoints(subject=subject1, year=year1, cross_section=cross_section2, points=66,
                                 student=student1)
        EgorovAV_cs3 = BRSPoints(subject=subject1, year=year1, cross_section=cross_section3, points=99,
                                 student=student1)

        IvamovII_cs1 = BRSPoints(subject=subject1, year=year1, cross_section=cross_section1, points=20,
                                 student=student2)
        IvamovII_cs2 = BRSPoints(subject=subject1, year=year1, cross_section=cross_section2, points=20,
                                 student=student2)
        IvamovII_cs3 = BRSPoints(subject=subject1, year=year1, cross_section=cross_section3, points=20,
                                 student=student2)

        EgorovAV_cs1_wrong = BRSPoints(subject=subject3, year=year1, cross_section=cross_section1, points=101,
                                       student=student1)
        EgorovAV_cs2_wrong = BRSPoints(subject=subject3, year=year1, cross_section=cross_section2, points=0,
                                       student=student1)
        EgorovAV_cs3_wrong = BRSPoints(subject=subject3, year=year1, cross_section=cross_section3, points=0,
                                       student=student1)

        IvamovII_cs1_wrong = BRSPoints(subject=subject3, year=year1, cross_section=cross_section1, points=65,
                                       student=student2)
        IvamovII_cs2_wrong = BRSPoints(subject=subject3, year=year1, cross_section=cross_section2, points=60,
                                       student=student2)
        IvamovII_cs3_wrong = BRSPoints(subject=subject3, year=year1, cross_section=cross_section3, points=30,
                                       student=student2)

        Egorov_subject1_2020_2021 = [EgorovAV_cs1, EgorovAV_cs2, EgorovAV_cs3]
        Egorov_subject3_2020_2021_wrong = [EgorovAV_cs1_wrong, EgorovAV_cs2_wrong, EgorovAV_cs3_wrong]

        Ivanov_subject1_2020_2021 = [IvamovII_cs1, IvamovII_cs2, IvamovII_cs3]
        Ivanov_subject1_2020_2021_wrong = [IvamovII_cs1_wrong, IvamovII_cs2_wrong, IvamovII_cs3_wrong]

        self.assertEqual(Checker.check_points(Egorov_subject1_2020_2021, cross_section3, EgorovAV_cs3.points), True)
        self.assertEqual(Checker.check_points(Ivanov_subject1_2020_2021, cross_section3, IvamovII_cs3.points), True)

        self.assertEqual(
            Checker.check_points(Egorov_subject3_2020_2021_wrong, cross_section1, EgorovAV_cs1_wrong.points), False)
        self.assertEqual(
            Checker.check_points(Ivanov_subject1_2020_2021_wrong, cross_section3, IvamovII_cs3_wrong.points), False)
