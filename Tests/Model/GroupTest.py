import unittest
from Tests.Mock.Models import Group
import Model.Group


class GroupTestCase(unittest.TestCase):
    def test_case_0(self):
        # given
        name = "М-ФИИТ"
        year = 2020
        # when
        group = Group(name=name, year=year)
        # then
        self.assertEqual((group.name, group.year), (name, year))
        # after TDD
        developed_group = Model.Group.Group(name=name, year=year)
        self.assertEqual((group.name, group.year),
                         (developed_group.name, developed_group.year))

    def test_case_1(self):
        # given
        name = "М-ФИИТ"
        year = 2020
        # when
        group = Group(name=year, year=name)
        # then
        self.assertNotEqual((group.name, group.year), (name, year))
        # after TDD
        developed_group = Model.Group.Group(name=year, year=name)
        self.assertEqual((group.name, group.year),
                         (developed_group.name, developed_group.year))
