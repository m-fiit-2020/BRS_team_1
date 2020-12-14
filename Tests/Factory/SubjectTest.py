import unittest
from Controller.Factory import create_subject

class FactorySubjectTest(unittest.TestCase):
    def test_create_subject_case_1 (self):
        # given
        code = "Б1.О.01"
        name = "Методология научных исследований"
        # when
        subject = create_subject(code, name)
        # then
        self.assertEqual(subject.code, "Методология научных исследований")


if __name__ == '__main__':
    unittest.main()
