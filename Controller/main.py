from Controller.Factory import create_group, create_student, create_subject
from Store.Collections import groups, subjects, students
from Store.Moks import add_groups, add_students, add_subjects
from View import UserInput


def print_main_menu():
    print("""
0 - выход
1 - студент
2 - группа
3 - предмет
4 - БРС""")


def print_student_menu():
    print("""
0 - назад
1 - добавить студента
2 - редактировать студента
3 - удалить студента""")


def print_group_menu():
    print("""
0 - назад
1 - добавить группу
2 - редактировать группу
3 - удалить группу""")


def print_subject_menu():
    print("""
0 - назад
1 - добавить предмет
2 - редактировать предмет
3 - удалить предмет""")


def print_brs_menu():
    print("""
0 - назад
1 - добавить БРС
2 - редактировать БРС
3 - удалить БРС""")


def add_group():
    pass


def edit_group():
    pass


def delete_group():
    pass


def add_student():
    pass


def edit_student():
    pass


def remove_student():
    pass


def add_subject():
    pass


def edit_subject():
    pass


def delete_subject():
    pass


def add_brs_point():
    pass


def edit_brs_point():
    pass


def delete_brs_point():
    pass


def start():
    try:
        print_main_menu()
        step_one = int(input('Выберите действие: '))
        if step_one == 0:
            return False
        main_menu_functions[step_one]()
        all_menus[step_one][int(input('Выберите действие: '))]()
    except KeyError:
        print('Неверное значение')
    return True


main_menu_functions = {1: print_student_menu,
                       2: print_group_menu,
                       3: print_subject_menu,
                       4: print_brs_menu}


student_menu_functions = {0: start,
                          1: add_student,
                          2: edit_student,
                          3: remove_student}


group_menu_functions = {0: start,
                        1: add_group,
                        2: edit_group,
                        3: delete_group}


subject_menu_functions = {0: start,
                          1: add_subject,
                          2: edit_subject,
                          3: delete_subject}


brs_menu_functions = {0: start,
                      1: add_brs_point,
                      2: edit_brs_point,
                      3: delete_brs_point}


all_menus = {1: student_menu_functions,
             2: group_menu_functions,
             3: subject_menu_functions,
             4: brs_menu_functions}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    add_groups()
    add_subjects()
    add_students()
    a = UserInput.input_group()
    create_group(a[0], a[1])
    working = True
    while working:
        working = start()
