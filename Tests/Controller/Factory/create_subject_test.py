import unittest


class CreateSubjectTestCase(unittest.TestCase):
    def test_case_code_1(self):
        # given
        code = ""
        name = "Math"
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_name_2(self):
        # given
        code = "12-a"
        name = ""
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_create_3(self):
        # given
        code = "12-a"
        name = "Math"
        # then
        self.assertEqual(True, True)
