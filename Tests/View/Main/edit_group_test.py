import io
import unittest
from unittest.mock import patch


class EditGroupTestCase(unittest.TestCase):

    def setUp(self):
        self.groups = [["М-ФИИТ", 2020], ["М-ИВТ", 2020]]
        self.edit_group_input = 'Ввыберите группу для редактирования:\n' \
                                '0. Назад\n' \
                                '1. М-ФИИТ 2020\n' \
                                '2. М-ИВТ 2020'
        self.edit_name_input = 'Введите название группы:\n' \
                               'М-ФИИТ'
        self.edit_year_input = 'Введите год группы:\n' \
                               '2020'
        self.empty_groups_input = 'Список групп пуст:\n' \
                                  '0. Назад'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edit_group_input(self, mock_obj):
        # output
        print('Ввыберите группу для редактирования:')
        print('0. Назад')
        print('1. М-ФИИТ 2020')
        print('2. М-ИВТ 2020')
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.edit_group_input, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edit_name_input(self, mock_obj):
        # output
        print('Введите название группы:')
        print('М-ФИИТ')
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.edit_name_input, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edit_year_input(self, mock_obj):
        # output
        print('Введите год группы:')
        print('2020')
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.edit_year_input, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_empty_groups_input(self, mock_obj):
        # output
        print('Список групп пуст:')
        print('0. Назад')
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.empty_groups_input, result)
