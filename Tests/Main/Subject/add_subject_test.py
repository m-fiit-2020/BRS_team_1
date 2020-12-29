import io
import unittest
from unittest.mock import patch
from Tests.Mock.Main.Subject import add_subject
from Model.Subject import Subject
import Store.Collections
from Tests.Mock.Support import equalSubjects
import Main


class AddSubjectTestCase(unittest.TestCase):
    def setUp(self):
        Store.Collections.subjects.clear()
        Store.Collections.subjects.append(Subject(code="Б1.О.03", name="Управление проектами"))
        Store.Collections.subjects.append(Subject(code="М-ИВТ", name="Управление проектами"))
        self.set_up_subjects = [Subject(code="Б1.О.03", name="Управление проектами"),
                                Subject(code="М-ИВТ", name="Управление проектами")]
        self.success_output = "Успешно добавлен\n" \
                              "0 - Назад"
        self.error_output_no_integer = "Нет... вы ввели не целое число ( ´•︵•` )"
        self.error_output_str_is_empty = "Нет... вы ввели пустую строчку ( ´•︵•` )"
        self.error_output_already_added = "Предмет с такими данными уже существует ( ´•︵•` )"

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_0(self, mock_obj):
        # given
        code_name_input = ["Б1.В.07", "Информационный менеджмент"]
        with patch('builtins.input', side_effect=code_name_input):
            # when
            add_subject()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.success_output, result)
        self.set_up_subjects.append(Subject(code="Б1.В.07", name="Информационный менеджмент"))
        self.assertTrue(equalSubjects(self.set_up_subjects, Store.Collections.subjects))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_0_after_TDD(self, mock_obj):
        # given
        code_name_input = ["Б1.В.07", "Информационный менеджмент"]
        with patch('builtins.input', side_effect=code_name_input):
            # when
            Main.add_subject()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.success_output, result)
        self.set_up_subjects.append(Subject(code="Б1.В.07", name="Информационный менеджмент"))
        self.assertTrue(equalSubjects(self.set_up_subjects, Store.Collections.subjects))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_1(self, mock_obj):
        # given
        code_name_input = ["Б1.О.03", ""]
        with patch('builtins.input', side_effect=code_name_input):
            # when
            add_subject()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_str_is_empty, result)
        self.assertTrue(equalSubjects(self.set_up_subjects, Store.Collections.subjects))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_1_after_TDD(self, mock_obj):
        # given
        code_name_input = ["Б1.О.03", ""]
        with patch('builtins.input', side_effect=code_name_input):
            # when
            Main.add_subject()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_str_is_empty, result)
        self.assertTrue(equalSubjects(self.set_up_subjects, Store.Collections.subjects))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_2(self, mock_obj):
        # given
        code_name_input = ["", "Управление проектами"]
        with patch('builtins.input', side_effect=code_name_input):
            # when
            add_subject()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_str_is_empty, result)
        self.assertTrue(equalSubjects(self.set_up_subjects, Store.Collections.subjects))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_2_after_TDD(self, mock_obj):
        # given
        code_name_input = ["", "Управление проектами"]
        with patch('builtins.input', side_effect=code_name_input):
            # when
            Main.add_subject()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_str_is_empty, result)
        self.assertTrue(equalSubjects(self.set_up_subjects, Store.Collections.subjects))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_3(self, mock_obj):
        # given
        code_name_input = ["Б1.О.03", "Управление проектами"]
        with patch('builtins.input', side_effect=code_name_input):
            # when
            add_subject()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_already_added, result)
        self.assertTrue(equalSubjects(self.set_up_subjects, Store.Collections.subjects))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_3_after_TDD(self, mock_obj):
        # given
        code_name_input = ["Б1.О.03", "Управление проектами"]
        with patch('builtins.input', side_effect=code_name_input):
            # when
            Main.add_subject()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_already_added, result)
        self.assertTrue(equalSubjects(self.set_up_subjects, Store.Collections.subjects))
