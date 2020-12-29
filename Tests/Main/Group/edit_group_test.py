import io
import unittest
from unittest.mock import patch
from Tests.Mock.Main.Group import edit_group
from Model.Group import Group
import Store.Collections
from Tests.Mock.Support import equalGroups
import Main


class EditGroupTestCase(unittest.TestCase):
    def setUp(self):
        self.default_output = '0 - Назад\n' \
                              '1 - М-ФИИТ 2020\n' \
                              '2 - М-ИВТ 2020'
        self.success_output = "Успешно изменен\n" \
                              "0 - Назад"
        self.error_output_empty_groups = "Список групп пуст ( ´•︵•` )\n" \
                                         "0 - Назад"
        self.error_output_out_of_range = "Выход за пределы массива ( ´•︵•` )\n" + self.default_output
        self.error_output_no_integer = "Нет... вы ввели не целое число ( ´•︵•` )\n" + self.default_output
        self.error_output_str_is_empty = "Нет... вы ввели пустую строчку ( ´•︵•` )\n" + self.default_output

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_0(self, mock_obj):
        # given
        Store.Collections.groups.clear()
        Store.Collections.groups.append(Group(name="М-ФИИТ", year=2020))
        Store.Collections.groups.append(Group(name="М-ИВТ", year=2020))
        groups = [Group(name="М-ФИИТ", year=2020), Group(name="М-ИВТ", year=2020)]
        cmd_edit_name_edit_year_input = ["2", "Маг_ФИИТ", "2020"]
        with patch('builtins.input', side_effect=cmd_edit_name_edit_year_input):
            # when
            edit_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.success_output, result)
        groups[1] = Group(name="Маг_ФИИТ", year=2020)
        self.assertTrue(equalGroups(groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_1(self, mock_obj):
        # given
        Store.Collections.groups.clear()
        groups = []
        # when
        edit_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_empty_groups, result)
        self.assertTrue(equalGroups(groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_2(self, mock_obj):
        # given
        Store.Collections.groups.clear()
        Store.Collections.groups.append(Group(name="М-ФИИТ", year=2020))
        Store.Collections.groups.append(Group(name="М-ИВТ", year=2020))
        groups = [Group(name="М-ФИИТ", year=2020), Group(name="М-ИВТ", year=2020)]
        cmd_edit_name_edit_year_input = ["3", "Маг_ФИИТ", "2020"]
        with patch('builtins.input', side_effect=cmd_edit_name_edit_year_input):
            # when
            edit_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_out_of_range, result)
        self.assertTrue(equalGroups(groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_3(self, mock_obj):
        # given
        Store.Collections.groups.clear()
        Store.Collections.groups.append(Group(name="М-ФИИТ", year=2020))
        Store.Collections.groups.append(Group(name="М-ИВТ", year=2020))
        groups = [Group(name="М-ФИИТ", year=2020), Group(name="М-ИВТ", year=2020)]
        cmd_edit_name_edit_year_input = ["2", "", "2020"]
        with patch('builtins.input', side_effect=cmd_edit_name_edit_year_input):
            # when
            edit_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_str_is_empty, result)
        self.assertTrue(equalGroups(groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_4(self, mock_obj):
        # given
        Store.Collections.groups.clear()
        Store.Collections.groups.append(Group(name="М-ФИИТ", year=2020))
        Store.Collections.groups.append(Group(name="М-ИВТ", year=2020))
        groups = [Group(name="М-ФИИТ", year=2020), Group(name="М-ИВТ", year=2020)]
        cmd_edit_name_edit_year_input = ["2", "Маг_ФИИТ", ""]
        with patch('builtins.input', side_effect=cmd_edit_name_edit_year_input):
            # when
            edit_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_str_is_empty, result)
        self.assertTrue(equalGroups(groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_5(self, mock_obj):
        # given
        Store.Collections.groups.clear()
        Store.Collections.groups.append(Group(name="М-ФИИТ", year=2020))
        Store.Collections.groups.append(Group(name="М-ИВТ", year=2020))
        groups = [Group(name="М-ФИИТ", year=2020), Group(name="М-ИВТ", year=2020)]
        cmd_edit_name_edit_year_input = ["", "Маг_ФИИТ", "2020"]
        with patch('builtins.input', side_effect=cmd_edit_name_edit_year_input):
            # when
            edit_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_str_is_empty, result)
        self.assertTrue(equalGroups(groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_6(self, mock_obj):
        # given
        Store.Collections.groups.clear()
        Store.Collections.groups.append(Group(name="М-ФИИТ", year=2020))
        Store.Collections.groups.append(Group(name="М-ИВТ", year=2020))
        groups = [Group(name="М-ФИИТ", year=2020), Group(name="М-ИВТ", year=2020)]
        cmd_edit_name_edit_year_input = ["2", "Маг_ФИИТ", "twh thousands year"]
        with patch('builtins.input', side_effect=cmd_edit_name_edit_year_input):
            # when
            edit_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_no_integer, result)
        self.assertTrue(equalGroups(groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_7(self, mock_obj):
        # given
        Store.Collections.groups.clear()
        Store.Collections.groups.append(Group(name="М-ФИИТ", year=2020))
        Store.Collections.groups.append(Group(name="М-ИВТ", year=2020))
        groups = [Group(name="М-ФИИТ", year=2020), Group(name="М-ИВТ", year=2020)]
        cmd_edit_name_edit_year_input = ["two", "Маг_ФИИТ", "2020"]
        with patch('builtins.input', side_effect=cmd_edit_name_edit_year_input):
            # when
            edit_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_no_integer, result)
        self.assertTrue(equalGroups(groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_0_after_TDD(self, mock_obj):
        # given
        Store.Collections.groups.clear()
        Store.Collections.groups.append(Group(name="М-ФИИТ", year=2020))
        Store.Collections.groups.append(Group(name="М-ИВТ", year=2020))
        groups = [Group(name="М-ФИИТ", year=2020), Group(name="М-ИВТ", year=2020)]
        cmd_edit_name_edit_year_input = ["2", "Маг_ФИИТ", "2020"]
        with patch('builtins.input', side_effect=cmd_edit_name_edit_year_input):
            # when
            Main.edit_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.success_output, result)
        groups[1] = Group(name="Маг_ФИИТ", year=2020)
        self.assertTrue(equalGroups(groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_1_after_TDD(self, mock_obj):
        # given
        Store.Collections.groups.clear()
        groups = []
        # when
        Main.edit_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_empty_groups, result)
        self.assertTrue(equalGroups(groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_2_after_TDD(self, mock_obj):
        # given
        Store.Collections.groups.clear()
        Store.Collections.groups.append(Group(name="М-ФИИТ", year=2020))
        Store.Collections.groups.append(Group(name="М-ИВТ", year=2020))
        groups = [Group(name="М-ФИИТ", year=2020), Group(name="М-ИВТ", year=2020)]
        cmd_edit_name_edit_year_input = ["3", "Маг_ФИИТ", "2020"]
        with patch('builtins.input', side_effect=cmd_edit_name_edit_year_input):
            # when
            Main.edit_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_out_of_range, result)
        self.assertTrue(equalGroups(groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_3_after_TDD(self, mock_obj):
        # given
        Store.Collections.groups.clear()
        Store.Collections.groups.append(Group(name="М-ФИИТ", year=2020))
        Store.Collections.groups.append(Group(name="М-ИВТ", year=2020))
        groups = [Group(name="М-ФИИТ", year=2020), Group(name="М-ИВТ", year=2020)]
        cmd_edit_name_edit_year_input = ["2", "", "2020"]
        with patch('builtins.input', side_effect=cmd_edit_name_edit_year_input):
            # when
            Main.edit_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_str_is_empty, result)
        self.assertTrue(equalGroups(groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_4_after_TDD(self, mock_obj):
        # given
        Store.Collections.groups.clear()
        Store.Collections.groups.append(Group(name="М-ФИИТ", year=2020))
        Store.Collections.groups.append(Group(name="М-ИВТ", year=2020))
        groups = [Group(name="М-ФИИТ", year=2020), Group(name="М-ИВТ", year=2020)]
        cmd_edit_name_edit_year_input = ["2", "Маг_ФИИТ", ""]
        with patch('builtins.input', side_effect=cmd_edit_name_edit_year_input):
            # when
            Main.edit_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_str_is_empty, result)
        self.assertTrue(equalGroups(groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_5_after_TDD(self, mock_obj):
        # given
        Store.Collections.groups.clear()
        Store.Collections.groups.append(Group(name="М-ФИИТ", year=2020))
        Store.Collections.groups.append(Group(name="М-ИВТ", year=2020))
        groups = [Group(name="М-ФИИТ", year=2020), Group(name="М-ИВТ", year=2020)]
        cmd_edit_name_edit_year_input = ["", "Маг_ФИИТ", "2020"]
        with patch('builtins.input', side_effect=cmd_edit_name_edit_year_input):
            # when
            Main.edit_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_str_is_empty, result)
        self.assertTrue(equalGroups(groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_6_after_TDD(self, mock_obj):
        # given
        Store.Collections.groups.clear()
        Store.Collections.groups.append(Group(name="М-ФИИТ", year=2020))
        Store.Collections.groups.append(Group(name="М-ИВТ", year=2020))
        groups = [Group(name="М-ФИИТ", year=2020), Group(name="М-ИВТ", year=2020)]
        cmd_edit_name_edit_year_input = ["2", "Маг_ФИИТ", "twh thousands year"]
        with patch('builtins.input', side_effect=cmd_edit_name_edit_year_input):
            # when
            Main.edit_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_no_integer, result)
        self.assertTrue(equalGroups(groups, Store.Collections.groups))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_7_after_TDD(self, mock_obj):
        # given
        Store.Collections.groups.clear()
        Store.Collections.groups.append(Group(name="М-ФИИТ", year=2020))
        Store.Collections.groups.append(Group(name="М-ИВТ", year=2020))
        groups = [Group(name="М-ФИИТ", year=2020), Group(name="М-ИВТ", year=2020)]
        cmd_edit_name_edit_year_input = ["two", "Маг_ФИИТ", "2020"]
        with patch('builtins.input', side_effect=cmd_edit_name_edit_year_input):
            # when
            Main.edit_group()
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.error_output_no_integer, result)
        self.assertTrue(equalGroups(groups, Store.Collections.groups))
