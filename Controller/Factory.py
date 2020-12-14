from Models.Student import Student
from Models.Group import Group
from Store.Collections import groups
from Models.Subject import Subject
from Controller.Support.CheckInput import check_input_on_empty
from Controller.Support.Convert import convert_input_to_int
from View import UserInput


def create_group(name, year):
    check_input_on_empty(name)
    check_input_on_empty(year)
    year = convert_input_to_int(year)
    return Group(name=name, year=year)


def create_subject(code, name):
    check_input_on_empty(code)
    check_input_on_empty(name)
    code = convert_input_to_int(code)
    return Subject(code=code, name=name)


def create_student(code, name, birthdate, email, phone, group):
    check_input_on_empty(code)
    check_input_on_empty(name)
    check_input_on_empty(birthdate)
    check_input_on_empty(email)
    check_input_on_empty(phone)
    check_input_on_empty(group)
    code = convert_input_to_int(code)
    birthdate = convert_input_to_int(birthdate)
    phone = convert_input_to_int(phone)
    return Student(code=code, fio=name, birthdate=birthdate, email=email, phone=phone, group=group,
                   brs_points=[])