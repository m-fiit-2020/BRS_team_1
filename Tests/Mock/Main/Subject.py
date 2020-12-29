from Factory import create_subject
from Store.Collections import subjects


def add_subject():
    code_input = input()
    name_input = input()
    if code_input == "Б1.В.07" and name_input == "Информационный менеджмент":
        subject = create_subject(code=code_input, name=name_input)
        subjects.append(subject)
        print("Успешно добавлен",
              "0 - Назад", sep="\n")
        return
    if code_input == "Б1.О.03" and name_input == "":
        print("Нет... вы ввели пустую строчку ( ´•︵•` )")
        return
    if code_input == "" and name_input == "Управление проектами":
        print("Нет... вы ввели пустую строчку ( ´•︵•` )")
        return
    if code_input == "Б1.О.03" and name_input == "Управление проектами":
        print("Предмет с такими данными уже существует ( ´•︵•` )")
        return


def delete_subject():
    if subjects == list():
        print("Список предметов пуст ( ´•︵•` )",
              "0 - Назад", sep="\n")
        return
    default_output = '0 - Назад\n' \
                     '1 - Б1.О.03 Управление проектами\n' \
                     '2 - Б1.В.07 Информационный менеджмент'
    cmd_input = input()
    if cmd_input == "1":
        subjects.remove(subjects[0])
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


def edit_subject():
    if subjects == list():
        print("Список предметов пуст ( ´•︵•` )",
              "0 - Назад", sep="\n")
        return
    default_output = '0 - Назад\n' \
                     '1 - Б1.О.03 Управление проектами\n' \
                     '2 - Б1.В.07 Информационный менеджмент'
    cmd_input = input()
    code_input = input()
    name_input = input()
    if cmd_input == "2" and code_input == "Б1234" and name_input == "Управление проектами":
        subject = create_subject(code=code_input, name="Управление проектами")
        subjects[1] = subject
        print("Успешно изменен",
              "0 - Назад", sep="\n")
        return
    if cmd_input == "3" and code_input == "Б1234" and name_input == "Управление проектами":
        print("Выход за пределы массива ( ´•︵•` )\n" + default_output)
        return
    if cmd_input == "2" and code_input == "" and name_input == "Управление проектами":
        print("Нет... вы ввели пустую строчку ( ´•︵•` )\n" + default_output)
        return
    if cmd_input == "" and code_input == "Б1234" and name_input == "Управление проектами":
        print("Нет... вы ввели пустую строчку ( ´•︵•` )\n" + default_output)
        return
    if cmd_input == "2" and code_input == "Б1234" and name_input == "":
        print("Нет... вы ввели пустую строчку ( ´•︵•` )\n" + default_output)
        return
    if cmd_input == "two" and code_input == "Б1234" and name_input == "Управление проектами":
        print("Нет... вы ввели не целое число ( ´•︵•` )\n" + default_output)
