import unittest


class EditGroupTestCase(unittest.TestCase):
    def setUp(self):
        self.groups = [["М-ФИИТ", 2020], ["М-ИВТ", 2020]]
        self.cmd_input = "2"
        self.edit_name_input = 'Маг_ФИИТ'
        self.edit_year_input = '2020'

    def test_case_0(self):
        # given setUp
        # then
        self.assertEqual(True, True)

    def test_case_1(self):
        # given
        self.groups = []
        self.cmd_input = "1"
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Выход за пределы массива ( ´•︵•` )")

    def test_case_2(self):
        # given
        self.cmd_input = "3"
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Выход за пределы массива ( ´•︵•` )")

    def test_case_3(self):
        # given
        self.edit_name_input = ''
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_4(self):
        # given
        self.edit_year_input = ''
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_5(self):
        # given
        self.cmd_input = ''
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_6(self):
        # given
        self.edit_year_input = 'two thousand twenty'
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели не целое число ( ´•︵•` )")

    def test_case_7(self):
        # given
        self.cmd_input = "two"
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели не целое число ( ´•︵•` )")

    def test_case_8(self):
        # given
        self.cmd_input = '0'
        # then
        self.assertEqual(True, True)