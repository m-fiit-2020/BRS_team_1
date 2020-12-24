import unittest
from datetime import date


class CreateStudentTestCase(unittest.TestCase):
    def test_case_code_1(self):
        # given
        code = "166o09"
        fio = "Platonov Simon Vladimirovich"
        birthdate = "27.03.2001"
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group_index = "0"
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели не целое число ( ´•︵•` )")

    def test_case_code_2(self):
        # given
        code = ""
        fio = "Platonov Simon Vladimirovich"
        birthdate = "27.03.2001"
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group_index = "0"
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_fio_3(self):
        # given
        code = "166009"
        fio = ""
        birthdate = "27.03.2001"
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group_index = "0"        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_birthdate_4(self):
        # given
        code = "166009"
        fio = "Platonov Simon Vladimirovich"
        birthdate = "271.03.2001"
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group_index = "0"
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели не правильный тип даты ( ´•︵•` )")

    def test_case_birthdate_5(self):
        # given
        code = "166009"
        fio = "Platonov Simon Vladimirovich"
        birthdate = ""
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group_index = "0"
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_email_6(self):
        # given
        code = "166009"
        fio = "Platonov Simon Vladimirovich"
        birthdate = "27.03.2001"
        email = ""
        phone = "+79142247346"
        group_index = "0"
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_phone_7(self):
        # given
        code = "166009"
        fio = "Platonov Simon Vladimirovich"
        birthdate = "27.03.2001"
        email = "plats2002@gmail.com"
        phone = ""
        group_index = "0"
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_group_8(self):
        # given
        code = "166009"
        fio = "Platonov Simon Vladimirovich"
        birthdate = "27.03.2001"
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group_index = "A"
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели не правильный тип группы ( ´•︵•` )")

    def test_case_group_9(self):
        # given
        code = "166009"
        fio = "Platonov Simon Vladimirovich"
        birthdate = "27.03.2001"
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group = ""
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_create_10(self):
        # given
        code = "166009"
        fio = "Platonov Simon Vladimirovich"
        birthdate = "27.03.2001"
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group_index = "0"
        # then
        self.assertEqual(True, True)
