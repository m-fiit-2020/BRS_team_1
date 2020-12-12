import unittest
from Models.Group import Group
from Controller.Factory import create_group


class FactoryGroupTest(unittest.TestCase):
    def test_create_group_case_1(self):
        # given
        name = "М-ФИИТ-20"
        year = "two thousand twenty"
        # then
        with self.assertRaises(Exception):
            # when
            create_group(name, year)

    def test_create_group_case_2(self):
        # given
        name = ""
        year = ""
        # then
        with self.assertRaises(Exception):
            # when
            create_group(name, year)

    def test_create_group_case_3(self):
        # given
        name = "М-ФИИТ"
        year = "2020"
        # when
        group = create_group(name, year)
        # then
        self.assertIsInstance(group, Group)
        self.assertEqual(group.name, "М-ФИИТ")
        self.assertEqual(group.year, 2020)


if __name__ == '__main__':
    unittest.main()