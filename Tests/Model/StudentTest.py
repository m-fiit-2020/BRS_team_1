import unittest
from datetime import date
from Tests.Mock.Models import Student
from Model.Group import Group
import Model.Student


class StudentTestCase(unittest.TestCase):
    def setUp(self):
        self.group = Group(name="М-ФИИТ", year=2020)

    def test_case_0(self):
        # given
        code = 166009
        fio = "Platonov Simon Vladimirovich"
        birthdate = date(2001, 3, 27)
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        # when
        student = Student(code=code, fio=fio, birthdate=birthdate, email=email, phone=phone, group=self.group)
        # then
        self.assertEqual((student.code, student.fio, student.birthdate, student.email, student.phone, student.group),
                         (code, fio, birthdate, email, phone, self.group))
        # after TDD
        developed_student = Model.Student.Student(code=code, fio=fio, birthdate=birthdate,
                                                  email=email, phone=phone, group=self.group)
        self.assertEqual((developed_student.code, developed_student.fio, developed_student.birthdate,
                          developed_student.email, developed_student.phone, developed_student.group),
                         (student.code, student.fio, student.birthdate, student.email, student.phone, student.group))

    def test_case_1(self):
        # given
        code = 166009
        fio = "Platonov Simon Vladimirovich"
        birthdate = date(2001, 3, 27)
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        # when
        student = Student(code=code, fio=email, birthdate=birthdate, email=fio, phone=phone, group=self.group)
        # then
        self.assertNotEqual((student.code, student.fio, student.birthdate, student.email, student.phone, student.group),
                            (code, fio, birthdate, email, phone, self.group))
        # after TDD
        developed_student = Model.Student.Student(code=code, fio=email, birthdate=birthdate,
                                                  email=fio, phone=phone, group=self.group)
        self.assertEqual((developed_student.code, developed_student.fio, developed_student.birthdate,
                          developed_student.email, developed_student.phone, developed_student.group),
                         (student.code, student.fio, student.birthdate, student.email, student.phone, student.group))
