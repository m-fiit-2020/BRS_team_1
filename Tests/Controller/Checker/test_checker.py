import unittest
from Controller import Checker
from Models.Student import Student
from Models.BRSPoints import BRSPoints
from Models.EducationYear import EducationYear
from Models.CrossSection import CrossSection
from Models.Group import Group
from Models.Subject import Subject


class TestChecker(unittest.TestCase):
    def test_check_email(self):
        list_emails = ("vladimirp1998@gmail.com", "eremenkoira19981998@gmail.com", "fhljkjhuh@gmail.com",
                       "saryal.basilev@gmail.com", "sarasti2400@gmail.com", "evgunarov@gmail.com",
                       "ivanovmksm98@gmail.com", "eavamga@gmail.com", "nikofed96@gmail.com", "ergis15@gmail.com",
                       "maksimbubyakin@mail.ru", "plats2002@gmail.com", "m.fiit2020@gmail.com",
                       "dayankoo201297@gmail.com", "semenovanatalya400180@gmail.com", "arsen3393@gmail.com",
                       "eremenkoira19981998@mail.ru", "maksimzlatov96@gmail.com")
        list_wrong_emails = ("vladimirp1998@gmailcom", "eremenkoira19981998@gmail.compsdfsa", "fhljkjhuh",
                             56, "sarasti2400gmail.comsdf", "com.evgunarov@gmail",
                             "ivanovmksm98@gmail.?com", "eavamga@gmail.34com", "nikofed96gmail.co1m",
                             "ergis15gmail.co2m",
                             "maksimbubyakin@mailru", "plats2002@gmail.90com", "m.fiit2020@gmailcom",
                             True, False, 2134234, 0.13343, (1, "eavamga@gmail.ru.com", 3, 5))
        for i in list_emails:
            self.assertEqual(Checker.check_email(i), True)
        for j in list_wrong_emails:
            self.assertEqual(Checker.check_email(j), False)

    def test_check_phone(self):
        list_phones = ("+79244669579", "+79969141275", "+79142981921", "+79243601678", "+79142247346", "+79990602363",
                       "+79142334939", "+79244640551", "+79248668556", "89618697027", "89100851951", "89142202681",
                       "89142673402", "89248751088", "89991736337")
        list_wrong_phones = ("+79244669579344", "7996914127544", "sas;klfj", "+7924360167!", "+79142247346?",
                             "_79990602363", "+89142334939", "+99244640551", 23456656, "896186970277",
                             (8, 9, 2, 4, 4, 6, 6, 9, 5, 7, 9), "&!&lsd?", "891426734020", "8924 8751088",
                             "899E1736337")
        for i in list_phones:
            self.assertEqual(Checker.check_phone(i), True)
        for j in list_wrong_phones:
            self.assertEqual(Checker.check_phone(j), False)

    def test_check_points(self):
        group1 = Group("М-ФИИТ-20", 2020)
        group2 = Group("М-ФИИТ-19", 2019)

        year1 = EducationYear(2020, 2021)
        year2 = EducationYear(2021, 2022)

        subject1 = Subject("321", "Психология")
        subject2 = Subject("322", "Методология")
        subject3 = Subject("323", "Английский")

        cross_section1 = CrossSection("Первый контрольный срез")
        cross_section2 = CrossSection("Второй контрольный срез")
        cross_section3 = CrossSection("Заключительный контрольный срез")

        student1 = Student(code=123, fio="Егоров Алексей Васильевич", birthdate="01. 04. 1996",
                           email="eavamga@gmail.com", phone="+79244669579", group=group1)
        student2 = Student(code=124, fio="Иванов Иван Иванович", birthdate="30. 12. 2000", email="example@gmail.com",
                           phone="+79991112233", group=group2)

        EgorovAV_s1_y1_cs1 = BRSPoints(subject=subject1, year=year1, cross_section=cross_section1, points=99,
                                       student=student1)
        EgorovAV_s2_y2_cs1 = BRSPoints(subject=subject2, year=year2, cross_section=cross_section1, points=17,
                                       student=student1)

        IvamovII_s1_y1_cs1 = BRSPoints(subject=subject1, year=year1, cross_section=cross_section1, points=20,
                                       student=student2)
        IvamovII_s2_y2_cs1 = BRSPoints(subject=subject2, year=year2, cross_section=cross_section1, points=77,
                                       student=student2)

        EgorovAV_s3_y1_cs1 = BRSPoints(subject=subject3, year=year1, cross_section=cross_section1, points=102,
                                       student=student1)
        EgorovAV_s3_y1_cs2 = BRSPoints(subject=subject3, year=year1, cross_section=cross_section2, points=-12,
                                       student=student1)

        IvamovII_s3_y1_cs1 = BRSPoints(subject=subject3, year=year1, cross_section=cross_section1, points=0.22,
                                       student=student2)
        IvamovII_s3_y1_cs2 = BRSPoints(subject=subject3, year=year1, cross_section=cross_section2, points=True,
                                       student=student2)

        self.assertEqual(Checker.check_points(EgorovAV_s1_y1_cs1, year1, cross_section1), True)
        self.assertEqual(Checker.check_points(EgorovAV_s2_y2_cs1, year2, cross_section1), True)
        self.assertEqual(Checker.check_points(IvamovII_s1_y1_cs1, year1, cross_section1), True)
        self.assertEqual(Checker.check_points(IvamovII_s2_y2_cs1, year2, cross_section1), True)

        self.assertEqual(Checker.check_points(EgorovAV_s3_y1_cs1, year1, cross_section1), False)
        self.assertEqual(Checker.check_points(EgorovAV_s3_y1_cs2, year1, cross_section2), False)
        self.assertEqual(Checker.check_points(IvamovII_s3_y1_cs1, year1, cross_section1), False)
        self.assertEqual(Checker.check_points(IvamovII_s3_y1_cs2, year1, cross_section2), False)
