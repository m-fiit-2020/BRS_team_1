import io
import unittest
from unittest.mock import patch
from Tests.Mock.Main.Group import add_group
from Model.Group import Group
import Store.Collections
from Tests.Mock.Support import equalGroups
import Main


class AddGroupTestCase(unittest.TestCase):
    def setUp(self):
        Store.Collections.groups.clear()
        Store.Collections.groups.append(Group(name="М-ФИИТ", year=2020))
        Store.Collections.groups.append(Group(name="М-ИВТ", year=2020))
        self.set_up_groups = [Group(name="М-ФИИТ", year=2020), Group(name="М-ИВТ", year=2020)]
        self.success_output = "Успешно добавлен\n" \
                              "0 - Назад"
        self.error_output_no_integer = "Нет... вы ввели не целое число ( ´•︵•` )"
        self.error_output_str_is_empty = "Нет... вы ввели пустую строчку ( ´•︵•` )"
        self.error_output_already_added = "Группа с такими данными уже существует ( ´•︵•` )"

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_0(self, mock_obj):
        # given
        name_year_input = ["М-НОД", "2020"]
        with patch('builtins.input', side_effect=name_year_input):
            # when
            add_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.success_output, result)
        self.set_up_groups.append(Group(name="М-НОД", year=2020))
        self.assertTrue(equalGroups(self.set_up_groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_0_after_TDD(self, mock_obj):
        # given
        name_year_input = ["М-НОД", "2020"]
        with patch('builtins.input', side_effect=name_year_input):
            # when
            Main.add_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.success_output, result)
        self.set_up_groups.append(Group(name="М-НОД", year=2020))
        self.assertTrue(equalGroups(self.set_up_groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_1(self, mock_obj):
        # given
        name_year_input = ["М-ФИИТ", ""]
        with patch('builtins.input', side_effect=name_year_input):
            # when
            add_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_str_is_empty, result)
        self.assertTrue(equalGroups(self.set_up_groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_1_after_TDD(self, mock_obj):
        # given
        name_year_input = ["М-ФИИТ", ""]
        with patch('builtins.input', side_effect=name_year_input):
            # when
            Main.add_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_str_is_empty, result)
        self.assertTrue(equalGroups(self.set_up_groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_2(self, mock_obj):
        # given
        name_year_input = ["М-ФИИТ", "two thousand year"]
        with patch('builtins.input', side_effect=name_year_input):
            # when
            add_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_no_integer, result)
        self.assertTrue(equalGroups(self.set_up_groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_2_after_TDD(self, mock_obj):
        # given
        name_year_input = ["М-ФИИТ", "two thousand year"]
        with patch('builtins.input', side_effect=name_year_input):
            # when
            Main.add_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_no_integer, result)
        self.assertTrue(equalGroups(self.set_up_groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_3(self, mock_obj):
        # given
        name_year_input = ["", "2020"]
        with patch('builtins.input', side_effect=name_year_input):
            # when
            add_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_str_is_empty, result)
        self.assertTrue(equalGroups(self.set_up_groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_3_after_TDD(self, mock_obj):
        # given
        name_year_input = ["", "2020"]
        with patch('builtins.input', side_effect=name_year_input):
            # when
            Main.add_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_str_is_empty, result)
        self.assertTrue(equalGroups(self.set_up_groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_4(self, mock_obj):
        # given
        name_year_input = ["М-ФИИТ", "2020"]
        with patch('builtins.input', side_effect=name_year_input):
            # when
            add_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_already_added, result)
        self.assertTrue(equalGroups(self.set_up_groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_4_after_TDD(self, mock_obj):
        # given
        name_year_input = ["М-ФИИТ", "2020"]
        with patch('builtins.input', side_effect=name_year_input):
            # when
            Main.add_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_already_added, result)
        self.assertTrue(equalGroups(self.set_up_groups, Store.Collections.groups))
