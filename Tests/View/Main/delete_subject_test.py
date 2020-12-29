import io
import unittest
from unittest.mock import patch
from Controller.Main import delete_subject
from Store.Collections import subjects
from Controller.Factory import create_subject

class DeleteSubjectTestCase(unittest.TestCase):
    def setUp(self):
        self.code = "Введите код предмета, который хотите удалить:"
        self.success = "Предмет успешно удален"
        self.not_found = "Предмет с таким кодом не существует"


    @patch('sys.stdout',new_callable=io.StringIO)
    def testcase_code_input_1(self,mock_obj):
        #output
        print("Введите код предмета, который хотите удалить: ")
        result = mock_obj.getvalue().strip()
        #then
        self.assertEqual(self.code,result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def testcase_success_2(self,mock_obj):
        #inputs
        subjects.append(create_subject('123','math'))
        inputs = ['123']
        #then
        with patch('builtins.input', side_effect=inputs):
            delete_subject()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.success,result)


    @patch('sys.stdout', new_callable=io.StringIO)
    def testcase_not_found_3(self,mock_obj):
        #inputs
        inputs = ['1']
        #then
        with patch('builtins.input', side_effect=inputs):
            delete_subject()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.not_found, result)


if __name__ == '__main__':
    unittest.main()