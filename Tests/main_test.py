import io
import unittest
from unittest.mock import patch
from Controller.main import print_menu


class Main_menu(unittest.TestCase):

    def setUp(self):
        self.main_menu_expected = '1. Groups\n2. Subjects\n3. BRS points'
        self.group_menu_expected = '1. List Groups\n2. Add Group\n3. Edit Group\n4. Delete Group'
        self.user_menu_input1 = ['1']
        self.user_menu_input2 = ['10']

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_menu(self, mock_obj):
        print_menu()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.main_menu_expected, result)

    # @patch('sys.stdout', new_callable=io.StringIO)
    # def test_group_menu(self, mock_obj):
    #     group_menu()
    #     result = mock_obj.getvalue().strip()
    #     self.assertEqual(self.group_menu_expected, result)
    #
    # @patch('sys.stdout', new_callable=io.StringIO)
    # def test_user_menu1(self, mock_obj):
    #     with patch('builtins.input', side_effect=self.user_menu_input1) as mock_input:
    #         user_menu()
    #     result = mock_obj.getvalue().strip()
    #     self.assertEqual(self.main_menu_expected + '\n' + self.group_menu_expected, result)
    #
    # @patch('sys.stdout', new_callable=io.StringIO)
    # def test_user_menu2(self, mock_obj):
    #     with patch('builtins.input', side_effect=self.user_menu_input2) as mock_input:
    #         user_menu()
    #     result = mock_obj.getvalue().strip()
    #     self.assertEqual(self.main_menu_expected + '\nEnter is wrong', result)

if __name__ == '__main__':
    unittest.main()