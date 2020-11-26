from Models.Student import Student
from Models.Group import Group
from Store.Collections import groups, subjects, students
from Models.Subject import Subject
from Support.CheckInput import convert_input_to_int, check_input_on_empty
import UserInput


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


def create_student(code, name, birthdate, email, phone):
    group_cmd = UserInput.input_choose_group()
    check_input_on_empty(group_cmd)
    group_cmd = convert_input_to_int(group_cmd)
    group = groups[group_cmd]
    return Student(code=code, fio=name, birthdate=birthdate, email=email, phone=phone, group=group,
                   brs_points=[])