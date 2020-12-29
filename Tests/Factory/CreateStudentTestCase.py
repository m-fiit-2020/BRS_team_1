import unittest
from Tests.Mock.Factory import CreateStudent
from Model.Student import Student
from datetime import date
from Model.Group import Group
import Factory


class CreateStudentTestCase(unittest.TestCase):
    def setUp(self):
        self.group = Group(name="М-ФИИТ", year=2020)

    def test_case_0(self):
        # given
        code = "160978"
        fio = "Васильев Сарыал Иннокентьевич"
        birthdate = "12.07.1998"
        email = "saryal.basilev@mail.ru"
        phone = "+79969141275"
        # when
        student = CreateStudent(code=code, fio=fio, birthdate=birthdate, email=email, phone=phone, group=self.group)
        # then
        code_int = 160978
        birthdate_date = date(1998, 7, 12)
        self.assertIsInstance(student, Student)
        self.assertEqual((student.code, student.fio, student.birthdate, student.email, student.phone, student.group),
                          (code_int, fio, birthdate_date, email, phone, self.group))
        # after TDD
        developed_student = Factory.create_student(code=code, fio=fio, birthdate=birthdate,
                                                   email=email, phone=phone, group=self.group)
        self.assertIsInstance(developed_student, Student)
        self.assertEqual((student.code, student.fio, student.birthdate, student.email, student.phone, student.group),
                         (developed_student.code, developed_student.fio, developed_student.birthdate,
                          developed_student.email, developed_student.phone, developed_student.group))

    def test_case_1(self):
        # given
        code = "160978"
        fio = ""
        birthdate = "12.07.1998"
        email = "saryal.basilev@mail.ru"
        phone = "+79969141275"
        # then
        with self.assertRaises(Exception):
            # when
            CreateStudent(code=code, fio=fio, birthdate=birthdate, email=email, phone=phone, group=self.group)
        # after TDD
        # then
        with self.assertRaises(Exception):
            # when
            Factory.create_student(code=code, fio=fio, birthdate=birthdate,
                                   email=email, phone=phone, group=self.group)

    def test_case_2(self):
        # given
        code = "ооо"
        fio = "Васильев Сарыал Иннокентьевич"
        birthdate = "12.07.1998"
        email = "saryal.basilev@mail.ru"
        phone = "+79969141275"
        # then
        with self.assertRaises(Exception):
            # when
            CreateStudent(code=code, fio=fio, birthdate=birthdate, email=email, phone=phone, group=self.group)
        # after TDD
        # then
        with self.assertRaises(Exception):
            # when
            Factory.create_student(code=code, fio=fio, birthdate=birthdate,
                                   email=email, phone=phone, group=self.group)

    def test_case_3(self):
        # given
        code = "160978"
        fio = "Васильев Сарыал Иннокентьевич"
        birthdate = "12.07.э1998"
        email = "saryal.basilev@mail.ru"
        phone = "+79969141275"
        # then
        with self.assertRaises(Exception):
            # when
            CreateStudent(code=code, fio=fio, birthdate=birthdate, email=email, phone=phone, group=self.group)
        # after TDD
        # then
        with self.assertRaises(Exception):
            # when
            Factory.create_student(code=code, fio=fio, birthdate=birthdate,
                                   email=email, phone=phone, group=self.group)

    def test_case_4(self):
        # given
        code = "160978"
        fio = "Васильев Сарыал Иннокентьевич"
        birthdate = "12.07.1998"
        email = "saryal.basilev@mail.ru"
        phone = "+799691412в75"
        # then
        with self.assertRaises(Exception):
            # when
            CreateStudent(code=code, fio=fio, birthdate=birthdate, email=email, phone=phone, group=self.group)
        # after TDD
        # then
        with self.assertRaises(Exception):
            # when
            Factory.create_student(code=code, fio=fio, birthdate=birthdate,
                                   email=email, phone=phone, group=self.group)
