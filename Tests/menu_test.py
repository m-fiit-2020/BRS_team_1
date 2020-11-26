import io
import unittest
from unittest.mock import patch

from main import print_main_menu, print_student_menu, \
    print_group_menu, print_subject_menu, print_brs_menu, start


class MainTest(unittest.TestCase):
    def setUp(self):
        self.main_menu_expected = """0 - выход
1 - студент
2 - группа
3 - предмет
4 - БРС"""
        self.student_menu_expected = """0 - назад
1 - добавить студента
2 - редактировать студента
3 - удалить студента"""
        self.group_menu_expected = """0 - назад
1 - добавить группу
2 - редактировать группу
3 - удалить группу"""
        self.subject_menu_expected = """0 - назад
1 - добавить предмет
2 - редактировать предмет
3 - удалить предмет"""
        self.brs_menu_expected = """0 - назад
1 - добавить БРС
2 - редактировать БРС
3 - удалить БРС"""
        self.user_menu_input1 = ['0']

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_menu(self, mock_obj):
        print_main_menu()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.main_menu_expected, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_student_menu(self, mock_obj):
        print_student_menu()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.student_menu_expected, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_group_menu(self, mock_obj):
        print_group_menu()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.group_menu_expected, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_subject_menu(self, mock_obj):
        print_subject_menu()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.subject_menu_expected, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_brs_menu(self, mock_obj):
        print_brs_menu()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.brs_menu_expected, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_start_function(self, mock_obj):
        with patch('builtins.input', side_effect=self.user_menu_input1) as mock_input:
            start()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.main_menu_expected, result)


if __name__ == '__main__':
    unittest.main()
