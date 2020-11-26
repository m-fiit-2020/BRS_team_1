from Controller.Factory import create_group, create_student, create_subject
from Store.Collections import groups, subjects, students
from Store.Moks import add_groups, add_students, add_subjects


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
    working = True
    while working:
        working = print_menu()

    # Example Create
    # group = Group(name="M-FIIT_20", year=20)
    # subject = Subject(code="111", name="Math")
    # section = CrossSection.FirstSection
    # year = EducationYear(begin_year="2020", end_year="2022")
    # points = BRSPoints(subject=subject, year=year, cross_section=section, points=120)
    # student = Student(code="1229", fio="Saryal Vasiliev Inn", birthdate="02.10.2102", email="ssss",
    #                   phone="dsasad", group=group, brs_points=[points, points])
    # print(check_points(student))
    # add_groups()
    # create_student()
