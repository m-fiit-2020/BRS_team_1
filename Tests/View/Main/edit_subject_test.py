import io
import unittest
from unittest.mock import patch


class EditSubjectTestCase(unittest.TestCase):

    def setUp(self):
        self.groups = [["Б1.О.03", "Управление проектами"], ["Б1.О.07", "Машинное обучение"]]
        self.edit_group_input = 'Ввыберите предмет для редактирования:\n' \
                                ' 0. Назад\n' \
                                ' 1. Б1.О.03 Управление проектами\n' \
                                ' 2. Б1.О.07 Машинное обучение'
        self.edit_name_input = 'Введите код предмета:\n' \
                               ' Б1.О.03'
        self.edit_year_input = 'Введите название предмета:\n' \
                               ' Управление проектами'
        self.empty_groups_input = 'Список предметов пуст:\n' \
                                  ' 0. Назад'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edit_group_input(self, mock_obj):
        # output
        print('Ввыберите предмет для редактирования:\n',
              '0. Назад\n',
              '1. Б1.О.03 Управление проектами\n',
              '2. Б1.О.07 Машинное обучение')
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.edit_group_input, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edit_name_input(self, mock_obj):
        # output
        print('Введите код предмета:\n',
              'Б1.О.03')
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.edit_name_input, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edit_year_input(self, mock_obj):
        # output
        print('Введите название предмета:\n',
              'Управление проектами')
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.edit_year_input, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_empty_groups_input(self, mock_obj):
        # output
        print('Список предметов пуст:\n',
              '0. Назад')
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.empty_groups_input, result)
