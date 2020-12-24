import unittest
from datetime import date


class StudentTestCase(unittest.TestCase):
    def test_case_1(self):
        # given missing 1 required positional argument: 'year'
        code = 166009
        fio = "Platonov Simon Vladimirovich"
        birthdate = date(2001, 3, 27)
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group = ["FIIT-20", 2020]
        # then
        self.assertEqual(True, True)

    def test_case_2(self):
        # given missing 1 required positional argument: 'code'
        fio = "Platonov Simon Vladimirovich"
        birthdate = date(2001, 3, 27)
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group = ["FIIT-20", 2020]
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception()

    def test_case_3(self):
        # given missing 1 required positional argument: 'fio'
        code = 166009
        birthdate = date(2001, 3, 27)
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group = ["FIIT-20", 2020]
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception()

    def test_case_4(self):
        # given missing 1 required positional argument: 'birthdate'
        code = 166009
        fio = "Platonov Simon Vladimirovich"
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group = ["FIIT-20", 2020]
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception()

    def test_case_5(self):
        # given missing 1 required positional argument: 'email'
        code = 166009
        fio = "Platonov Simon Vladimirovich"
        birthdate = date(2001, 3, 27)
        phone = "+79142247346"
        group = ["FIIT-20", 2020]
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception()

    def test_case_6(self):
        # given missing 1 required positional argument: 'phone'
        code = 166009
        fio = "Platonov Simon Vladimirovich"
        birthdate = date(2001, 3, 27)
        email = "plats2002@gmail.com"
        group = ["FIIT-20", 2020]
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception()

    def test_case_7(self):
        # given missing 1 required positional argument: 'group'
        code = 166009
        fio = "Platonov Simon Vladimirovich"
        birthdate = date(2001, 3, 27)
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception()
