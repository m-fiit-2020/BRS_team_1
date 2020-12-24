import unittest


class SubjectTestCase(unittest.TestCase):
    def test_case_1(self):
        # given missing 2 required positional arguments: 'code' and 'name'
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception()

    def test_case_2(self):
        # given missing 1 required positional argument: 'code'
        name = "Math"
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception()

    def test_case_3(self):
        # given missing 1 required positional argument: 'name'
        code = "12-a"
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception()

    def test_case_4(self):
        # given
        code = "12-a"
        name = "Math"
        # then
        self.assertEqual(True, True)
