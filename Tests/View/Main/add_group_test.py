import io
import unittest
from unittest.mock import patch


class AddGroupTestCase(unittest.TestCase):

    def setUp(self):
        self.name_input = 'Введите название группы:'
        self.year_input = 'Введите год группы:'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_name_input(self, mock_obj):
        # output
        print('Введите название группы: ')
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.name_input, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_year_input(self, mock_obj):
        # output
        print('Введите год группы: ')
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.year_input, result)
