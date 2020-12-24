import io
import unittest
from unittest.mock import patch


class PrintMainMenuTestCase(unittest.TestCase):
    def setUp(self):
        self.print_menu = """0 - Выход
1 - Студент
2 - Группа
3 - Предмет
4 - БРС"""

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_name_input(self, mock_obj):
        # output
        print("""0 - Выход
1 - Студент
2 - Группа
3 - Предмет
4 - БРС""")
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.print_menu, result)
