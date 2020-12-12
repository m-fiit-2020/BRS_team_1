from Controller.Factory import create_group, create_student, create_subject
from Store.Collections import groups, subjects, students
from Store.Moks import add_groups, add_students, add_subjects
from View import UserInput


def print_menu():
    print("0 - выход")
    print("1 - студент")
    print("2 - группа")
    print("3 - предмет")
    step_one = int(input("Выберите действие: "))
    if step_one == 0:
        return False
    elif step_one == 1:
        print("1 - Добавить студента")
        print("2 - Просмотр студентов")
        step_two = int(input("Выберите действие: "))
        if step_two == 1:
            create_student()
        else:
            for student in students:
                print(f"{student.code}\n"
                      f"{student.fio}\n"
                      f"{student.phone}\n"
                      f"{student.email}\n"
                      f"{student.birthdate}\n"
                      f"{student.group.name} {student.group.year}\n")
    elif step_one == 2:
        print("1 - Добавить группу")
        print("2 - Просмотр групп")
        step_two = int(input("Выберите действие: "))
        if step_two == 1:
            create_group()
        else:
            for group in groups:
                print(f"{group.name} {group.year}\n")
    elif step_one == 3:
        print("1 - Добавить предмет")
        print("2 - Просмотр предмета")
        step_two = int(input("Выберите действие: "))
        if step_two == 1:
            create_subject()
        else:
            for subject in subjects:
                print(f"{subject.code} - {subject.name}\n")
    return True



def print_group_menu(self):
    pass


def print_subject_menu(self):
    pass


def add_group(self):
    pass


def edit_group(self):
    pass


def delete_group(self):
    pass


def add_student(self):
    pass


def edit_student(self):
    pass


def remove_student(self):
    pass


def add_subject(self):
    pass


def edit_subject(self):
    pass


def delete_subject(self):
    pass


def add_brs_point(self):
    pass


def edit_brs_point(self):
    pass


def delete_brs_point(self):
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    add_groups()
    add_subjects()
    add_students()
    create_group(UserInput.input_group())
    working = True
    while working:
        working = print_menu()
