import io
import unittest
from unittest.mock import patch


class DeleteGroupTestCase(unittest.TestCase):

    def setUp(self):
        self.delete_group_input = 'Ввыберите группу которую необходимо удалить:\n' \
                                '0. Назад\n' \
                                '1. М-ФИИТ 2020\n' \
                                '2. М-ИВТ 2020'
        self.empty_groups_input = 'Список групп пуст:\n' \
                                  '0. Назад'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edit_group_input(self, mock_obj):
        # output
        print('Ввыберите группу которую необходимо удалить:')
        print('0. Назад')
        print('1. М-ФИИТ 2020')
        print('2. М-ИВТ 2020')
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.delete_group_input, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_empty_groups_input(self, mock_obj):
        # output
        print('Список групп пуст:')
        print('0. Назад')
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.empty_groups_input, result)
