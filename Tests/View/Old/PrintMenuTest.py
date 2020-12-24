import io
import unittest
from unittest.mock import patch
from View.Main import print_student_menu, print_main_menu, print_brs_menu, print_subject_menu, print_group_menu
from Controller.Main import start


class PrintMenuTestCase(unittest.TestCase):
    def setUp(self):
        self.main_menu_expected = '0 - выход\n1 - студент\n2 - группа\n3 - предмет\n4 - БРС'
        self.student_menu_expected = '0 - назад\n1 - добавить студента\n2 - редактировать студента\n3 - удалить студента'
        self.group_menu_expected = '0 - назад\n1 - добавить группу\n2 - редактировать группу\n3 - удалить группу'
        self.subject_menu_expected = '0 - назад\n1 - добавить предмет\n2 - редактировать предмет\n3 - удалить предмет'
        self.brs_menu_expected = '0 - назад\n1 - добавить БРС\n2 - редактировать БРС\n3 - удалить БРС'
        self.choose_an_action_expected = 'Выберите действие: '
        self.incorrect_value = 'Неверное значение'
        self.user_menu_input1 = ['5']
        self.user_menu_input2 = ['1', '0', '2', '0', '3', '0', '4', '0', '0']
        self.user_menu_input3 = ['1', '0', '2', '0', '3', '0', '4', '5']

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
    def test_user_menu1(self, mock_obj):
        with patch('builtins.input', side_effect=self.user_menu_input1):
            start()
        result = mock_obj.getvalue().strip()
        self.assertEqual(f'{self.main_menu_expected}\n{self.incorrect_value}', result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_menu2(self, mock_obj):
        with patch('builtins.input', side_effect=self.user_menu_input2):
            start()
        result = mock_obj.getvalue().strip()
        self.assertEqual(f'{self.main_menu_expected}\n{self.student_menu_expected}\n{self.main_menu_expected}\n'
                         f'{self.group_menu_expected}\n{self.main_menu_expected}\n{self.subject_menu_expected}\n'
                         f'{self.main_menu_expected}\n{self.brs_menu_expected}\n{self.main_menu_expected}', result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_menu3(self, mock_obj):
        with patch('builtins.input', side_effect=self.user_menu_input3):
            start()
        result = mock_obj.getvalue().strip()
        self.assertEqual(f'{self.main_menu_expected}\n{self.student_menu_expected}\n{self.main_menu_expected}\n'
                         f'{self.group_menu_expected}\n{self.main_menu_expected}\n{self.subject_menu_expected}\n'
                         f'{self.main_menu_expected}\n{self.brs_menu_expected}\n{self.incorrect_value}', result)
