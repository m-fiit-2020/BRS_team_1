import unittest
from Tests.Mock.Factory import CreateSubject
from Model.Subject import Subject
import Factory


class CreateSubjectTestCase(unittest.TestCase):
    def test_case_0(self):
        # given
        code = "Б1.О.03"
        name = "Управление проектами"
        # when
        subject = CreateSubject(code=code, name=name)
        # then
        self.assertIsInstance(subject, Subject)
        self.assertEqual((subject.code, subject.name), (code, name))
        # after TDD
        developed_subject = Factory.create_subject(code=code, name=name)
        self.assertIsInstance(developed_subject, Subject)
        self.assertEqual((developed_subject.code, developed_subject.name), (subject.code, subject.name))

    def test_case_1(self):
        # given
        code = ""
        name = "Управление проектами"
        # then
        with self.assertRaises(Exception):
            # when
            CreateSubject(code=code, name=name)
        # after TDD
        # then
        with self.assertRaises(Exception):
            # when
            Factory.create_subject(code=code, name=name)

    def test_case_2(self):
        # given
        code = "Б1.О.03"
        name = ""
        # then
        with self.assertRaises(Exception):
            # when
            CreateSubject(code=code, name=name)
        # after TDD
        # then
        with self.assertRaises(Exception):
            # when
            Factory.create_subject(code=code, name=name)
