import re
from Models.EducationYear import EducationYear
from Models.CrossSection import CrossSection
from Models.BRSPoints import BRSPoints


def check_email(email: str):
    """Проверяет надпись электронной почты. Пока что знает только 'gmail.com' и 'mail.ru'"""
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-z.]{2,6}$)", str(email)):
        print("правильный email")
        return True
    else:
        print("непрвильный email")
        return False


def check_phone(phone: str):
    """Проверяет надпись номера телефона"""
    if re.match(r"(^(\+7)|8)\d{10}$", str(phone)):
        print("правильный номер")
        return True
    else:
        print("неправильный номер")
        return False


def check_points(bp: BRSPoints, ey: EducationYear, cs: CrossSection):
    if bp.year == ey and bp.cross_section == cs:
        if bp.points > 100 or bp.points < 0 or type(bp.points) == float or type(bp.points) == bool:
            print("Балл поставлен НЕКОРРЕКТНО\n"
                  f"Название предмета: {bp.subject.name}\n"
                  f"Код предмета: {bp.subject.code}\n"
                  f"Года обучения: c {bp.year.begin_year} по {bp.year.end_year}\n"
                  f"Срез: {bp.cross_section.value}\n"
                  f"Количество баллов: {bp.points}")
            return False
        print("правильно", bp.points, bp.subject.name, bp.student.fio)
        return True
    print("Здесь пусто")
