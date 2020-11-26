from Models.Student import Student
from Models.Group import Group
from Store.Collections import groups, subjects, students
from Models.Subject import Subject


def create_group():
    name = input("Введите название группы: ")
    year = int(input("Введите год группы: "))
    group = Group(name=name, year=year)
    groups.append(group)


def create_subject():
    code = int(input("Введите код предмета: "))
    name = input("Введите название предмета: ")
    subject = Subject(code=code, name=name)
    subjects.append(subject)


def create_student():
    code = int(input("Введите уникальный код студента: "))
    name = input("Введите ФИО студента: ")
    birthdate = input("Введите дату рождения студента: ")
    email = input("Введите e-mail студента: ")
    phone = input("Введите номер телефона студента: ")
    print("0 - создать группу")
    for i, group in enumerate(groups):
        print(f"{i+1} - {group.name} {group.year}")
    group_cmd = int(input("Выберите группу студента: "))
    if group_cmd == 0:
        create_group()
        group = groups[len(groups) - 1]
    else:
        group = groups[group_cmd - 1]
    student = Student(code=code, fio=name, birthdate=birthdate, email=email, phone=phone, group=group, brs_points=[])
    students.append(student)