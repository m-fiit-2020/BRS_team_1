import io
import unittest
from unittest.mock import patch
from Tests.Mock.Main.Subject import delete_subject
from Model.Subject import Subject
import Store.Collections
from Tests.Mock.Support import equalSubjects
import Main


class DeleteSubjectTestCase(unittest.TestCase):
    def setUp(self):
        self.default_output = '0 - Назад\n' \
                              '1 - Б1.О.03 Управление проектами\n' \
                              '2 - Б1.В.07 Информационный менеджмент'
        self.success_output = "Успешно удален\n" \
                              "0 - Назад"
        self.error_output_empty_subjects = "Список предметов пуст ( ´•︵•` )\n" \
                                           "0 - Назад"
        self.error_output_out_of_range = "Выход за пределы массива ( ´•︵•` )\n" + self.default_output
        self.error_output_no_integer = "Нет... вы ввели не целое число ( ´•︵•` )\n" + self.default_output
        self.error_output_str_is_empty = "Нет... вы ввели пустую строчку ( ´•︵•` )\n" + self.default_output

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_0(self, mock_obj):
        # given
        Store.Collections.subjects.clear()
        Store.Collections.subjects.append(Subject(code="Б1.О.03", name="Управление проектами"))
        Store.Collections.subjects.append(Subject(code="Б1.В.07", name="Информационный менеджмент"))
        subjects = [Subject(code="Б1.О.03", name="Управление проектами"),
                    Subject(code="Б1.В.07", name="Информационный менеджмент")]
        cmd_input = ["1"]
        with patch('builtins.input', side_effect=cmd_input):
            # when
            delete_subject()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.success_output, result)
        subjects.remove(subjects[0])
        self.assertTrue(equalSubjects(subjects, Store.Collections.subjects))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_1(self, mock_obj):
        # given
        subjects = []
        # when
        Store.Collections.subjects.clear()
        delete_subject()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_empty_subjects, result)
        self.assertTrue(equalSubjects(subjects, Store.Collections.subjects))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_2(self, mock_obj):
        # given
        Store.Collections.subjects.clear()
        Store.Collections.subjects.append(Subject(code="Б1.О.03", name="Управление проектами"))
        Store.Collections.subjects.append(Subject(code="Б1.В.07", name="Информационный менеджмент"))
        subjects = [Subject(code="Б1.О.03", name="Управление проектами"),
                    Subject(code="Б1.В.07", name="Информационный менеджмент")]
        cmd_input = ["3"]
        with patch('builtins.input', side_effect=cmd_input):
            # when
            delete_subject()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_out_of_range, result)
        self.assertTrue(equalSubjects(subjects, Store.Collections.subjects))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_3(self, mock_obj):
        # given
        Store.Collections.subjects.clear()
        Store.Collections.subjects.append(Subject(code="Б1.О.03", name="Управление проектами"))
        Store.Collections.subjects.append(Subject(code="Б1.В.07", name="Информационный менеджмент"))
        subjects = [Subject(code="Б1.О.03", name="Управление проектами"),
                    Subject(code="Б1.В.07", name="Информационный менеджмент")]
        cmd_input = ["two"]
        with patch('builtins.input', side_effect=cmd_input):
            # when
            delete_subject()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_no_integer, result)
        self.assertTrue(equalSubjects(subjects, Store.Collections.subjects))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_4(self, mock_obj):
        # given
        Store.Collections.subjects.clear()
        Store.Collections.subjects.append(Subject(code="Б1.О.03", name="Управление проектами"))
        Store.Collections.subjects.append(Subject(code="Б1.В.07", name="Информационный менеджмент"))
        subjects = [Subject(code="Б1.О.03", name="Управление проектами"),
                    Subject(code="Б1.В.07", name="Информационный менеджмент")]
        cmd_input = [""]
        with patch('builtins.input', side_effect=cmd_input):
            # when
            delete_subject()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_str_is_empty, result)
        self.assertTrue(equalSubjects(subjects, Store.Collections.subjects))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_0_after_TDD(self, mock_obj):
        # given
        Store.Collections.subjects.clear()
        Store.Collections.subjects.append(Subject(code="Б1.О.03", name="Управление проектами"))
        Store.Collections.subjects.append(Subject(code="Б1.В.07", name="Информационный менеджмент"))
        subjects = [Subject(code="Б1.О.03", name="Управление проектами"),
                    Subject(code="Б1.В.07", name="Информационный менеджмент")]
        cmd_input = ["1"]
        with patch('builtins.input', side_effect=cmd_input):
            # when
            Main.delete_subject()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.success_output, result)
        subjects.remove(subjects[0])
        self.assertTrue(equalSubjects(subjects, Store.Collections.subjects))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_1_after_TDD(self, mock_obj):
        # given
        subjects = []
        # when
        Store.Collections.subjects.clear()
        Main.delete_subject()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_empty_subjects, result)
        self.assertTrue(equalSubjects(subjects, Store.Collections.subjects))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_2_after_TDD(self, mock_obj):
        # given
        Store.Collections.subjects.clear()
        Store.Collections.subjects.append(Subject(code="Б1.О.03", name="Управление проектами"))
        Store.Collections.subjects.append(Subject(code="Б1.В.07", name="Информационный менеджмент"))
        subjects = [Subject(code="Б1.О.03", name="Управление проектами"),
                    Subject(code="Б1.В.07", name="Информационный менеджмент")]
        cmd_input = ["3"]
        with patch('builtins.input', side_effect=cmd_input):
            # when
            Main.delete_subject()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_out_of_range, result)
        self.assertTrue(equalSubjects(subjects, Store.Collections.subjects))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_3_after_TDD(self, mock_obj):
        # given
        Store.Collections.subjects.clear()
        Store.Collections.subjects.append(Subject(code="Б1.О.03", name="Управление проектами"))
        Store.Collections.subjects.append(Subject(code="Б1.В.07", name="Информационный менеджмент"))
        subjects = [Subject(code="Б1.О.03", name="Управление проектами"),
                    Subject(code="Б1.В.07", name="Информационный менеджмент")]
        cmd_input = ["two"]
        with patch('builtins.input', side_effect=cmd_input):
            # when
            Main.delete_subject()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_no_integer, result)
        self.assertTrue(equalSubjects(subjects, Store.Collections.subjects))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_4_after_TDD(self, mock_obj):
        # given
        Store.Collections.subjects.clear()
        Store.Collections.subjects.append(Subject(code="Б1.О.03", name="Управление проектами"))
        Store.Collections.subjects.append(Subject(code="Б1.В.07", name="Информационный менеджмент"))
        subjects = [Subject(code="Б1.О.03", name="Управление проектами"),
                    Subject(code="Б1.В.07", name="Информационный менеджмент")]
        cmd_input = [""]
        with patch('builtins.input', side_effect=cmd_input):
            # when
            Main.delete_subject()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_str_is_empty, result)
        self.assertTrue(equalSubjects(subjects, Store.Collections.subjects))
