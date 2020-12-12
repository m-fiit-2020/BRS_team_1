import unittest
from Controller.Factory import create_student, create_group


class FactoryStudentTest(unittest.TestCase):
    def test_create_student_case_1(self):
        # given
        code = 160978
        name = "Васильев Сарыал Иннокентьевич"
        birthdate = "12.07.1998"
        email = "example@mail.ru"
        phone = "79969141275"
        group = create_group(name="М-ФИИТ-20", year=2020)
        # when
        student = create_student(code, name, birthdate, email, phone, group)
        # then
        self.assertEqual(student.fio, "Васильев Сарыал Иннокентьевич")
        self.assertEqual(student.code, 160978)
        self.assertEqual(student.birthdate, "12.07.1998")
        self.assertEqual(student.email, "example@mail.ru")
        self.assertEqual(student.phone, "79969141275")


if __name__ == '__main__':
    unittest.main()
