from Store.Collections import groups


def input_group():
    name = input("Введите название группы: ")
    year = input("Введите год группы: ")
    return name, year


def input_choose_group():
    for i, group in enumerate(groups):
        print(f"{i} - {group.name} {group.year}")
    group_cmd = input("Выберите группу студента: ")
    return group_cmd


def input_subject():
    code = input("Введите код предмета: ")
    name = input("Введите название предмета: ")
    return code, name

def input_subject_delete():
    code = input("Введите код предмета, который хотите удалить: ")
    return code


def input_student():
    code = int(input("Введите уникальный код студента: "))
    name = input("Введите ФИО студента: ")
    birthdate = input("Введите дату рождения студента: ")
    email = input("Введите e-mail студента: ")
    phone = input("Введите номер телефона студента: ")
    return code, name, birthdate, email, phone
