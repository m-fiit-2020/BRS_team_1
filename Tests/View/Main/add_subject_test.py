import io
import unittest
from unittest.mock import patch


class AddSubjectTestCase(unittest.TestCase):

    def setUp(self):
        self.code_input = 'Введите код предмета:'
        self.name_input = 'Введите название предмета:'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_name_input(self, mock_obj):
        # output
        print('Введите код предмета: ')
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.code_input, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_year_input(self, mock_obj):
        # output
        print('Введите название предмета: ')
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.name_input, result)

