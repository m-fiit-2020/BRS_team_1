import unittest
from Tests.Mock.Checker import check_brs_points
import Checker


class CheckBRSPointsTestCase(unittest.TestCase):
    def test_check_email(self):
        # given
        list_points = (
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
            75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92,
            93, 94, 95, 96, 97, 98, 99, 100)
        list_wrong_points = (-1, 0, 101)
        for point in list_points:
            # when
            is_correct_point = check_brs_points(point)
            # then
            self.assertEqual(is_correct_point, True)
        for point in list_wrong_points:
            # when
            is_correct_point = check_brs_points(point)
            # then
            self.assertEqual(is_correct_point, False)
        # after TDD
        for point in list_points:
            # when
            is_correct_point = check_brs_points(point)
            developed_is_correct_point = Checker.check_points(point)
            # then
            self.assertEqual(is_correct_point, developed_is_correct_point)
        for point in list_wrong_points:
            # when
            is_correct_point = check_brs_points(point)
            developed_is_correct_point = Checker.check_points(point)
            # then
            self.assertEqual(is_correct_point, developed_is_correct_point)
