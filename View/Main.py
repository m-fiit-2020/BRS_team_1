from Controller.Main import main_menu_functions, all_menus


def print_main_menu():
    print('0 - выход\n1 - студент\n2 - группа\n3 - предмет\n4 - БРС')


def print_student_menu():
    print('0 - назад\n1 - добавить студента\n2 - редактировать студента\n3 - удалить студента')


def print_group_menu():
    print('0 - назад\n1 - добавить группу\n2 - редактировать группу\n3 - удалить группу')


def print_subject_menu():
    print('0 - назад\n1 - добавить предмет\n2 - редактировать предмет\n3 - удалить предмет')


def print_brs_menu():
    print('0 - назад\n1 - добавить БРС\n2 - редактировать БРС\n3 - удалить БРС')


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
