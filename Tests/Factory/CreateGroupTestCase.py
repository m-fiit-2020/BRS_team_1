import unittest
from Tests.Mock.Factory import CreateGroup
from Model.Group import Group
import Factory


class CreateGroupTestCase(unittest.TestCase):
    def test_case_0(self):
        # given
        name = "М-ФИИТ"
        year = "2020"
        # when
        group = CreateGroup(name=name, year=year)
        # then
        year_int = 2020
        self.assertIsInstance(group, Group)
        self.assertEqual((group.name, group.year), (name, year_int))
        # after TDD
        developed_group = Factory.create_group(name=name, year=year)
        self.assertIsInstance(developed_group, Group)
        self.assertEqual((developed_group.name, group.year), (group.name, group.year))

    def test_case_1(self):
        # given
        name = ""
        year = "2020"
        # then
        with self.assertRaises(Exception):
            # when
            CreateGroup(name=name, year=year)
        # after TDD
        # then
        with self.assertRaises(Exception):
            # when
            Factory.create_group(name=name, year=year)

    def test_case_2(self):
        # given
        name = "М-ФИИТ"
        year = ""
        # then
        with self.assertRaises(Exception):
            # when
            CreateGroup(name=name, year=year)
        # after TDD
        # then
        with self.assertRaises(Exception):
            # when
            Factory.create_group(name=name, year=year)

    def test_case_3(self):
        # given
        name = "М-ФИИТ"
        year = "two thousand"
        # then
        with self.assertRaises(Exception):
            # when
            CreateGroup(name=name, year=year)
        # after TDD
        # then
        with self.assertRaises(Exception):
            # when
            Factory.create_group(name=name, year=year)