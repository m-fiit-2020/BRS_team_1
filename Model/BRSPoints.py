from MVC.Model.EducationYear import EducationYear
from MVC.Model.Subject import Subject
from MVC.Model.CrossSection import CrossSection


class BRSPoints:
    def __init__(self, subject: Subject, year: EducationYear, cross_section: CrossSection, points: int):
        self.subject = subject
        self.year = year
        self.cross_section = cross_section
        self.points = points
