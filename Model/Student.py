from MVC.Model.BRSPoints import BRSPoints
from MVC.Model.Group import Group


class Student:
    def __init__(self,
                 code: str,
                 fio: int,
                 birthdate: str,
                 email: str,
                 phone: str,
                 group: Group,
                 brs_points: [BRSPoints]):
        self.code = code
        self.fio = fio
        self.birthdate = birthdate
        self.email = email
        self.phone = phone
        self.group = group
        self.brs_points = brs_points
