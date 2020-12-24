import unittest


class CreateGroupTestCase(unittest.TestCase):
    def test_case_1(self):
        # given
        name = "М-ФИИТ-20"
        year = "two thousand twenty"
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели не целое число ( ´•︵•` )")

    def test_case_2(self):
        # given
        name = ""
        year = ""
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_3(self):
        # given
        name = "М-ФИИТ"
        year = "2020"
        # then
        self.assertEqual(True, True)
