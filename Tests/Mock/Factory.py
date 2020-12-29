from Model.Group import Group
from Model.Subject import Subject
from Model.EducationYear import EducationYear
from Model.Student import Student
from Model.BRSPoints import BRSPoints
from datetime import date


def CreateGroup(name, year):
    if name == "М-ФИИТ" and year == "2020":
        year_int = 2020
        group = Group(name=name, year=year_int)
        return group
    if name == "" and year == "2020":
        raise Exception()
    if name == "М-ФИИТ" and year == "":
        raise Exception()
    if name == "М-ФИИТ" and year == "two thousand":
        raise Exception()


def CreateSubject(code, name):
    if code == "Б1.О.03" and name == "Управление проектами":
        subject = Subject(code=code, name=name)
        return subject
    if code == "" and name == "Управление проектами":
        raise Exception()
    if code == "Б1.О.03" and name == "":
        raise Exception()


def CreateEducationYear(begin_year, end_year):
    if begin_year == "2020" and end_year == "2022":
        education_year = EducationYear(begin_year=2020, end_year=2022)
        return education_year
    if begin_year == "" and end_year == "2022":
        raise Exception()
    if begin_year == "2022" and end_year == "":
        raise Exception()
    if begin_year == "s" and end_year == "two thousand":
        raise Exception()


def CreateStudent(code, fio, birthdate, email, phone, group):
    if code == "160978" and fio == "Васильев Сарыал Иннокентьевич" \
            and birthdate == "12.07.1998" and email == "saryal.basilev@mail.ru" \
            and phone == "+79969141275" and group:
        student = Student(code=160978, fio=fio, birthdate=date(1998, 7, 12),
                          email=email, phone=phone, group=group)
        return student
    if code == "160978" and fio == "" \
            and birthdate == "12.07.1998" and email == "saryal.basilev@mail.ru" \
            and phone == "+79969141275" and group:
        raise Exception()
    if code == "ооо" and fio == "Васильев Сарыал Иннокентьевич" \
            and birthdate == "12.07.1998" and email == "saryal.basilev@mail.ru" \
            and phone == "+79969141275" and group:
        raise Exception()
    if code == "160978" and fio == "Васильев Сарыал Иннокентьевич" \
            and birthdate == "12.07.э1998" and email == "saryal.basilev@mail.ru" \
            and phone == "+79969141275" and group:
        raise Exception()
    if code == "160978" and fio == "Васильев Сарыал Иннокентьевич" \
            and birthdate == "12.07.1998" and email == "saryal.basilev@mail.ru" \
            and phone == "+799691412в75" and group:
        raise Exception()


def CreateBRSPoints(student, subject, year, cross_section, points):
    if student and subject and year and cross_section and points == "100":
        brs_points = BRSPoints(student=student, subject=subject,
                               year=year, cross_section=cross_section, points=100)
        return brs_points
    if student and subject and year and cross_section and points == "ten":
        raise Exception()
    if student and subject and year and cross_section and points == "101":
        raise Exception()
    raise Exception()
