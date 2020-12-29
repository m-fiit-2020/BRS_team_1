from Model.CrossSection import CrossSection
from datetime import date


class Group:
    def __init__(self, name: str, year: int):
        self.name = name
        self.year = year


class Subject:
    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name


class EducationYear:
    def __init__(self, begin_year: int, end_year: int):
        self.begin_year = begin_year
        self.end_year = end_year


class Student:
    def __init__(self,
                 code: int,
                 fio: str,
                 birthdate: date,
                 email: str,
                 phone: str,
                 group: Group):
        self.code = code
        self.fio = fio
        self.birthdate = birthdate
        self.email = email
        self.phone = phone
        self.group = group


class BRSPoints:
    def __init__(self, student: Student, subject: Subject, year: EducationYear,
                 cross_section: CrossSection, points: int):
        self.student = student
        self.subject = subject
        self.year = year
        self.cross_section = cross_section
        self.points = points
