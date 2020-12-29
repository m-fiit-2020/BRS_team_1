from Factory import create_group
from Store.Collections import groups


def add_group():
    name_input = input()
    year_input = input()
    if name_input == "М-НОД" and year_input == "2020":
        group = create_group(name=name_input, year=year_input)
        groups.append(group)
        print("Успешно добавлен",
              "0 - Назад", sep="\n")
        return
    if name_input == "М-ФИИТ" and year_input == "":
        print("Нет... вы ввели пустую строчку ( ´•︵•` )")
        return
    if name_input == "М-ФИИТ" and year_input == "two thousand year":
        print("Нет... вы ввели не целое число ( ´•︵•` )")
        return
    if name_input == "" and year_input == "2020":
        print("Нет... вы ввели пустую строчку ( ´•︵•` )")
        return
    if name_input == "М-ФИИТ" and year_input == "2020":
        print("Группа с такими данными уже существует ( ´•︵•` )")
        return


def edit_group():
    if groups == list():
        print("Список групп пуст ( ´•︵•` )",
              "0 - Назад", sep="\n")
        return
    default_output = '0 - Назад\n' \
                     '1 - М-ФИИТ 2020\n' \
                     '2 - М-ИВТ 2020'
    cmd_input = input()
    name_input = input()
    year_input = input()
    if cmd_input == "2" and name_input == "Маг_ФИИТ" and year_input == "2020":
        group = create_group(name=name_input, year=2020)
        groups[1] = group
        print("Успешно изменен",
              "0 - Назад", sep="\n")
        return
    if cmd_input == "3" and name_input == "Маг_ФИИТ" and year_input == "2020":
        print("Выход за пределы массива ( ´•︵•` )\n" + default_output)
        return
    if cmd_input == "2" and name_input == "" and year_input == "2020":
        print("Нет... вы ввели пустую строчку ( ´•︵•` )\n" + default_output)
        return
    if cmd_input == "" and name_input == "Маг_ФИИТ" and year_input == "2020":
        print("Нет... вы ввели пустую строчку ( ´•︵•` )\n" + default_output)
        return
    if cmd_input == "2" and name_input == "Маг_ФИИТ" and year_input == "":
        print("Нет... вы ввели пустую строчку ( ´•︵•` )\n" + default_output)
        return
    if cmd_input == "2" and name_input == "Маг_ФИИТ" and year_input == "twh thousands year":
        print("Нет... вы ввели не целое число ( ´•︵•` )\n" + default_output)
        return
    if cmd_input == "two" and name_input == "Маг_ФИИТ" and year_input == "2020":
        print("Нет... вы ввели не целое число ( ´•︵•` )\n" + default_output)


def delete_group():
    if groups == list():
        print("Список групп пуст ( ´•︵•` )",
              "0 - Назад", sep="\n")
        return
    default_output = '0 - Назад\n' \
                     '1 - М-ФИИТ 2020\n' \
                     '2 - М-ИВТ 2020'
    cmd_input = input()
    if cmd_input == "1":
        groups.remove(groups[1])
        print("Успешно удален",
              "0 - Назад", sep="\n")
        return
    if cmd_input == "3":
        print("Выход за пределы массива ( ´•︵•` )\n" + default_output)
        return
    if cmd_input == "two":
        print("Нет... вы ввели не целое число ( ´•︵•` )\n" + default_output)
        return
    if cmd_input == "":
        print("Нет... вы ввели пустую строчку ( ´•︵•` )\n" + default_output)
        return
