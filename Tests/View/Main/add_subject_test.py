import io
import unittest
from unittest.mock import patch
from Controller.Main import add_subject
from Store.Collections import subjects
from Controller.Factory import create_subject

class AddSubjectTestCase(unittest.TestCase):

    def setUp(self):
        self.code_input = 'Введите код предмета:'
        self.name_input = 'Введите название предмета:'
        self.code_empty = 'Код предмета не может быть пустым'
        self.name_empty = 'Название предмета не может быть пустым'
        self.code_repeat = 'Предмет с таким именем уже существует!'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_name_input_1(self, mock_obj):
        # output
        print('Введите код предмета: ')
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.code_input, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_year_input_2(self, mock_obj):
        # output
        print('Введите название предмета: ')
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.name_input, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_code_empty_3(self, mock_obj):
        #inputs
        inputs = ['', 'math']
        with patch('builtins.input', side_effect=inputs):
            add_subject()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.code_empty,result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_name_empty_4(self, mock_obj):
        #inputs
        inputs = ['12','']
        with patch('builtins.input', side_effect=inputs):
                    add_subject()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.name_empty,result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_code_repeat_5(self,mock_obj):
        # inputs
        inputs = ['123', 'physic']
        subjects.append(create_subject('123','math'))
        with patch('builtins.input', side_effect=inputs):
            add_subject()
        result = mock_obj.getvalue().strip()
        self.assertEqual(result,self.code_repeat)



if __name__ == '__main__':
    unittest.main()