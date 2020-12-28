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


def check_points(bp: [BRSPoints], cs: CrossSection, point: int):
    if point > 100:
        print("Не правильно поставлен бал")
        return False
    if cs == CrossSection.FinalSection:
        for i in bp:
            if (i.cross_section == CrossSection.SecondSection or i.cross_section == CrossSection.FirstSection) \
                    and i.points > point:
                print("Бал контрольного среза не должен быть меньше предыдущего контрольного среза")
                return False
    if cs == CrossSection.SecondSection:
        for i in bp:
            if i.cross_section == CrossSection.FirstSection and i.points > point:
                print("Бал контрольного среза не должен быть меньше предыдущего контрольного среза")
                return False
    print("Бал поставлен правильно")
    return True





# FirstSection = "Первый контрольный срез"
# SecondSection = "Второй контрольный срез"
# FinalSection = "Заключительный контрольный срез"

