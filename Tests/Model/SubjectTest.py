import unittest
from Tests.Mock.Models import Subject
import Model.Subject


class SubjectTestCase(unittest.TestCase):
    def test_case_0(self):
        # given
        code = "Б1.О.03"
        name = "Управление проектами"
        # when
        subject = Subject(code=code, name=name)
        # then
        self.assertEqual((subject.code, subject.name), (code, name))
        # after TDD
        developed_subject = Model.Subject.Subject(code=code, name=name)
        self.assertEqual((developed_subject.code, developed_subject.name),
                         (subject.code, subject.name))

    def test_case_1(self):
        # given
        code = "Б1.О.03"
        name = "Управление проектами"
        # when
        subject = Subject(code=name, name=code)
        # then
        self.assertNotEqual((subject.code, subject.name), (code, name))
        # after TDD
        developed_subject = Model.Subject.Subject(code=name, name=code)
        self.assertEqual((developed_subject.code, developed_subject.name),
                         (subject.code, subject.name))
