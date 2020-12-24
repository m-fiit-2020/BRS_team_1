import unittest


class GroupTestCase(unittest.TestCase):
    def test_case_1(self):
        # given missing 2 required positional arguments: 'name' and 'year'
        # then
        with self.assertRaises(Exception):
            # when
            # TODO Добавить вызов функции
            raise Exception()

    def test_case_2(self):
        # given missing 1 required positional argument: 'year'
        name = "Saryal"
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception()

    def test_case_3(self):
        # given missing 1 required positional argument: 'name'
        year = 2020
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception()

    def test_case_4(self):
        # given
        name = "Saryal"
        year = 2020
        # then
        self.assertEqual(True, True)
