from Models.Subject import Subject
from Models.Group import Group
from Models.Student import Student
from Store.Collections import groups, subjects, students


def add_groups():
    groups.append(Group(name="ФИИТ", year=2020))
    groups.append(Group(name="ИВТ", year=2020)),
    groups.append(Group(name="ИВТ", year=2016)),
    groups.append(Group(name="ФИИТ", year=2016))


def add_subjects():
    subjects.append(Subject(code="2200", name="Math"))
    subjects.append(Subject(code="2201", name="English"))
    subjects.append(Subject(code="2111", name="Physics"))


def add_students():
    students.append(Student(code="1",
                            fio="Васильев Сарыал Иннокентьевич",
                            birthdate="12.07.1998",
                            email="saryal.basilev@mail.ru",
                            phone="+79969141275",
                            group=groups[0],
                            brs_points=[]))
    students.append(Student(code="2",
                            fio="Иванов Иван Иванович",
                            birthdate="11.01.2002",
                            email="example@mail.ru",
                            phone="+71234567890",
                            group=groups[3],
                            brs_points=[]))